# solar_system
APCSP Final

About:

This simulation calculates the orbits of the inner planets (Mercury, Venus, Earth, Mars) 
using the planetary data from NASA's planetary fact sheet. The program uses Turtle graphics 
to create the planets and trace their orbits. The orbits are calculated using ellipse geometry 
(taking the longest and shortest distance of the orbit and the eccentricity of the orbit to calculate 
a list of the x and y coordinates).

Running the Code:

1. Set the number of earth days you want the simulation to run (the default is 1000)
2. If you want to add a new planet, create a new planet and plug in the parameters of the orbit 
3. Add the new planet to planet_list
3. Run the code from the command line: python solar.py

What I learned:

1. How to code in Python
  
  Python syntax is much different from java and using built in functions (such as
  len(), writing loops (since the formating is completely different), and creating
  global variables were all very different from what I was used to.

2. How to use Turtle graphics
  
  It was hard to set the background image because the image had to be a gif and
  the right size.
  I also struggled with how to get the orbits to draw at the same time, instead
  of one at a time which is how turtle typically does it.

3. Ellipse math is hard
  
  Calculating the orbits made my have to relearn ellipse geometry and I had to do it 
  all in polar coordinates, which involve trig and make it even more complicated.
  Calculating the orbits so they all went the proper distance over the same amount of 
  time was hard because it meant that all the math was relative to theta and I had to
  calculate the distance of each theta section by using the orbital period (amount of 
  time it take to go around the sun).
