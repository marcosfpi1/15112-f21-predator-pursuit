def getMainButDims(app):
    margin, reMargin, reLen, offset = \
        app.width//25, app.width//35, \
            (app.height-app.width//25*2-app.width//35*3)//5, 7
    x0TitleRe, y0TitleRe, x1TitleRe, y1TitleRe = \
        margin, margin, app.width//2-margin, margin+reLen
    x0TitleBaRe, y0TitleBaRe, x1TitleBaRe, y1TitleBaRe = \
        x0TitleRe+offset, y0TitleRe+offset, x1TitleRe+offset, y1TitleRe+offset
    x0But1Re, y0But1Re, x1But1Re, y1But1Re = \
        x0TitleRe, y1TitleRe+reMargin, x1TitleRe, y1TitleRe+reMargin+reLen
    x0But1BaRe, y0But1BaRe, x1But1BaRe, y1But1BaRe = \
        x0But1Re+offset, y0But1Re+offset, x1But1Re+offset, y1But1Re+offset
    x0But2Re, y0But2Re, x1But2Re, y1But2Re = \
        x0TitleRe, y1But1Re+reMargin, x1TitleRe, y1But1Re+reMargin+reLen
    x0But2BaRe, y0But2BaRe, x1But2BaRe, y1But2BaRe = \
        x0But2Re+offset, y0But2Re+offset, x1But2Re+offset, y1But2Re+offset
    x0But3Re, y0But3Re, x1But3Re, y1But3Re = \
        x0TitleRe, y1But2Re+reMargin, x1TitleRe, y1But2Re+reMargin+reLen
    x0But3BaRe, y0But3BaRe, x1But3BaRe, y1But3BaRe = \
        x0But3Re+offset, y0But3Re+offset, x1But3Re+offset, y1But3Re+offset
    x0SBRe, y0SBRe, x1SBRe, y1SBRe = \
        app.width//2+margin, y0TitleRe, app.width-margin, y1But1Re
    x0SBBaRe, y0SBBaRe, x1SBBaRe, y1SBBaRe = \
        x0SBRe-offset, y0SBRe-offset, x1SBRe-offset, y1SBRe-offset
    x0USRe, y0USRe, x1USRe, y1USRe = \
        x0SBRe, y0But2Re, x1SBRe, y1But3Re
    x0USBaRe, y0USBaRe, x1USBaRe, y1USBaRe = \
        x0USRe-offset, y0USRe-offset, x1USRe-offset, y1USRe-offset
    return [[x0TitleBaRe, y0TitleBaRe, x1TitleBaRe, y1TitleBaRe],\
        [x0TitleRe, y0TitleRe, x1TitleRe, y1TitleRe],\
        [x0But1BaRe, y0But1BaRe, x1But1BaRe, y1But1BaRe],\
        [x0But1Re, y0But1Re, x1But1Re, y1But1Re],\
        [x0But2BaRe, y0But2BaRe, x1But2BaRe, y1But2BaRe],\
        [x0But2Re, y0But2Re, x1But2Re, y1But2Re],\
        [x0But3BaRe, y0But3BaRe, x1But3BaRe, y1But3BaRe],\
        [x0But3Re, y0But3Re, x1But3Re, y1But3Re],\
        [x0SBRe, y0SBRe, x1SBRe, y1SBRe],\
        [x0SBBaRe, y0SBBaRe, x1SBBaRe, y1SBBaRe],\
        [x0USRe, y0USRe, x1USRe, y1USRe],\
        [x0USBaRe, y0USBaRe, x1USBaRe, y1USBaRe]]

def getGameButDims(app):
    x0EscBut, y0EscBut, x1EscBut, y1EscBut = \
        app.width//2-app.width//10, 0, app.width//2, app.height//15
    x0ReBut, y0ReBut, x1ReBut, y1ReBut = \
        app.width//2, 0, app.width//2+app.width//10, app.height//15
    x0ScoBut, y0ScoBut, x1ScoBut, y1ScoBut = \
        app.width//2-app.width//10, app.height//15, \
            app.width//2, (app.height//15)*2
    x0LivBut, y0LivBut, x1LivBut, y1LivBut = \
        app.width//2, app.height//15, \
            app.width//2+app.width//10, (app.height//15)*2
    x0PowBut, y0PowBut, x1PowBut, y1PowBut = \
        app.width//2-(app.width//10)//2, (app.height//15)*2, \
            app.width//2+(app.width//10)//2, (app.height//15)*3
    return [[x0EscBut, y0EscBut, x1EscBut, y1EscBut],\
            [x0ReBut, y0ReBut, x1ReBut, y1ReBut],\
            [x0ScoBut, y0ScoBut, x1ScoBut, y1ScoBut],\
            [x0LivBut, y0LivBut, x1LivBut, y1LivBut],\
            [x0PowBut, y0PowBut, x1PowBut, y1PowBut]]

def getPlyrCarDim(app):
    x0 = app.width//2-app.width//15
    y0 = app.height-app.height//5
    x1 = app.width//2+app.width//15
    y1 = app.height
    return [x0, y0, x1, y1]

def getCrossHairDims(app):
    margin, length = 5, 20
    x0T, y0T, x1T, y1T = app.width//2, app.height//2-margin-length, \
                         app.width//2, app.height//2-margin
    x0R, y0R, x1R, y1R = app.width//2+margin, app.height//2, \
                         app.width//2+margin+length, app.height//2
    x0B, y0B, x1B, y1B = app.width//2, app.height//2+margin, \
                         app.width//2, app.height//2+margin+length
    x0L, y0L, x1L, y1L = app.width//2-margin, app.height//2, \
                         app.width//2-margin-length, app.height//2
    return [[x0T, y0T, x1T, y1T], [x0R, y0R, x1R, y1R], [x0B, y0B, x1B, y1B],\
                                                        [x0L, y0L, x1L, y1L]]

def getRoadMarksDims(app):
    fulldist, margin = (app.height-app.newRoadMarkY0), 15
    smalllen = (fulldist-margin*4)//8
    incLenFac = 0.05
    x0, x1 = app.width//2-5, app.width//2+5
    y01, y11 = app.newRoadMarkY0, app.newRoadMarkY0+margin
    y02, y12 = y11+margin, y11+margin+smalllen+smalllen*(incLenFac*1)
    y03, y13 = y12+margin, y12+margin+smalllen+smalllen*(incLenFac*2)
    y04, y14 = y13+margin, y13+margin+smalllen+smalllen*(incLenFac*3)
    y05, y15 = y14+margin, y14+margin+smalllen+smalllen*(incLenFac*4)
    return [[x0, y01, x1, y11], [x0, y02, x1, y12], [x0, y03, x1, y13],\
            [x0, y04, x1, y14], [x0, y05, x1, y15]]
    
def getSetButDims(app):
    margin, offset = app.width//25, 7
    x0MMRe, y0MMRe, x1MMRe, y1MMRe = \
        margin, margin, app.width//2-margin, app.height//2-margin    
    x0MMBaRe, y0MMBaRe, x1MMBaRe, y1MMBaRe = \
        x0MMRe-offset, y0MMRe-offset, x1MMRe-offset, y1MMRe-offset
    x0WeRe, y0WeRe, x1WeRe, y1WeRe = \
        x0MMRe, app.height//2, x1MMRe, app.height-margin*3
    x0WeBaRe, y0WeBaRe, x1WeBaRe, y1WeBaRe = \
        x0WeRe-offset, y0WeRe-offset, x1WeRe-offset, y1WeRe-offset
    x0LivRe, y0LivRe, x1LivRe, y1LivRe = \
        app.width//2+margin, y0MMRe, app.width-margin, y1MMRe
    x0LivBaRe, y0LivBaRe, x1LivBaRe, y1LivBaRe = \
        x0LivRe-offset, y0LivRe-offset, x1LivRe-offset, y1LivRe-offset
    x0DifRe, y0DifRe, x1DifRe, y1DifRe = \
        x0LivRe, y0WeRe, x1LivRe, y1WeRe
    x0DifBaRe, y0DifBaRe, x1DifBaRe, y1DifBaRe = \
        x0DifRe-offset, y0DifRe-offset, x1DifRe-offset, y1DifRe-offset
    return [[x0MMRe, y0MMRe, x1MMRe, y1MMRe],\
            [x0MMBaRe, y0MMBaRe, x1MMBaRe, y1MMBaRe],\
            [x0WeRe, y0WeRe, x1WeRe, y1WeRe],\
            [x0WeBaRe, y0WeBaRe, x1WeBaRe, y1WeBaRe],\
            [x0LivRe, y0LivRe, x1LivRe, y1LivRe],\
            [x0LivBaRe, y0LivBaRe, x1LivBaRe, y1LivBaRe],\
            [x0DifRe, y0DifRe, x1DifRe, y1DifRe],\
            [x0DifBaRe, y0DifBaRe, x1DifBaRe, y1DifBaRe]]