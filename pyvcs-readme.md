- autoconf
- ./configure
- make -j13 (I have 12 cores)

- create a virtual env with ./python.exe
- source ven/bin/activate
- pip install cython
- pip install --no-binary :all: --upgrade cffi==1.14.6 --no-use-pep517
- pip install --no-binary :all: -U numpy==1.21.2 --no-use-pep517
- pip install -r ../pyvcs/requirements.txt
- sudo apt-get install libportaudio2


Windows
=======
- .\PCbuild\build.bat
- create a venv with .\PCBuild\amd64\python.exe

WOAH, it's running colors_new with about 76 FPS using the PGO version of my custom python build.
game.py is around 55; flickering is happening though because right now the timing is still different.
