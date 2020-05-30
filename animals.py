from chicken.chicken import chicken
from ships.ship import ship
from wolf.wolf import wolf
from cow.cow import cow
from lion.lion import lion
from hunter.hunter import hunter
import random
cows=[]
ships=[]
chickens=[]
wolfs=[]
lions=[]
hunters=[]

a=random.randint(0,500)
b=random.randint(0,500)
hunters.append(hunter(a,b))


for i in range(30):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    if(i<15):
        ships.append(ship(x,y,"erkek"))
    else:
        ships.append(ship(x,y,"dişi"))

for i in range(10):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    if(i<5):
        cows.append(cow(x,y,"erkek"))
    else:
        cows.append(cow(x,y,"dişi"))
for i in range(20):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    if (i < 9):
        chickens.append(chicken(x, y,"chicken"))
    else:
        chickens.append(chicken(x, y,"rooster"))
for i in range(10):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    if(i<5):
        wolfs.append(wolf(x,y,"erkek"))
    else:
        wolfs.append(wolf(x,y,"dişi"))

for i in range(8):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    if(i<4):
        lions.append(lion(x,y,"erkek"))
    else:
        lions.append(lion(x,y,"dişi"))
