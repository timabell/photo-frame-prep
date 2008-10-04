#!/usr/bin/python

#standard library imports
import wx #import normal wxPython widgets library
import shutil #file utilities
import os #to execute shell commands (ideally remove this and use native python libaries to deal with images)

#local module imports
import gui # import wxGlade generated gui from gui.py

#inherit from the gui class to separate hand crafted code from generated form code
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

#main class for doing the work of this application
class PhotoProcessing():
	output = ''
	def __init__(self,  outputPath):
		global output
		output=outputPath
		
	def  processFolder(self,  inputFolder):
		print 'processing folder ',  inputFolder
		
	def processPhoto(self,  inputPhotoPath):
		print 'processing photo, path: ',  inputPhotoPath,  ' output path: ',  output
		filename = os.path.basename(inputPhotoPath)
		#copy to output folder
		shutil.copy(inputPhotoPath,  output)
		outputfile = output + filename
		#rotate to match exif rotate tag
		print 'executing exiftran -ai ',  outputfile 
		os.system('exiftran -ai ' + outputfile )
		#exiftran -ai "$INPUTFILE"
		#resize and add black background if aspect ratio doesn't match frame size
		print 'convert "' + outputfile  + '" -resize \'800x600>\' -background black -gravity center -extent 800x600 ' + outputfile 
		os.system('convert "' + outputfile  + '" -resize \'800x600>\' -background black -gravity center -extent 800x600 ' + outputfile)
		#convert "$INPUTFILE" -resize '800x600>' -background black -gravity center -extent 800x600 "$INPUTFILE"

#program flow starts here.
print 'starting up app...'
app = wx.App() # um, something to initialize the app i guess. don't really know
frame = MyApp(None, -1,  'photo-frame-prep.py') # load the frame overriden gui class
frame.Show() #show the frame (presumably)
app.MainLoop() #run the app, or something

