# Click in shapes and use keys to control the turtle
def setup():
    global shapes, colour
    global clickable, clicked, canClick
    global turThere, turtle
    #                                              range
    squX = 200
    squY = 200
    squS = 200
    rectX = 600
    rectY = 200
    rectW = 300
    rectH = 200
    cirX = 1100
    cirY = 200
    cirR = 200
    #                                              shape setting
    shapes = [[squX, squY, squS, squS, False], [rectX, rectY, rectW, rectH, False], [cirX, cirY, cirR, cirR, True]]
    colour = [[255, 255, 0], [0, 255, 255], [255, 0, 255], [0,0,0]]
    rectMode(CORNER)
    ellipseMode(CORNER)
    size(1500, 600)
    #                                              mouse setting
    clicked = False
    canClick = True
    clickable = [ [[squX, squY], [squX+squS, squY+squS], False] , [[rectX, rectY], [rectX+rectW, rectY+rectH], False] , [[cirX+cirR/2-sqrt((cirR/2)**2/2), cirY+cirR/2-sqrt((cirR/2)**2/2)], [cirX+cirR/2+sqrt((cirR/2)**2/2), cirY+cirR/2+sqrt((cirR/2)**2/2)], True] ]
    #                                              turtle setting
    turThere = False
    #                                              text setting
    textAlign(CENTER)
    textSize(20)
    #                                              load image
    turtle = loadImage("turtle.png")
    
def draw():
    global colour, shapes, turx, tury
    global clickable, clicked, canClick
    global turThere, turtle, valRangeNum, valRange
    #                                              background
    background(51)
    if len(shapes) == 0:
        fill(255)
        text("thanks for playing", 750,300)
    elif not(turThere):
        fill(255)
        text("click the shape", 750,500)
    for i in range(len(shapes)):
        if shapes[i][4]:
            fill(colour[i][0], colour[i][1], colour[i][2])
            ellipse(shapes[i][0], shapes[i][1], shapes[i][2], shapes[i][3])
        else:
            fill(colour[i][0], colour[i][1], colour[i][2])
            rect(shapes[i][0], shapes[i][1], shapes[i][2], shapes[i][3])
        
    if clicked:
        #                                          change clickable    
        valRange = clickable[valRangeNum]  
        clicked = False
        canClick = False
        #                                          pop put
        clickable.pop(valRangeNum)
        #                                          turtle settiing
        turThere = True
        turx = mouseX - 25/2
        tury = mouseY - 25/2
        if turx < valRange[0][0]:
            turx = valRange[0][0]
        elif turx+25 > valRange[1][0]:
            turx = valRange[1][0] - 25
        if tury < valRange[0][1]:
            tury = valRange[0][1]
        elif tury+25 > valRange[1][1]:
            tury = valRange[1][1] - 25
    if keyPressed and turThere:
        #                                          Enter key pressed
        if key == ENTER:
            turThere = False
            shapes.pop(valRangeNum)
            colour.pop(valRangeNum)
            pop = False
            canClick = True
        elif keyCode == UP or keyCode == DOWN or keyCode == LEFT or keyCode == RIGHT:
        #                                          Circle
            if valRange[2]:
                cirx = (valRange[0][0]+valRange[1][0]) / 2
                ciry = (valRange[0][1]+valRange[1][1]) / 2
                cirr = sqrt((valRange[0][0]-valRange[1][0])**2+(valRange[0][1]-valRange[1][1])**2)/2 - 25/2
                if keyCode == UP and sqrt((cirx-turx-12.5)**2+(ciry-tury-12.5+5)**2)<=cirr:
                    tury -= 5
                if keyCode == DOWN and sqrt((cirx-turx-12.5)**2+(ciry-tury-12.5-5)**2)<=cirr:
                    tury += 5
                if keyCode == LEFT and sqrt((cirx-turx-12.5+5)**2+(ciry-tury-12.5)**2)<=cirr:
                    turx -= 5
                if keyCode == RIGHT and sqrt((cirx-turx-12.5-5)**2+(ciry-tury-12.5)**2)<=cirr:
                    turx += 5
        #                                          Square and Rectangle
            else:    
                if keyCode == UP and tury-5 >= valRange[0][1]:
                    tury -= 5
                if keyCode == DOWN and tury+5 <= valRange[1][1]-25:
                    tury += 5
                if keyCode == LEFT and turx-5 >= valRange[0][0]:
                    turx -= 5
                if keyCode == RIGHT and turx+5 <= valRange[1][0]-25:
                    turx += 5
        else:
            fill(255, 255, 255)
            text ("use arrow key to move the turtle\nuse ENTER key to delete the shape", 750, 500)
#                                              draw turtle
    if turThere:
        image(turtle, turx, tury, 25, 25)
        
def mouseReleased():
    global clickable, clicked, valRangeNum, canClick
    if canClick:
        for i in range(len(clickable)):
            if (clickable[i][0][0]<mouseX<clickable[i][1][0] and clickable[i][0][1]<mouseY<clickable[i][1][1]):
                clicked = True
                valRangeNum = i




















            
