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

## Build / Release

1. `pyupdater build --app-version=1.0.0 nix64.spec`
2. `pyupdater pkg --process --sign`

## Notes

- You almost always want to use wx.ID_ANY or another standard ID (v2.8) provided by wxWidgets.
- List of Events: https://wiki.wxpython.org/ListOfEvents
- List of IDs: https://docs.wxwidgets.org/2.8.12/wx_stdevtid.html


## Fileserver for Uploading and Testing Updates

Start a fileserver so you are able to check for updates.
Run: `./run_fileserver`


## Contributions

This project was created with the content of the following ressources:
- An example pyupdater project: https://github.com/wettenhj/pyupdater-wx-demo
- Tutorials from the official wxpython documentation: https://wxpython.org/
