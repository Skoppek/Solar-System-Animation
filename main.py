import turtle
import math
import random

from numpy import pi

colors = ['DarkGrey', 'DarkGoldenRod1', 'blue', 'brown', 'bisque3', 'bisque', 'DeepSkyBlue', 'CornflowerBlue', 'azure4']

cuts = 180
#prędkości muszą być dzielnikami ilości klatek oraz planety poruszającej się szybciej
velocities = {
    'My' : 12,
    'Ws' : 10,
    'Za' : 9,
    'Ms' : 6,
    'Jz' : 5,
    'Sn' : 4,
    'Un' : 3,
    'Nn' : 2,
    'Pn' : 1,
}

init_positions = {
    'My' : random.randrange(0, cuts),
    'Ws' : random.randrange(0, cuts),
    'Za' : random.randrange(0, cuts),
    'Ms' : random.randrange(0, cuts),
    'Jz' : random.randrange(0, cuts),
    'Sn' : random.randrange(0, cuts),
    'Un' : random.randrange(0, cuts),
    'Nn' : random.randrange(0, cuts),
    'Pn' : random.randrange(0, cuts)
}

sizes = [
    3,
    3,
    5,
    4,
    20,
    15,
    10,
    10,
    2
]

positions = init_positions.copy()
history = []

f = open("Pozycje", "w")

def move(turns):
    f.write(f'{turns:3d}. | ')
    for planet in positions.keys():
        f.write(f'{planet:2s} {positions[planet]:3d} | ')
        positions[planet] += velocities[planet]
        if(positions[planet] >= cuts):
            positions[planet] %= cuts
    f.write('\n')

def is_finished():
    for planet in positions.keys():
        if(positions[planet] != init_positions[planet]):
            return True
    return False

def remember():
    temp = []
    for pos in positions.values():
        temp.append(pos)
    history.append(temp)

frames = 0
remember()
move(frames)
while(is_finished()):
    frames += 1
    remember()
    move(frames)
f.write("KONIEC")
f.close()

wn = turtle.Screen()
wn.title("Solar System Animation - Mateusz Skop")
wn.bgcolor("black")

players = []
for i in range(0, len(history[0])):
    player = turtle.Turtle()
    player.shape("circle")
    player.color(colors[i])
    player.pencolor("black")
    player.turtlesize(stretch_wid=sizes[i] / 8, stretch_len=sizes[i] / 8)
    player.speed("fastest")
    players.append(player)

while True:
    for t in history:
        for i in range(0, len(t)):
            angle = 2 * math.pi * t[i] / cuts
            radius = ((i+5) / 3) ** 4 
            players[i].goto(radius * math.cos(angle), radius * math.sin(angle))

wn.mainloop()
