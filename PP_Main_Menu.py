def drawMainSBStat(app,canvas):
    try:
        acc = app.lasersHit/app.lasersFired
    except:
        acc = "N/A"
    canvas.create_text(app.width-app.width//6, 
                        app.height-app.height//8*2.6,
                        text=f"{acc}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//6*2, 
                        app.height-app.height//8*2.6,
                        text=f"Accuracy:",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")                  
    canvas.create_text(app.width-app.width//6,
                        app.height-app.height//8*2,
                        text=f"{app.lasersHit}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//6*2,
                        app.height-app.height//8*2,
                        text=f"Kills:",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    try:
        avgsco = sum(app.scores)/len(app.scores)
    except:
        avgsco = "N/A"
    canvas.create_text(app.width-app.width//6,
                        app.height-app.height//8*1.4,
                        text=f"{avgsco}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//6*2,
                        app.height-app.height//8*1.4,
                        text=f"Average Score:",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    try:
        score1 = app.scores[len(app.scores)-1]
    except:
        score1 = "N/A"
    canvas.create_text(app.width-app.width//6, 
                        app.height//2-app.height//8*2.6,
                        text=f"{score1}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//6*2, 
                        app.height//2-app.height//8*2.6,
                        text=f"1st:",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")  
    try:
        score2 = app.scores[len(app.scores)-2]
    except:
        score2 = "N/A"                
    canvas.create_text(app.width-app.width//6,
                        app.height//2-app.height//8*2,
                        text=f"{score2}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//6*2,
                        app.height//2-app.height//8*2,
                        text=f"2nd:",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    try:
        score3 = app.scores[len(app.scores)-3]
    except:
        score3 = "N/A"
    canvas.create_text(app.width-app.width//6,
                        app.height//2-app.height//8*1.4,
                        text=f"{score3}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//6*2,
                        app.height//2-app.height//8*1.4,
                        text=f"3rd:",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")

def drawMainMenu(app,canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="SeaGreen3")
    i = 0
    j = 0
    for button in app.mainButDims:
        k = i%2
        l = j%4
        canvas.create_rectangle(button[0], button[1], button[2], button[3],
                                fill=f"{app.mainButCol[k]}")
        if i > 7:
            yc = (button[1]+button[3])//15+button[1]
            canvas.create_text((button[0]+button[2])//2+3, 
                               yc+3, 
                                text=f"{app.mainTextRight[l]}", 
                                font=f"Times 36 bold", 
                                fill=f"{app.mainTextCol[k-1]}")
            canvas.create_text((button[0]+button[2])//2, 
                               yc, 
                                text=f"{app.mainTextRight[l]}", 
                                font=f"Times 36 bold", 
                                fill=f"{app.mainTextCol[k]}")                    
            i += 1
            if i%2 == 0:
                j += 1
            continue
        canvas.create_text((button[0]+button[2])//2+5, 
                            (button[1]+button[3])//2+5, 
                            text=f"{app.mainText[l]}", 
                            font=f"Times 72 bold", 
                            fill=f"{app.mainTextCol[k-1]}")
        canvas.create_text((button[0]+button[2])//2, 
                            (button[1]+button[3])//2, 
                            text=f"{app.mainText[l]}", 
                            font=f"Times 72 bold", 
                            fill=f"{app.mainTextCol[k]}")
        i += 1
        if i%2 == 0:
            j += 1
    drawMainSBStat(app,canvas)