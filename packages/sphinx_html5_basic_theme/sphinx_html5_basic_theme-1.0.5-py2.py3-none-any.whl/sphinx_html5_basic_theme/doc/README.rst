Sphinx HTML5 basic theme
========================

.. caution::

   'html5_sphinxdoc' will not work until the `bug <https://github.com/sphinx-doc/sphinx/issues/1884>`_ is resolved.
   'html5_basic' theme and 'sphinx_html5_translator' extension go fine.

   If you want to use 'html5_sphinxdoc', add the path to 'html_theme'. see 'doc/conf.py'.

.. note::

   Japanese version of this document is also available, on the `site <http://h12u.com/sphinx/html5_basic_theme/README_ja.html>`_ or the doc folder of this package.

.. role:: fn_rst

Introduction
------------
Currently, May 6, 2015, Sphinx 1.3.1 cannot generate valid HTML5 files\ [#f1]_\ .

This package includes HTML5 and CSS3 versions of the two standard themes,
*basic* and *sphinxdoc*.
And one extension, named :fn_rst:`sphinx_html5_translator(.py)`.

By using them, you can generate HTML files that will pass the validator. Enjoy!

License
-------
BSD, same as the Sphinx project itself.
(All files are intend to enable merge or enable overwrite the Sphinx project for the future.)

Installation
------------
You can install or uninstall this package like another Python packages.
Also, you can use this package without installing this package on your Python
systems, the configuration file of Sphinx(:fn_rst:`conf.py`) enable you to use.

Requirements
............
- Sphinx 1.3 compatible

  - docutils 0.12 compatible
  - note that their changes may or may not break the functionality of the code in this packages, as the one in another packages may.

- tested with: 32bit version of Python 2.7.9 and 64bit version of 3.4.3, both on the Microsoft Windows 8.1 Pro 64bit edition
  - but with another versions and on another OSs would be usable

How to install
..............
Again, you can install this package as you will do with another one.

#. Open a console and do :code:`pip install sphinx_html5_basic_theme`.

   On the MS-Windows,
   :code:`<python_installed_path>\Scripts\pip.exe install sphinx_html5_basic_theme`.

#. Or when you get zip archive like :fn_rst:`sphinx_html5_basic_theme-1.0.5(.zip)`
   where '1.0.5' is version number,
   change current directiory to the folder that has the zip file,
   and do :code:`pip install sphinx_html5_basic_theme-1.0.5.zip`.

   On the MS-Windows,
   :code:`<python_installed_path>\Scripts\pip.exe install sphinx_html5_basic_theme-1.0.5.zip`.

#. Or, this way is the Sphinx specific, you can use this package just extracted
   any folder you want. the :fn_rst:`conf.py` enables you to use the themes and
   extensions.

How to use
----------

Do you already know how to `switch HTML theme <http://sphinx-doc.org/theming.html>`_
and to `use extension <http://sphinx-doc.org/extensions.html>`_ ?
if not, learn them first.

1) set the html5 theme
......................
At first, you should choice the theme :code:`html5_basic` or
:code:`html5_sphinxdoc`. The latter refers the former, but you
don't have to care about that as the structure of the folders resolves.

On the :fn_rst:`conf.py` in your project(s), fix :code:`html_theme` like
:code:`html_theme = 'html5_sphinxdoc'` as you choise.

If you want to use this package just extracted zip and not
installed on your python system, you should do more, add
:code:`html_theme_path = ['<path_to_(themes_)folder>',]`.

.. note::

   As described the top of this document, you should declare
   :code:`html_theme_path` anyway, above until the bug is fixed.

2) set the html5 translator extension
.....................................
Second, you should use the extension :fn_rst:`sphinx_html5_translator(.py)`.
Because some invalid tags and attributes are emitted by docutils.

to use :fn_rst:`sphinx_html5_translator`, you should add the path to the 
extension to :code:`sys.path` like below, at the early part of your
:fn_rst:`conf.py`. This part is different whether this package is installed
on the Python system or not.

After that, set the extension as :code:`extension = ['sphinx_html5_translator', ]`.
Of course you can add another extensions you want to use.

Add the path for installed this package:

.. code-block:: python

  # add 3 lines below
  import distutils.sysconfig
  site_package_path = distutils.sysconfig.get_python_lib()
  sys.path.insert(0, os.path.join(site_package_path, 'sphinx_html5_basic_theme'))

and for not installed this package:

.. code-block:: python

  # add just 1 line below
  sys.path.insert(0, '<path_to_(extensions_)folder>')

Note that :code:`<path_to_(themes_)forder>` and :code:`<path_to_(extensions_)folder>`
is same as the case of this package.

.. note::

  If you don't mind or want to do, you can copy the file
  :fn_rst:`sphinx_html5_translator.py` to the folder you want, 
  add :code:`sys.path.insert(0, '<the_folder_you_copied_the_extension_file>')`,
  and set the valuable :code:`extension` like above.

Changes against html4 version
-----------------------------
- Uses CSS3, but some modules are not W3C Reccomendation yet.

  - `Flexible Box Layout Module Level 1 <http://www.w3.org/TR/css-flexbox-1/>`_ is last call working draft
  - `Multi-column Layout Module <http://www.w3.org/TR/css3-multicol/>`_ is cadidate reccomendation

- Flexible Box Layouts used

  - relational navigations
  - sidebar box and main contents box
  - input box and go button in quick search

- Multi-column Layout used

  - :fn_rst:`genindex.html`. you can change column count with style sheet.

- sidebarwidth is now accepts unit postfix, like :code:`"50em"`
- the sidebar is displayed even sphinx_html5_basic
- width defition of the quick search button is deleted. that is too narrow to show the translations of 'Go !'
- :code:`table.indextable` is replaced with Flexible Box Layout. The new style :code:`genindex-multi-columens` is added.
- Some brakets and markers are removed, intend to use style sheets.

  - relational navigations (:code:`»` and :code:`|`)
  - separators between head characters in index pages(:code:`|`)
  - brakets with footnote and common named index(:code:`[` and :code:`]`)

- :code:`{% block searchtip %}` is defined, to replace the description of the quick search
- :code:`{% block extra_footer %}` is defined, to append something at last of the footer
- :code:`{% expired_html_link %}` is defined and emit nothing. :code:`top` and :code:`up` is obsoleted.
- images used with sphinxdoc theme is deleted. altered with style sheet.
- the separator lines designed with sphinxdoc now always touch the top of the footer, even when the main content is too short.

Author
------
Suzumizaki-Kimitaka, 2015-04-30

Related products
----------------
- unicode_ids_

  - enable the Sphinx to generate URL with Non-ASCII characters.

History
-------
1.0.5(2015-06-19):

  - add wheel build for install.
  - work around added in doc/conf.py until resolve the bug of Sphinx.
  - work around against setup.py due to the bug of pip running on Python 3.
    see https://github.com/pypa/pip/pull/2916

1.0.4(2015-05-25):

  fix document about the project extension folder.

1.0.3(2015-05-10):

  fix how to use chapter.

1.0.2(2015-05-10):

  Re-upload

1.0.1(2015-05-10):

  Add README.rst to doc folder that lost from the previous version.

1.0.0(2015-05-09):

  First release. All files are copied at first from Sphinx 1.3.1 and
  docutils 0.12 with Python 2.7.9 and 3.4.3 on Microsoft Windows 8.1 Pro 64bit.

  the themes html5_basic and html5_sphinxdoc are released.
  the extension sphinx_html5_translator is released.

.. rubric:: Footnote

.. [#f1] `W3C Markup Validation Service <https://validator.w3.org/>`_

.. _unicode_ids: https://pypi.python.org/pypi/unicode_ids
