def setup():
    global rectw, recth, rectX, rectY, squaw, squah, squaX, squaY, circd, circX, circY
    global picture
    global clicked, canClick, boundary
    global turThere, turtle
    
    clicked = False
    canClick = True
    boundary = [ [rectX+rectw, rextY+recth, False], [squaX+squaw, squaY+squah, False], [[circX+circd/2+sqrt((circr/2)**2/2), circY+circd/2+sqrt((circr/2)**2/2 ]

    turThere = True
    turtle = False
    
    shapes = [ [rectX, rectY, rectw, recth, False], [squaX, squaY, squaw, squah, False], [circX, circY, circd, circd, False]]
    rectw= 150
    recth= 300
    rectX= 100
    rectY= 100
    
    squaw= 200
    squah= 200
    squaX= 300   
    squaY= 100
    
    circd= 200
    circX= 650
    circY= 200

    
    picture=loadImage("turtle.png")
    size(800, 550)
    
def draw():
    global rectw, recth, rectX, rectY, squaw, squah, squaX, squaY, circd, circX, circY
    global picture
    global clicked, canClick, boundary
    global turThere, turtle
    # fill(252, 8, 8)
    # rect ( rectX, rectY, rectw, recth)
    
    # fill (8, 144, 252)
    # rect ( squaX, squaY, squaw, squah)
    
    # fill (200)
    # ellipse(circX, circY, circd, circd)
    
    background(60)
    
    if len(shapes) == 0:
        fill(255)
        text("Thanks for playing", 750, 300)
        
    elif not(turThere):
        fill(255)
        text("Click in the shapes", 750, 500)
        
        
        