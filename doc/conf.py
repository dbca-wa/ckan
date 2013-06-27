# -*- coding: utf-8 -*-
#
# CKAN documentation build configuration file, created by
# sphinx-quickstart on Sun Oct 25 16:47:17 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If your extensions (or modules documented by autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

rst_epilog = '''

.. |virtualenv_parent_dir| replace:: /usr/lib/ckan
.. |virtualenv| replace:: |virtualenv_parent_dir|/default
.. |activate| replace:: . |virtualenv|/bin/activate
.. |config_parent_dir| replace:: /etc/ckan
.. |config_dir| replace:: |config_parent_dir|/default
.. |production.ini| replace:: |config_dir|/production.ini
.. |development.ini| replace:: |config_dir|/development.ini
.. |git_url| replace:: https://github.com/okfn/ckan.git
.. |postgres| replace:: PostgreSQL
.. |database| replace:: ckan_default
.. |database_user| replace:: ckan_default
.. |datastore| replace:: datastore_default
.. |datastore_user| replace:: datastore_default
.. |test_database| replace:: ckan_test
.. |test_datastore| replace:: datastore_test
.. |apache_config_file| replace:: /etc/apache2/sites-available/ckan_default
.. |apache.wsgi| replace:: |config_dir|/apache.wsgi
.. |data_dir| replace:: |config_dir|/data
.. |sstore| replace:: |config_dir|/sstore
.. |storage_parent_dir| replace:: /var/lib/ckan
.. |storage_dir| replace:: |storage_parent_dir|/default
.. |reload_apache| replace:: sudo service apache2 reload
.. |solr| replace:: Solr
.. |restructuredtext| replace:: reStructuredText
.. |nginx| replace:: Nginx
.. |sqlite| replace:: SQLite
.. |python| replace:: Python
.. |sqlalchemy| replace:: SQLAlchemy
.. |javascript| replace:: JavaScript
.. |apache| replace:: Apache

'''

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'ckan.lib.sphinx_extensions']

autodoc_member_order = 'bysource'

todo_include_todos = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'CKAN Documentation'
project_short_name = u'CKAN'
copyright = u'''&copy; 2009-2012, <a href="http://okfn.org/">Open Knowledge Foundation</a>.
    Licensed under <a
    href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons
    Attribution ShareAlike (Unported) v3.0 License</a>.<br />
    <img src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" alt="CC License Logo" />
    <a href="http://opendefinition.org/"><img src="http://assets.okfn.org/images/ok_buttons/oc_80x15_blue.png" border="0" 
      alt="{{ _('Open Content') }}" /></a>
  '''
html_show_sphinx = False

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import ckan
version = ckan.__version__.rstrip('abcdefgh')
# The full version, including alpha/beta/rc tags.
release = ckan.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['.build']

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


# Options for HTML output
# -----------------------

#html_theme = 'default'
#html_theme_options = {
#"relbarbgcolor": "#777",
#'sidebarbgcolor': '#F2F2F2',
#'sidebartextcolor': 'black',
#'sidebarlinkcolor': '#355F7C',
#'headfont': 'Trebuchet MS'    
#}
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'sphinx-theme-okfn'
html_theme_options = {
        'logo_icon': 'http://assets.okfn.org/p/opendatahandbook/img/data-wrench-inverted.png',
        'show_version': True
    }

html_sidebars = {
    '**':  ['relations.html', 'globaltoc.html'],
    # There's no point in showing the table of contents in the sidebar on the
    # table of contents page! So:
    'index': ['relations.html'],
}

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = "%s v%s Guide" % (project, release)

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = "%s Admin Guide" % (project_short_name)

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = 'images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'ComprehensiveKnowledgeArchiveNetworkCKANdoc'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'ComprehensiveKnowledgeArchiveNetworkCKAN.tex', ur'Comprehensive Knowledge Archive Network (CKAN) Developer Documentation',
   ur'Open Knowledge Foundation', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
