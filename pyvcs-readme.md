- autoconf
- ./configure
- make

- create a virtual env with ./python.exe
- source ven/bin/activate
- pip install cython
- pip install --no-binary :all: --upgrade cffi==1.14.6 --no-use-pep517
- pip install --no-binary :all: -U numpy==1.21.2 --no-use-pep517
- pip install -r ../pyvcs/requirements.txt
- sudo apt-get install libportaudio2