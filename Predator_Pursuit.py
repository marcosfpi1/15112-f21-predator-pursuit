#################################################
# Predator Pursuit
# By Marcos Pi Marrero
#################################################

from cmu_112_graphics import *
from PP_App_Start import *
from PP_Main_Menu import *
from PP_Game import *
from PP_How_to_Play import *
from PP_Settings import *
from PP_Mechanics import *

def appStarted(app):
    app.lasersFired = 0
    app.lasersHit = 0
    app.timerDelayCnt = 0
    app.diff = 0
    app.window = 0
    app.score = 0
    app.currentHCTime = 0
    app.powerUpTimer = 0
    app.plyrLaserSpeed = 0.5
    app.powerUpSpeed = 0.5
    app.weaponTypeI = 1
    app.powerUpIndex = 3
    app.lives = 5
    app.laserWidth = 5
    app.pulseShift = 10
    app.plyrCarMove = 15
    app.crossHairMove = 15
    app.laserDist = 30
    app.roadObjLength = 50
    app.newRoadMarkY0 = 470
    app.powerUpY0 = 470
    app.timerDelay = 500
    app.scores = []
    app.plyrLaserDims = []
    app.enemLaserDims = []
    app.powerUpDims = []
    app.alienDims = []
    app.trafficCarDims = []
    app.alienLives = [1, 2, 3]
    app.alienY = [460, 410]
    app.alienXs = [630,770]
    app.roadObjXs = [app.width//2-50, app.width//2+50]
    app.colorDiff = ["green", "blue", "red"]
    app.mainButCol = ["black","gray"]
    app.mainTextCol = ["black","grey95"]
    app.mainText = ["Predator Pursuit", "Play Game", "How to Play", "Settings"]
    app.mainTextRight = ["High Scores", "Statistics"]
    app.gameButTxts = ["Main Menu","Restart","Score:","Lives:", "Powerup:"]
    app.weaponTypes = ["Auto Rifle", "Hand Cannon", "Pulse Rifle"]
    app.powerUps = ["2X", "Invis", "Shield", "None"]
    app.alienRaces = ["red", "green", "blue"]
    app.setText = ["Main Menu", "Weapon\n(Change with left, right)", \
                   "Start Lives\n(Can't change manually)", \
                   "Start Difficulty\n(Change with up, down)"]
    app.mainButDims = getMainButDims(app)
    app.gameButDims = getGameButDims(app)
    app.plyrCarDim = getPlyrCarDim(app)
    app.crossHairDims = getCrossHairDims(app)
    app.roadMarksDims = getRoadMarksDims(app)
    app.settingsButtonDims = getSetButDims(app)
    app.htpButtonDims = getSetButDims(app)

def timerFired(app):
    if app.score >= 5:
        if app.diff == 0:
            app.diff += 1
    elif app.score >= 10:
        if app.diff == 1:
            app.diff += 1
    app.timerDelayCnt += 1
    app.powerUpTimer += 1
    if app.powerUpTimer % 30 == 0:
        app.powerUpIndex = 3
    if app.window == 0:
        pass
    elif app.window == 1:
        if app.timerDelayCnt % 2 == 0:
            alienCycle(app)
            trafficCarCycle(app)
            powerUpCycle(app)
        plaserCycle(app)
        enemLaserCycle(app)
        powerUpCycle(app)
        if app.diff == 0:
            if app.timerDelayCnt % 60 == 0:
                createPowerUp(app)
            elif app.timerDelayCnt % 40 == 0:
                createTrafficCar(app)
            elif app.timerDelayCnt % 30 == 0:
                createAlien(app)
            elif app.timerDelayCnt % 8 == 0:
                createAlienLaser(app)
        elif app.diff == 1:
            if app.timerDelayCnt % 70 == 0:
                createPowerUp(app)
            elif app.timerDelayCnt % 35 == 0:
                createTrafficCar(app)
            elif app.timerDelayCnt % 25 == 0:
                createAlien(app)
            elif app.timerDelayCnt % 7 == 0:
                createAlienLaser(app)
        elif app.diff == 2:
            if app.timerDelayCnt % 80 == 0:
                createPowerUp(app)
            elif app.timerDelayCnt % 30 == 0:
                createTrafficCar(app)
            elif app.timerDelayCnt % 20 == 0:
                createAlien(app)
            elif app.timerDelayCnt % 6 == 0:
                createAlienLaser(app)



def redrawAll(app,canvas):
    if app.window == 0:
        drawMainMenu(app,canvas)
    elif app.window == 1:
        drawGame(app, canvas)
    elif app.window == 2:
        drawHTP(app,canvas)
    elif app.window == 3:
        drawSettings(app,canvas)

def playFPSArcade():
    runApp(width=1400, height=1000)

playFPSArcade()