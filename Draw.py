import turtle
from math import sqrt
def RoadLength(RoadEnds,PointCoords,Road):
    point1=RoadEnds[Road][0]
    point2=RoadEnds[Road][1]
    x1=PointCoords[point1][0]
    y1=PointCoords[point1][1]
    x2=PointCoords[point2][0]
    y2=PointCoords[point2][1]
    Length=sqrt((x2-x1)**2+(y2-y1)**2)

    return Length

def CarCoords(RoadEnds,PointCoords,Road,u):
    point1=RoadEnds[Road][0]
    point2=RoadEnds[Road][1]
    x1=PointCoords[point1][0]
    y1=PointCoords[point1][1]
    x2=PointCoords[point2][0]
    y2=PointCoords[point2][1]
    x=x1*(1.0-u)+x2*u
    y=y1*(1.0-u)+y2*u
    return x,y

print ("Staring program...")
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Define town.
# Intersections are just points.
# Roads are line segments between intersections or between points.
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
PointCoords=[[0.0,0.0],[100.0,0.0],[100.0,150.0],[0.0,100.0],[150.0,50.0]]
RoadEnds=[[2,3],[3,0],[0,1],[1,2],[1,4],[4,2],[3,1],[1,3]]
RoadSpeed=[10.0,2.5,3.0,5.0,4.0,3.0,7.0,10.0]
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Build (draw) the town.
# Create a turtle that will draw the town.
# Loop over roads and draw each one.
# To draw a road:
# ­ Raise the builder turtle's pen
# ­ Go to start of road
# ­ Lower the build turtle's pen
# ­ Go to end of road
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
print (CarCoords(RoadEnds,PointCoords,0,0.5))
builder=turtle.Turtle()
numRoads = len(RoadSpeed)
builder.hideturtle()
for Road in range(numRoads):
    builder.penup()
    point1=RoadEnds[Road][0]
    point2=RoadEnds[Road][1]
    x1=PointCoords[point1][0]
    y1=PointCoords[point1][1]
    x2=PointCoords[point2][0]
    y2=PointCoords[point2][1]
    builder.goto(x1,y1)
    builder.pendown()
    builder.goto(x2,y2)
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Define car.
# Need route (list of roads that tells how the car goes around the town).
# Need route road directions/orientation (forward vs backward along each road).
# Need starting u value (how far the car is along the starting road).
# Need to set which route command the car starts with.
# Get the number of roads along the car's route
# Get the starting (x,y) for the car
# Get the first road in the route
# Move the car to its starting location
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
car = turtle.Turtle()
car.shape("circle")
Route=[2,3,0,1,2,4,5,0,6,7,6]
RouteDir=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
u_start = 0.5
routeCommand = 0
numCommands=len(Route)
u0=u_start
R0=Route[routeCommand]
dir0=RouteDir[routeCommand]
#coords=[0.0,0.0]
coords=CarCoords(RoadEnds,PointCoords,R0,u0)
x=coords[0]
y=coords[1]
car.penup()
car.goto(x,y)
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Initial conditions for time loop.
# T=0
# time step size: dt
# Number of cycles in time loop.
# Termination time.
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
t=0.0
dt=1.0
maxcycle=1000
stoptime=60.0
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Initialize car's u0 value to starting value.
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
coords=CarCoords(RoadEnds,PointCoords,0,0.5)
print (coords)
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Start the time loop (start the simulation)
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
for n in range(maxcycle):
    L0=RoadLength(RoadEnds,PointCoords,R0)
    s0=RoadSpeed[R0]
    u1=u0+s0*dt/L0
    if u1>1.0:
        routeCommand = routeCommand+1
        if routeCommand > numCommands-1:
            break
        R1=Route[routeCommand]
        dir1=RouteDir[routeCommand]
        s1=RoadSpeed[R1]
        L1=RoadLength(RoadEnds,PointCoords,R1)
        u1=s1*(dt-(L0*(1.0-u0))/s0)/L1
    else:
        R1=R0
        s1=s0
        L1=L0
        dir1=dir0
    coords=CarCoords(RoadEnds,PointCoords,R1,u1)
    x=coords[0]
    y=coords[1]
    car.goto(x,y)
    u0=u1
    s0=s1
    L0=L1
    dir0=dir1
    R0=R1
    t=t+dt

print ("time=",t," road=",R1," u=",u1)
print ("Program finished!")