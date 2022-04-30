def getExReDims(app):
    x0 = app.width/2 - (app.width/20)
    x1 = app.width/2 + (app.width/20)
    rslope = app.height/app.width
    y1 = x1*rslope
    y0 = y1 - (x1-x0)/2
    return x0, y0, x1, y1

def drawGameBack(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="gray17")
    canvas.create_polygon(0, app.height, app.width//2, app.height//2, 
                          app.width, app.height, fill="gray")
    x0ExRe, y0ExRe, x1ExRe, y1ExRe = getExReDims(app)
    canvas.create_rectangle(x0ExRe, y0ExRe, x1ExRe, y1ExRe, fill="black")
    cxExOv, cyExOv, radExOv = app.width/2, (y1ExRe+y0ExRe)/2-(y1ExRe-y0ExRe)/2,\
                              y1ExRe-y0ExRe
    canvas.create_oval(cxExOv-radExOv, cyExOv-radExOv,
                       cxExOv+radExOv, cyExOv+radExOv, fill="black")
    0, 0, cxExOv, cyExOv
    canvas.create_line(0, 0, cxExOv, cyExOv, width=5)
    canvas.create_line(cxExOv, cyExOv, app.width, 0, width=5)
    i = 0
    for button in app.gameButDims:
        canvas.create_rectangle(button[0], button[1], button[2], button[3],
                                fill=f"{app.colorDiff[app.diff]}")
        if i == 0:
            canvas.create_text((button[0]+button[2])//2, 
                               (button[1]+button[3])//2, 
                                text=f"{app.gameButTxts[i]}",
                                font="Times 18 bold")
        elif i == 1:
            canvas.create_text((button[0]+button[2])//2, 
                               (button[1]+button[3])//2, 
                                text=f"{app.gameButTxts[i]}",
                                font="Times 18 bold")
        elif i == 2:
            canvas.create_text((button[0]+button[2])//2, 
                               (button[1]+button[3])//2, 
                                text=f"{app.gameButTxts[i]}"+f"{app.score}", 
                                font="Times 18 bold")
        elif i == 3:
            canvas.create_text((button[0]+button[2])//2, 
                               (button[1]+button[3])//2, 
                                text=f"{app.gameButTxts[i]}"+f"{app.lives}", 
                                font="Times 18 bold")
        elif i == 4:
            canvas.create_text((button[0]+button[2])//2, 
                               (button[1]+button[3])//2, 
                                text=f"{app.gameButTxts[i]}"+ \
                                    f"{app.powerUps[app.powerUpIndex]}", 
                                font="Times 18 bold")
        i += 1

def drawGameObjs(app,canvas):
    for plaser in app.plyrLaserDims:
        canvas.create_line(plaser[0], plaser[1], plaser[2], plaser[3],
                                fill="blue", width = app.laserWidth)
    for elaser in app.enemLaserDims:
        canvas.create_line(elaser[0], elaser[1], elaser[2], elaser[3],
                                fill="red", width = app.laserWidth)
    for powup in app.powerUpDims:
        canvas.create_polygon(powup[0], powup[1], powup[2],
                              powup[3], powup[4], powup[5],
                              fill="red")
    for trafcar in app.trafficCarDims:
        canvas.create_rectangle(trafcar[0],trafcar[1],trafcar[2],trafcar[3], 
                                fill="red")
    for alien in app.alienDims:
        canvas.create_rectangle(alien[0], alien[1], alien[2], alien[3],
                                fill="red")
        xOvAdj = ((alien[2]-alien[0])*0.25)//2
        x0, y0, x1, y1 = alien[0]+xOvAdj, alien[1]-((alien[2]-alien[0])*0.75), \
                         alien[2]-xOvAdj, alien[1]
        canvas.create_oval(x0, y0, x1, y1, fill="red")
    for dash in app.roadMarksDims:
        canvas.create_rectangle(dash[0], dash[1], dash[2], dash[3],
                                fill="yellow")
    for line in app.crossHairDims:
        canvas.create_line(line[0], line[1], line[2], line[3], fill="white")
    canvas.create_rectangle(app.plyrCarDim[0], app.plyrCarDim[1], 
                            app.plyrCarDim[2], app.plyrCarDim[3],
                            fill="blue")
    
def drawGame(app, canvas):
    drawGameBack(app,canvas)
    drawGameObjs(app,canvas)  