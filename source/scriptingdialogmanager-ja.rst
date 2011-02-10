------------------------------
対話マネージャスクリプトの書式
------------------------------

はじめに
========

対話マネージャは対話機能を管理する対話システムの中心部です。

OpenHRIは2つの対話マネージャを用意しています。目的に応じて選択してください。


SEAT: シンプルな対話マネージャ
==============================

SEAT (Speech Event Action Transfer) はシンプルな状態遷移モデルに基づく対話マネージャです。
以下のXMLタグを使用してシステムの動作を定義することができます。

タグ
----

- アダプタの定義

  SEATには、名前と接続メソッド(RTMとソケット)を接続可能にするアダプタ機能を持っています。
  アダプタ機能は、システムのハードウェア・コンフィギュレーションによらず対話ロジックの利便性を促進します。

  general
    このタグは、アダプタ定義部を示すのに使用されます。

  agent
    名前と接続メソッドの割り当てを示します。 
    "type"属性は"rtcin"、"rtcout"、"socket"を取ることができます。
    タイプが"rtcin"か"rtcout"と定義されるとき、"datatype" 属性を定義できます(データ型に関しては、RTMの仕様を参照してください)。
    タイプが"socket"と定義されるとき、"host" 、"port" 属性を定義できます。

- スクリプト定義

  state
    状態遷移モデルで状態を示します。

  rule
    キーワードとコマンドのセットを定義します。

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

スクリプトが有効であれば以下のようなメッセージが出力されます。::
  
  $ validateseatml sample-en.seatml
  validating script file sample-en.seatml...
  script file is valid.

スクリプトが正しくないとき、以下のようなエラーメッセージが出力されます。::

  $ validateseatml sample-invalid.seatml
  validating script file sample-invalid.seatml...
  [error] invalid script file.
  Element 'transition': This element is not expected. Expected is one of ( command, statetransition )., line 23

視覚化ツール
------------

OpenHRIは、SEATMLスクリプトの構造を有効にするより強力なツールを用意しています。 
"seatmltographviz"は、スクリプトをグラフ表示させて正当性をチェックするツールです。

以下のコマンドでグラフ描画処理を行います。::

  $ seatmltographviz sample-en.seatml | dot -Txlib

以下のような画像が出力されます。:

  .. image:: sample-script.png

Soar: General Artificial Intelligence
=====================================

Soar ( http://sitemaker.umich.edu/soar/home ) はプロダクションシステムベースのAIで最も人気があるソフトウェアの1つです。

OpenHRIは、コンポーネントとしてRTMベースのシステムにSoarを埋め込むためのラッパーを提供します。

More documents T.B.D
