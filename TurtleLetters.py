import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":#Goutham's 5
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":#Carter's 5
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":#Gabe's5
        tur.pu()
        tur.back(5)
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()  
    elif letter == "M":
        tur.pu()
        tur.back(5)
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.setheading(-45)
        tur.pd()
        tur.fd(30)
        tur.setheading(45)
        tur.fd(30)
        tur.setheading(-90)
        tur.fd(30)
        tur.back(30)
        tur.left(90)
        tur.fd(5)
        tur.pu() 
    elif letter == "N":
        tur.pu()
        tur.back(5)
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.setheading(-60)
        tur.pd()
        tur.fd(35)
        tur.setheading(45)
        tur.setheading(90)
        tur.fd(30)
        tur.right(90)
        tur.pu()
    elif letter == "O":
        tur.pu()
        tur.back(5)
        tur.pd()
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(35)
        tur.pu()  
    elif letter == "P":
        tur.pu()
        tur.back(5)
        tur.pd()
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.setheading(270)
        tur.fd(60)
        tur.setheading(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
        tur.pu()		
    elif letter == "Q":#Nick's 5
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":#Chase does last 5
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
