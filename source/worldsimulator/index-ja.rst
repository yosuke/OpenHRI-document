----------------------------
ワールドシミュレータの使い方
----------------------------

OpenHRIでは、実ロボットがなくてもロボットとのインタラクション機能をテストすることができるワールドシミュレータを用意しています。

この章では、ワールドシミュレータの使い方について説明します。

   .. image:: blocksworld.png

インストール
------------

Windowsへのインストール
=======================

1. OpenHRIWorldsパッケージのインストール

  インストーラを以下のURLよりダウンロード・実行してください。
  
  http://openhri.net/getinstaller.php
  
  インストール可能なパッケージが順次表示されますので、「OpenHRIWorlds」パッケージを選択します。

2. OpenHRPSDKのインストール
  
  以下のページの一番下から「OpenHRP SDK Windows版」をダウンロードしてインストールしてください。
  
  http://openrtp.info/openhrp3/jp/download.html

Ubuntuへのインストール
======================

Ubuntuには現在対応していません（開発中です）。


BlocksWorldシミュレータ
-----------------------

BlocksWorldシミュレータは、三菱重工PA10アームのモデルを使ってブロックを操作するワールドシミュレータです。

起動方法
========

1. OpenHRPの起動

  エクスプローラを開き「C:\\Program Files (x86)\\OpenHRPSDK\\GrxUI」フォルダの中にある「GrxUI.exe」を起動します。

  .. note:: 今後のためにデスクトップにショートカットなどを作っておくとよいでしょう。

2. BlocksWorldの起動

  「スタートメニュー > OpenHRI > worlds」から「BlocksWorld」を選択します。

OpenHRPの画面上にPA10アームと複数のブロックが表示され、ロボットがテスト動作「一つの箱を取って置く」をすることを確認してください。

.. note:: BlocksWorldがうまく起動しない場合の対処法

  BlocksWorldが起動に失敗しロボットがテスト動作をしない場合があります（原因は調査中です）。その場合は、以下の手順を試してみてください。

  1. OpenHRP付属のサンプルプロジェクトをロードする。
       メニューバーの「GrxUI > プロジェクトの読み込み」を選択し、「C:\\Program Files (x86)\\OpenHRPSDK\\share\\OpenHRP-3.1\\sample\\project」の中から「PA10Sample」をロードしてください。

  2. OpenHRPのシミュレーションを一度実行する。
        シミュレーションの開始ボタンを押してシミュレーションを開始してください（すぐに終了しても構いません）。

  3. OpenHRPのビューをクリアする。
        メニューバーの「GrxUI > 新規プロジェクト」を選択し、ビュー画面をクリアしてください。

  4. BlocksWorldを実行する。
        BlocksWorldコンポーネントを起動して動作を確認してください。


コンポーネントの機能
====================

BlocksWorldコンポーネントは、commandポートから入力を受け付けます。

下記のテキストコマンドを与えることでロボットが動作します。

grasp
  ハンドの下にあるものを拾います。

release
  ハンドで持ったものを放します。

moveHandToBox [name]
  [name]で指定されたブロックの上にハンドを移動します。「box1」「box2」「box3」が指定できます。

moveHandXY [X] [Y]
  現在の位置から[X][Y]で指定された距離、ハンドを移動します。

テストスクリプト
================

対話によってPA10アームを操作するスクリプトの例を示します。

1. 音声認識文法

  .. literalinclude:: blocksworld-ja.grxml
     :language: xml

2. 対話スクリプト

  .. literalinclude:: blocksworld-ja.seatml
     :language: xml

それぞれのファイルをJuliusコンポーネントとSEATコンポーネントに読み込ませ、SEATコンポーネントの「command」ポートとBlocksWorldコンポーネントの「command」ポートを接続してください。
