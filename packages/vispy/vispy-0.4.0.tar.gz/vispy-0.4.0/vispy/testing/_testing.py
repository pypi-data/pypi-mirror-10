# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from __future__ import print_function

import numpy as np
import sys
import os
import inspect

from distutils.version import LooseVersion

from ..ext.six import string_types
from ..util import use_log_level

###############################################################################
# Adapted from Python's unittest2
# http://docs.python.org/2/license.html

try:
    from unittest.case import SkipTest
except ImportError:
    try:
        from unittest2.case import SkipTest
    except ImportError:
        class SkipTest(Exception):
            pass


def _safe_rep(obj, short=False):
    """Helper for assert_* ports"""
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
    if not short or len(result) < 80:
        return result
    return result[:80] + ' [truncated]...'


def _safe_str(obj):
    """Helper for assert_* ports"""
    try:
        return str(obj)
    except Exception:
        return object.__str__(obj)


def _format_msg(msg, std_msg):
    """Helper for assert_* ports"""
    if msg is None:
        msg = std_msg
    else:
        try:
            msg = '%s : %s' % (std_msg, msg)
        except UnicodeDecodeError:
            msg = '%s : %s' % (_safe_str(std_msg), _safe_str(msg))
    return msg


def nottest(func):
    """Decorator to mark a function or method as *not* a test
    """
    func.__test__ = False
    return func


def assert_raises(exp, func, *args, **kwargs):
    """Backport"""
    try:
        func(*args, **kwargs)
    except exp:
        return
    std_msg = '%s not raised' % (_safe_rep(exp))
    raise AssertionError(_format_msg(None, std_msg))


def assert_in(member, container, msg=None):
    """Backport"""
    if member in container:
        return
    std_msg = '%s not found in %s' % (_safe_rep(member), _safe_rep(container))
    raise AssertionError(_format_msg(msg, std_msg))


def assert_true(x, msg=None):
    """Backport"""
    if x:
        return
    std_msg = '%s is not True' % (_safe_rep(x),)
    raise AssertionError(_format_msg(msg, std_msg))


def assert_equal(x, y, msg=None):
    """Backport"""
    if x == y:
        return
    std_msg = '%s not equal to %s' % (_safe_rep(x), _safe_rep(y))
    raise AssertionError(_format_msg(msg, std_msg))


def assert_not_equal(x, y, msg=None):
    """Backport"""
    if x != y:
        return
    std_msg = '%s equal to %s' % (_safe_rep(x), _safe_rep(y))
    raise AssertionError(_format_msg(msg, std_msg))


def assert_not_in(member, container, msg=None):
    """Backport"""
    if member not in container:
        return
    std_msg = '%s found in %s' % (_safe_rep(member), _safe_rep(container))
    raise AssertionError(_format_msg(msg, std_msg))


def assert_is(expr1, expr2, msg=None):
    """Backport"""
    if expr1 is not expr2:
        std_msg = '%s is not %s' % (_safe_rep(expr1), _safe_rep(expr2))
        raise AssertionError(_format_msg(msg, std_msg))


###############################################################################
# GL stuff

def has_pyopengl():
    try:
        from OpenGL import GL  # noqa, analysis:ignore
    except Exception:
        return False
    else:
        return True


def requires_pyopengl():
    return np.testing.dec.skipif(not has_pyopengl(), 'Requires PyOpenGL')


###############################################################################
# App stuff

def has_backend(backend, has=(), capable=(), out=()):
    from ..app.backends import BACKENDMAP
    using = os.getenv('_VISPY_TESTING_APP', None)
    if using is not None and using != backend:
        # e.g., we are on  a 'pyglet' run but the test requires PyQt4
        ret = (False,) if len(out) > 0 else False
        for o in out:
            ret += (None,)
        return ret

    # let's follow the standard code path
    module_name = BACKENDMAP[backend.lower()][1]
    with use_log_level('warning', print_msg=False):
        mod = __import__('app.backends.%s' % module_name, globals(), level=2)
    mod = getattr(mod.backends, module_name)
    good = mod.testable
    for h in has:
        good = (good and getattr(mod, 'has_%s' % h))
    for cap in capable:
        good = (good and mod.capability[cap])
    ret = (good,) if len(out) > 0 else good
    for o in out:
        ret += (getattr(mod, o),)
    return ret


def has_application(backend=None, has=(), capable=()):
    """Determine if a suitable app backend exists"""
    from ..app.backends import BACKEND_NAMES
    # avoid importing other backends if we don't need to
    if backend is None:
        for backend in BACKEND_NAMES:
            if has_backend(backend, has=has, capable=capable):
                good = True
                msg = backend
                break
        else:
            good = False
            msg = 'Requires application backend'
    else:
        good, why = has_backend(backend, has=has, capable=capable,
                                out=['why_not'])
        if not good:
            msg = 'Requires %s: %s' % (backend, why)
        else:
            msg = backend
    return good, msg


def composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco


def requires_application(backend=None, has=(), capable=()):
    """Return a decorator for tests that require an application"""
    good, msg = has_application(backend, has, capable)
    dec_backend = np.testing.dec.skipif(not good, "Skipping test: %s" % msg)
    try:
        import pytest
    except Exception:
        return dec_backend
    dec_app = pytest.mark.vispy_app_test
    return composed(dec_app, dec_backend)


def requires_img_lib():
    """Decorator for tests that require an image library"""
    from ..io import _check_img_lib
    if sys.platform.startswith('win'):
        has_img_lib = False  # PIL breaks tests on windows (!)
    else:
        has_img_lib = not all(c is None for c in _check_img_lib())
    return np.testing.dec.skipif(not has_img_lib, 'imageio or PIL required')


def has_matplotlib(version='1.2'):
    """Determine if mpl is a usable version"""
    try:
        import matplotlib
    except Exception:
        has_mpl = False
    else:
        if LooseVersion(matplotlib.__version__) >= LooseVersion(version):
            has_mpl = True
        else:
            has_mpl = False
    return has_mpl


###############################################################################
# Visuals stuff

def _has_scipy(min_version):
    try:
        assert isinstance(min_version, string_types)
        import scipy  # noqa, analysis:ignore
        from distutils.version import LooseVersion
        this_version = LooseVersion(scipy.__version__)
        if this_version < min_version:
            return False
    except Exception:
        return False
    else:
        return True


def requires_scipy(min_version='0.13'):
    return np.testing.dec.skipif(not _has_scipy(min_version),
                                 'Requires Scipy version >= %s' % min_version)


@nottest
def TestingCanvas(bgcolor='black', size=(100, 100), dpi=None, **kwargs):
    """Class wrapper to avoid importing scene until necessary"""
    from ..scene import SceneCanvas

    class TestingCanvas(SceneCanvas):
        def __init__(self, bgcolor, size, dpi, **kwargs):
            self._entered = False
            kwargs['bgcolor'] = bgcolor
            kwargs['size'] = size
            kwargs['dpi'] = dpi
            SceneCanvas.__init__(self, **kwargs)

        def __enter__(self):
            SceneCanvas.__enter__(self)
            # sometimes our window can be larger than our requsted draw
            # area (e.g. on Windows), and this messes up our tests that
            # typically use very small windows. Here we "fix" it.
            scale = np.array(self.physical_size) / np.array(self.size, float)
            scale = int(np.round(np.mean(scale)))
            self._wanted_vp = 0, 0, size[0] * scale, size[1] * scale
            self.context.set_state(clear_color=self._bgcolor)
            self.context.set_viewport(*self._wanted_vp)
            self._entered = True
            return self

        def draw_visual(self, visual, event=None, viewport=None, clear=True):
            if not self._entered:
                return
            if clear:
                self.context.clear()
            SceneCanvas.draw_visual(self, visual, event, viewport)
            # must set this because draw_visual sets it back to the
            # canvas size when it's done
            self.context.set_viewport(*self._wanted_vp)
            self.context.finish()

    return TestingCanvas(bgcolor, size, dpi, **kwargs)


@nottest
def save_testing_image(image, location):
    from ..gloo.util import _screenshot
    from ..util import make_png
    if image == "screenshot":
        image = _screenshot(alpha=False)
    with open(location+'.png', 'wb') as fid:
        fid.write(make_png(image))


@nottest
def run_tests_if_main():
    """Run tests in a given file if it is run as a script"""
    local_vars = inspect.currentframe().f_back.f_locals
    if not local_vars.get('__name__', '') == '__main__':
        return
    # we are in a "__main__"
    fname = local_vars['__file__']
    # Run ourselves. post-mortem debugging!
    try:
        import faulthandler
        faulthandler.enable()
    except Exception:
        pass
    import __main__
    try:
        import pytest
        pytest.main(['-s', '--tb=short', fname])
    except ImportError:
        print('==== Running tests in script\n==== %s' % fname)
        run_tests_in_object(__main__)
        print('==== Tests pass')


def run_tests_in_object(ob):
    # Setup
    for name in dir(ob):
        if name.lower().startswith('setup'):
            print('Calling %s' % name)
            getattr(ob, name)()
    # Exec
    for name in sorted(dir(ob), key=lambda x: x.lower()):  # consistent order
        val = getattr(ob, name)
        if name.startswith('_'):
            continue
        elif callable(val) and (name[:4] == 'test' or name[-4:] == 'test'):
            print('Running test-func %s ... ' % name, end='')
            try:
                val()
                print('ok')
            except Exception as err:
                if 'skiptest' in err.__class__.__name__.lower():
                    print('skip')
                else:
                    raise
        elif isinstance(val, type) and 'Test' in name:
            print('== Running test-class %s' % name)
            run_tests_in_object(val())
            print('== Done with test-class %s' % name)
    # Teardown
    for name in dir(ob):
        if name.lower().startswith('teardown'):
            print('Calling %s' % name)
            getattr(ob, name)()
