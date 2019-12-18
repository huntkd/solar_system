import math
import turtle
from turtle import *


class Planet:

## Sets the number of Earth days you want the simulation to run for
  global number_of_earth_days
  number_of_earth_days = 1000

##  Planet Class takes in the parameters needed to calculate the orbit

  def __init__(self, name, eccentricity, a, b, orbital_period, diameter, color):
    self.eccentricity = eccentricity
    self.name = name
    self.a = a
    self.b = b
    self.orbital_period = orbital_period
    self.diameter = diameter
    self.color = color
    self.turtle = turtle.Turtle()

    ## Creates a list of the orbit coordinates of each planet
    self.x = self.make_orbit_x()
    self.y = self.make_orbit_y()

## Makes the x coordinates of the orbit

  def make_orbit_x(self):
    theta_step = (2 * math.pi) / (365 * self.orbital_period)
    t = 0
    d = 0
    c = math.sqrt(self.a ** (2) - self.b ** (2))
    x_coordinates = []
    for d in range (number_of_earth_days):
      r = (self.a * (1 - self.eccentricity ** (2)))/(1 + self.eccentricity*math.cos(t))
      x_coor = c + r*math.cos(t) * 190
      y_coor = r*math.sin(t) * 190
      x_coordinates.append(x_coor)
      t += theta_step
      d += 1
    print(x_coordinates)
    return x_coordinates

## Makes the y coordinates of the orbit

  def make_orbit_y(self):
    theta_step = (2 * math.pi) / (365 * self.orbital_period)
    t = 0
    d = 0
    c = math.sqrt(self.a ** (2) - self.b ** (2))
    y_coordinates = []
    for d in range (number_of_earth_days):
      r = (self.a * (1 - self.eccentricity ** (2)))/(1 + self.eccentricity*math.cos(t))
      x_coor = c + r*math.cos(t) * 190
      y_coor = r*math.sin(t) * 190
      y_coordinates.append(y_coor)
      t += theta_step
      d += 1
    print(y_coordinates)
    return y_coordinates


#########################################################################################


class SolarSystem:

## Creates the solar system

  def __init__(self, name, image):
    self.name = name
    self.image = image

## Draws the orbits

  def animation(self, planet_list):

    furthest = len(planet_list) - 1

    for planet in planet_list:
      ## Create the planets
      p_turtle = planet.turtle
      p_turtle.shape("circle")
      width = planet.diameter
      p_turtle.shapesize(width, width, width)
      p_turtle.fillcolor(planet.color)
      p_turtle.penup() ## needs to start up so there is no line drawn while they move into the initial position
      p_turtle.pencolor("white")

      ## Moves planet to initial positions
      p_turtle.goto(planet.x[0], planet.y[0])
      p_turtle.pendown()

    ## Draws orbits, needs two loops so it doesn't draw the orbits one at a time
    i = 0
    for i in range(number_of_earth_days):
      for planet in planet_list:
        planet.turtle.goto(planet.x[i], planet.y[i])
    i = i + 1


#########################################################################################


## Creates the Solar System
Solar_System = SolarSystem("Solar1", "stars.gif")


## Creates the window w/ star back ground
wn = turtle.Screen()
wn.title("Solar System")
wn.bgpic(Solar_System.image)


## Creates the Sun (stationary, doesn't move like a planet)
p0 = turtle.Turtle()
p0.shapesize(2.5, 2.5, 2.5)
p0.fillcolor("yellow")
p0.shape("circle")


## Creates the planets and set the parameters

Mercury = Planet("mercury", 0.18, 0.47, 0.31, 0.2410, .20, "brown")
Venus = Planet("venus", 0.05, 0.728, 0.718, 0.61643, .20, "orange")
Earth = Planet("mars", 0.017, 1.02, .98, 1, .20, "blue")
Mars = Planet("earth", 0.093, 1.67, 1.38, 1.88219, .20, "red")

planet_list = [Mercury, Venus, Earth, Mars]

Solar_System.animation(planet_list)

turtle.done()



