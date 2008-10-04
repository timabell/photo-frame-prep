#!/usr/bin/python

# http://www.zetcode.com/wxpython/firststeps/ - how to show a frame

import wx #import normal wxPython widgets library
import gui # import wxGlade generated gui from gui.py
app = wx.App() # um, something to initialize the app i guess. don't really know
frame = gui.MyFrame(None, -1,  'photo-frame-prep.py') # load the frame defined in our gui file
frame.Show() #show the frame (presumably)
app.MainLoop() #run the app, or something
