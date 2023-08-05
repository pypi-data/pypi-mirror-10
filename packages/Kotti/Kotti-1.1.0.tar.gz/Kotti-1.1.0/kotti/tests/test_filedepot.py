import datetime
import pytest

from kotti.filedepot import DBFileStorage, DBStoredFile
from kotti.resources import File
from kotti.resources import Image


class TestDBStoredFile:

    def test_storedfile_interface(self, db_session, events, setup_app):
        f = DBStoredFile('fileid', filename=u'f.jpg', content_type='image/jpeg',
                         content_length=1000, data='content')

        assert f.close() is None
        assert f.closed() is False
        assert f.seekable() is True
        assert f.writable() is False

        assert f.read() == 'content'
        assert f.read() == ''
        f.seek(0)
        assert f.read() == 'content'
        f.seek(0)
        assert f.read(-1) == 'content'
        f.seek(0)
        assert f.read(2) == 'co'
        assert f.read(4) == 'nten'
        assert f.tell() == 6
        f.seek(0)
        f.seek(100)
        assert f.tell() == 100
        assert f.read() == ''

        assert f.content_length == 1000
        assert f.content_type == 'image/jpeg'
        assert f.file_id == 'fileid'
        assert f.filename == u'f.jpg'
        assert f.name == u"f.jpg"
        assert f.public_url is None

        f.data = None
        db_session.add(f)
        db_session.flush()
        assert f.content_length == 0

    def test_content_length(self, db_session, events, setup_app):
        f = DBStoredFile('fileid', data="content")
        db_session.add(f)
        db_session.flush()

        assert f.content_length == 7

        f.data = 'content changed'
        db_session.flush()

        assert f.content_length == len('content changed')

    def test_last_modified(self, monkeypatch, db_session, events, setup_app):
        from kotti import filedepot

        now = datetime.datetime.now()

        class mockdatetime:
            @staticmethod
            def now():
                return now

        monkeypatch.setattr(filedepot, 'datetime', mockdatetime)

        f = DBStoredFile('fileid', data="content")
        db_session.add(f)
        db_session.flush()

        assert f.last_modified == now

        f.last_modified = None
        f.data = 'content changed'
        db_session.flush()

        assert f.last_modified == now


class TestDBFileStorage:

    def make_one(self,
                 content='content here',
                 filename=u'f.jpg',
                 content_type='image/jpg'):

        file_id = DBFileStorage().create(
            content=content, filename=filename, content_type=content_type)
        return file_id

    def test_create(self, db_session):
        file_id = self.make_one()
        assert len(file_id) == 36

        fs = db_session.query(DBStoredFile).filter_by(file_id=file_id).one()
        assert fs.data == "content here"

    def test_get(self, db_session):
        with pytest.raises(IOError):
            DBFileStorage().get("1")

        file_id = self.make_one()
        assert DBFileStorage().get(file_id).data == "content here"

    def test_delete(self, db_session):
        file_id = DBFileStorage().create('content here', u'f.jpg', 'image/jpg')
        fs = DBFileStorage().get(file_id)

        db_session.add(fs)
        db_session.flush()

        assert db_session.query(DBStoredFile.file_id).one()[0] == file_id

        DBFileStorage().delete(file_id)
        assert db_session.query(DBStoredFile).count() == 0

    def test_replace(self, db_session):
        file_id = self.make_one()

        DBFileStorage().replace(file_id, 'second content', u'f2.jpg', 'doc')
        fs = DBFileStorage().get(file_id)
        assert fs.filename == u'f2.jpg'
        assert fs.content_type == 'doc'
        assert fs.read() == 'second content'

        DBFileStorage().replace(fs, 'third content', u'f3.jpg', 'xls')
        assert fs.filename == u'f3.jpg'
        assert fs.content_type == 'xls'
        assert fs.read() == 'third content'

    def test_session_integration(self, db_session):
        from depot.manager import DepotManager

        DepotManager._default_depot = 'default'
        DepotManager._depots = {'default': DBFileStorage()}

        file_id = DepotManager.get().create('content here', u'f.jpg', 'image/jpg')
        fs = DepotManager.get().get(file_id)

        db_session.add(fs)
        import transaction
        transaction.commit()

        transaction.begin()
        db_session.delete(fs)
        transaction.commit()

        with pytest.raises(IOError):
            DepotManager.get().get(file_id)


class TestMigrateBetweenStorage:

    def _create_content(self, db_session, root):
        data = [
            ('f1...', u'file1.jpg', 'image/jpeg'),
            ('f2...', u'file2.png', 'image/png'),
        ]
        for row in data:
            f = File(data=row[0], filename=row[1], mimetype=row[2])
            root[row[1]] = f

        data = [
            ('i1...', u'image1.jpg', 'image/jpeg'),
            ('i2...', u'image2.png', 'image/png'),
        ]
        for row in data:
            f = Image(data=row[0], filename=row[1], mimetype=row[2])
            root[row[1]] = f

        db_session.flush()

    def test_migrate_between_storages(self, db_session, root, no_filedepots):
        from kotti.filedepot import configure_filedepot
        from kotti.filedepot import migrate_storage
        from kotti.resources import Node
        from depot.fields.sqlalchemy import _SQLAMutationTracker
        from sqlalchemy import event
        import os
        import tempfile
        import shutil

        event.listen(db_session,
                    'before_commit',
                    _SQLAMutationTracker._session_committed)

        tmp_location = tempfile.mkdtemp()

        settings = {
            'kotti.depot.0.backend': 'kotti.filedepot.DBFileStorage',
            'kotti.depot.0.name': 'dbfiles',

            'kotti.depot.1.backend': 'depot.io.local.LocalFileStorage',
            'kotti.depot.1.name': 'localfs',
            'kotti.depot.1.storage_path': tmp_location,
        }

        configure_filedepot(settings)
        self._create_content(db_session, root)

        assert db_session.query(DBStoredFile).count() == 4

        migrate_storage('dbfiles', 'localfs')

        folders = os.listdir(tmp_location)
        assert len(folders) == 4

        db_session.flush()

        # here we need a transaction.commit(), but that would mess with the
        # rest of the tests; we'll just trigger the event handler manually
        _SQLAMutationTracker._session_committed(db_session)

        root = db_session.query(Node).filter_by(parent=None).one()
        f1 = root['file1.jpg']
        assert f1.data.file_id in folders
        assert f1.data.file.read() == 'f1...'

        f2 = root['file2.png']
        assert f2.data.file_id in folders
        assert f2.data.file.read() == 'f2...'

        i1 = root['image1.jpg']
        assert i1.data.file_id in folders
        assert i1.data.file.read() == 'i1...'

        i2 = root['image2.png']
        assert i2.data.file_id in folders
        assert i2.data.file.read() == 'i2...'

        assert db_session.query(DBStoredFile).count() == 0

        shutil.rmtree(tmp_location)
