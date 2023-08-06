import glob
import os
import tempfile

from seedbox import db
from seedbox.db import models
from seedbox.tests import test
from seedbox.torrent import loader
from seedbox.torrent import parser

torrent_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            'testdata')


class TorrentLoaderTest(test.ConfiguredBaseTestCase):

    def setUp(self):
        super(TorrentLoaderTest, self).setUp()

        self.CONF.set_override('torrent_path',
                               torrent_path,
                               group='torrent')

        self.CONF.set_override('media_paths',
                               [torrent_path],
                               group='torrent')

        self.CONF.set_override('incomplete_path',
                               torrent_path,
                               group='torrent')

        self.patch(db, '_DBAPI', {})
        self.dbapi = db.dbapi(self.CONF)

    def test_load_torrents(self):
        loader.load_torrents(self.dbapi)

    def test_load_torrents_still_downloading(self):

        def _is_torrent_downloading(media_items):
            return True

        self.patch(loader, '_is_torrent_downloading', _is_torrent_downloading)
        loader.load_torrents(self.dbapi)

    def test_load_torrents_parse_error(self):

        class TorrentParser(object):

            def __init__(self, tfile):
                raise parser.ParsingError('failed to parse')

        self.patch(parser, 'TorrentParser', TorrentParser)
        loader.load_torrents(self.dbapi)

    def test_load_torrents_no_parse(self):
        for tor in glob.glob(os.path.join(torrent_path, '*.torrent')):
            _tor = models.Torrent.make_empty()
            _tor.name = os.path.basename(tor)
            _tor.invalid = True
            self.dbapi.save_torrent(_tor)

        loader.load_torrents(self.dbapi)

    def test_parsing_required(self):
        _tor = models.Torrent.make_empty()
        _tor.name = 'preq-check'
        torrent = self.dbapi.save_torrent(_tor)
        result = loader._is_parsing_required(torrent)
        self.assertTrue(result)

        torrent.invalid = True
        torrent = self.dbapi.save_torrent(torrent)
        result = loader._is_parsing_required(torrent)
        self.assertFalse(result)

        torrent.invalid = False
        torrent.purged = True
        torrent = self.dbapi.save_torrent(torrent)
        result = loader._is_parsing_required(torrent)
        self.assertFalse(result)

        torrent.purged = False
        torrent = self.dbapi.save_torrent(torrent)

        _media = models.MediaFile.make_empty()
        _media.filename = 'media'
        _media.file_ext = '.mp4'
        _media.torrent_id = torrent.torrent_id
        self.dbapi.save_media(_media)

        torrent = self.dbapi.get_torrent(torrent.torrent_id)
        result = loader._is_parsing_required(torrent)
        self.assertFalse(result)

    def test_torrent_downloading(self):

        mediafiles = [('fake1.mp4', 150000), ('fake2.mp4', 150000)]

        self.CONF.set_override('incomplete_path',
                               self.base_dir,
                               group='torrent')

        result = loader._is_torrent_downloading(mediafiles)
        self.assertFalse(result)

        media1 = tempfile.NamedTemporaryFile(suffix='.mp4',
                                             dir=self.base_dir)
        media2 = tempfile.NamedTemporaryFile(suffix='.mp4',
                                             dir=self.base_dir)
        mediafiles = [(media1.name, 150000), (media2.name, 150000)]

        result = loader._is_torrent_downloading(mediafiles)
        self.assertTrue(result)

    def test_filter_media(self):

        self.CONF.set_override('media_paths',
                               [self.base_dir],
                               group='torrent')

        media1 = tempfile.NamedTemporaryFile(suffix='.mp4',
                                             dir=self.base_dir)

        media_list = loader._filter_media('1234', [(media1.name, 75000001)])
        self.assertEqual(len(media_list),  1)
        self.assertEqual(media_list[0].filename, os.path.basename(media1.name))

    def test_get_file_path(self):

        self.CONF.set_override('media_paths',
                               [self.base_dir],
                               group='torrent')

        (location, filename) = loader._get_file_path('fake-name.mp4')
        self.assertIsNone(location)

        media1 = tempfile.NamedTemporaryFile(suffix='.mp4',
                                             dir=self.base_dir)

        (location, filename) = loader._get_file_path(media1.name)
        self.assertIsNotNone(location)
