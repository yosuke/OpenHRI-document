------------------------------
対話マネージャスクリプトの書式
------------------------------

はじめに
========

対話マネージャは対話機能を管理する対話システムの中心部です。

OpenHRIは2つの対話マネージャを用意しています。目的に応じて選択してください。


SEAT: シンプルな対話マネージャ
===========================

SEAT (Speech Event Action Transfer) はシンプルな状態遷移モデルに基づく対話マネージャです。
以下のXMLタグを使用してシステムの動作を定義することができます。

Tags
----

- アダプタの定義


  SEATには、名前と実際の接続メソッド(RTMとソケット)の間にマッピングを与えるOpenRTMやソケット通信と接続可能なアダプタ機能。
  アダプタ機能は、システムのハードウェア・コンフィギュレーションを抜き取って、対話論理の再利用を促進します。
  SEAT has an adaptor mechanism which gives mappings between the name
  and the actual connection method (RTM and socket). The adaptor
  mechanism abstracts the hardware configuration of the system and
  assists the reuse of the dialog logic.

  general
    このタグは、アダプタ定義部を示すのに使用されます。
    This tag is used to indicate the adaptor definition part.

  agent
    名前と実際の接続メソッドの地図。 
    "type"属性は"rtcin"、"rtcout"、"socket"を取ることができます。
    タイプが"rtcin"か"rtcout"と定義されるとき、"datatype" 属性を定義できます(標準のデータ型に関するRTMの仕様を見てください)。
    タイプが"socket"と定義されるとき、"host" 、"port" 属性を定義できます。
    Map of the name and actual connection method. Attribute "type"
    can take "rtcin", "rtcout" or "socket". When type is defined as
    "rtcin" or "rtcout", you can define "datatype" attribute (see RTM's
    specification for standard data types). When type is defined as
    "socket", you can define "host" and "port" attributes.

- スクリプト定義

  state
    状態遷移モデルで状態を示します。
    Indicates a state in state-transition model.

  rule
    キーワードとコマンドのセットを定義します。
    Defines set of keywords and commands.

  key
    入力に合わせられるべきキーワード。
    Keywords to be matched to the inputs.

  command
    キーワードが入力に合っていたら実行されると命令してください。
    Command to be executed when the keyword matches the input.

  statetransition
    異なった状態へのトランジット。
    Transit to different state.

Example
-------

.. literalinclude:: sample.seatml

検証ツール
---------------

"validateseatml"ツールでは、SEATML形式のスクリプトの検証を行います。
You can validate your script in SEATML format by using "validateseatml" tool.

検証ツールは以下のコマンドで単純な検証を行うことができます。:
You can use the validation tool by simply entering the following command::
  
  $ validateseatml [scriptfile]

スクリプトが有効であれば以下のようなメッセージが出力されます。
If the script is correct, you will get the following output::
  
  $ validateseatml sample.seatml
  validating script file sample.seatml...
  script file is valid.

スクリプトが正しくないとき、以下のようなエラーメッセージが出力されます。
If the script is not correct, you will get error messages for example as follows::

  $ validateseatml sample-invalid.seatml
  validating script file sample-invalid.seatml...
  [error] invalid script file.
  Element 'transition': This element is not expected. Expected is one of ( command, statetransition )., line 23

視覚化ツール
------------------

OpenHRIには、SEATMLスクリプトの構造を有効にする多くの強力なツールがあります。 
"seatmltographviz"ツールは、スクリプトをグラフ表示させて正当性をチェックできます。
OpenHRI has more powerful tool to validate the structure of the
SEATML script.  "seatmltographviz" tool can visualize the script
in graph to check the correctness.

以下のコマンドでグラフ描画できます。
To draw the graph, enter following command::

  $ seatmltographviz sample.seatml | dot -Txlib

以下ようなグラフが表示できます。
For example, you will get the following output:

  .. image:: sample-script.png

Soar: General Artificial Intelligence
=====================================

Soar ( http://sitemaker.umich.edu/soar/home ) はプロダクションシステムベースのAIがわかる最も人気があるソフトウェアの1つです。
Soar ( http://sitemaker.umich.edu/soar/home ) is one of the most
popular software to realize production system based AI.

OpenHRIは、コンポーネントとしてRTMベースのシステムにSoarを埋め込むためにラッパーを提供します。
OpenHRI provides a wrapper to embed Soar into RTM based systems as a
component.

More documents T.B.D
