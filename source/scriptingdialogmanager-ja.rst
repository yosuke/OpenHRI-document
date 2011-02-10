------------------------------
対話マネージャスクリプトの書式
------------------------------

はじめに
========

対話マネージャは対話機能を管理する機能を持ち、対話システムの中核となる部分です。

OpenHRIは2つの対話マネージャを用意しており、目的に応じて選択することができます（独自の対話マネージャを書くこともできます）。


SEAT: シンプルな対話マネージャ
==============================

SEAT (Speech Event Action Transfer) はシンプルな状態遷移モデルに基づく対話マネージャです。
以下のXMLタグを使用してシステムの動作を定義することができます。

タグ
----

- アダプタの定義

  SEATには、名前と通信方法(RTMとソケット)を対応付けるアダプタ機構を持っています。
  アダプタ機構は、通信方法の差異を隠蔽化することで、システムのハードウェア構成の変化に適応し、対話ロジックの再利用性を向上させます。

  general
    アダプタ定義部を示します。

  agent
    名前と通信方法の対応を示します。 
    "type"属性は"rtcin"、"rtcout"、"socket"を取ることができます。
    タイプが"rtcin"か"rtcout"と定義されたとき、"datatype"属性を定義できます(データ型に関しては、RTMの仕様を参照してください)。
    タイプが"socket"と定義されたとき、"host" 、"port" 属性を定義できます。

- スクリプト定義

  state
    状態遷移モデルで状態を示します。

  rule
    キーワードとコマンドの組を定義します。

  key
    キーワードを示します。

  command
    キーワードと入力が一致したとき実行されるコマンドを示します。

  statetransition
    状態遷移を示します。

例
---

.. literalinclude:: sample-en.seatml

検証ツール
----------

"validateseatml"は、SEATML形式のスクリプトの検証を行うツールです。

検証ツールは以下のコマンドで実行できます。::
  
  $ validateseatml [scriptfile]

スクリプトが正しい形式で書かれていれば以下のようなメッセージが出力されます。::
  
  $ validateseatml sample-en.seatml
  validating script file sample-en.seatml...
  script file is valid.

スクリプトの形式が正しくないとき、以下のようなエラーメッセージが出力されます。::

  $ validateseatml sample-invalid.seatml
  validating script file sample-invalid.seatml...
  [error] invalid script file.
  Element 'transition': This element is not expected. Expected is one of ( command, statetransition )., line 23

視覚化ツール
------------

OpenHRIは、SEATMLスクリプトの構造を検証するより強力なツールを用意しています。 
"seatmltographviz"は、スクリプトをグラフ表示させて構造をチェックするツールです。

以下のコマンドでグラフ描画処理を行います。::

  $ seatmltographviz sample-en.seatml | dot -Txlib

以下のような画像が出力されます。:

  .. image:: sample-script.png

Soar: General Artificial Intelligence
=====================================

Soar ( http://sitemaker.umich.edu/soar/home ) はプロダクションシステムベースのAIで最も人気がある実装の1つです。

OpenHRIは、RTMベースのシステムにコンポーネントとしてSoarを埋め込むためのラッパーを提供します。

More documents T.B.D
