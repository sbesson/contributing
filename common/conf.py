#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ome documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 22 20:24:38 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime
import sys, os
sys.path.insert(0, os.path.abspath('../_ext'))

def split_release(release):
    import re
    split_release =  re.split("^([0-9]+)\.([0-9]+)\.([0-9]+)(.*?)$", release)
    return (int(split_release[1]), int(split_release[2]), int(split_release[3]))

def get_previous_version(majornumber, minornumber=0):
    # Return the previous version number for the first minor versions of a
    # major series i.e. x.0.y
    # Implemented as an hard-coded list until we work out an automated way to
    # upgrade the database without specifying version numbers e.g.
    # bin/omero db upgrade
    if minornumber == 0:
        if majornumber == 5:
            return "4.4"
        elif majornumber == 4:
            return "3.2"
        else:
            raise Exception("No previous version defined for %s.%s"
                            % (majornumber, minornumber))
    else:
        return "%s.%s" % (majornumber, minornumber - 1)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.)
extensions = ['sphinx.ext.extlinks', 'edit_on_github']

# Configuration for the edit_on_github extension
edit_on_github_project = 'openmicroscopy/ome-documentation'
edit_on_github_branch = 'dev_5_0'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
author = u'The Open Microscopy Environment'
copyright = u'2000-%d, ' % datetime.datetime.now().year + author

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'downloads']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Variables used to define Github extlinks
if "SOURCE_BRANCH" in os.environ and len(os.environ.get('SOURCE_BRANCH')) > 0:
    branch = os.environ.get('SOURCE_BRANCH')
else:
    branch = 'develop'

if "SOURCE_USER" in os.environ and len(os.environ.get('SOURCE_USER')) > 0:
    user = os.environ.get('SOURCE_USER')
else:
    user = 'openmicroscopy'

github_root = 'https://github.com/'
omero_github_root = github_root + user + '/openmicroscopy/'
bf_github_root = github_root + user + '/bioformats/'
doc_github_root = github_root + user + '/ome-documentation/'

# Variables used to define Jenkins extlinks
jenkins_root = 'http://ci.openmicroscopy.org'
jenkins_job_root = jenkins_root + '/job'
jenkins_view_root = jenkins_root + '/view'

# Variables used to define other extlinks
cvs_root = 'http://cvs.openmicroscopy.org.uk'
trac_root = 'http://trac.openmicroscopy.org.uk/ome'
oo_root = 'http://www.openmicroscopy.org'
oo_site_root = oo_root + '/site'
lists_root = 'http://lists.openmicroscopy.org.uk'
downloads_root = 'http://downloads.openmicroscopy.org'
help_root = 'http://help.openmicroscopy.org'

extlinks = {
    # Trac links
    'ticket' : (trac_root + '/ticket/%s', '#'),
    'milestone' : (trac_root + '/milestone/%s', ''),
    'report' : (trac_root + '/report/%s', ''),
    # Jenkins links
    'jenkins' : (jenkins_root + '/%s', ''),
    'jenkinsjob' : (jenkins_job_root + '/%s', ''),
    'jenkinsview' : (jenkins_view_root + '/%s', ''),
    # Mailing list/forum links
    'mailinglist' : (lists_root + '/mailman/listinfo/%s', ''),
    'ome-users' : (lists_root + '/pipermail/ome-users/%s' ,''),
    'ome-devel' : (lists_root + '/pipermail/ome-devel/%s' ,''),
    'forum' : (oo_root + '/community/%s', ''),
    # Plone links. Separating them out so that we can add prefixes and
    # suffixes during testing.
    'community_plone' : (oo_site_root + '/community/%s', ''),
    'legacy_plone' : (oo_site_root + '/support/previous/%s', ''),
    'about_plone' : (oo_site_root + '/about/%s', ''),
    'team_plone' : (oo_site_root + '/team/%s', ''),
    'faq_plone' : (oo_site_root + '/support/faq/%s', ''),
    'training_plone' : (oo_site_root + '/support/training/%s', ''),
    'schema_plone' : (oo_root + '/Schemas/%s', ''),
    'omero_plone' : (oo_site_root + '/products/omero/%s', ''),
    'omero_doc' : (oo_site_root + '/support/omero5/%s', ''),
    'model_doc' : (oo_site_root + '/support/ome-model/%s', ''),
    'devs_doc' : (oo_site_root + '/support/contributing/%s', ''),
    'bf_plone' : (oo_site_root + '/products/bio-formats/%s', ''),
    'bf_doc' : (oo_site_root + '/support/bio-formats5/%s', ''),
    'partner_plone' : (oo_site_root + '/products/partner/%s', ''),
    # Downloads
    'downloads' : (downloads_root + '/latest/omero5/%s', ''),
    'bf_downloads' : (downloads_root + '/latest/bio-formats5/%s', ''),
    # Help links
    'help' : (help_root + '/%s', ''),
    # Miscellaneous links
    'snapshot' : (cvs_root + '/snapshots/%s', ''),
    'zeroc' : ('http://zeroc.com/%s', ''),
    'zerocdoc' : ('http://doc.zeroc.com/%s', ''),
    'doi' : ('http://dx.doi.org/%s', ''),
    }

rst_epilog = """
.. _Hibernate: http://www.hibernate.org
.. _ZeroC: http://www.zeroc.com
.. _Ice: http://www.zeroc.com
.. _Jenkins: http://jenkins-ci.org
.. _roadmap: https://trac.openmicroscopy.org.uk/ome/roadmap
.. _Open Microscopy Environment: http://www.openmicroscopy.org/site
.. _Glencoe Software, Inc.: http://www.glencoesoftware.com/
.. _Pillow: http://pillow.readthedocs.org
.. _Matplotlib: http://matplotlib.org/
.. _Python: http://python.org
.. _Libjpeg: http://libjpeg.sourceforge.net/

.. |SSH| replace:: :abbr:`SSH (Secure Shell)`
.. |VM| replace:: :abbr:`VM (Virtual Machine)`
.. |OS| replace:: :abbr:`OS (Operating System)`
.. |SSL| replace:: :abbr:`SSL (Secure Socket Layer)`
.. |HDD| replace:: :abbr:`HDD (Hard Disk Drive)`
.. |CLI| replace:: :abbr:`CLI (Command Line Interface)`

.. |OME| replace:: `Open Microscopy Environment`_
.. |Glencoe| replace:: `Glencoe Software, Inc.`_
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../common/themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = { '**' : ['pagetoc.html', 'relations.html', 'searchbox.html', 'sourcelink.html'] }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'projstandardsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    'classoptions': ',oneside',
    'pointsize': '10pt',
    'inputenc': '%% Unused',
    'utf8extra': '%% Unused',
    'fontenc' : '%% Unused',
    'fontpkg': '%% Unused',
    'babel': '%% Unused',
    'printindex': '''\\phantomsection
\\addcontentsline{toc}{part}{\indexname}
\\printindex''',
    'preamble': '''
\input{../../../common/preamble.tex}
''',
}

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for the linkcheck builder ----------------------------------------

# Timeout value, in seconds, for the linkcheck builder
if not (sys.version_info[0] == 2 and sys.version_info[1] <= 5):
    linkcheck_timeout = 30

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore = []
import urllib
brokenfiles_url = 'https://raw.github.com/openmicroscopy/sphinx-ignore-links/master/broken_links.txt'
try:
   brokenlinks = urllib.urlopen(brokenfiles_url)
   linkcheck_ignore.extend(brokenlinks.read().splitlines())
except IOError:
    print "Could not open list of broken links."

# -- Custom roles for the OMERO documentation -----------------------------------------------

from docutils import nodes
from sphinx import addnodes

def omero_command_role(typ, rawtext, etext, lineno, inliner,
                     options={}, content=[]):
    """Role for CLI commands that generates an index entry."""

    env = inliner.document.settings.env
    targetid = 'cmd-%s' % env.new_serialno('index')

    # Create index and target nodes
    indexnode = addnodes.index()
    targetnode = nodes.target('', '', ids=[targetid])
    inliner.document.note_explicit_target(targetnode)
    indexnode['entries'] = [('single', "omero " + "; ".join(etext.split(" ")), targetid, '')]

    # Mark the text using literal node
    sn = nodes.literal('omero ' + etext, 'omero ' +  etext)
    return [indexnode, targetnode, sn], []

def setup(app):
    app.add_role('omerocmd', omero_command_role)
