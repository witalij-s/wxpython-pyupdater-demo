#!/usr/bin/env python
import wx
import os
import logging as log

from . import __version__

class MainWindow(wx.Frame):
    """ We simply derive a new class of frame."""
    def __init__(self, parent, title):
        log.info("Creating MainWindow Frame")
        wx.Frame.__init__(self, parent, title=title, size=(400,400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control.SetValue("Update works " + __version__ + "!")
        self.CreateStatusBar() # A Statusbar at the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuItemOpen = filemenu.Append(wx.ID_OPEN, "Open"," Information about this program")
        filemenu.AppendSeparator()
        menuItemAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuItemExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events
        self.Bind(wx.EVT_MENU, self.OnOpen, menuItemOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItemAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuItemExit)

        self.Show(True)

    def OnOpen(self,e):
        # Open a file
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor. Version: "+__version__, "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    @staticmethod
    def Run():
        app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
        # A Frame is a top-level window.
        frame = MainWindow(None, "Small editor") #(No Parent, wx will pick ID for us, Title)
        app.MainLoop()
        return app
