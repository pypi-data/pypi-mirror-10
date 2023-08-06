#
# Copyright (C) 2015 Satoru SATOH <ssato at redhat.com>
# License: MIT
#
import os
import unittest

import anytemplate.tests.common

try:
    import anytemplate.engines.mako as TT
except ImportError:
    TT = None


class Test_00_pure_functions(unittest.TestCase):

    def test_20_renders(self):
        tmpl_s = "hello, ${name}!"
        exp = "hello, John!"

        if TT is not None:
            egn = TT.Engine()
            self.assertEquals(egn.renders(tmpl_s, {"name": "John", }), exp)

    def test_22_renders__no_context(self):
        tmpl_s = "hello world!"

        if TT is not None:
            egn = TT.Engine()
            self.assertEquals(egn.renders(tmpl_s), tmpl_s)

    def test_24_renders__no_context__w_at_path(self):
        tmpl_s = "hello world!"

        if TT is not None:
            egn = TT.Engine()
            self.assertEquals(egn.renders(tmpl_s, at_paths=['.']), tmpl_s)

    def test_26_renders__no_context__w_filename(self):
        tmpl_s = "hello world!"

        if TT is not None:
            egn = TT.Engine()
            self.assertEquals(egn.renders(tmpl_s, filename="x"), tmpl_s)


class Test_10_effectful_functions(unittest.TestCase):

    def setUp(self):
        self.workdir = anytemplate.tests.common.setup_workdir()

    def tearDown(self):
        anytemplate.tests.common.cleanup_workdir(self.workdir)

    def test_10_render(self):
        tmpl = "a.t"
        open(os.path.join(self.workdir, tmpl), 'w').write("a = ${a}")

        if TT is not None:
            egn = TT.Engine()
            r = egn.render(tmpl, {'a': "aaa", }, at_paths=[self.workdir])
            self.assertEquals(r, "a = aaa")

    def test_12_render__no_context(self):
        tmpl = os.path.join(self.workdir, "a.t")
        open(tmpl, 'w').write("hello!")

        if TT is not None:
            egn = TT.Engine()
            r = egn.render(tmpl, text="x")
            self.assertEquals(r, "hello!")

# vim:sw=4:ts=4:et:
