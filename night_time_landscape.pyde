#while loop
#increase variable
#use draw() for animation
import time

cloud = 0

def setup():
    size(1000, 480)
    
def draw():
    global cloud
    if cloud >= 1500:
        cloud = 0
    cloud += 1
    #to make background colour
    background(40,40,40)
    noStroke()    
    fill(170,170,170)
    ellipse(cloud,height/2,50,50)
    #create a cluster of circles
    #to simulate a moving cloud
    #cloudnumber1
    ellipse(cloud+25,height/2,50,50)
    ellipse(cloud+50,height/2,50,50)
    ellipse(cloud+25,height/2.25,50,50)
    
    #moon
    fill(142,142,142)
    ellipse(950,height/9,150,150)
    
    #cloud2
    fill(170,170,170)
    ellipse(cloud-60,height/3,50,50)
    ellipse(cloud-85,height/3.25,60,60)
    ellipse(cloud-110,height/3,50,50)
    ellipse(cloud-85,height/3,50,50)
    
    #cloud3
    fill(170,170,170)
    ellipse(cloud-450,height/3,50,50)
    ellipse(cloud-475,height/3,50,50)
    ellipse(cloud-500,height/3,50,50)
    ellipse(cloud-475,height/3.25,50,50)
    
    #cloud4
    fill(170,170,170)
    ellipse(cloud-350,height/2,50,50)
    ellipse(cloud-375,height/2,50,50)
    ellipse(cloud-400,height/2,50,50)
    ellipse(cloud-375,height/2.3,60,60)
    
    #cloud5
    fill(170,170,170)
    ellipse(cloud-250,height/3,50,50)
    ellipse(cloud-275,height/3,50,50)
    ellipse(cloud-300,height/3,50,50)
    ellipse(cloud-275,height/3.25,50,50)
    
     #stars
    fill(0, 50);
    rect(0, 0, width, height);
    fill(255);
    ellipse(random(width), random(height), 5, 5);
    
    #1st tree
    fill(138,54,15)
    rect(100, 300, 50, 200)
    fill(0,100,0)
    ellipse(100,300,100,100)
    ellipse(150,300,100,100)
    ellipse(125,250,100,100)
    
    #2nd tree
    fill(138,54,15)
    rect(250, 350, 50, 200)
    fill(0,100,0)
    ellipse(250,350,100,100)
    ellipse(300,350,100,100)
    ellipse(275,300,100,100)
    
    #3rd tree
    fill(138,54,15)
    rect(850,300,50,200)
    fill(0,100,0)
    ellipse(850,300,100,100)
    ellipse(900,300,100,100)
    ellipse(875,250,100,100)
    
    #house
    fill(138,54,15)
    triangle(450,350,525,250,600,350)
    fill(178,34,34)
    rect(450,350,150,150)
    
    #door
    fill(0)
    rect(525,410,50,75)
    fill(205,155,29)  
    ellipse(535,450,10,10)
    
