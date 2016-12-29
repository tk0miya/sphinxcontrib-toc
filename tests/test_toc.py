# -*- coding: utf-8 -*-
import unittest
from sphinx_testing import with_app


class TestCase(unittest.TestCase):
    @with_app(srcdir='tests/template')
    def test_toc(self, app, status, warnings):
        app.build()

        content = (app.outdir / 'index.html').read_text()
        self.assertIn('href="part1.html">1. Part1', content)
        self.assertIn('href="part2.html">2. Part2', content)
        self.assertIn('href="part3/index.html">3. Part3', content)
        self.assertIn('href="part3/section1.html">3.1. Part3 - section1', content)
        self.assertIn('href="part3/section2.html">3.2. Part3 - section2', content)

        content = (app.outdir / 'part3' / 'index.html').read_text()
        self.assertIn('href="section1.html">3.1. Part3 - section1', content)
        self.assertIn('href="section2.html">3.2. Part3 - section2', content)
