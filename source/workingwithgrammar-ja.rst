----------------------
音声認識文法の作成方法
----------------------

はじめに
========

音声認識文法は、音声認識器に与える認識可能な文法（単語の構造）を定義し
ます。

OpenHRIのJulius音声認識コンポーネントは、W3C-SRGS形式を使用して音声認識
文法を定義します。

ここでは、W3C-SRGS形式の音声認識文法について解説するとともにOpenHRIで用
意している文法作成用のツールについて説明します。

W3C-SRGS音声認識文法
====================

W3C-SRGS(Speech Recognition Grammar Specification)は音声認識文法を定義
する規格の1つです。使用するXML形式のタグを以下に示します。

タグ
----

lexicon
  W3C-PLS辞書(次のセクション)のURIを定義します。 必須項目。

rule
  IDによって区別された各文法を定義します。
  IDは音声認識文法の相互参照や、Julius音声認識コンポーネントによって認識されるアクティブな文法を
  切り換えるのに利用します。

item
  認識される単語や文を定義します。

one-of
  子項目で定義される文法がすべて許容できることを示します。

例
---

.. literalinclude:: sample-en.grxml

W3C-PLS音声認識辞書
===================

W3C-PLS(Pronunciation Lexicon Specification)は音声認識辞書を定義する規格の1つです。
次のタグからなるXMLフォーマットを使用します。

タグ
----

lexeme
  表記と発音のセットを定義します。

grapheme
  単語の表記を定義します。

phoneme
  単語の発音を定義します。

例
---

.. literalinclude:: sample-lex-en.xml

ツール
======


検証ツール
----------

"validatesrgs"はW3C-SRGS形式の文法を検証することができるツールです。

検証ツールは以下のコマンドで実行できます。::
  
  $ validatesrgs [grammarfile]

文法が正しい形式で書かれていれば以下のようなメッセージが出力されます。::
  
  $ validatesrgs sample-en.grxml
  Validating SRGS file sample-en.grxml...
  SRGS file is valid.
  Validating PLS file sample-lex-en.xml...
  PLS file is valid.

文法の形式が正しくないとき、以下のようなエラーメッセージが出力されます。::

  $ validatesrgs sample-invalid.grxml
  Validating SRGS file sample-invalid.grxml...
  [error] Invalid SRGS file.
  Element '{http://www.w3.org/2001/06/grammar}one-of': Missing child element(s). Expected is ( {http://www.w3.org/2001/06/grammar}item )., line 12

視覚化ツール
------------

OpenHRIは、W3C-SRGS形式の文法を検証するより強力なツールを用意しています。 
"juliustographviz"は、音声認識文法をグラフ表示させて正しさをチェックするツールです。

以下のコマンドでグラフ描画処理を行います。::

  $ srgstojulius sample-en.grxml | juliustographviz | dot -Txlib

以下のような画像が出力されます。:

  .. image:: sample-grammar.png

Lexicon generation tool
-----------------------

W3C-SRGS音声認識文法の作成が終わったら、W3C-PLS辞書も用意しなければなりません。

OpenHRIは、W3C-SRGS文法からW3C-PLS辞書を自動的に生成するツールを用意しています。

"srgstopls"ツールは以下のコマンドで実行できます。::
  
  $ srgstopls sample-en.grxml > sample-lex-en.xml

このツールは現在、英語辞書(julius-voxforge辞書を使用するのによる)と日本語辞書(julius-runkit辞書を使用するのによる)をサポートしています。

.. note:: 辞書に含まれない単語は出力XMLファイルの該当個所が空欄になります。出力されたXMLファイルは必ずチェックし、空欄箇所には手動で単語を登録してください。

