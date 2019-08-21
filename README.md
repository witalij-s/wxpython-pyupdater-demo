# WXPython Updater

A demo project using pyupdater and wxPython for creating a self updating
linux application.

## Installation

Ubuntu 16.04 & Python2.7:

```shell
pip install pyupdater
pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux gtk3/ubuntu-16.04 \
   wxPython
```

## Configuration

1. Create a keypack. In the repo folder type: `pyupdater keys -c`
2. Enter the name of you application: `maindemo`
3. Now initialize the project: `pyupdater init`
4. Enter projectname: _maindemo_ | Company: _maindemo Ltd_ | Url: _localhost:8000_ | Backup URL: _N_ | Enable patch update: _N_ | Use current directory: _Y_
5. Import the keys: `pyupdater keys -i`
6. Now create a spec file for future builds: `pyupdater make-spec -w run.py`
7. Your project folder should now contain a `/nix64.spec` file.
8. Next you can start to build a release with the generated spec.


## Build / Release

1. Open the file `wxpythonupdater/__init__.py` and increase the version to **1.0.0**.
2. Create a release: `pyupdater build --app-version=1.0.0 nix64.spec`
3. Sign the release: `pyupdater pkg --process --sign`
4. In `pyu-data/deploy` is now version 1.0.0 and a `keys.tar.gz` and a `versions.tar.gz`.
5. Your release is ready and depoyed on your machine
6. Now start a fileserver for testing.


## Fileserver for Uploading and Testing Updates

Start a fileserver so you are able to check for updates.
1. Run: `./run_fileserver`
2. Open your browser and navigate to: `localhost:8000`
3. Download and extract the release
4. Execute the demo application: `./maindemo`


## One-Click Start of you Application

This enables a file for double click execution. Test on Linux Mint:
1. Open the `nix64.spec`
2. Add the `Start.desktop` file to the project like the following
```
...

added_files = [('assets/Start.desktop', '.')]

a = Analysis(['/home/<username>/Git/wx-python/run.py'],
             pathex=['/home/<username>/Git/wx-python', u'/home/<username>/Git/wx-python'],
             binaries=[],
             datas=added_files,
...
```
3. Replace `<username>` with your linux username.
4. Now build and sign.

## Contributions

This project was created with the content of the following ressources:
- An example pyupdater project: https://github.com/wettenhj/pyupdater-wx-demo
- Tutorials from the official wxpython documentation: https://wxpython.org/


[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)
