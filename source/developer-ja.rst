sudo apt-add-repository ppa:clazzes.org/ppa
sudo apt-get update
sudo apt-get install mingw-w32-omniorb 

apt-get source libresample1-dev 
cd libresample-0.1.3/
./configure --host=i686-pc-mingw32
make
less libresample.a 
cd ..

apt-get source libfftw3-dev
cd fftw3-3.2.2/
./configure --host=i686-pc-mingw32 --with-gcc-arch=prescott --enable-portable-binary --with-our-malloc16 --with-windows-f77-mangling --enable-threads --with-combined-threads --enable-sse2
make
ls .libs/
cd ..

apt-get source portaudio19-dev
cd portaudio19-19+svn20090620/
./configure --host=i686-pc-mingw32
make
ls lib
cd ..

