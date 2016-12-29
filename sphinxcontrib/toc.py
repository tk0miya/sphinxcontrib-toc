# -*- coding: utf-8 -*-

from docutils import nodes

from sphinx import addnodes
from sphinx.parsers import Parser
from sphinx.util import docname_join


class TableOfContentsParser(Parser):
    def parse(self, inputstring, document):
        entries = []
        includefiles = []
        for docname in inputstring.splitlines():
            docname = self.strip_ext(docname.strip())
            if docname:
                docname = docname_join(self.env.docname, docname)
                entries.append((None, docname))
                includefiles.append(docname)

        toc = addnodes.toctree(parent=self.env.docname, glob=None,
                               entries=entries, includefiles=includefiles,
                               maxdepth=self.config.toc_maxdepth)
        if self.env.docname == self.config.master_doc:
            if self.config.toc_numbered is True:
                toc['numbered'] = 999  # A magic number of toctree directive
            else:
                toc['numbered'] = self.config.toctree_numbered
        else:
            toc['numbered'] = False
        wrappernode = nodes.compound(classes=['toctree-wrapper'])
        wrappernode.append(toc)
        section = nodes.section()
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
