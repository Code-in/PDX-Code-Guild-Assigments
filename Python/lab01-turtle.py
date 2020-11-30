from turtle import *

# Drawing a stick figure person for a assigment

#head
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)

# Neck
setposition(-5,-15)
forward(-35)

#arm
left(225)
forward(100)
left(135)
forward(15)
left(45)
forward(90)

#left waist
left(-135)
forward(90)


#Left Leg
left(-45)
forward(100)
left(135)
forward(15)
left(45)
forward(90)
left(-45)
forward(30)

#right leg
left(-45)
forward(90)
left(45)
forward(15)
left(135)
forward(100)

#right waist
left(-45)
forward(90)


#right arm
left(-135)
forward(90)
left(45)
forward(15)
left(135)
forward(100)
left(45)
forward(30)


done()