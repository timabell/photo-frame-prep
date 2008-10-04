#!/usr/bin/python

# http://www.zetcode.com/wxpython/firststeps/ - how to show a frame

import wx #import normal wxPython widgets library
import gui # import wxGlade generated gui from gui.py
import shutil #file utilities

#inherit from the gui class

class MyApp(gui.MyFrame):
	def __init__(self, *args, **kwds):
		gui.MyFrame.__init__(self, *args, **kwds) #call base class init
		#bind event handler for go button
		self.gobutton.Bind(wx.EVT_BUTTON,  self.goClicked)
		
	#event handler for go button
	def goClicked(source,  event):
		print 'go clicked'
		processor = PhotoProcessing(source.outputfolder.GetValue())
		processor.processPhoto(source.inputfolder.GetValue())


class PhotoProcessing():
	output = ''
	def __init__(self,  outputPath):
		global output
		output=outputPath
		
	def  processFolder(self,  inputFolder):
		print 'processing folder ',  inputFolder
		
	def processPhoto(self,  inputPhotoPath):
		print 'processing photo, path: ',  inputPhotoPath,  ' output path: ',  output
		#copy to output folder
		shutil.copy(inputPhotoPath,  output)
		#rotate to match exif rotate tag
		#exiftran -ai "$INPUTFILE"
		#resize and add black background if aspect ratio doesn't match frame size
		#convert "$INPUTFILE" -resize '800x600>' -background black -gravity center -extent 800x600 "$INPUTFILE"

print 'starting up app...'
app = wx.App() # um, something to initialize the app i guess. don't really know
frame = MyApp(None, -1,  'photo-frame-prep.py') # load the frame overriden gui class
frame.Show() #show the frame (presumably)
app.MainLoop() #run the app, or something

