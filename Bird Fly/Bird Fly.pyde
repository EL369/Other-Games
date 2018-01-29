def setup():
    global cornerpointx, cornerpointy, canvasw, canvash, back
    global t2, t3, mode, bird, bird2, showbird, birdx, birdy, birdw, birdh, incrbirdx,incrbirdy
    global lboundbird,rboundbird,uboundbird,bboundbird, mboundbird
    global snowman, snowmanx, snowmany, snowmanw, snowmanh
    
    snowmanw = 300
    snowmanh = 300
    snowmanx = 200
    snowmany = 400
    birdw = 100
    birdh = 100
    cornerpointx = 0
    cornerpointy = 0
    canvasw = 700
    canvash = 700
    lboundbird = 0
    rboundbird = canvasw - birdw - 1
    uboundbird = 0
    bboundbird = ( canvash - snowmanh - birdh ) - 1
    
    t2 = 50
    t3 = 60
    mode = "load"
    size( 700, 700 )
    
    add_library('minim')
    minim=Minim(this)
    intro=minim.loadFile("Intro.wav")
    sound=minim.loadFile("game.mp3")
    intro.play()
    delay(4300)
    sound.loop()
    snowman = loadImage( "snowman.png" )
    bird = loadImage( "bird.png" )
    bird2 = loadImage( "bird2.png" )
    back = loadImage( "back.png" )
    birdx = 0
    birdy = 0
    incrbirdx = 10
    incrbirdy = 10
   
    showbird = bird
    
def draw():
    global cornerpointx, cornerpointy, canvasw, canvash, back
    global t2, t3, mode, bird, bird2, showbird, birdx, birdy, birdw, birdh, incrbirdx,incrbirdy
    global lboundbird,rboundbird,uboundbird,bboundbird, mboundbird
    global snowman, snowmanx, snowmany, snowmanw, snowmanh    
    
    background = image( back, cornerpointx, cornerpointy, canvasw, canvash )
    image ( snowman, snowmanx, snowmany, snowmanw, snowmanh )
    #if mode == "load":
    #    textSize (t2)
    #    fill (255,255,255)
    #    text ("Press S to start the game",50,200)
        
    image ( showbird,birdx,birdy,birdw,birdh )
    birdx = birdx + incrbirdx
    birdy = birdy + incrbirdy
    if birdx >= rboundbird:
        birdx = rboundbird
        incrbirdx = incrbirdx * -1
        showbird = bird2
    elif birdx < lboundbird:
        birdx = lboundbird
        incrbirdx = incrbirdx * -1
        showbird = bird
    
    if birdy < uboundbird:
        birdy = uboundbird
        incrbirdy = incrbirdy * -1
    elif birdy >= bboundbird:
        birdy = bboundbird
        incrbirdy = incrbirdy * -1