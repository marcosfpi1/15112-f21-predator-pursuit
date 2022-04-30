def drawHTP(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="turquoise2")
    i = 0
    j = 0
    for button in app.settingsButtonDims:
        k = i%2
        l = j%4
        canvas.create_rectangle(button[0], button[1], button[2], button[3],
                                fill=f"{app.mainButCol[k]}")    
        if i == 1:
            canvas.create_text((button[0]+button[2])//2, 
                                (button[1]+button[3])//2,
                                text=f"Main Menu",
                                font=f"Times 72 bold",
                                fill=f"{app.mainTextCol[0]}")   
        if i == 3:
            canvas.create_text((button[0]+button[2])//2, 
                                (button[1]+button[3])//2,
                                text=f"To navigate through the windows,\nyou" +
                                 " can use the Escape key to always\nreturn" +
                                 " to the Main Menu. To restart\nthe round" +
                                 " without going back to the\nmain menu, you" +
                                 " can use the r key.",
                                font=f"Times 24 bold",
                                fill=f"{app.mainTextCol[0]}")  
        if i == 5:
            canvas.create_text((button[0]+button[2])//2,
                                (button[1]+button[3])//2,
                                text=f"To lose in this game, your car\nhas" +
                                " to either get hit by a laser\nmultiple" +
                                " times, or to run into opposing\ntraffic" +
                                " cars. To move your car to not\nget hit," +
                                " you can use the left and\nright arrow" +
                                " keys.",
                                font=f"Times 24 bold",
                                fill=f"{app.mainTextCol[0]}")
        if i == 7:
            canvas.create_text((button[0]+button[2])//2,
                                (button[1]+button[3])//2,
                                text=f"To score points you have to\nshoot" +
                                " aliens. To do so you will shoot\nlasers" +
                                " with the spacebar key, and it\nwill" + 
                                " make a laser go from your car\nto" +
                                " your crosshair. The crosshair can\n" +
                                "be moved with the awsd keys, a\nfor" +
                                " left, d for right, w for up, and\ns for" +
                                " down."
                                ,
                                font=f"Times 24 bold",
                                fill=f"{app.mainTextCol[0]}")
        i += 1
        if i%2 == 0:
            j += 1