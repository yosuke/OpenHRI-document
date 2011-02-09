-------------------------------------
Step3: 音声合成コンポーネントのテスト
-------------------------------------

ここでは、音声合成コンポーネントの使い方を学びます。

準備
----

1. テスト用コンポーネントの準備

  定期的にテキストデータを出力するコンポーネントを用意します。以下のようなテストプログラムを作成して下さい。

  .. literalinclude:: ConsoleIn.py

  以後、このテスト用コンポーネントをConsoleInコンポーネントと呼称します。

2. rtc.confの用意

  Step2で使用したものと同等の設定ファイルを用意します。 :doc:`step2`.

テスト手順
----------

1. ConsoleInコンポーネント、OpenJTalkコンポーネントを起動します。

  ターミナルを開き、以下のコマンドを入力します。
  ::

  % python ConssoleIn.py
  
  ::
  
  % openjtalkrtc

  RT SystemEditorのネームサービスビューに起動したコンポーネントが表示されていることを確認します。

  .. image:: ss_jtalk01.png

2. RT System EditorにConsoleInコンポーネント、OpenJTalkコンポーネントを配置します。

  ドラッグ＆ドロップでエディタに配置します。

  .. image:: ss_jtalk02.png

3. AudioInput-AudioOutput間のリンクを削除します。

  リンクを選択してDeleteキーまたは右クリックメニューから"Delete"を選ぶと、リンクが削除されます。

  .. image:: ss_jtalk03.png

4. ConsoleIn、OpenJTalk、AudioOutputをそれぞれ接続します。

  * ConsoleInの出力ポートとOpenJTalkの入力ポートを接続します。

  * OpenJTalkの出力ポート「result」とAudioOutputの入力ポートを接続します。

  (違うポートに接続しないように注意して下さい。)

  .. image:: ss_jtalk04.png

5. アクティブ化して動作を確認します。

  "All Activate" ボタンを押してで全コンポーネントをアクティブ化します。

  ConsoleInコンポーネントに設定した文が音声として出力されることを確認してください。

次は、音声認識コンポーネントと接続することで簡単な対話システムを作ってみましょう。

Proceed to :doc:`step4`.

