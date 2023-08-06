sortorder拡張(日本語版説明書)
=============================
.. note::
   本書(日本語版)は\ `公式サイト <http://h12u.com/sphinx/sortorder/README_ja.html>`_\ 及びパッケージのdocフォルダで読むことができます。

.. role:: fn_rst

はじめに
--------
2015年6月1日現在、Sphinx 1.3.1では日本語による索引を作ることはできません。また glossary ディレクティブ内で読みに基づく並べ替えもできません。

このパッケージはSphinxにそのような機能を与える土台部分を提供します。つまりこれ単体では使えず、Sphinx用に別のパッケージが必要です。pipで Gosyu の名で公開しますのでそちらを検索してください。

このパッケージ自身はSphinxに依存しません。従って他の文書処理アプリケーションでも利用はできます。

利用条件
--------
二項BSDです。Sphinx本体に合わせています。

設置
----
他のPythonパッケージと同じ方法で設置できます。

環境条件
........
32ビット版Python 2.7.9と64ビット版Python 3.4.3をマイクロソフトウィンドウズ 8.1 Pro 64ビット版で動作させて検証しました。環境依存の要素はないはずなので、他のPythonや他のOSでも動作すると思います。

設置方法
........
前述の通り、通常のPythonパッケージと同様の方法で設置できます。

#. コンソールを開き\ :code:`pip install sortorder`\ を実行してください。

   マイクロソフトウィンドウズでは\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install sortorder`\
   を実行してください。

#. あるいは\ :fn_rst:`sortorder-2.0.6(.zip)`\ (2.0.6はバージョン番号)\
   というファイルを入手し、このファイルがあるフォルダへ移動した後\
   :code:`pythonを設置したフォルダ\Scripts\pip.exe install sortorder-2.0.6.zip`\
   を実行してください。

Sphinxからの使い方
------------------
既存の並び順提供moduleを使う方法については\ yogosyu_\ や\ gosyu_\
の説明書をご覧ください。\

本作で提供している日本語版(:code:`ja`)・エスペラント(語)(:code:`eo`)・\
ギリシャ語(:code:`el`)・ロシア語版(:code:`ru`)のいずれかを使う場合は\
:code:`language` を指定することで自動読み込みが動作します。\
これらの言語に対してであっても、独自に用意した\ :file:`sort_order_xx.py`\
が\ :code:`sys.path`\ のどこかに見つかった場合はそちらを優先して使います。

独自の並び順moduleを作る方法については\ :doc:`module_init`\ などを参照ください。\
簡単に説明しておくと:

- moduleの名前を決めてそのファイルを作ります。\
  :file:`sort_order_xx.py`\ という名前であれば\
  :code:`language = 'xx'`\ の場合に自動読み込みを行います。
- はじめのほうで\ :code:`import sortorder`\ と記述しておきます。
- :class:`sortorder.SortOrderBase`\ を継承したクラスを作ります。
- そのクラスの\ :meth:`get_string_to_sort`\ と :meth:`get_group_name`\ を実装します。
- :meth:`get_default_sort_order`\ でそのクラスを実体化して返すよう実装します。
- :meth:`setup`\ を用意します。こちらは\ :mod:`sortorder.ja`\ などを参照するとよいでしょう。

一般的な使い方
--------------
pipで設置していない場合は
:code:`sys.path.insert(0, '<拡張moduleのpyファイルがあるフォルダへのパス>')`
を最初に記述してください。

次に、同梱されている日本語(:code:`ja`)・エスペラント(語)(:code:`eo`)・\
ギリシャ語(:code:`el`)・ロシア語版(:code:`ru`)のいずれかを使う場合は単に
:code:`import sortorder.xx` によって利用できるようになります。

そうでない場合、並べ替えを独自に作るか他の方が作ったものを使うことに\
なります。自作する場合は :class:`sortorder.SortOrderBase` を継承したクラスを\
定義してください。ファイル名は :code:`sort_order_` を前置したものにします。\
:fn_rst:`sort_order_xx.py` といった感じになります。
:meth:`get_default_sort_order` や :meth:`setup` は Sphinx
で使うためのものです。

:fn_rst:`sort_order_xx.py` が準備出来ましたら、Pythonにおけるmodule\
の一般的な方法で利用できるようになります。

.. code-block:: python

   sys.path.insert(0, '<拡張モジュール(pyファイル)があるフォルダへのパス>')
   # (中略)
   import sort_order_xx

:fn_rst:`sortorder.__init__.py`\ は\ :meth:`get_sort_order` method\
を持っています。Sphinxで使うときのように自動選択機能をつけるために
:meth:`get_default_sort_order` methodを用意することもできます。

著者
----
鈴見咲 君高, 2011-2015

履歴
----
2.0.6(2015-07-04):

  英語版の README.rst を PyPI用に修正しました。

2.0.5(2015-07-04):

  - yogosyu_\ (用語集)から独立させて、少し構造や使い方を変えました。
  - PyPIに公開しました。

2013-12-14:

  Sphinx の公式対応化に応じて Python 3 に対応しました。

2011-06-28:

  ロシア語用とギリシャ語用を追加しました。

2011-05-24:

  初回版。Sphinx用の\ yogosyu_\ (用語集) 拡張を構成する部品として公開されました。
  日本語版のほかエスペラント(語)版を同梱しました。

.. _yogosyu: https://pypi.python.org/pypi/yogosyu
.. _gosyu: https://pypi.python.org/pypi/gosyu