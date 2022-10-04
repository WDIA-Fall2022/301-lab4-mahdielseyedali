from sense_hat import SenseHat
import time


def getUserChoice():
    choice = -1
    print('What do you want to display? ')
    print('1. Logo')
    print('2. Plus sign')
    print('3. Equals sign')
    print('4. Raspberry')
    print('5. Heart')
    print('6. Elephant')
    print('0. Exit')

    while choice < 0:
      choice = input("Enter a number")
      choice = int(choice)
      try:
            print(choice)
            choice_type = type(choice)
            if choice_type == str:
                print("input is a string not a number")

            if choice == 0:
                exit()

      except ValueError:
            print("Invalid Input, please enter a number from the menu")

    return choice

s = SenseHat()
s.low_light = True

gray = (220, 220, 220)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo( G = green, Y = yellow, B = blue, O = nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo(  G = green, R = red, O = nothing):

    logo = [
    O, G, G, O, O, G, G, O,
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus(   W = white, O = nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals( W = white, O = nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart(  P = pink, O = nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def elephant(o = nothing, c2 = white, c1 = gray):

    elephant = [
    o, o, c1, c1, o, o, o, o,
    o, c1, c1, c1, c1, c1, c1, o,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, c1, c1, c1, c1, c1, c1, c1,
    c1, c2, c2, c1, c1, c1, c1, c1,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, o, c1, c1, o, c1, c1, o,
    c1, o, c2, c1, o, c2, c1, o,
    ]
    return elephant

images = [exit, trinket_logo, plus, equals, raspi_logo, heart, elephant]

while True:
  s.set_pixels(images[getUserChoice()]())

