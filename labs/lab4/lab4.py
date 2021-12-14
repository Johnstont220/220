"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of squares user can make
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to make a square")
    instructions.draw(win)

    # builds a square

    shape = Rectangle(Point(20, 20), Point(40,40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to make squares
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        nshape = shape.clone()
        nshape.move(dx, dy)
        nshape.draw(win)
    instructions.setText("Click again to close")
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """


    pass

def circle():
    win = GraphWin("Circles", 400, 400)


    center = Point(100, 200)         # create a point to serve as the center of the circle
    radius = 40
    circle = Circle(center, radius)  # create a circle centered at "center" with radius "radius"
    circle.setOutline('blue')
    circle.draw(win)              # draw the circle in the window that we created earlier

    win.getMouse()                # wait for the mouse to be clicked in the window
    win.close()                   # close the window after the mouse is clicked in the window



def pi2():
    n = int(input("Enter a value for N: "))
    total=0
    for i in range(1,n):
        total += (-1)**(i+1)*((1.0/(i+i+1)))

    value = 4*(1-total)
    print(value)

def main():
    #squares()
    # rectangle()
    circle()
    #pi2()


main()
