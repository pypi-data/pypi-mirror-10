from __future__ import absolute_import

import hashlib
import os
import os.path
import shutil
import sys
import tempfile

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from zipfile2 import ZipFile

from ..common import PY2, string_types
from .common import NOSE_EGG, VTK_EGG, ZIP_WITH_SOFTLINK

if PY2:
    import StringIO
    BytesIO = StringIO.StringIO
else:
    import io
    BytesIO = io.BytesIO

SUPPORT_SYMLINK = hasattr(os, "symlink")

HERE = os.path.dirname(__file__)


def list_files(top):
    paths = []
    for root, dirs, files in os.walk(top):
        for f in files:
            paths.append(os.path.join(os.path.relpath(root, top), f))
    return paths


def compute_md5(path):
    m = hashlib.md5()
    block_size = 2 ** 16

    def _compute_checksum(fp):
        while True:
            data = fp.read(block_size)
            m.update(data)
            if len(data) < block_size:
                break
        return m.hexdigest()

    if isinstance(path, string_types):
        with open(path, "rb") as fp:
            return _compute_checksum(fp)
    else:
        return _compute_checksum(path)


def create_broken_symlink(link):
    d = os.path.dirname(link)
    os.makedirs(d)
    os.symlink(os.path.join(d, "nono_le_petit_robot"), link)


class TestZipFile(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    if PY2:
        def assertCountEqual(self, first, second, msg=None):
            return self.assertItemsEqual(first, second, msg)

    def test_simple(self):
        # Given
        path = NOSE_EGG
        r_paths = [
            os.path.join("EGG-INFO", "entry_points.txt"),
            os.path.join("EGG-INFO", "PKG-INFO"),
            os.path.join("EGG-INFO", "spec", "depend"),
            os.path.join("EGG-INFO", "spec", "summary"),
            os.path.join("EGG-INFO", "usr", "share", "man", "man1",
                         "nosetests.1"),
        ]

        # When
        with ZipFile(path) as zp:
            zp.extractall(self.tempdir)
        paths = list_files(self.tempdir)

        # Then
        self.assertCountEqual(paths, r_paths)

    def test_extract(self):
        # Given
        path = NOSE_EGG
        arcname = "EGG-INFO/PKG-INFO"

        # When
        with ZipFile(path) as zp:
            zp.extract(arcname, self.tempdir)
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, arcname)))

    def test_extract_to(self):
        # Given
        path = NOSE_EGG
        arcname = "EGG-INFO/PKG-INFO"

        # When
        with ZipFile(path) as zp:
            zp.extract_to(arcname, "FOO", self.tempdir)
            extracted_data = zp.read(arcname)
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, "FOO")))
        self.assertEqual(compute_md5(os.path.join(self.tempdir, "FOO")),
                         compute_md5(BytesIO(extracted_data)))
        self.assertFalse(os.path.exists(os.path.join(self.tempdir, "EGG-INFO",
                                                     "PKG-INFO")))

    @unittest.skipIf(not SUPPORT_SYMLINK,
                     "this platform does not support symlink")
    def test_softlink(self):
        # Given
        path = ZIP_WITH_SOFTLINK

        # When/Then
        with ZipFile(path) as zp:
            zp.extractall(self.tempdir)
        paths = list_files(self.tempdir)

        self.assertCountEqual(paths, [os.path.join("lib", "foo.so.1.3"),
                                      os.path.join("lib", "foo.so")])
        self.assertTrue(os.path.islink(
            os.path.join(self.tempdir, "lib", "foo.so"))
        )

    @unittest.skipIf(not SUPPORT_SYMLINK,
                     "this platform does not support symlink")
    def test_softlink_with_broken_entry(self):
        self.maxDiff = None

        # Given
        path = VTK_EGG
        expected_files = [
            os.path.join('EGG-INFO', 'PKG-INFO'),
            os.path.join('EGG-INFO', 'inst', 'targets.dat'),
            os.path.join('EGG-INFO', 'inst', 'files_to_install.txt'),
            os.path.join('EGG-INFO', 'usr', 'lib', 'vtk-5.10',
                         'libvtkViews.so.5.10.1'),
            os.path.join('EGG-INFO', 'usr', 'lib', 'vtk-5.10',
                         'libvtkViews.so.5.10'),
            os.path.join('EGG-INFO', 'usr', 'lib', 'vtk-5.10',
                         'libvtkViews.so'),
            os.path.join('EGG-INFO', 'spec', 'lib-provide'),
            os.path.join('EGG-INFO', 'spec', 'depend'),
            os.path.join('EGG-INFO', 'spec', 'lib-depend'),
            os.path.join('EGG-INFO', 'spec', 'summary'),
        ]

        existing_link = os.path.join(self.tempdir,
                                     'EGG-INFO/usr/lib/vtk-5.10/'
                                     'libvtkViews.so')
        create_broken_symlink(existing_link)

        # When
        with ZipFile(path) as zp:
            zp.extractall(self.tempdir)
        files = list_files(self.tempdir)

        # Then
        self.assertCountEqual(files, expected_files)
        path = os.path.join(self.tempdir,
                            "EGG-INFO/usr/lib/vtk-5.10/libvtkViews.so")
        self.assertTrue(os.path.islink(path))

    def test_multiple_archives_write(self):
        # Given
        zipfile = os.path.join(self.tempdir, "foo.zip")
        to = os.path.join(self.tempdir, "to")

        # When
        with ZipFile(zipfile, "w") as zp:
            zp.write(__file__, "file.py")
            with self.assertRaises(ValueError):
                zp.write(__file__, "file.py")

        with ZipFile(zipfile) as zp:
            zp.extractall(to)

        # Then
        self.assertTrue(os.path.exists(zipfile))
        self.assertTrue(os.path.exists(os.path.join(to, "file.py")))

    def test_multiple_archives_writestr(self):
        # Given
        zipfile = os.path.join(self.tempdir, "foo.zip")
        target = os.path.join(self.tempdir, "file.py")

        # When
        with ZipFile(zipfile, "w") as zp:
            zp.writestr("file.py", b"data")
            with self.assertRaises(ValueError):
                zp.writestr("file.py", b"dato")

        with ZipFile(zipfile) as zp:
            new_path = zp.extract("file.py", self.tempdir)
            data = zp.read("file.py")

        # Then
        self.assertTrue(os.path.exists(zipfile))
        self.assertTrue(os.path.exists(target))
        self.assertEqual(data, b"data")
        self.assertEqual(new_path, target)

    def test_multiple_archives_read(self):
        # Given
        zipfile = os.path.join(self.tempdir, "foo.zip")

        # When
        with ZipFile(zipfile, "w", low_level=True) as zp:
            zp.writestr("file.py", b"data")
            zp.writestr("file.py", b"dato")

        # Then
        # ensure we have indeed two members with archive name file.py
        with ZipFile(zipfile, low_level=True) as zp:
            self.assertEqual(len(zp.namelist()), 2)

        # ensure we raise an error if duplicates
        with self.assertRaises(ValueError):
            with ZipFile(zipfile) as zp:
                pass

    @unittest.skipIf(not SUPPORT_SYMLINK,
                     "this platform does not support symlink")
    def test_write_symlink_file(self):
        # Given
        zipfile = os.path.join(self.tempdir, "foo.zip")
        real_file = os.path.join(self.tempdir, "foo.txt")
        symlink = os.path.join(self.tempdir, "symlink")

        with open(real_file, "wb") as fp:
            fp.write(b"data")
        os.symlink(real_file, symlink)

        extract_dir = os.path.join(self.tempdir, "to")
        os.makedirs(extract_dir)

        r_real_file = os.path.join(extract_dir, "foo.txt")
        r_symlink = os.path.join(extract_dir, "symlink")

        # When
        with ZipFile(zipfile, "w") as zp:
            zp.write(symlink, "symlink")
            zp.write(real_file, "foo.txt")

        with ZipFile(zipfile) as zp:
            zp.extractall(extract_dir)

        # Then
        with ZipFile(zipfile) as zp:
            self.assertEqual(len(zp.namelist()), 2)
            self.assertCountEqual(zp.namelist(), ("foo.txt", "symlink"))

        self.assertFalse(os.path.islink(r_real_file))
        self.assertTrue(os.path.islink(r_symlink))
        self.assertTrue(os.readlink(r_symlink), r_real_file)

    @unittest.skipIf(not SUPPORT_SYMLINK,
                     "this platform does not support symlink")
    def test_write_symlink_directory(self):
        # Given
        zipfile = os.path.join(self.tempdir, "foo.zip")
        real_file = os.path.join(self.tempdir, "include", "foo.h")
        symlink = os.path.join(self.tempdir, "HEADERS")

        os.makedirs(os.path.dirname(real_file))
        with open(real_file, "wb") as fp:
            fp.write(b"/* header */")
        os.symlink(os.path.dirname(real_file), symlink)

        extract_dir = os.path.join(self.tempdir, "to")
        os.makedirs(extract_dir)

        r_real_file = os.path.join(extract_dir, "include", "foo.h")
        r_symlink = os.path.join(extract_dir, "HEADERS")

        # When
        with ZipFile(zipfile, "w") as zp:
            zp.write(symlink, "HEADERS")
            zp.write(real_file, "include/foo.h")

        with ZipFile(zipfile) as zp:
            zp.extractall(extract_dir)

        # Then
        with ZipFile(zipfile) as zp:
            self.assertEqual(len(zp.namelist()), 2)
            self.assertCountEqual(zp.namelist(), ("include/foo.h", "HEADERS"))

        self.assertFalse(os.path.islink(r_real_file))
        self.assertTrue(os.path.islink(r_symlink))
        self.assertTrue(os.path.isdir(r_symlink))
        self.assertTrue(os.readlink(r_symlink), r_real_file)

    def test_context_manager(self):
        # Given
        path = NOSE_EGG

        # When/Then
        with ZipFile(path) as zp:
            self.assertIsNotNone(zp.fp)

        # Then
        self.assertIsNone(zp.fp)

        # When/Then
        try:
            with ZipFile(path) as zp:
                raise ValueError("I am failing !")
        except ValueError:
            pass

        # Then
        self.assertIsNone(zp.fp)
