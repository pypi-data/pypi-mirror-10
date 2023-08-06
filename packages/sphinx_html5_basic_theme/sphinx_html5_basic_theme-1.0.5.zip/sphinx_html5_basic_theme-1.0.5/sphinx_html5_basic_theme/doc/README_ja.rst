Sphinx HTML5 basic themes(日本語版説明書)
=========================================

.. caution::
   公開時現在ではSphinx側の\ `バグ <https://github.com/sphinx-doc/sphinx/issues/1884>`_\ によりsphinx_html5_sphinxdocテーマが使えません。
   sphinx_html5_basicテーマとsphinx_html5_translator拡張は利用できます。

   sphinx_html5_sphinxdoc を使いたい場合は\ :file:`doc/conf.py`\ を参考にして\
   :code:`html_theme_path`\ を設定してください。

.. note::
   本書(日本語版)は\ `公式サイト <http://h12u.com/sphinx/html5_basic_theme/README_ja.html>`_\ 及びパッケージのdocフォルダで読むことができます。

.. role:: fn_rst

はじめに
--------
2015年5月6日現在、Sphinx 1.3.1はHTML5を満たすファイルを出力できません\ [#f1]_\ 。

これを解決するため、このパッケージにはHTML5+CSS3版の\ *basic*\ テーマと\
*sphinxdoc*\ テーマ、それから\ :fn_rst:`sphinx_html5_translator(.py)`\ というSphinx拡張を\
収録しています。

これらを運用することでW3C Validatorを通るHTML出力が得られます。

利用条件
--------
BSDです。Sphinx本体に合わせています。
(いずれのファイルも将来的に必要ならSphinx本体に導入できるように作っています。)

インストール
------------
他のPythonパッケージと同じ方法で設置できますし、Sphinxの\ :fn_rst:`conf.py`\
を利用してPython管理下フォルダを汚さずに使うこともできます。

環境条件
........
- Sphinx 1.3と互換性のある環境

  - docutils 0.12 と互換性のある環境
  - バージョンアップなどによってこれらの内部構造が変わってしまうと、当パッケージに含まれるテーマや拡張の動作を止めてしまう可能性があります。もっとも、これは本作に限ったことではありません。

- 32ビット版Python 2.7.9と64ビット版Python 3.4.3をマイクロソフトウィンドウズ 8.1 Pro 64ビット版で動作させて検証しました

  - 環境依存の要素はないはずなので、他のPythonや他のOSでも動作すると思います

インストール方法
................
前述の通り、通常のPythonパッケージと同様の方法で設置できます。

#. コンソールを開き\ :code:`pip install sphinx_html5_basic_theme`\ を実行してください。

   マイクロソフトウィンドウズでは\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install sphinx_html5_basic_theme`\
   を実行してください。

#. あるいは\ :fn_rst:`sphinx_html5_basic_theme-1.0.5(.zip)`\ (1.0.5はバージョン番号)\
   というファイルを入手し、このファイルがあるフォルダへ移動した後\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install sphinx_html5_basic_theme-1.0.5.zip`\
   を実行してください。

#. 最後の別の方法として、これはSphinxに特有の方法ですが、単にzipファイルを任意の\
   フォルダに展開して使うという手段があります。Sphinxで使う\ :fn_rst:`conf.py`\
   を適切に編集することで利用可能です。

使い方
------
`HTMLテーマの切り替え方 <http://docs.sphinx-users.jp/theming.html>`_\ と\
`Sphinx拡張の使い方 <http://docs.sphinx-users.jp/extensions.html>`_\ はご存じですか?
よく分からない場合はまずそちらを確認してください。

1) テーマの適用
...............

テーマは現在\ :code:`html5_basic`\ と\ :code:`html5_sphinxdoc`\
の二つのみ用意されています。
後者は前者を参照していますのでうっかり削除しないようにしてください。

このパッケージを\ :code:`easy_install`, :code:`pip`,
:code:`setup.py`\ のいずれかで設置した場合は\
:code:`html_theme`\ にテーマ名を指定するだけで切り替えられます\
(:fn_rst:`conf.py`\ を編集してください)。

前述の最後の設置方法を使う場合は、これにくわえて\
:code:`html_theme_path = ['展開されたテーマフォルダ群の親フォルダ',]`\
の追加が必要となります。Python文字列としてのパス指定なので、Windowsで
使われる方はパス区切り記号の扱いなどに気をつけてください\ [#f2]_ \ 。

.. note::

  なお、本書の冒頭で述べたとおり、Sphinxのバグが修正されるまでは\
  いずれにしても\ :code:`html_theme_path`\ の指定が必要となります。

2) HTML5化のための拡張
......................

HTML5化のためにはテーマの差し替えだけでなくSphinx拡張の追加も必要です。\
:fn_rst:`sphinx_html5_translator(.py)`\ を利用する拡張に加えてください。\
この作業が必要なのは、Sphinxではなくdocutilsが直接廃止されたタグや属性を\
出力してしまうからです。

具体的には\ :fn_rst:`conf.py`\ に次の内容を記述します。\
:code:`extension = ['sphinx_html5_translator', ]`\ より前の部分に置いてください。

pipなどを使ってPythonシステムにインストールした場合:

.. code-block:: python

  import distutils.sysconfig
  site_package_path = distutils.sysconfig.get_python_lib()
  sys.path.insert(0, os.path.join(site_package_path, 'sphinx_html5_basic_theme'))

展開したzipファイルを直に使う場合:

.. code-block:: python
  
  sys.path.insert(0, '展開されたsphinx_html5_translator(.py)があるフォルダ')
  # さきほどの'展開されたテーマフォルダ群の親フォルダ'と同じになります

合わせて上述のように\ :code:`extension`\ 部分の更新してください。\
内容が衝突しない限り他のSphinx拡張と同時に利用できます。

展開したzipファイルを直に使う場合においてテーマと拡張のために
それぞれ指定するフォルダは実は同じです。

.. note::

   特に気にならない、あるいは意図的にそうしたい場合は\
   :fn_rst:`sphinx_html5_translator.py`\ をお好きなフォルダに複製し、
   :code:`sys.path.insert(0, 'コピー先のフォルダ')` を追加する方法があります。
   もちろん\ :code:`extension`\ は前述同様にご指定ください。

元のテーマからの変更点
----------------------
- CSS3 を使っていますが一部はまだ勧告仕様になっていません

  - `Flexible Box Layout Module Level 1 <http://www.w3.org/TR/css-flexbox-1/>`_\ は最終作業草案です。
  - `Multi-column Layout Module <http://www.w3.org/TR/css3-multicol/>`_\ は勧告候補です。

- Flexible Box Layoutを次のところで使っています

  - 各頁の相対移動案内部分
  - 主文とサイドバーの位置関係
  - クイック検索部分の入力部と検索ボタンの位置関係

- Multi-column Layoutを総合索引(:fn_rst:`genindex.html`)で使っています。索引の列数をスタイルシートで変更できます。
- :code:`sidebarwidth`\ に単位を含めた文字列を指定できます
- sphinx_html5_basicであってもサイドバーは表示されます
- クイック検索ボタンの幅指定は削除しました。日本語での検索ボタンがちょん切れた感じになってたのは短く決め打ちされてたせいです、ええ。
- 総合索引でtable要素やdl要素を使わなくなったため、\ :code:`table.indextable`\ はなくなりました。新たに\ :code:`genindex-multi-columens`\ クラスが追加されました。
- 一部の括弧類や記号はスタイルシートで指定できるようにHTMLファイルから除きました

  - 相対移動案内部分(:code:`»`\ と :code:`|`)
  - 索引頁の上にある頭字列の区切り(:code:`|`)
  - 脚注と同名索引出現時に使う角括弧(:code:`[`\ と :code:`]`)

- :code:`{% block searchtip %}`\ を定義しました。この部分はPythonプログラマー向けに定義されていて、一般の文書には不適切だからです。このブロックによってテンプレートで差し替えることができます。
- :code:`{% block extra_footer %}`\ を定義しました。フッターの最後に任意のHTMLを追加できます。
- :code:`{% expired_html_link %}`\ を定義しました。HTML5では\ :code:`top`\ と\ :code:`up`\ が廃止されたためで、初期設定もJinja2コメントで事実上空にしています。
- sphinxdocテーマで使っていた画像を削除し、スタイルシートの指定で置き換えました。
- sphinxdocテーマにおける主文とサイドバーの境界線が常に下まで届くようになりました。主文の方が短い場合でもちょん切れたりしません。

著者
----
鈴見咲 君高, 2015-04-30

履歴
----
1.0.5(2015-06-19):

  - インストール用のwheelビルドを加えました。
  - Sphinxのバグが解消されるまでの回避手段を\ :file:`doc/conf.py`\ に加えておきました。
  - Python 3で動作するpipにバグがあったため、それを回避する記述を\ :file:`setup.py`\ に加えました。
    このpipのバグについては https://github.com/pypa/pip/pull/2916 を参照ください。

1.0.4(2015-05-25):

  - Sphinx拡張を自由に設定するフォルダの記述について修正しました。
  - 公式サイトとパッケージの doc フォルダに日本語版の文書があることを追記しました。

1.0.3(2015-05-10):

  使い方に関する部分を中心に本書を修正しました。

1.0.2(2015-05-10):

  公開に失敗したようなので再公開しました。

1.0.1(2015-05-10):

  追加し忘れていたREADME.rst(英語の取説)を収録しました。

1.0.0(2015-05-09):

  初回版。同梱ファイルはSphinx 1.3.1とdocutils 0.12に含まれていたものに修正を\
  入れています。Python 2.7.9とPython 3.4.3をマイクロソフトウィンドウズ 8.1 Pro\
  上で使って試行しました。

  テーマ二つ(html5_basic, html5_sphinxdoc)と\
  拡張一つ(sphinx_html5_translator)を同梱しました。

.. rubric:: 脚注

.. [#f1] `W3C Markup Validation Service <https://validator.w3.org/>`_

.. [#f2] \\を\\\\または\ :code:`/`\ に置き換える、あるいは\ :code:`r`\ を\
         前に付けて\ :code:`r'フォルダ名'`\ の形にする、さらに半角英数字以外が含まれる場合は\
         :code:`u'フォルダ名'`\ や\ :code:`ur'フォルダ名'`\ の形にする、などです。