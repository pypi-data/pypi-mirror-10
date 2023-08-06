gosyu extension
===============

.. note::

   Japanese version of this document is also available, on the `site
   <http://h12u.com/sphinx/gosyu/README_ja.html>`_ or the doc
   folder of this package.

.. role:: fn_rst

Introduction
------------
Currently, June 7, 2015, Sphinx 1.3.1 sorts indices *only* with
'Normalization Form Canonical Decomposition(NFD)'. And what is worse,
grouping is done *only* with US-ASCII. There is non or few problems 
when you use the language similar to English, because the NFD method
decompose diacritical marks.

But with the other languages, the grouping is useless. Almost all
characters are grouped into 'Symbols'. What a meaningless behavior
it is!

I don't know what happens with each language in the world, but one 
of the worst might be Japanese case. The many terms are written with
kanzi (kanji, 漢字, Chinese characters), and the sorting should be
done by how to read, that generally cannot be defined from the
characters of the terms.

This extension tries to resolve these problems above, using sortorder_.
Not only with these problematic languages, you can define the alternate
sort order for any language you want.

Sorry to say, this extension can resolve :code:`.. glossary::` directive
only, by replacing with :code:`.. gosyu::` one. Other directives like
:code:`index` would be resolved with future release. 

License
-------
2-clause BSD, same as the Sphinx project.

Installation
------------
You can install or uninstall this package like another Python packages.
Also, you can use this package without installing this package on your Python
systems, the configuration file of Sphinx(:fn_rst:`conf.py`) enable you to use.

System requirements
...................
Tested with 32bit version of Python 2.7.10 and 64bit version of 3.4.3,
both on the Microsoft Windows 8.1 Pro 64bit edition. But with another
versions and on another OSs would be usable.

Python 3 is required if you need full unicode support.
When used with Python 2, the usable character set is limited
with local encoding.

.. note::

   There's another extension yogosyu_ that fixes generation
   of the :fn_rst:`genindex.html` instead of adding
   :file:`std-gosyu.html`.

   But yogosyu_ can be unstable against Sphinx or docutils
   update than this module.

How to install
..............
You can install this package as you will do with another one.

#. Open a console and do :code:`pip install gosyu`.

   On the MS-Windows,
   :code:`<python_installed_path>\Scripts\pip.exe install gosyu`.

#. Or when you get zip archive like :fn_rst:`gosyu-2.0.5(.zip)`
   where '2.0.5' is version number,
   change current directiory to the folder that has the zip file,
   and do :code:`pip install gosyu-2.0.5.zip`.

   On the MS-Windows,
   :code:`<python_installed_path>\Scripts\pip.exe install gosyu-2.0.5.zip`.

#. Or, this way is the Sphinx specific, you can use this package just extracted
   any folder you want. the :fn_rst:`conf.py` enables you to use the themes and
   extensions.

If you don't resolve dependencies, you also have to get sortorder_ module.

How to use
----------

1) Add the paths
................
As another extensions, you can use this extension by editing :fn_rst:`conf.py`.

First, you should add:

.. code-block:: python

  # add 4 lines below
  import distutils.sysconfig
  site_package_path = distutils.sysconfig.get_python_lib()
  sys.path.insert(0, os.path.join(site_package_path, 'sortorder'))
  sys.path.insert(0, os.path.join(site_package_path, 'sphinxcontrib/gosyu'))

Or, when you don't install with pip or like,

.. code-block:: python

  # add just 2 line below
  sys.path.insert(0, '<path_to_the_folder_contains_sortorder___init___py>')
  sys.path.insert(0, '<path_to_the_folder_contains_gosyu_py>')

If you want to use your own sort order module(.py file), you should add
the path of it, too:

.. code-block:: python

  # after adding paths as above, add the line below.
  sys.path.insert(0, '<path_to_the_folder_sort_order_xx_py>')

.. note::

  The module sortorder_ has each preset order for some languages.

  Please read the document of the module to know how to use them or how
  to make your own order.

2) declare the extensions
.........................
Next, add gosyu extension into :code:`extension` list:

.. code-block:: python

   language = 'xx' # make sure your language if you want to use autodetect

   #
   # (snip...)
   #

   extension = [
     'sort_order_xx', # omit when using one of preset sort order or autodetect
     'sortorder', # you can omit always, because 'gosyu' automatically loads
     'gosyu', # required.
   ] # Of course you can add another extensions.

3) replace 'glossary' with 'gosyu'
....................................
Now, just replace :code:`.. glossary::` with :code:`.. gosyu::`.
When :code:`:sorted:` is given, the terms are sorted in each glossary.

And anyway, the general index in :fn_rst:`genindex.html` is also sorted
as you want to define.

4) add the how to read each terms
.................................
For the languages like Japanese, :code:`.. gosyu::` directive has another 
option :code:`:yomimark: <a separater char>`. the separator is a character
you want to use split. When the separator is given, the term can be followed
the string how to read. If you think some terms don't need the reading, you
can simply omit for the terms.

Consider to use the preset Japanese sort order defined in sortorder_
extension:

.. code-block:: python

   language = 'ja'

   #
   # (snip...)
   #

   extension = [
     'gosyu',
   ]  # all omitted modules will be automatically loaded

And write glossary like:

.. code-block:: rst

  .. gosyu::
    :sorted:
    :yomimark: 、

    ひらがな

      比較的曲線が多い日本語の表音文字

    カタカナ

      比較的直線が多い日本語の表音文字

    漢字、かんじ

      日本語でも使われる表意文字

    英字、えいじ

      義務教育で教わるため、日本語でもよく使われる表音文字

    記号、きごう

      国内国外を問わず多種多様な記号が携帯電話などでも使えるようになってきた

The separator is :code:`、` (U+3001) in this case.

This reorders the terms :code:`英字 -> カタカナ -> 漢字 -> 記号 -> ひらがな`.
The preset :fn_rst:`sortorder.ja` module sorts them depending on
:code:`えいじ, カタカナ, かんじ, きごう, ひらがな`.

And in the :fn_rst:`genindex.html`, :code:`カタカナ, 漢字, 記号` is grouped in
one heading :code:`か`. Also because the module desides it depending on how to
read.

.. note::

   If you want to use space(U+0020) or tab(U+0009) for the separator, you can
   write :code:`:yomimark: space` or :code:`:yomimark: tab`.

5) options written in conf.py
.............................
There is 3 options to change some strings.

- :code:`gosyu_shortname = u'用語集'` 

  - a short name for the index, for use in the relation bar in

- :code:`gosyu_localname = u'用語集'`

  - the section title for the index

- :code:`gosyu_anchor_prefix = 'yogo_'`

  - the prefix of the anchors to link from/to HTML files.

TODO
----

I don't know how to make the reference to :fn_rst:`std-gosyu.html` like
\:ref\:\`genindex\` .

As workaround, use:

.. code:: ReST

   `gosyu index <./std-gosyu.html>`_

or:

.. code:: ReST

   gosyu_index_

   ...

   .. _gosyu_index: ./std-gosyu.html

Related products
----------------
- unicode_ids_

  - enable the Sphinx to generate URL with Non-ASCII characters.

- sortorder_

  - the base module of this product.

- yogosyu_

  - anothor implementation for the same purpose of this package.
    more unstable against Sphinx updates, but directly fixes
    :fn_rst:`genindex.html` instead of generating
    :fn_rst:`std-gosyu.html`.

Author
------
Suzumizaki-Kimitaka(鈴見咲 君高), 2011-2015

History
-------
2.0.5(2015-07-04):

  - part the modules sortorder_ and unicode_ids_ from this package.
  - registered on PyPI.

2013-12-07:

  Add Python 3 support.

2013-12-06:

  updated to meet Sphinx 1.2.

2011-05-24:

  First release. Includes sortorder_ and unicode_ids_.

.. _sortorder: https://pypi.python.org/pypi/sortorder
.. _unicode_ids: https://pypi.python.org/pypi/unicode_ids
.. _yogosyu: https://pypi.python.org/pypi/yogosyu



