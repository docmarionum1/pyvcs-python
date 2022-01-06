# pyvcs-python

This repo is a Python interpreter for the [pyvcs](https://github.com/docmarionum1/pyvcs)
(Python Video Computer System) fantasy console. See that repo for details about the project.

This is a fork of [Python 3.9.6](https://github.com/python/cpython/tree/v3.9.6) with a
[modified eval loop](https://github.com/docmarionum1/pyvcs-python/blob/pyvcs/Python/ceval.c#L1009)
to call the pyvcs system code while executing user code. The rest of the pyvcs implementation is
in the pyvcs repo.

Currently you need to build pyvcs-python on your machine. We're planning on releasing prebuilt
executables in the future.

## Building pyvcs-python


Clone this repository locally and then follow the platform-specific instructions below:

### Windows

- Install Microsoft Visual Studio 2017 with Python workload and
Python native development component.
(From the python PCBuild readme: )

Then from PowerShell run:
```bash
.\PCbuild\build.bat -e --pgo -q
```

See the official python PC build
[readme](https://github.com/docmarionum1/pyvcs-python/blob/pyvcs/PCbuild/readme.txt) for
troubleshooting.

### Ubuntu (Untested)

From bash run:
```bash
sudo apt-get install libportaudio2
./configure --enable-optimizations --with-lto
make -j8
```

### Mac (Untested)

From bash run:
```bash
HOMEBREW_NO_AUTO_UPDATE=1 brew install openssl xz gdbm openblas
./configure --with-openssl=$(brew --prefix openssl) --enable-optimizations --with-lto
make -j8
```


### Setting a new version(?)

Run:
```bash
autoconf
```
