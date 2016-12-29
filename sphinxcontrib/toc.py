# -*- coding: utf-8 -*-

from collections import namedtuple

from docutils import nodes

from sphinx import addnodes
from sphinx.parsers import Parser
from sphinx.util import docname_join

ToC = namedtuple('ToC', ['title', 'entries'])


class TableOfContentsParser(Parser):
    def parse_toc(self, inputstring):
        toc = ToC(None, [])
        for line in inputstring.splitlines():
            entry = line.strip()
            if entry.startswith('#'):
                assert toc.title is None, "The title of ToC appeared twice"
                assert toc.entries == [], "The title of ToC appeared after entries"

                title = entry[1:].strip()
                toc = ToC(title, [])
            elif entry:
                toc.entries.append(entry)

        return toc

    def parse(self, inputstring, document):
        toc = self.parse_toc(inputstring)
        entries = []
        includefiles = []
        for entry in toc.entries:
            docname = docname_join(self.env.docname, self.strip_ext(entry))
            entries.append((None, docname))  # title is always None
            includefiles.append(docname)

        tocnode = addnodes.toctree(parent=self.env.docname, glob=None,
                                   entries=entries, includefiles=includefiles,
                                   maxdepth=self.config.toc_maxdepth)
        if self.env.docname == self.config.master_doc:
            if self.config.toc_numbered is True:
                tocnode['numbered'] = 999  # A magic number of toctree directive
            else:
                tocnode['numbered'] = self.config.toctree_numbered
        else:
            tocnode['numbered'] = False
        wrappernode = nodes.compound(classes=['toctree-wrapper'])
        wrappernode.append(tocnode)
        section = nodes.section()
        if toc.title:
            section += nodes.title(text=toc.title)
        else:
            section += nodes.title(text=self.config.toc_title)
        section += wrappernode
        document.note_implicit_target(section, section)
        document += section

    def strip_ext(self, docname):
        for suffix in self.config.source_suffix:
            if docname.endswith(suffix):
                return docname[:-len(suffix)]

        return docname


def setup(app):
    app.add_config_value('toc_numbered', True, 'html')
    app.add_config_value('toc_title',
                         lambda conf: "%s Documentation" % conf.project,
                         'html')
    app.add_config_value('toc_maxdepth', -1, 'html')
    app.add_source_parser('.toc', TableOfContentsParser)
