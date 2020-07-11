def setup():
    size(600,400)
    frameRate(60)
    global kolory
    rectMode(CENTER)
    kolory = {"1":(255,0,0,80),"2":(0,0,255,80), "3":(0,255,0,80), "4":(205,124,127,80)}
    global a
    a=0
    global d
    d=height/2
def draw():
    global a
    global d
    global t
    background(0)
    global lista
    lista = []
    for klucz, wartosc in kolory.items():
        lista.append(wartosc)
    stroke(255,60,40,80)  
    stroke(*kolory["3"])
    rect(a, d, 100, 100)
    if a==0 and d==height/2:
        t=1
    if a==300 and d==0:
        t=2
    if a==600 and d==200:
        t=3
    if a==300 and d==400:
        t=4
        
    if t==1:
        a+=3
        d-=2
        fill(*kolory["3"])
    if t==2:
        a+=3
        d+=2
        fill(*kolory["4"])
    if t==3:
        a-=3
        d+=2
        fill(*kolory["2"])
    if t==4:
        a-=3
        d-=2
        fill(*kolory["1"])
    
    if mousePressed:
        exit()
