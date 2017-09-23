'''Card Match Game 
Sept. 22, 2017'''

from random import shuffle

target = (None,None)
tiger = loadImage("/home/tcssm4/Desktop/tiger.jpg");
zebra = loadImage("/home/tcssm4/Desktop/zebra.jpg");
lion = loadImage("/home/tcssm4/Desktop/lion.jpg");

imageList = [tiger, zebra, lion]
pickList = [1,1,2,2,3,3].shuffle()

class Card:
    def __init__(self,x,y,pic):
        self.x = x
        self.y = y
        self.state = 0
        self.clicked = False
        self.cardpic = loadImage("/home/tcssm4/Desktop/card2.jpg");
        self.animalpic = pic
        
    def checkClicked(self):
        global target
        if self.x < target[0] < self.x+100 and self.y < target[1] < self.y+150:
            self.clicked = True
            target = (None,None)
            
    def update(self):
        if self.clicked:
            println("Clicked")
            self.state = (self.state + 1)% 2
            self.clicked = False

        if self.state == 0:
            image(self.cardpic,self.x, self.y)
            
        elif self.state == 1:
            image(self.clockpic,self.x,self.y)
    
cardList = []

def setup():
    global cardList
    size(600,600)
    for x in range(0,600,100):
        for y in range(0,600,150):
            cardList.append(Card(x,y))
  

def draw():
    global cardList
    background(255);
    for card in cardList:
        card.checkClicked()
        card.update()
    
def mouseClicked():
    global target
    target = (mouseX,mouseY)    