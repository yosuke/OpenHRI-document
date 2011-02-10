----------------------
音声認識文法の作成方法
----------------------

はじめに
========

音声認識文法は、認識される単語の構造を定義します。

OpenHRIの音声認識コンポーネントJuliusは、W3C-SRGS形式を使用して音声認識文法を定義しています。

ここでは、OpenHRIで用意しているW3C-SRGS書式の音声認識文法作成用のツールを説明します。

W3C-SRGS音声認識分法
====================

W3C-SRGS(Speech Recognition Grammar Specification)は音声認識文法を定義する規格の1つです。
使用するXML形式のタグを以下に示します。

タグ
----

lexicon
  W3C-PLS辞書(次のセクション)のURIを示します。 必須項目。

rule
  IDによって区別された文法のセットを示します。
  別の音声認識文法の参照や、Julius音声認識コンポーネントによって認識されたアクティブな文法を
  切り換えるのに利用できます。

item
  認識される言葉や文章を示します。

one-of
  子項目がすべて許容できることを示します。

例
---

.. literalinclude:: sample-en.grxml

W3C-PLS音声認識辞書
===================

W3C-PLS(Pronunciation Lexicon Specification)は音声認識辞書を定義する規格の1つです。
次のタグがあるXML形式を使用します。

タグ
----

lexeme
  書記素と音素のセットを示します。

grapheme
  単語の書式を示します。

phoneme
  単語の発音を示します。

例
---

.. literalinclude:: sample-lex-en.xml

Tools
=====


検証ツール
----------

"validatesrgs"はW3C-SRGS形式の文法を検証することができるツールです。

検証ツールは以下のコマンドで実行できます。::
  
  $ validatesrgs [grammarfile]

スクリプトが有効であれば以下のようなメッセージが出力されます。::
  
  $ validatesrgs sample-en.grxml
  Validating SRGS file sample-en.grxml...
  SRGS file is valid.
  Validating PLS file sample-lex-en.xml...
  PLS file is valid.

スクリプトが正しくないとき、以下のようなエラーメッセージが出力されます。::

  $ validatesrgs sample-invalid.grxml
  Validating SRGS file sample-invalid.grxml...
  [error] Invalid SRGS file.
  Element '{http://www.w3.org/2001/06/grammar}one-of': Missing child element(s). Expected is ( {http://www.w3.org/2001/06/grammar}item )., line 12

視覚化ツール
------------

OpenHRIは、W3C-SRGS書式を有効にするより強力なツールを用意しています。 
"juliustographviz"は、音声認識文法をグラフ表示させて正当性をチェックするツールです。

以下のコマンドでグラフ描画処理を行います。::

  $ srgstojulius sample-en.grxml | juliustographviz | dot -Txlib

以下のような画像が出力されます。:

  .. image:: sample-grammar.png

Lexicon generation tool
-----------------------

W3C-SRGS音声認識文法の作成を終えたら、W3C-PLS辞書を用意します。

OpenHRIは、W3C-SRGS文法からW3C-PLS辞書を自動的に生成するツールを用意しました。

"srgstopls"ツールは以下のコマンドで実行できます。::
  
  $ srgstopls sample-en.grxml > sample-lex-en.xml

このツールは現在、英語辞書(julius-voxforge辞書を使用するのによる)と日本語辞書(julius-runkit辞書を使用するのによる)をサポートしています。

.. note:: 単語は出力XMLファイルの辞書の空欄には追加されません。出力XMLのチェックを行い、手動で単語を登録してください。

