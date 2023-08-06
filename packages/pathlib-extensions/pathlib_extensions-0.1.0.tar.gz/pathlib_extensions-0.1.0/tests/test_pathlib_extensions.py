import os
import unittest
from test import test_pathlib, support

from pathlib_extensions import pathlib_extensions


#
# Tests for the pure classes.
#

class _BasePurePathTest(test_pathlib._BasePurePathTest):
    def test_repr_common(self):
        for pathstr in ('a', 'a/b', 'a/b/c', '/', '/a/b', '/a/b/c'):
            p = self.cls(pathstr)
            clsname = p.__class__.__name__
            r = repr(p)
            # The repr() is in the form ClassName("forward-slashes path")
            self.assertTrue(r.startswith(clsname + '('), r)
            self.assertTrue(r.endswith(')'), r)
            inner = r[len(clsname) + 1: -1]
            self.assertEqual(eval(inner), p.as_posix())
            # The repr() roundtrips
            q = eval(r, pathlib_extensions.__dict__)
            self.assertIs(q.__class__, p.__class__)
            self.assertEqual(q, p)
            self.assertEqual(repr(q), r)

    # 3.9+
    if hasattr(test_pathlib._BasePurePathTest, "test_with_stem_common"):
        test_with_stem_common = test_pathlib._BasePurePathTest.test_with_stem_common
    # 3.6-3.8
    else:
        def test_with_stem_common(self):
            P = self.cls
            self.assertEqual(P('a/b').with_stem('d'), P('a/d'))
            self.assertEqual(P('/a/b').with_stem('d'), P('/a/d'))
            self.assertEqual(P('a/b.py').with_stem('d'), P('a/d.py'))
            self.assertEqual(P('/a/b.py').with_stem('d'), P('/a/d.py'))
            self.assertEqual(P('/a/b.tar.gz').with_stem('d'), P('/a/d.gz'))
            self.assertEqual(P('a/Dot ending.').with_stem('d'), P('a/d'))
            self.assertEqual(P('/a/Dot ending.').with_stem('d'), P('/a/d'))
            self.assertRaises(ValueError, P('').with_stem, 'd')
            self.assertRaises(ValueError, P('.').with_stem, 'd')
            self.assertRaises(ValueError, P('/').with_stem, 'd')
            self.assertRaises(ValueError, P('a/b').with_stem, '')
            self.assertRaises(ValueError, P('a/b').with_stem, '/c')
            self.assertRaises(ValueError, P('a/b').with_stem, 'c/')
            self.assertRaises(ValueError, P('a/b').with_stem, 'c/d')

    # 3.9+
    if hasattr(test_pathlib._BasePurePathTest, "test_is_relative_to_common"):
        test_is_relative_to_common = test_pathlib._BasePurePathTest.test_is_relative_to_common
    # 3.6-3.8
    else:
        def test_is_relative_to_common(self):
            P = self.cls
            p = P('a/b')
            self.assertRaises(TypeError, p.is_relative_to)
            self.assertRaises(TypeError, p.is_relative_to, b'a')
            self.assertTrue(p.is_relative_to(P()))
            self.assertTrue(p.is_relative_to(''))
            self.assertTrue(p.is_relative_to(P('a')))
            self.assertTrue(p.is_relative_to('a/'))
            self.assertTrue(p.is_relative_to(P('a/b')))
            self.assertTrue(p.is_relative_to('a/b'))
            # With several args.
            self.assertTrue(p.is_relative_to('a', 'b'))
            # Unrelated paths.
            self.assertFalse(p.is_relative_to(P('c')))
            self.assertFalse(p.is_relative_to(P('a/b/c')))
            self.assertFalse(p.is_relative_to(P('a/c')))
            self.assertFalse(p.is_relative_to(P('/a')))
            p = P('/a/b')
            self.assertTrue(p.is_relative_to(P('/')))
            self.assertTrue(p.is_relative_to('/'))
            self.assertTrue(p.is_relative_to(P('/a')))
            self.assertTrue(p.is_relative_to('/a'))
            self.assertTrue(p.is_relative_to('/a/'))
            self.assertTrue(p.is_relative_to(P('/a/b')))
            self.assertTrue(p.is_relative_to('/a/b'))
            # Unrelated paths.
            self.assertFalse(p.is_relative_to(P('/c')))
            self.assertFalse(p.is_relative_to(P('/a/b/c')))
            self.assertFalse(p.is_relative_to(P('/a/c')))
            self.assertFalse(p.is_relative_to(P()))
            self.assertFalse(p.is_relative_to(''))
            self.assertFalse(p.is_relative_to(P('a')))


class PurePosixPathTest(_BasePurePathTest, unittest.TestCase):
    cls = pathlib_extensions.PurePosixPath


class PureWindowsPathTest(_BasePurePathTest, unittest.TestCase):
    cls = pathlib_extensions.PureWindowsPath

    # 3.9+
    if hasattr(test_pathlib.PureWindowsPathTest, "test_with_stem"):
        test_with_stem = test_pathlib.PureWindowsPathTest.test_with_stem
    # 3.6-3.8
    else:
        def test_with_stem(self):
            P = self.cls
            self.assertEqual(P('c:a/b').with_stem('d'), P('c:a/d'))
            self.assertEqual(P('c:/a/b').with_stem('d'), P('c:/a/d'))
            self.assertEqual(P('c:a/Dot ending.').with_stem('d'), P('c:a/d'))
            self.assertEqual(P('c:/a/Dot ending.').with_stem('d'), P('c:/a/d'))
            self.assertRaises(ValueError, P('c:').with_stem, 'd')
            self.assertRaises(ValueError, P('c:/').with_stem, 'd')
            self.assertRaises(ValueError, P('//My/Share').with_stem, 'd')
            self.assertRaises(ValueError, P('c:a/b').with_stem, 'd:')
            self.assertRaises(ValueError, P('c:a/b').with_stem, 'd:e')
            self.assertRaises(ValueError, P('c:a/b').with_stem, 'd:/e')
            self.assertRaises(ValueError, P('c:a/b').with_stem, '//My/Share')

    # 3.9+
    if hasattr(test_pathlib.PureWindowsPathTest, "test_is_relative_to"):
        test_is_relative_to = test_pathlib.PureWindowsPathTest.test_is_relative_to
    # 3.6-3.8
    else:
        def test_is_relative_to(self):
            P = self.cls
            p = P('C:Foo/Bar')
            self.assertTrue(p.is_relative_to(P('c:')))
            self.assertTrue(p.is_relative_to('c:'))
            self.assertTrue(p.is_relative_to(P('c:foO')))
            self.assertTrue(p.is_relative_to('c:foO'))
            self.assertTrue(p.is_relative_to('c:foO/'))
            self.assertTrue(p.is_relative_to(P('c:foO/baR')))
            self.assertTrue(p.is_relative_to('c:foO/baR'))
            # Unrelated paths.
            self.assertFalse(p.is_relative_to(P()))
            self.assertFalse(p.is_relative_to(''))
            self.assertFalse(p.is_relative_to(P('d:')))
            self.assertFalse(p.is_relative_to(P('/')))
            self.assertFalse(p.is_relative_to(P('Foo')))
            self.assertFalse(p.is_relative_to(P('/Foo')))
            self.assertFalse(p.is_relative_to(P('C:/Foo')))
            self.assertFalse(p.is_relative_to(P('C:Foo/Bar/Baz')))
            self.assertFalse(p.is_relative_to(P('C:Foo/Baz')))
            p = P('C:/Foo/Bar')
            self.assertTrue(p.is_relative_to('c:'))
            self.assertTrue(p.is_relative_to(P('c:/')))
            self.assertTrue(p.is_relative_to(P('c:/foO')))
            self.assertTrue(p.is_relative_to('c:/foO/'))
            self.assertTrue(p.is_relative_to(P('c:/foO/baR')))
            self.assertTrue(p.is_relative_to('c:/foO/baR'))
            # Unrelated paths.
            self.assertFalse(p.is_relative_to(P('C:/Baz')))
            self.assertFalse(p.is_relative_to(P('C:/Foo/Bar/Baz')))
            self.assertFalse(p.is_relative_to(P('C:/Foo/Baz')))
            self.assertFalse(p.is_relative_to(P('C:Foo')))
            self.assertFalse(p.is_relative_to(P('d:')))
            self.assertFalse(p.is_relative_to(P('d:/')))
            self.assertFalse(p.is_relative_to(P('/')))
            self.assertFalse(p.is_relative_to(P('/Foo')))
            self.assertFalse(p.is_relative_to(P('//C/Foo')))
            # UNC paths.
            p = P('//Server/Share/Foo/Bar')
            self.assertTrue(p.is_relative_to(P('//sErver/sHare')))
            self.assertTrue(p.is_relative_to('//sErver/sHare'))
            self.assertTrue(p.is_relative_to('//sErver/sHare/'))
            self.assertTrue(p.is_relative_to(P('//sErver/sHare/Foo')))
            self.assertTrue(p.is_relative_to('//sErver/sHare/Foo'))
            self.assertTrue(p.is_relative_to('//sErver/sHare/Foo/'))
            self.assertTrue(p.is_relative_to(P('//sErver/sHare/Foo/Bar')))
            self.assertTrue(p.is_relative_to('//sErver/sHare/Foo/Bar'))
            # Unrelated paths.
            self.assertFalse(p.is_relative_to(P('/Server/Share/Foo')))
            self.assertFalse(p.is_relative_to(P('c:/Server/Share/Foo')))
            self.assertFalse(p.is_relative_to(P('//z/Share/Foo')))
            self.assertFalse(p.is_relative_to(P('//Server/z/Foo')))


class PurePathTest(_BasePurePathTest, unittest.TestCase):
    cls = pathlib_extensions.PurePath


#
# Tests for the concrete classes.
#

# Make sure any symbolic links in the base test path are resolved.
BASE = test_pathlib.BASE
join = test_pathlib.join
rel_join = test_pathlib.rel_join

only_nt = test_pathlib.only_nt
only_posix = test_pathlib.only_posix


@only_posix
class PosixPathAsPureTest(PurePosixPathTest):
    cls = pathlib_extensions.PosixPath


@only_nt
class WindowsPathAsPureTest(PureWindowsPathTest):
    cls = pathlib_extensions.WindowsPath


class _BasePathTest(test_pathlib._BasePathTest):
    """Tests for the FS-accessing functionalities of the Path classes."""

    # 3.9+
    if hasattr(test_pathlib._BasePathTest, "test_readlink"):
        test_readlink = test_pathlib._BasePathTest.test_readlink
    # 3.6-3.8
    else:
        @support.skip_unless_symlink
        def test_readlink(self):
            P = self.cls(BASE)
            self.assertEqual((P / 'linkA').readlink(), self.cls('fileA'))
            self.assertEqual((P / 'brokenLink').readlink(),
                             self.cls('non-existing'))
            self.assertEqual((P / 'linkB').readlink(), self.cls('dirB'))
            with self.assertRaises(OSError):
                (P / 'fileA').readlink()

    # 3.8+
    if hasattr(test_pathlib._BasePathTest, "test_link_to"):
        test_link_to = test_pathlib._BasePathTest.test_link_to
    # 3.6-3.7
    else:
        @unittest.skipUnless(hasattr(os, "link"), "os.link() is not present")
        def test_link_to(self):
            P = self.cls(BASE)
            p = P / 'fileA'
            size = p.stat().st_size
            # linking to another path.
            q = P / 'dirA' / 'fileAA'
            try:
                p.link_to(q)
            except PermissionError as e:
                self.skipTest('os.link(): %s' % e)
            self.assertEqual(q.stat().st_size, size)
            self.assertEqual(os.path.samefile(p, q), True)
            self.assertTrue(p.stat)
            # Linking to a str of a relative path.
            r = rel_join('fileAAA')
            q.link_to(r)
            self.assertEqual(os.stat(r).st_size, size)
            self.assertTrue(q.stat)

    if hasattr(test_pathlib._BasePathTest, "test_link_to_not_implemented"):
        test_link_to_not_implemented = test_pathlib._BasePathTest.test_link_to_not_implemented
    # 3.6-3.7
    else:
        @unittest.skipIf(hasattr(os, "link"), "os.link() is present")
        def test_link_to_not_implemented(self):
            P = self.cls(BASE)
            p = P / 'fileA'
            # linking to another path.
            q = P / 'dirA' / 'fileAA'
            with self.assertRaises(NotImplementedError):
                p.link_to(q)

    # 3.7+
    if hasattr(test_pathlib._BasePathTest, "test_is_mount"):
        test_is_mount = test_pathlib._BasePathTest.test_is_mount
    # 3.6
    else:
        @only_posix
        def test_is_mount(self):
            P = self.cls(BASE)
            R = self.cls('/')  # TODO: Work out Windows.
            self.assertFalse((P / 'fileA').is_mount())
            self.assertFalse((P / 'dirA').is_mount())
            self.assertFalse((P / 'non-existing').is_mount())
            self.assertFalse((P / 'fileA' / 'bah').is_mount())
            self.assertTrue(R.is_mount())
            if support.can_symlink():
                self.assertFalse((P / 'linkA').is_mount())
            self.assertIs(self.cls('/\udfff').is_mount(), False)
            self.assertIs(self.cls('/\x00').is_mount(), False)


class PathTest(_BasePathTest, unittest.TestCase):
    cls = pathlib_extensions.Path


@only_posix
class PosixPathTest(_BasePathTest, unittest.TestCase):
    cls = pathlib_extensions.PosixPath


@only_nt
class WindowsPathTest(_BasePathTest, unittest.TestCase):
    cls = pathlib_extensions.WindowsPath


if __name__ == '__main__':
    unittest.main()
