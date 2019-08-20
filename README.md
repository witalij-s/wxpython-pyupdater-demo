# WXPython Updater

A demo project using pyupdater and wxPython for creating a self updating
linux application.

## Install wx

```
pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux gtk3/ubuntu-16.04 \
   wxPython
```


## Build / Release

1. `pyupdater build --app-version=1.0.0 main.spec`
2. `pyupdater pkg --process --sign`


## Notes

- You almost always want to use wx.ID_ANY or another standard ID (v2.8) provided by wxWidgets.
- List of Events: https://wiki.wxpython.org/ListOfEvents
- List of IDs: https://docs.wxwidgets.org/2.8.12/wx_stdevtid.html


## Fileserver for Uploading and Testing Updates

Start a fileserver so you are able to check for updates.
Run: `./run_fileserver`



