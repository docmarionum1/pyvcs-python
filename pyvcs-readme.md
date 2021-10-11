- autoconf
- ./configure --enable-optimizations --with-lto
- make -j13 (I have 12 cores)

Ubuntu
=====
sudo apt-get install libportaudio2


Windows
=======
- .\PCbuild\build.bat
- create a venv with .\PCBuild\amd64\python.exe

WOAH, it's running colors_new with about 76 FPS using the PGO version of my custom python build.
game.py is around 55; flickering is happening though because right now the timing is still different.


Mac
===
HOMEBREW_NO_AUTO_UPDATE=1 brew install openssl xz gdbm openblas
./configure --with-openssl=$(brew --prefix openssl) --enable-optimizations --with-lto
make -j8


Setup for pyvcs
===============

- create a virtual env with ./python.exe

    ./python.exe -m venv venv
    source venv/bin/activate
    pip install cython
    pip install --no-binary :all: --upgrade cffi==1.14.6 --no-use-pep517

    # On mac
    OPENBLAS="$(brew --prefix openblas)" pip install --no-binary :all: -U numpy==1.21.2 --no-use-pep517
    # otherwise
    pip install --no-binary :all: -U numpy==1.21.2 --no-use-pep517

    pip install -r ../pyvcs/requirements.txt
