gosyu拡張(日本語版説明書)
===========================
.. note::

   日本語版(本頁)は\ `公式サイト
   <http://h12u.com/sphinx/gosyu/README_ja.html>`_\ とこのパッケージの\
   docフォルダでご覧になれます。

はじめに
--------
2015年6月7日現在、Sphinx 1.3.1は '正規化形式D'(Normalization Form
Canonical Decomposition, NFD) に基づく並べ替えしか行いません。\
さらにまずいことに、索引の見出しは英字に対してしか行われません。

英語に似た言語では、NFDの効果もあって問題が少ないか全くないことが\
多いのですが、英字を共有しない言語では悲惨なことになります。\
ほとんど全部の文字が記号扱いとなり、索引の見出しが機能しないからです。

日本語においてはさらにまずいことになります。漢字を使った用語に対する\
読み方を提供できないため、並べ替えの結果はUnicodeの漢字並び順という\
全く役に立たない結果をもたらします。

この拡張機能では、これらの解決を試みています。並び順は別途配布している
sortorder_ moduleを使います。\
日本語などには事前に並べ方が定義されているほか、任意の言語に対し\
自前の並べ方を定義することもできます。

残念ながら現在は :code:`.. glossary::` directive を置き換える
:code:`.. gosyu::` 以外は未解決です。\ :code:`index` などを含む\
の他のものは将来の版で解決する…かもしれません。

利用条件
--------
Sphinxと同じく二項BSDです。

設置について
------------
他のPythonパッケージと同様に設置・撤去できます。また他のSphinx拡張と同様に\
必要なファイルだけ各自の管理下に複製し、そのフォルダを\ :fn_rst:`conf.py`\
で指定することでも利用いただけます。

動作条件
........
32ビット版のPython 2.7.9と64ビット版のPython 3.4.3をマイクロソフトウィンドウズ
8.1上で動かして挙動を確認しました。特段の依存性はないので、他のPython実装や\
他のOSでも動作すると思います。

Unicodeで定義された全文字への対応はPython 3が必須です。Python 2ではその標準\
符号化法かファイルシステムの符号化法に利用できる文字が限定されます。

.. note::

   Sphinxやdocutilsの更新に対する安定さに欠けますが :file:`genindex.html` を\
   直接改良する別の拡張 yogosyu_ があります。

設置方法
........
前述の通り、通常のPythonパッケージと同様の方法で設置できます。

#. コンソールを開き\ :code:`pip install gosyu`\ を実行してください。

   マイクロソフトウィンドウズでは\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install gosyu`\
   を実行してください。

#. あるいは\ :fn_rst:`gosyu-2.0.1(.zip)`\ (2.0.1はバージョン番号)\
   というファイルを入手し、このファイルがあるフォルダへ移動した後\
   :code:`pip install gosyu-2.0.1.zip`\ を実行してください。

   同様にウィンドウズでは代わりに\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install gosyu-2.0.1.zip`\
   を実行してください。

#. 最後の別の方法として、これはSphinx特有の方法ですが、単にzipファイルを任意の\
   フォルダに展開して使うという手段があります。Sphinxで使う\ :fn_rst:`conf.py`\
   を適切に編集することで利用可能です。

依存関係を解決しなかった場合は、別途 sortorder_ が必要となります。

使い方
------

1) パスの追加
.............
他のSphinx拡張同様、\ :fn_rst:`conf.py`\ の編集によって使えるようになります。

まず、次のコードを追加してください:

.. code-block:: python

  # 次の4行を追加
  import distutils.sysconfig
  site_package_path = distutils.sysconfig.get_python_lib()
  sys.path.insert(0, os.path.join(site_package_path, 'sortorder/sphinxcontrib'))
  sys.path.insert(0, os.path.join(site_package_path, 'gosyu/sphinxcontrib'))

ただし、もしpipで設置していないのであれば代わりに次を追加してください:

.. code-block:: python

  # 代わりに次の2行を追加
  sys.path.insert(0, '<sortorder.__init__.pyがあるフォルダへのパス>')
  sys.path.insert(0, '<gosyu.pyがあるフォルダへのパス>')

さらに独自の並び順を提供するPythonファイルがある場合は、それへのパスも\
追加してください:

.. code-block:: python

  # 上記のいずれかに加えて次の行を追加
  sys.path.insert(0, '<用意した独自sort_order_xx.pyがあるフォルダへのパス>')

.. note::

  sortorder_ には日本語を含めいくつかの言語用に予め用意された並び順提供module
  が含まれています。それらの使い方や独自の並び順を定義する方法については、
  sortorder_ の\ `説明書 <http://h12u.com/sphinx/sortorder/README_ja.html>`_\
  をご覧ください。

2) 使う拡張の宣言
.................
次に当拡張を :code:`extension` の中で宣言してください:

.. code-block:: python

   language = 'xx' # 自動読み込みを使う場合は言語指定を確認して下さい

   #
   # (中略)
   #

   extension = [
     'sort_order_xx', # 自動検出かsortorderで提供するものを使う場合は省きます
     'sortorder', # gosyu拡張が自動的に読み込むので省略できます
     'gosyu', # 必須です
   ] # もちろん他の拡張も任意で追加できます

.. note::

   将来\ `Sphinx Contrib repository
   <https://bitbucket.org/birkenfeld/sphinx-contrib>`_\ へのpull requestを行う\
   予定です。それが通り次第別の方法も利用できるようになります。

3) 'glossary' を 'gosyu' に置き換え
.....................................
ここまでできましたら、\ :code:`.. glossary::` directiveを
:code:`.. gosyu::` に置き換えるだけです。\
:code:`:sorted:` はそのままで使えます。

:file:`std-gosyu.html` が総合索引とは別に出力され、そちらでは索引としての\
指定された並び順とグループ化が行われるようになります。

4) 読みがなを加える
...................
日本語のような言語で使うために :code:`.. gosyu::` directive は
:code:`:yomimark: <区切り文字>` という option も用意しています。\
:code:`:yomimark:` で指定した文字の前が本来の用語、後ろが読みがなと\
いう形になります。

日本語での使用例を示します。\ :file:`conf.py`\ で次のように記述してください:

.. code-block:: python

   language = 'ja'

   #
   # (中略)
   #

   extension = [
     'user_ordered_index_patch',
   ]  # 省略された拡張は前述のとおりすべて自動的に読み込まれます

その上で次のように用語集を記述した場合を考えます:

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

ここでは区切り記号を読点 :code:`、` (U+3001) にしています。

単語は :code:`英字→カタカナ→漢字→記号→ひらがな` の順で並べられます。
:fn_rst:`sortorder.ja` module が読みがなである
:code:`えいじ, カタカナ, かんじ, きごう, ひらがな` にもとに判断するからです。

また :fn_rst:`genindex.html` においては :code:`カタカナ, 漢字, 記号` が単一\
の見出し :code:`か` にまとめられます。やはり同じ module が指定された読みがな\
に基いて振り分けを行うからです。

5) conf.py で変更できる設定
............................
用語集に関連するいくつかの文字列を変更できます。

- :code:`gosyu_shortname = u'用語集'` 

  - relation bar に表示する用語集へのリンク文字列です。

- :code:`gosyu_localname = u'用語集'`

  - 用語集のHTMLファイル冒頭に表示する見出し文字列です。

- :code:`gosyu_anchor_prefix = 'yogo_'`

  - HTMLファイルの中でリンクに使われるanchorの前置部文字列です。

関連配布物
----------
- unicode_ids_

  - Sphinxが出力するHTMLファイルに非ASCII文字を含まれるように修正します

- sortorder_

  - この拡張の基盤moduleです

- yogosyu_

  - 同じ目的の他の実装です。Sphinxの更新に対する安定性は落ちますが、\
    総合索引(:file:`genindex.html`)を直接改良します。

著者
------
Suzumizaki-Kimitaka(鈴見咲 君高), 2011-2015

履歴
----
2.0.0(2015-06-xx):

  sortorder_\ と\ unicode_ids_\ を分離しました。

2013-12-07:

  Sphinx に合わせて Python 3 にも対応しました。

2013-12-06:

  Sphinx 1.2 へパッチ対象を変更しました。

2011-05-24:

  初回公開。\ sortorder_\ と\ unicode_ids_\ を含んでいました。

.. _sortorder: https://pypi.python.org/pypi/sortorder
.. _unicode_ids: https://pypi.python.org/pypi/unicode_ids
.. _yogosyu: https://pypi.python.org/pypi/yogosyu