#stairmaker.py

import maya.cmds as mc
import functools

def createUI(pWindowTitle, pApply):
	winID = 'stairmaker'

	if mc.window(winID, exists = True):
		mc.deleteUI(winID)

	mc.window(winID, title = "stairmaker", sizeable = False, resizeToFitChildren = True)
	mc.rowColumnLayout(numberOfColumns = 3, columnWidth = [[1,75],[2,60],[3,60]], columnOffset = [[1,'right',3]])

	#first row
	mc.text('Height Range')
	hm = mc.floatField(value = 0)
	hM = mc.floatField(value = 10)

	hr = [hm,hM]

	#second row
	mc.text('Width Range')
	wm = mc.floatField(value = 0)
	wM = mc.floatField(value = 10)

	wr = [wm,wM]

	#third row
	mc.text('Depth Range')
	dm = mc.floatField(value = 0)
	dM = mc.floatField(value = 10)

	dr = [dm,dM]
	
	#fourth row
	mc.text('Steps')
	st = mc.intField(value = 10)
	mc.separator(height = 10, style = 'none')


	#blank row
	mc.separator(height = 10, style = 'none')
	mc.separator(height = 10, style = 'none')
	mc.separator(height = 10, style = 'none')

	def cancelCall( *pArgs):
		if mc.window(winID, exists = True):
			mc.deleteUI(winID)

	#buttons			
	mc.separator(height = 10, style = 'none')
	mc.button(label = 'Apply', command = functools.partial(pApply, hr, wr, dr, st))
	mc.button(label = 'Cancel', command = cancelCall)

	mc.showWindow(winID)

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


def apply(pHr, pWr, pDr, pSt, *pArgs):	
	hr = [mc.floatField(i, query = True, value = True) for i in pHr]
	wr = [mc.floatField(i, query = True, value = True) for i in pWr]
	dr = [mc.floatField(i, query = True, value = True) for i in pDr]
	st = mc.intField(pSt, query = True, value = True)
	stairs(hr, wr, dr, st)
	print "Apply Button Pressed"

createUI('stairmaker', apply)


