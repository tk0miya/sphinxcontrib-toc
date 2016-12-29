# -*- coding: utf-8 -*-
import unittest
from sphinx_testing import with_app


class TestCase(unittest.TestCase):
    @with_app(srcdir='tests/template')
    def test_toc(self, app, status, warnings):
        app.build()

        content = (app.outdir / 'index.html').read_text()
        self.assertIn('href="section1.html">1. Section1', content)
        self.assertIn('href="section2.html">2. Section2', content)
        self.assertIn('href="section3/index.html">3. Python Documentation', content)
        self.assertIn('href="section3/part1.html">3.1. Section3 - part1', content)
        self.assertIn('href="section3/part2.html">3.2. Section3 - part2', content)

        content = (app.outdir / 'section3' / 'index.html').read_text()
        self.assertIn('href="part1.html">3.1. Section3 - part1', content)
        self.assertIn('href="part2.html">3.2. Section3 - part2', content)
