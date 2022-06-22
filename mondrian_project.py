from p5 import *
import random
def setup():
    size(640, 360)
    no_stroke()
    background(204)

# initially sets gate to open
cantog = True

# randomly choose 2 xcoords and 2 ycoords to draw lines
xcoord1 = random.randrange(50, 590)
xcoord2 = random.randrange(50, 590)

ycoord1 = random.randrange(50, 310)
ycoord2 = random.randrange(50, 310)

# create list of colors
colors = ["red", "yellow", "blue", "white", "white", "white", "white", "white", "white"]

# create list of colors to toggle through when rectangle is clicked
togcolors = ["red", "yellow", "blue", "white"]

# create 9 randomly picked colors from the list above and assign each to a variable
color1 = random.choice(colors)
color2 = random.choice(colors)
color3 = random.choice(colors)
color4 = random.choice(colors)
color5 = random.choice(colors)
color6 = random.choice(colors)
color7 = random.choice(colors)
color8 = random.choice(colors)
color9 = random.choice(colors)

# variable for the number of times each rectangle has been clicked
togcolor = 0

# creates function that prints text
def starttext(text):
    print(text)

# create an empty list that rectangle values will be appended to
rectangles = []

# compare the 2 xcoord and 2 ycoord values, create rectangle values according to this, and append rectangle values to the list above
if xcoord1 < xcoord2 and ycoord1 < ycoord2:
    rectangles.append({"xy" : (0, 0), "w" : xcoord1, "h" : ycoord1, "color" : color1, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10,0), "w" : xcoord2-xcoord1-10, "h" : ycoord1, "color" : color2, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10,0), "w" : 640-xcoord2-10, "h" : ycoord1, "color" : color3, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord1+10), "w" : xcoord1, "h" : ycoord2-ycoord1-10, "color" : color4, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord1+10), "w" : xcoord2-xcoord1-10, "h" : ycoord2-ycoord1-10, "color" : color5, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord1+10), "w" : 640-xcoord2-10, "h" : ycoord2-ycoord1-10, "color" : color6, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord2+10), "w" : xcoord1, "h" : 360-ycoord2-10, "color" : color7, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord2+10), "w" : xcoord2-xcoord1-10, "h" : 360-ycoord2-10, "color" : color8, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord2+10), "w" : 640-xcoord2-10, "h" : 360-ycoord2-10, "color" : color9, "tog" : 0})

elif xcoord1 < xcoord2 and ycoord1 > ycoord2:
    rectangles.append({"xy" : (0, 0), "w" : xcoord1, "h" : ycoord2, "color" : color1, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10,0), "w" : xcoord2-xcoord1-10, "h" : ycoord2, "color" : color2, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10,0), "w" : 640-xcoord2-10, "h" : ycoord2, "color" : color3, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord2+10), "w" : xcoord1, "h" : ycoord1-ycoord2-10, "color" : color4, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord2+10), "w" : xcoord2-xcoord1-10, "h" : ycoord1-ycoord2-10, "color" : color5, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord2+10), "w" : 640-xcoord2-10, "h" : ycoord1-ycoord2-10, "color" : color6, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord1+10), "w" : xcoord1, "h" : 360-ycoord1-10, "color" : color7, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord1+10), "w" : xcoord2-xcoord1-10, "h" : 360-ycoord1-10, "color" : color8, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord1+10), "w" : 640-xcoord2-10, "h" : 360-ycoord1-10, "color" : color9, "tog" : 0})

elif xcoord1 > xcoord2 and ycoord1 < ycoord2:
    rectangles.append({"xy" : (0, 0), "w" : xcoord2, "h" : ycoord1, "color" : color1, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10,0), "w" : xcoord1-xcoord2-10, "h" : ycoord1, "color" : color2, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10,0), "w" : 640-xcoord1-10, "h" : ycoord1, "color" : color3, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord1+10), "w" : xcoord2, "h" : ycoord2-ycoord1-10, "color" : color4, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord1+10), "w" : xcoord1-xcoord2-10, "h" : ycoord2-ycoord1-10, "color" : color5, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord1+10), "w" : 640-xcoord1-10, "h" : ycoord2-ycoord1-10, "color" : color6, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord2+10), "w" : xcoord2, "h" : 360-ycoord2-10, "color" : color7, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord2+10), "w" : xcoord1-xcoord2-10, "h" : 360-ycoord2-10, "color" : color8, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord2+10), "w" : 640-xcoord1-10, "h" : 360-ycoord2-10, "color" : color9, "tog" : 0})

else:
    rectangles.append({"xy" : (0, 0), "w" : xcoord2, "h" : ycoord2, "color" : color1, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10,0), "w" : xcoord1-xcoord2-10, "h" : ycoord2, "color" : color2, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10,0), "w" : 640-xcoord1-10, "h" : ycoord2, "color" : color3, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord2+10), "w" : xcoord2, "h" : ycoord1-ycoord2-10, "color" : color4, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord2+10), "w" : xcoord1-xcoord2-10, "h" : ycoord1-ycoord2-10, "color" : color5, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord2+10), "w" : 640-xcoord1-10, "h" : ycoord1-ycoord2-10, "color" : color6, "tog" : 0})
    rectangles.append({"xy" : (0, ycoord1+10), "w" : xcoord2, "h" : 360-ycoord1-10, "color" : color7, "tog" : 0})
    rectangles.append({"xy" : (xcoord2+10, ycoord1+10), "w" : xcoord1-xcoord2-10, "h" : 360-ycoord1-10, "color" : color8, "tog" : 0})
    rectangles.append({"xy" : (xcoord1+10, ycoord1+10), "w" : 640-xcoord1-10, "h" : 360-ycoord1-10, "color" : color9, "tog" : 0})

# create a function that determines if mouse is in a certain rectangle
def mouse_is_in_rect(mx, my, my_rect):
    # creates variables based on rectangle parameters
    rx = my_rect["xy"][0]
    ry = my_rect["xy"][1]
    rw = my_rect["w"]
    rh = my_rect["h"]

    # sets Boolean values to variables
    is_above = ry > my
    is_right = rx + rw < mx
    is_below = ry + rh < my
    is_left = rx > mx

    # returns True if variables above are False
    if is_above == False and is_right == False and is_below == False and is_left == False:
        return True


def draw():
    # globalizes variables
    global xcoord1
    global xcoord2

    global ycoord1
    global ycoord2

    global togcolor
    global cantog

    # draws 2 vertical, 2 horizontal lines
    fill(0)
    rect((xcoord1, 0), 10, 360)
    rect((xcoord2, 0), 10, 360)
    rect((0, ycoord1), 640, 10)
    rect((0, ycoord2), 640, 10)

    # create the 9 rectangles based on the values in the rectangles list
    for rectangle in rectangles:
        fill(rectangle["color"])
        rect(rectangle["xy"], rectangle["w"], rectangle["h"])

    # if mouse is pressed, will go through each rectangle and determine if the mouse was pressed in that rectangle
    if mouse_is_pressed and cantog == True:
        # closes the gate
        cantog = False
        for rectangle in rectangles:
            if mouse_is_in_rect(mouse_x, mouse_y, rectangle):
                # if the mouse was pressed in a certain rectangle, the color will change to the tog value
                rectangle["color"] = togcolors[rectangle["tog"]]
                # the toggle color becomes the next value in the togcolors list
                if rectangle["tog"] < 3:
                    rectangle["tog"] += 1
                else:
                    rectangle["tog"] = 0
                # the rectangle is filled with whatever togcolor value it is, and the rectangle is drawn again
                fill(rectangle["color"])

    if not mouse_is_pressed:
        # opens the gate when mouse is not pressed
        cantog = True

# informs user that they can click rectangles to toggle their color
starttext("Click rectangle to toggle color")
run()
