def drawSettings(app,canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="Coral2")
    i = 0
    j = 0
    for button in app.settingsButtonDims:
        k = i%2
        l = j%4
        canvas.create_rectangle(button[0], button[1], button[2], button[3],
                                fill=f"{app.mainButCol[k]}")  
        canvas.create_text((button[0]+button[2])//2+3, 
                            (button[1]+button[3])//6+button[1]+3, 
                            text=f"{app.setText[l]}", 
                            font=f"Times 36 bold", 
                            fill=f"{app.mainTextCol[k-1]}")
        canvas.create_text((button[0]+button[2])//2, 
                            (button[1]+button[3])//6+button[1], 
                            text=f"{app.setText[l]}", 
                            font=f"Times 36 bold", 
                            fill=f"{app.mainTextCol[k]}")                
        i += 1
        if i%2 == 0:
            j += 1
    canvas.create_text(app.width//4, app.height//2+app.width//25*3,
                        text=f"{app.weaponTypes[app.weaponTypeI]}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//4, app.height//2+app.width//25*3,
                        text=f"{app.diff+1}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")
    canvas.create_text(app.width-app.width//4, app.width//25*5,
                        text=f"{app.lives}",
                        font=f"Times 36 bold",
                        fill=f"{app.mainTextCol[0]}")