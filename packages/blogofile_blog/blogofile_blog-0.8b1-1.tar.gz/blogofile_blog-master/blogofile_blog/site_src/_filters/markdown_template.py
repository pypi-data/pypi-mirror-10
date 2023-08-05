# -*- coding: utf-8 -*-
import markdown
import logging
from blogofile.cache import HierarchicalCache as HC

"""
A markdown filter - see http://daringfireball.net/projects/markdown

Extensions (http://www.freewisdom.org/projects/python-markdown/Extensions)
are disabled by default, but can be turned on in _config.py:

filters.markdown.extensions.def_list.enabled    = True
filters.markdown.extensions.abbr.enabled        = True
filters.markdown.extensions.footnotes.enabled   = True
filters.markdown.extensions.fenced_code.enabled = True
filters.markdown.extensions.headerid.enabled    = True
filters.markdown.extensions.tables.enabled      = True
"""

meta = {
    "name": "Markdown",
    "author": "Ryan McGuire",
    "description": "Renders markdown formatted text to HTML"
    }

config = HC(
    aliases = ["markdown"],
    extensions = HC(def_list    = HC(enabled=False),
                    abbr        = HC(enabled=False),
                    footnotes   = HC(enabled=False),
                    fenced_code = HC(enabled=False),
                    headerid    = HC(enabled=False),
                    tables      = HC(enabled=False)),
    extension_parameters = HC(headerid = HC(level=1,forceid=True))
    )

#Markdown logging is noisy, pot it down:
logging.getLogger("MARKDOWN").setLevel(logging.ERROR)

extensions = []

def init():
    #Create the list of enabled extensions with their arguments
    for name, ext in list(config["extensions"].items()):
        if ext.enabled:
            params = []
            if name in config["extension_parameters"]:
                p = config["extension_parameters"][name]
            else:
                extensions.append(name)
                continue
            for param,value in list(p.items()):
                params.append(param+"="+repr(value))
            extensions.append(name+"("+",".join(params)+")")

def run(content):
    return markdown.markdown(content, extensions)
