""""

CS558 Second Assignment
Students: Jesus Gonzalez, Ryan Garcia

"""
from numpy import *
from scipy import integrate

"""
derive uses the 2 first order differential equations
Each describes mackerel and shark
a is the rate of encounter between the 2 species
"""
a = .01
def derive(X, t=0):
    return array([2*X[0] - a*X[0]*X[1], -X[1] + a*X[0]*X[1]])
"""
X0 will control the inputs.
at the moment, 300 is the number of mackerel and 150 is the number of sharks
if we change this to 15 and 22, at the end of the run you will see extra print statements that indeed
prove the mackerel population reaching a number below 1
"""
time = linspace(0, 60, 60)
X0 = array([4, 3])
X = integrate.odeint(derive, X0, time)

"""
prints out the populations of the species at each state
"""
b = 0
for a in X:
    print 'at time: ', math.floor(time[b]), 'min there are:'
    print 'Mackerels: ', math.floor(a[0])
    print 'Sharks: ', math.floor(a[1])
    print '----------------------------'
    b += 1

"""
The Following for loops will calculate all our data metrics
"""
mackMax = 0
for b in X:
    if b[0] > mackMax:
        mackMax = b[0]

sharkMax = 0
for b in X:
    if b[1] > sharkMax:
        sharkMax = b[1]

mackMin = mackMax
for b in X:
    if b[0] < mackMin:
        mackMin = b[0]

sharkMin = sharkMax
for b in X:
    if b[1] < sharkMin:
        sharkMin = b[1]

mackTotal = 0
for b in X:
    mackTotal += b[0]

sharkTotal = 0
for b in X:
    sharkTotal += b[1]

print "     DATA METRICS!"
print " "
print "Average life of Mackerel: ", math.floor((mackTotal/60))
print "Max life of Mackerel: ", math.floor(mackMax)
print "Min life of the Mackerel: ", math.floor(mackMin)
print " "
print "Average life of Shark: ", math.floor((sharkTotal/60))
print "Max life of Shark: ", math.floor(sharkMax)
print "Min life of the Shark: ", math.floor(sharkMin)

if mackMin < 1:
    print " "
    print "----------------------------"
    print "     EXTRA NOTES"
    print "As you see in the DATA METRICS, using certain values, proves mackerel population reach 0"
