import math, random
from PP_App_Start import *

def carMoveLegal(app):
    if app.plyrCarDim[0] < 0 or app.plyrCarDim[2] > app.width:
        return False
    return True

def changeCrossHair(app,event,dx,dy):
    for line in app.crossHairDims:
        for i in range(len(line)):
            if i%2 == 1:
                line[i] += dy
            else:
                line[i] += dx

def chMoveLegal(app):
    for line in app.crossHairDims:
        for i in range(len(line)):
            if i%2 == 1:
                if line[i] < 0 or line[i] > app.height:
                    return False
            else:
                if line[i] < 0 or line[i] > app.width:
                    return False
    return True

def restartRound(app):
    app.scores.append(app.score)
    app.scores.sort()
    app.score = 0
    app.plyrCarDim[0] = app.width//2-app.width//15
    app.plyrCarDim[2] = app.width//2+app.width//15
    app.crossHairDims = getCrossHairDims(app)
    app.plyrLaserDims = []
    app.powerUpDims = []
    app.timerDelayCnt = 0
    app.lives = 5
    app.enemLaserDims = []
    app.currentHCTime = 0
    app.alienDims = []
    app.trafficCarDims = []
    app.powerUpIndex = 3

def plyrFireLaser(app):
    if app.weaponTypeI == 1:
        if app.timerDelayCnt - app.currentHCTime < 4:
            return None
        app.currentHCTime = app.timerDelayCnt
    x0, y0 = (app.plyrCarDim[0]+app.plyrCarDim[2])//2, app.plyrCarDim[1]
    xch, ych = app.crossHairDims[0][0], app.crossHairDims[1][3]
    try: 
        slope = (y0-ych)/(x0-xch)
        inter = y0-slope*x0
    except:
        slope = 0
        inter = 0
    if slope > 0:
        x1, y1 = x0-(app.laserDist/(math.sqrt(1+(slope**2)))), \
                 y0-((app.laserDist*slope)/(math.sqrt(1+(slope**2))))
    elif slope < 0:
        x1, y1 = x0+(app.laserDist/(math.sqrt(1+(slope**2)))), \
                 y0+((app.laserDist*slope)/(math.sqrt(1+(slope**2))))
    else:
        x1, y1 = x0, y0 - app.laserDist
    app.lasersFired += 1
    app.plyrLaserDims.append([x0,y0,x1,y1,slope,inter])
    if app.weaponTypeI == 2:
        app.lasersFired += 1
        app.plyrLaserDims.append([x0-app.pulseShift,y0,x1-app.pulseShift,\
                                  y1,slope,inter-app.pulseShift])
        app.plyrLaserDims.append([x0+app.pulseShift,y0,x1+app.pulseShift,\
                                  y1,slope,inter+app.pulseShift])

def powUpIndCycle(app):
    if app.powerUpIndex >= 0 and app.powerUpIndex < 3:
        app.powerUpIndex += 1
    elif app.powerUpIndex == 3:
        app.powerUpIndex = 0

def gameKey(app, event):
    if event.key == "Left":
        app.plyrCarDim[0] -= app.plyrCarMove
        app.plyrCarDim[2] -= app.plyrCarMove
        if carMoveLegal(app) == False:
            app.plyrCarDim[0] += app.plyrCarMove
            app.plyrCarDim[2] += app.plyrCarMove
    elif event.key == "Right":
        app.plyrCarDim[0] += app.plyrCarMove
        app.plyrCarDim[2] += app.plyrCarMove
        if carMoveLegal(app) == False:
            app.plyrCarDim[0] -= app.plyrCarMove
            app.plyrCarDim[2] -= app.plyrCarMove
    elif event.key == "a":
        changeCrossHair(app,event,-app.plyrCarMove,0)
        if chMoveLegal(app) == False:
            changeCrossHair(app,event,app.plyrCarMove,0)
    elif event.key == "s":
        changeCrossHair(app,event,0,app.plyrCarMove)
        if chMoveLegal(app) == False:
            changeCrossHair(app,event,0,-app.plyrCarMove)
    elif event.key == "d":
        changeCrossHair(app,event,app.plyrCarMove,0)
        if chMoveLegal(app) == False:
            changeCrossHair(app,event,-app.plyrCarMove,0)
    elif event.key == "w":
        changeCrossHair(app,event,0,-app.plyrCarMove)
        if chMoveLegal(app) == False:
            changeCrossHair(app,event,0,app.plyrCarMove)
    elif event.key == "Escape":
        app.window = 0
        restartRound(app)
    elif event.key == "r":
        restartRound(app)
    elif event.key == "Space":
        plyrFireLaser(app)
    elif event.key == "p":
        powUpIndCycle(app)
    
def setKey(app,event):
    if event.key == "Escape":
        app.window = 0
    elif event.key == "Left":
        if app.weaponTypeI > 0 and app.weaponTypeI < 3:
            app.weaponTypeI -= 1
    elif event.key == "Right":
        if app.weaponTypeI > -1 and app.weaponTypeI < 2:
            app.weaponTypeI += 1
    elif event.key == "Up":
        if app.diff > -1 and app.diff < 2:
            app.diff += 1
            app.lives -= 1
    elif event.key == "Down":
        if app.diff > 0 and app.diff < 3:
            app.diff -= 1
            app.lives += 1

def htpKey(app,event):
    if event.key == "Escape":
        app.window = 0

def keyPressed(app,event):
    if app.window == 0:
        pass
    elif app.window == 1:
        gameKey(app,event)
    elif app.window == 2:
        htpKey(app,event)
    elif app.window == 3:
        setKey(app,event)


def mainMenuClick(app,event):
    i = 0
    for button in app.mainButDims:
        if event.x >= button[0] and event.x <= button[2] \
            and event.y >= button[1] and event.y <= button[3]:
            if i in [2,3]:
                app.window = 1
            elif i in [4,5]:
                app.window = 2
            elif i in [6,7]:
                app.window = 3
        i += 1

def gameClick(app,event):
    i = 0
    for button in app.gameButDims:
        if event.x >= button[0] and event.x <= button[2] \
            and event.y >= button[1] and event.y <= button[3]:
            if i == 0:
                app.window = 0
                restartRound(app)
            elif i == 1:
                restartRound(app)
        i += 1

def setClick(app,event):
    if event.x >= app.settingsButtonDims[0][0] and \
        event.x <= app.settingsButtonDims[0][2] \
        and event.y >= app.settingsButtonDims[0][1] \
        and event.y <= app.settingsButtonDims[0][3]:
        app.window = 0

def htpClick(app,event):
    if event.x >= app.settingsButtonDims[0][0] and \
        event.x <= app.settingsButtonDims[0][2] \
        and event.y >= app.settingsButtonDims[0][1] \
        and event.y <= app.settingsButtonDims[0][3]:
        app.window = 0

def mousePressed(app,event):
    if app.window == 0:
        mainMenuClick(app,event)
    elif app.window == 1:
        gameClick(app,event)
    elif app.window == 2:
        htpClick(app,event)
    elif app.window == 3:
        setClick(app,event)

def checkElaserPlyrCar(app,elaser):
    if (elaser[0] > app.plyrCarDim[0] and elaser[0] < app.plyrCarDim[2] and \
        elaser[1] > app.plyrCarDim[1] and elaser[1] < app.plyrCarDim[3]) or \
        (elaser[2] > app.plyrCarDim[0] and elaser[2] < app.plyrCarDim[2] \
        and elaser[3] > app.plyrCarDim[1] and elaser[3] < app.plyrCarDim[3]):
        return False
    return True

def checkElaserLegal(app, elaser):
    if elaser[0] < 0 or elaser[0] > app.width or elaser[2] < 0 or \
        elaser[2] > app.width or elaser[1] < 0 or elaser[1] > app.height or \
            elaser[3] < 0 or elaser[3] > app.height:
        return False
    elif checkElaserPlyrCar(app,elaser) == False:
        app.lives -= 1
        if app.powerUpIndex == 2:
            app.lives += 1
        return False
    return True

def enemLaserCycle(app):
    i = 0
    for elaser in app.enemLaserDims:
        xdist = abs(elaser[2]-elaser[0])
        if xdist == 0:
            xdist = 0.75
        xadj = xdist*app.plyrLaserSpeed
        if elaser[4] > 0:
            elaser[0] += xadj
            elaser[2] += xadj
            oldy0, oldy1 = elaser[1], elaser[3]
            elaser[1], elaser[3] = elaser[4]*elaser[0]+elaser[5], \
                                   elaser[4]*elaser[2]+elaser[5]
            if checkElaserLegal(app, elaser) == False:
                if app.powerUpIndex == 2:
                    app.lasersFired += 1
                    app.plyrLaserDims.append(app.enemLaserDims[i])  
                app.enemLaserDims.pop(i)
                if app.lives == 0:
                    restartRound(app)
        elif elaser[4] < 0:
            elaser[0] -= xadj
            elaser[2] -= xadj
            oldy0, oldy1 = elaser[1], elaser[3]
            elaser[1], elaser[3] = elaser[4]*elaser[0]+elaser[5], \
                                   elaser[4]*elaser[2]+elaser[5]
            if checkElaserLegal(app, elaser) == False:
                if app.powerUpIndex == 2:
                    app.lasersFired += 1
                    app.plyrLaserDims.append(app.enemLaserDims[i])
                app.enemLaserDims.pop(i)
                if app.lives == 0:
                    restartRound(app)
        else:
            elaser[1] += 15
            elaser[3] += 15
            if checkElaserLegal(app, elaser) == False:
                app.enemLaserDims.pop(i)
                if app.lives == 0:
                    restartRound(app)
        i += 1

def checkPlaserEnem(app, plaser):
    i = 0
    for enem in app.alienDims:
        xOvAdj = ((enem[2]-enem[0])*0.25)//2
        x0, y0, x1, y1 = enem[0]+xOvAdj, enem[1]-((enem[2]-enem[0])*0.75), \
                         enem[2]-xOvAdj, enem[1]
        if (plaser[0] > x0 and plaser[0] < x1 and \
            plaser[1] > y0 and plaser[1] < y1) or \
           (plaser[2] > x0 and plaser[2] < x1 \
            and plaser[3] > y0 and plaser[3] < y1):
            app.score += 2
            if app.powerUpIndex == 0:
                app.score += 2
            app.alienDims.pop(i)
            return True
        elif (plaser[0] > enem[0] and plaser[0] < enem[2] and \
              plaser[1] > enem[1] and plaser[1] < enem[3]) or \
             (plaser[2] > enem[0] and plaser[2] < enem[2] \
              and plaser[3] > enem[1] and plaser[3] < enem[3]):
            app.score += 1
            if app.powerUpIndex == 0:
                app.score += 1
            app.alienDims.pop(i)
            return True
        i += 1
    return False

def checkPlaserLegal(app, plaser):
    if plaser[0] < 0 or plaser[0] > app.width or plaser[2] < 0 or \
        plaser[2] > app.width or plaser[1] < 0 or plaser[1] > app.height or \
            plaser[3] < 0 or plaser[3] > app.height:
        return False
    elif checkPlaserEnem(app, plaser) == True:
        app.lasersHit += 1
        return False
    return True

def plaserCycle(app):
    i = 0
    for plaser in app.plyrLaserDims:
        xdist = abs(plaser[2]-plaser[0])
        if xdist == 0:
            xdist = 0.75
        xadj = xdist*app.plyrLaserSpeed
        if plaser[4] > 0:
            plaser[0] -= xadj
            plaser[2] -= xadj
            oldy0, oldy1 = plaser[1], plaser[3]
            plaser[1], plaser[3] = plaser[4]*plaser[0]+plaser[5], \
                                   plaser[4]*plaser[2]+plaser[5]
            if checkPlaserLegal(app, plaser) == False:
                app.plyrLaserDims.pop(i)
        elif plaser[4] < 0:
            plaser[0] += xadj
            plaser[2] += xadj
            oldy0, oldy1 = plaser[1], plaser[3]
            plaser[1], plaser[3] = plaser[4]*plaser[0]+plaser[5], \
                                   plaser[4]*plaser[2]+plaser[5]
            if checkPlaserLegal(app, plaser) == False:
                app.plyrLaserDims.pop(i)
        else:
            plaser[1] -= 15
            plaser[3] -= 15
            if checkPlaserLegal(app, plaser) == False:
                app.plyrLaserDims.pop(i)
        i += 1
        

def createPowerUp(app):
    xrandi = random.randint(0,1)
    x0, y0 = app.roadObjXs[xrandi],app.powerUpY0
    x1, y1, x2, y2 = x0-app.roadObjLength//2, \
                     y0+(math.sqrt(3))*(app.roadObjLength//2), \
                     x0+app.roadObjLength//2, \
                     y0+(math.sqrt(3))*(app.roadObjLength//2)
    if xrandi == 0:
        slope = (app.height-y0)/(app.width//4-x0)
    else:
        slope = (app.height-y0)/((app.width-app.width//4)-x0)
    inter = y0-(slope*x0)
    typerandi = random.randint(0,2)
    app.powerUpDims.append([x0,y0,x1,y1,x2,y2,slope,inter,typerandi])

def createAlien(app):
    randi = random.randint(0,1)
    if randi == 0:
        x1, y1 = app.alienXs[randi], app.alienY[randi]
        x0, y0 = x1-30,y1-50
        direc = 0
    else:
        x0, y0 = app.alienXs[randi], app.alienY[randi]
        x1, y1 = x0+30,y0+50
        direc = 1
    app.alienDims.append([x0,y0,x1,y1, direc])

def checkPowUpPlyrCar(app, powup):
    if (powup[0] > app.plyrCarDim[0] and powup[0] < app.plyrCarDim[2] and \
        powup[1] > app.plyrCarDim[1] and powup[1] < app.plyrCarDim[3]) or \
        (powup[2] > app.plyrCarDim[0] and powup[2] < app.plyrCarDim[2] \
        and powup[3] > app.plyrCarDim[1] and powup[3] < app.plyrCarDim[3]) \
        or (powup[4] > app.plyrCarDim[0] and powup[4] < app.plyrCarDim[2] \
        and powup[5] > app.plyrCarDim[1] and powup[5] < app.plyrCarDim[3]):
        app.powerUpIndex = powup[8]
        app.powerUpTimer = 0
        return True
    return False

def checkPowUpLegal(app, powup):
    if powup[0] < 0 or powup[0] > app.width or powup[2] < 0 or \
        powup[2] > app.width or powup[1] < 0 or powup[1] > app.height or \
            powup[3] < 0 or powup[3] > app.height:
        return False
    elif checkPowUpPlyrCar(app, powup) == True:
        return False
    return True

def powerUpCycle(app):
    i = 0
    for powup in app.powerUpDims:
        if powup[6] > 0:
            dx, dy = (20/(math.sqrt(1+(powup[6]**2)))), \
                    ((20*powup[6])/(math.sqrt(1+(powup[6]**2))))
            powup[0] += dx
            powup[1] += dy
            powup[2] += dx      
            powup[3] += dy
            powup[4] += dx
            powup[5] += dy
        elif powup[6] < 0:
            dx, dy = (20/(math.sqrt(1+(powup[6]**2)))), \
                    ((20*powup[6])/(math.sqrt(1+(powup[6]**2))))
            powup[0] -= dx
            powup[1] -= dy
            powup[2] -= dx      
            powup[3] -= dy
            powup[4] -= dx
            powup[5] -= dy
        if checkPowUpLegal(app, powup) == False:
            app.powerUpDims.pop(i)
        i += 1
            

def alienCycle(app):
    for alien in app.alienDims:
        alien[1] -= 3
        alien[3] += 3
        if alien[4] == 0:
            alien[0] -= 15
            alien[2] -= 15
        else:
            alien[0] += 15
            alien[2] += 15

def createAlienLaser(app):
    if app.powerUpIndex != 1:
        for alien in app.alienDims:
            x0, y0 = (alien[0]+alien[2])//2, (alien[1]+alien[3])//2
            xcar, ycar = (app.plyrCarDim[0]+app.plyrCarDim[2])//2, \
                         (app.plyrCarDim[1]+app.plyrCarDim[3])//2
            try: 
                slope = (ycar-y0)/(xcar-x0)
                inter = y0-slope*x0
            except:
                slope = 0
                inter = 0
            if slope > 0:
                x1, y1 = x0-(app.laserDist/(math.sqrt(1+(slope**2)))), \
                         y0-((app.laserDist*slope)/(math.sqrt(1+(slope**2))))
            elif slope < 0:
                x1, y1 = x0+(app.laserDist/(math.sqrt(1+(slope**2)))), \
                         y0+((app.laserDist*slope)/(math.sqrt(1+(slope**2))))
            else:
                x1, y1 = x0, y0 - app.laserDist
            app.enemLaserDims.append([x0,y0,x1,y1,slope,inter])

def createTrafficCar(app):
    xrandi = random.randint(0,1)
    cx, y0 = app.roadObjXs[xrandi], app.newRoadMarkY0
    x0, x1, y1 = cx-app.roadObjLength//2, cx+app.roadObjLength//2, \
                 app.newRoadMarkY0+app.roadObjLength//3
    if xrandi == 0:
        slope = (app.height-y1)/(app.width//4-cx)
    else:
        slope = (app.height-y1)/((app.width-app.width//4)-cx)
    inter = y0-(slope*x0)
    app.trafficCarDims.append([x0,y0,x1,y1,slope,inter])

def trafficCarCycle(app):
    i = 0
    for trafcar in app.trafficCarDims:
        if trafcar[4] > 0:
            dx, dy = (20/(math.sqrt(1+(trafcar[4]**2)))), \
                    ((20*trafcar[4])/(math.sqrt(1+(trafcar[4]**2))))
            trafcar[0] += dx
            trafcar[1] += dy
            trafcar[2] += dx      
            trafcar[3] += dy
        elif trafcar[4] < 0:
            dx, dy = (20/(math.sqrt(1+(trafcar[4]**2)))), \
                    ((20*trafcar[4])/(math.sqrt(1+(trafcar[4]**2))))
            trafcar[0] -= dx
            trafcar[1] -= dy
            trafcar[2] -= dx      
            trafcar[3] -= dy
        # if checkTrafCarLegal(app, trafcar) == False:
        #     app.trafficCarDims.pop(i)
        i += 1
