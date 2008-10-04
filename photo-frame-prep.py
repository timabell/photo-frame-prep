#!/usr/bin/python

# http://www.zetcode.com/wxpython/firststeps/ - how to show a frame

import wx #import normal wxPython widgets library
import gui # import wxGlade generated gui from gui.py

#inherit from the gui class

class MyApp(gui.MyFrame):
	def __init__(self, *args, **kwds):
		gui.MyFrame.__init__(self, *args, **kwds) #call base class init
		#bind event handler for go button
		self.gobutton.Bind(wx.EVT_BUTTON,  self.goClicked)
		
	#event handler for go button
	def goClicked(source,  event):
		print 'clicked'


print 'starting up app...'
app = wx.App() # um, something to initialize the app i guess. don't really know
frame = MyApp(None, -1,  'photo-frame-prep.py') # load the frame overriden gui class
frame.Show() #show the frame (presumably)
app.MainLoop() #run the app, or something

