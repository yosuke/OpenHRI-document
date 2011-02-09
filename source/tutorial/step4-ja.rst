---------------------------
Step4: 対話システムを作ろう
---------------------------

音声認識コンポーネントと対話マネージャコンポーネントと組み合わせることで、入力した音声に対して応答を返す簡単な対話システムを作成してみましょう。

準備
----

1. 音声認識コンポーネントの準備

  音声認識コンポーネントに設定する音声認識文法データを用意します。

  以下のような２つのテキストデータを作成して下さい。テキストデータの文字コードはUTF-8を使用します。

  sample-en.xml

  .. literalinclude:: sample-en.xml

  sample-lex-en.xml

  .. literalinclude:: sample-lex-en.xml

  Windowsの メモ帳から作成する場合、コードを貼り付けたあと、[ファイル＞名前をつけて保存]を選び、開いたウィンドウ下部の[文字コード]から[UTF-8]

  を選択して保存してください。

  .. image:: ss_winstep4_0.png

  .. image:: ss_winstep4_1.png

2. 対話マネージャコンポーネントの準備

  対話マネージェコンポーネントに設定するスクリプトデータを用意します。

  以下のようなテキストデータを作成して下さい。

  sample-en.seatml
  
  .. literalinclude:: sample-en.seatml	   


3. 設定ファイルrtc.confの用意

  You may copy the setting used in :doc:`step2`.

テスト手順
----------

1. SEATコンポーネント、Juliusコンポーネントを起動します。

  Juliusコンポーネントは準備1.で用意した文法ファイル（sample.xml）を読み込みます。

  ::
  
  $ juliusrtc sample-en.xml

  SEATコンポーネントは準備2.で用意したスクリプトファイル（sample.seatml）を読み込みます。

  ::

  $ seat sample-en.seatml

  RT System Editorのネームサービスビューに起動したコンポーネントが表示されていることを確認します。

  .. image:: step4_11.png

2. RT System EditorにSEATコンポーネント、Juliusコンポーネントを配置します。

3. 各コンポーネントを接続します。

  * ConsoleInとOpenJTalk間のリンクを削除する。
  * AudioInputの出力ポートとJuliusの入力ポートを接続する。
  * Juliusの出力ポート“result”とSEATの入力ポート接続する。
  * SEATの出力ポートとOpenJTalkの入力ポート接続する。

  Make sure that everything is connected!

  .. image:: step4_10.png

4. アクティブ化して動作を確認します。

  "All Activate" ボタンを押して全コンポーネントをアクティブ状態に遷移させます。

  台詞「こんにちは」「さようなら」をマイクの前でしゃべって、応答音声が出力されるのを確認しましょう。

  .. note:: うまく認識できない場合の注意:

     うまく認識できない場合は以下の点を確認してみてください。

     静かなところで行う
       背景雑音が入っていないかどうか、周囲の雑音に注意してください。雑音が多い環境で認識したい場合はヘッドセットマイクや指向性マイクなど、雑音が入りにくいマイクの使用を検討してください。

     マイクの入力音量を変えてみる
       マイクの音量が大きすぎたり小さすぎたりすると音声認識をすることができません（Juliusを起動したコンソールに”Warning: strip～”などの警告が表示されている場合、マイクの音量設定が適切でない可能性があります）。ボリュームメーターを見ながらメーターが振り切れない程度の大きさに調整してください。

Proceed to :doc:`step5`.
