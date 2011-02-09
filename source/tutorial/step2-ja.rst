---------------------------------------------------------------
Step2: RTSystemEditorの使い方と音声入出力コンポーネントのテスト
---------------------------------------------------------------

このステップでは、オーディオコンポーネントの動作テストを行います。

音声入力コンポーネントと音声出力コンポーネントを直接つないで、オーディオコンポーネントが正常に動作していることを確認します。

準備
----

1. RT System Editorがインストールされたeclipseをダウンロードしてインストールします。(こちら http://www.openrtm.org/ を参照して下さい)

2. マイクとスピーカ（イヤホン、ヘッドフォン）を用意し、PCと接続します。

3. rtc.confファイルを作成します。

  RTCコンフィギュレーションファイル “rtc.conf” を作成します。作業ディレクトリ に、次のような内容のテキストファイル“rtc.conf” を作成し配置してください。

  .. code-block:: guess  

     corba.nameservers: localhost:9876
     naming.formats: %n.rtc

4. ネームサーバーを立ち上げます。

  rtc.confファイルでポートナンバーを指定したときは、指定したポートナンバーでネームサーバーを起動します。（上記の例なら9876）
  ::
  
  $ rtm-naming 9876

   .. image:: ss_run011.png

5. RT System Editorを立ち上げます。

RT System Editorの基本的な使い方
--------------------------------

音声入出力コンポーネントの起動とRT System Editorの基本的な使用方法を説明します。

1. AudioInputコンポーネントおよびAudioOutputコンポーネントを立ち上げます。

   .. warning::
   
      Ubuntuで使用する場合Uubuntuのバージョンにより立ち上げるコンポーネントを変更します。
      Ubuntu9.10以降はPulseAudioInput、PulseAudioOutputコンポーネントを使用します。
      それ以前のバージョンではPortAudioInput、PortAudioOutputコンポーネントを使用します。

   Ubuntu9.10以降の場合：端末上より以下のコマンドを入力してください。
     ::
 
     $ pulseaudioinput

     ::
     
     $ pulseaudiooutput

   それ以前のバージョンの場合：端末上より以下のコマンドを入力してください。
     ::

     $ portaudioinput

     ::
     
     $ portaudiooutput

2. RT System Editorを開きます。

   .. image:: ss_run03.png

   .. image:: ss_run04.png

3. ネームサービス内の「ネームサーバーを追加」を選択してrtc.confファイルで指定したネームサーバーを登録します。

   （上記の例なら　localhost:9876）

   .. image:: step2_6.png

   .. image:: step2_7.png

4. 左上のアイコンをクリックし新規エディタ画面を開きます。

   .. image:: ss_step2_3.png

5. ネームサービスビュー（左のパネル）のAudioInput（およびAudioOutput）をエディタ画面にドラッグ＆ドロップして配置します。

   .. image:: ss_run06.png

6. 配置したコンポーネントのデータポート同士を接続します。

   データポートのコネクタ部分をクリックして、

   .. image:: ss_run09.png

   そのままもう一方の端子までドラッグします。

   .. image:: ss_run10.png

   ドロップすると接続設定ダイアログが出現します。設定は変更しません。

   .. image:: ss_run11.png

   OKボタンを押すと接続されます。（コネクタの色が緑に変化します）

   .. image:: ss_run12.png

コンポーネントのアクティブ化と動作確認
--------------------------------------

7. RTCをアクティブ状態にします。

  “All Activate” ボタンを押して、すべてのRTCコンポーネントをアクティブ状態に遷移させます。

   .. image:: ss_step2_1.png

   AudioInputとAudioOutputがアクティブ化し、オブジェクトの色が青から緑に変化します。

   .. image:: ss_step2_2.png

8. 動作を確認します。

   マイクに音声を入力してスピーカに音声が流れることを確認します。

Step２ではオーディオコンポーネントのテストからRT System Editorの基本的な使用方法を説明しました。

:doc:`step3-ja` へ
