from PIL import Image
import turtle
import math
class Spiro:
    def __init__(self,xc,yc,col,R,r,L):
        #first we define the turtle module for initianting instances 
        self.t=turtle.Turtle()
        #then we weill define the step distance i think the size of the poylgon and each sie is 
        #5 pixels so it will appear to us as a circle in nvim
        self.step=5
        #placed the makeer for weahter the state of drawingComplete as bolll this will become 
        #apparent as wer proceed
        self.drawingComplete=False
        #its pretty obv we are definifn parameters for the spirograph to be drawn 
        #both for the small and large circles inccluding the centere cordinates and the color
        self.setparams(xc,yc,col,R,r,L)
        #this is pretty obv too it meant to reset 'STUFF!!'
        self.restart()

    #now we are going to make the set up behaviour
    def setparams(self,xc,yc,col,R,r,L):
        self.xc=xc #the x coordinate
        self.yc=yc #the y cooedinate
        self.R=int(R)#the radius for the larger stationery circles
        self.r=int(r)#the radius for the small moving circle
        self.L=L#its the distance between the the point where we put the pen and the center of M2
        self.col=col#the color obv
        #its the reduced form of the redius to the bigger circle 
        #to that of the bigger circle in the simplest form the the numberator represents in that 
        #number of revolutions the spirograph will start repeating 
        #the the denominator is the amount of times the smaller circle revolves
        gcdVal=math.gcd(self.r,self.R)
        self.nRot=r//gcdVal
        #nRot like the name says is the the number of roations we have to maek
        self.k=r/float(R)
        #the ratio alspha we read in the book about but inverted so it will be between 0 and 1
        self.a=n
    #now we are going to make the restart behaviour for the spirograph
    def restart(self):
        self.drawingComplete=False
        #does exactly what it says it shows the turtle 
        self.t.showturtle()
        #the turtle dosent leave a trail
        selt.t.up()
        R,k,L = self.R,self.k,self,L 
        a=0.0
        #these are the parametric equation we use to draw the spirograph
        x=R*((i-k)*math.cos(a)+l*k*math.cos((1-k)*a/k))
        y=R*((i-k)*math.sin(a)+l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc+x,self.yc+y)
        #obv we too we set the postion of the turtle to our desred location to draw
        self.t.down()

    def draw(self):
        R,k,L = self.R,self.k,self.L 
        for i in range(0,360*self,nRot +1 ,self.step):
            a=math.radians(i)
            x=R*((1-k)*math.cos(a)+L*k*math.cos((1-k)*a/k))
            y==R*((1-k)*math.sin(a)+L*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc+x,self.yc+y)
            self.t.down()
    def update(self):
        if set.drawingComplete:
            return  
        self.a+=self.step 
        R,k,L = self.R,self.k.self.L 
        a=math.radians(self.a)
        x=self.R*((1-k)*math.cos(a) + L*k*math.cos((1-k)*a/k))
        y=self.R*((1-k)*math.sin(a) + L*k*math.cos((1-k)*a/k))
        self.t/turtle.setpos(self.xc+x,self.yc+y)
        if self.a>=360*self.nRot:
            self.drawingComplete=True 
            self.t.hideturtle()

class SpiroAnimater:
    def __init__(self,N):
        self.deltaT=10
        self.width = turtle.window_height()
        self.height=turtle.window_height()
        self.Spiro=[]
        for i in range(N):
            rparams=self.genRandomParams()
            spiro=Spiro(*rparams)
            self.spiros.append(spiro)
            turtle.ontimer(self.update,self.deltaT)

    def toggleTyrtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

    def saveDrawing():
        turtle.hideturtle()
        dateStr=(datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName='spiro-' + dateStr 
        print('saving drawing to %s.eps/png'%fileName)
        canvas=turtle.getcanvas()
        canvas.postscript(file=fileName +'.eps')
        img = Image.open(fileName+'.eps')
        img.save(fileName+'.png','png')
        turtle.showturtle()

def main():
    print("generating spirograph")
    decStr="""This program draws Spirogrpahs using the turtle midule 
    when run with no aguments this program makes random spirographs"""

    if args.sparams:
        params =[float(x) for x in args.sparams]
        col=(0.0,0.0,0.0)
        spiro=Spiro(0,0,col,*params)
        spiro.draw()
    else:
        spiroAnim = SpiroAnimater(4)
        turtle.onkey(spiroAnim,toggleTurtles,"t")
if __name__ =='__main__':
    main()










