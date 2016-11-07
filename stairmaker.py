#stairmaker.py

import maya.cmds as mc
import functools

#function to create and display the UI
#params - pWindowTitle - Title of the Window
#	  pApply       - Apply callback
#return - nothing
def createUI(pWindowTitle, pApply):
	winID = 'stairmaker'

	if mc.window(winID, exists = True):
		mc.deleteUI(winID)

	mc.window(winID, title = "stairmaker", sizeable = False, resizeToFitChildren = True)
	mc.rowColumnLayout(numberOfColumns = 3, columnWidth = [[1,75],[2,60],[3,60]], columnOffset = [[1,'right',3]])

	#first row - obtain height range
	mc.text('Height Range')
	hm = mc.floatField(value = 0)
	hM = mc.floatField(value = 10)
	
	#put height range in a list
	hr = [hm,hM]

	#second row - obtain width range
	mc.text('Width Range')
	wm = mc.floatField(value = 0)
	wM = mc.floatField(value = 10)

	#put width range in a list
	wr = [wm,wM]

	#third row - obtain depth range
	mc.text('Depth Range')
	dm = mc.floatField(value = 0)
	dM = mc.floatField(value = 10)

	#put depth range in a list
	dr = [dm,dM]
	
	#fourth row - obtain number of steps
	mc.text('Steps')
	st = mc.intField(value = 10)
	mc.separator(height = 10, style = 'none')


	#blank row
	mc.separator(height = 10, style = 'none')
	mc.separator(height = 10, style = 'none')
	mc.separator(height = 10, style = 'none')

	#cancel callback
	def cancelCall( *pArgs):
		if mc.window(winID, exists = True):
			mc.deleteUI(winID)

	#buttons - apply button calls the pApply callback	
	mc.separator(height = 10, style = 'none')
	mc.button(label = 'Apply', command = functools.partial(pApply, hr, wr, dr, st))
	mc.button(label = 'Cancel', command = cancelCall)

	#display the UI
	mc.showWindow(winID)

#function to make the staircase
#params - pHr - Height range
#	  pWr - Width range
#	  pDr - Depth range
#	  pSt - Number of steps
#return - nothing
def stairs(pHr, pWr, pDr, pSt):
	print pHr, pWr, pSt
	pHr = sorted(pHr)
	pWr = sorted(pWr)
	pDr = sorted(pDr)
	h = pHr[1] - pHr[0]
	w = pWr[1] - pWr[0]
	d = pDr[1] - pDr[0]
	d/=pSt
	print h, w, d
	staircase = []
	#generate staircase step by step and add each step to the staircase list
	for i in range(pSt):
		sht = (h/pSt) * i
		single = h/pSt
		sh = sht + single/2
		sd = (i+0.5)*(d)
		cube = mc.polyCube(h = 1, n = "Stair"+str(i+1))
		staircase.append(cube)
		mc.move(w/2, sh, sd, cube)
		mc.scale(w, single, d, cube)

	staircase = mc.polyUnite(*staircase, n = "Staircase")

#apply function callback
#params - pHr - Height range
#	  pWr - Width range
#	  pDr - Depth range
#	  pSt - Number of steps
#return - nothing
def apply(pHr, pWr, pDr, pSt, *pArgs):	
	hr = [mc.floatField(i, query = True, value = True) for i in pHr]
	wr = [mc.floatField(i, query = True, value = True) for i in pWr]
	dr = [mc.floatField(i, query = True, value = True) for i in pDr]
	st = mc.intField(pSt, query = True, value = True)
	stairs(hr, wr, dr, st)
	print "Apply Button Pressed"

#create and display the UI
createUI('stairmaker', apply)
