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
		self.inputBrowseFile.Bind(wx.EVT_BUTTON,  self.browseInputFile)
		self.inputBrowseFolder.Bind(wx.EVT_BUTTON,  self.browseinputPath)
		self.outputBrowse.Bind(wx.EVT_BUTTON,  self.browseOutput)
		
	#event handler for go button
	def goClicked(self,  event):
		print 'go clicked'
		#TODO fail if paths missing / invalid
		processor = PhotoProcessing(self.outputPath.GetValue())
		processor.process(self.inputPath.GetValue())
		
	def browseInputFile(self, event):
		self.browseFile(self.inputPath)
		
	def browseinputPath(self, event):
		self.browseFolder(self.inputPath)
		
	def browseOutput(self, event):
		self.browseFolder(self.outputPath)
		
	def browseFile(self,  target):
		dlg = wx.FileDialog(self, message="Choose a file")
		filename = ""
		dlg.SetPath(os.path.dirname(target.GetValue())) #open at last location
		if dlg.ShowModal() == wx.ID_OK:
			filename = dlg.GetPath()
		if filename:
			target.SetValue(filename)
		
	def browseFolder(self,  target):
		dlg = wx.DirDialog(self, message="Choose a file")
		filename = ""
		dlg.SetPath(target.GetValue()) #open at last location
		if dlg.ShowModal() == wx.ID_OK:
			filename = dlg.GetPath()
		if filename:
			target.SetValue(filename + '/')

#main class for doing the work of this application
class PhotoProcessing():
	output = ''
	def __init__(self,  outputPath):
		global output
		output=outputPath
		
	#process file or folder (recursively)
	def  process(self,  inputPath):
		if os.path.basename(inputPath)=="": #check if path has a filename
			self.processFolder(inputPath)
		else:
			self.processPhoto(inputPath)
		
	def  processFolder(self,  inputPath):
		print 'processing folder ',  inputPath
		
	def processPhoto(self,  inputPhotoPath):
		print 'processing photo, path: ',  inputPhotoPath,  ' output path: ',  output
		filename = os.path.basename(inputPhotoPath)
		#copy to output folder
		shutil.copy(inputPhotoPath,  output)
		outputfile = os.path.join(output, filename)
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

