"""
LDAvis URLs
==========
URLs and filepaths for the LDAvis javascript libraries
"""

import os
from . import __path__, __version__
import warnings

__all__ = ["D3_URL", "LDAVIS_URL", "LDAVISMIN_URL", "LDAVIS_CSS_URL",
           "D3_LOCAL", "LDAVIS_LOCAL", "LDAVISMIN_LOCAL", "LDAVIS_CSS_LOCAL"]

D3_URL = "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"

# for dev
#WWW_JS_DIR = "https://rawgit.com/bmabey/pyLDAvis/master/pyLDAvis/js/"
# for stable releases
WWW_JS_DIR = "https://cdn.rawgit.com/bmabey/pyLDAvis/master/pyLDAvis/js/"

LDAVIS_URL = WWW_JS_DIR + "ldavis.v{0}.js".format(__version__)
LDAVISMIN_URL = LDAVIS_URL
LDAVIS_CSS_URL = WWW_JS_DIR + "ldavis.v{0}.css".format(__version__)

LOCAL_JS_DIR = os.path.join(__path__[0], "js")
D3_LOCAL = os.path.join(LOCAL_JS_DIR, "d3.v3.min.js")
LDAVIS_LOCAL = os.path.join(LOCAL_JS_DIR,
                           "ldavis.v{0}.js".format(__version__))

LDAVIS_CSS_LOCAL = os.path.join(LOCAL_JS_DIR,
                           "ldavis.v{0}.css".format(__version__))
LDAVISMIN_LOCAL = os.path.join(LOCAL_JS_DIR,
                              "ldavis.v{0}.min.js".format(__version__))
