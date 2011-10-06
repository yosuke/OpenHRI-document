------------------
開発者向け情報
------------------

OpenHRIは主にgithubとUbuntuを使って開発されています。

最新のソースコード（機能が不安定だったりバグがある可能性があります）をテストしたい場合、
以下の手順に従ってコンポーネントをコンパイルしてください。

OpenHRIAudio
--------------------------------

音響コンポーネント群（OpenHRIAudio）はconfigureスクリプトを使ってパッケージ化されたC++プログラムです。

以下の手順でコンパイルしてインストールすることができます。

依存ライブラリをインストールする::

 $ sudo apt-get install autotools-dev pkg-config omniidl4 uuid-dev libomniorb4-dev libspeex-dev libspeexdsp-dev libresample1-dev openrtm-aist openrtm-aist-dev portaudio19-dev libpulse-dev

最新のソースコードをチェックアウトする::

 $ git clone https://yosuke@github.com/yosuke/OpenHRIAudio.git

ソースコードがあるフォルダに移動してconfigureスクリプトをセットアップする::

 $ cd OpenHRIAudio
 $ ./autogen.sh

configureスクリプトを起動してプロジェクトをコンパイルする::

 $ ./configure
 $ make

コンポーネントをインストールする::

 $ sudo make install
 $ sudo ldconfig

OpenHRIVoice
--------------------------------

音声コンポーネント群（OpenHRIVoice）はsetupスクリプトを使ってパッケージ化されたPythonプログラムです。

以下の手順でコンパイルしてインストールすることができます。

依存ライブラリをインストールする::

 $ sudo apt-get install python-beautifulsoup python-lxml python-matplotlib openrtm-aist-python

最新のソースコードをチェックアウトする::

 $ git clone https://yosuke@github.com/yosuke/OpenHRIVoice.git

ソースコードがあるフォルダに移動してコンポーネントをインストールする::

 $ cd OpenHRIVoice
 $ sudo python setup.py install


