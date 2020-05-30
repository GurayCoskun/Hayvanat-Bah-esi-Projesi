import animals
import random
from chicken.chicken import chicken
def hunting(hunterlistX,hunterlistY,x,y,n,type):
    for i in range(len(hunterlistX)):
        numberOFloop = 0
        if type == "Chicken":
            numberOFloop = len(animals.chickens)
        elif type == "Ship":
            numberOFloop = len(animals.ships)
        elif type == "Cow":
            numberOFloop = len(animals.cows)
        elif type == "Wolf":
            numberOFloop = len(animals.wolfs)
        elif type == "Lion":
            numberOFloop = len(animals.lions)
        b = 0
        for c in range(numberOFloop):
            if (abs(hunterlistX[i] - x[c]) < n+1 or abs(hunterlistY[i] - y[c]) <n+1):
                if (type == "Chicken"):
                    if n==4:   #hunter gets location of prey
                        animals.wolfs[i].xKoordinat=animals.chickens[c-b].xKoordinat
                        animals.wolfs[i].yKoordinat=animals.chickens[c-b].yKoordinat
                    animals.chickens.pop(c-b)
                    b=b+1
                elif (type == "Ship"):
                    if n==4:#hunter gets location of prey
                        animals.wolfs[i].xKoordinat=animals.ships[c-b].xKoordinat
                        animals.wolfs[i].yKoordinat=animals.ships[c-b].yKoordinat
                    elif(n==5):#hunter gets location of prey
                        animals.lions[i].xKoordinat = animals.ships[c-b].xKoordinat
                        animals.lions[i].yKoordinat = animals.ships[c-b].yKoordinat
                    animals.ships.pop(c-b)
                    b+=1
                elif (type == "Cow"):
                    if (n == 5):#hunter gets location of prey
                        animals.lions[i].xKoordinat = animals.cows[c-b].xKoordinat
                        animals.lions[i].yKoordinat = animals.cows[c-b].yKoordinat
                    animals.cows.pop(c-b)
                    b=b+1
                elif (type == "Wolf"):
                    animals.wolfs.pop(c-b)
                    b+=1
                elif (type == "Lion"):
                    animals.lions.pop(c-b)
                    b+=1
def hunter(n,forx,fory,typePrey):
    hunterlistX=[]
    hunterlistY=[]
    if n ==4:
        for i in range(len(animals.wolfs)):
            hunterlistX.append(animals.wolfs[i].xKoordinat)
            hunterlistY.append(animals.wolfs[i].yKoordinat)
        hunting(hunterlistX,hunterlistY,forx,fory,n,typePrey)

    elif(n==5):
        for i in range(len(animals.lions)):
            hunterlistX.append(animals.lions[i].xKoordinat)
            hunterlistY.append(animals.lions[i].yKoordinat)
        hunting(hunterlistX,hunterlistY,forx,fory,n,typePrey)
    else:
        for i in range(len(animals.hunters)):
            hunterlistX.append(animals.hunters[i].xKoordinat)
            hunterlistY.append(animals.hunters[i].yKoordinat)
        hunting(hunterlistX,hunterlistY,forx,fory,n,typePrey)
def moving(type):
    global move
    a=random.choice([0,1])   #0 is for x and 1 is for y
    numberOFloop=0
    if type=="Chicken":
        numberOFloop=len(animals.chickens)
    elif type=="Ship":
        numberOFloop=len(animals.ships)
    elif type=="Cow":
        numberOFloop=len(animals.cows)
    elif type=="Wolf":
        numberOFloop=len(animals.wolfs)
    elif type=="Lion":
        numberOFloop=len(animals.lions)
    elif type=="hunter":
        numberOFloop=len(animals.hunters)
    for i in range(numberOFloop):
        if (type == "Chicken"):
            if (a == 1):
                animals.chickens[i].xKoordinat=animals.chickens[i].xKoordinat+1
            else:
                animals.chickens[0].yKoordinat = animals.chickens[i].yKoordinat + 1
            move += 1
        elif (type == "Ship"):
            if (a == 1):
                animals.ships[i].xKoordinat = animals.ships[i].xKoordinat + 2
            else:
                animals.ships[i].yKoordinat=animals.ships[i].yKoordinat+2
            move += 2
        elif (type == "Cow"):
            if (a == 1):
                animals.cows[i].xKoordinat = animals.cows[i].xKoordinat + 2
            else:
                animals.cows[i].yKoordinat = animals.cows[i].yKoordinat + 2
            move += 2
        elif (type == "Wolf"):
            if (a == 1):
                animals.wolfs[i].xKoordinat = animals.wolfs[i].xKoordinat + 3
            else:
                animals.wolfs[i].yKoordinat = animals.wolfs[i].yKoordinat + 3
            move += 3
        elif (type == "Lion"):
            if (a == 1):
                animals.lions[i].xKoordinat = animals.lions[i].xKoordinat + 4
            else:
                animals.lions[i].yKoordinat = animals.lions[i].yKoordinat + 4
            move += 4
        elif(type=="Hunter"):
            if (a == 1):
                animals.hunters[i].xKoordinat = animals.hunters[i].xKoordinat + 1
            else:
                animals.hunters[i].yKoordinat = animals.hunters[i].yKoordinat + 1
            move += 1
    return move
def born(forX,forY,type):  #new child borning with random coordination.
    randomX = random.randint(0, 500)
    randomY = random.randint(0, 500)
    for i in range(len(forX)):
        for y in range(len(forX)):
            if (i!=y) and i>y :
                if((abs(forX[i]-forX[y])<4) or abs(forY[i]-forY[y])<4):
                    if type=="Chicken":
                        if(animals.chickens[i].cinsiyet!=animals.chickens[y].cinsiyet):
                            animals.chickens.append(chicken(randomX,randomY,random.choice(["Chicken","rooster"])))
                    elif type=="Ship":
                        if (animals.ships[i].cinsiyet != animals.ships[y].cinsiyet):
                            animals.ships.append(chicken(randomX,randomY,random.choice(["erkek","dişi"])))
                    elif type=="Cow":
                        if (animals.cows[i].cinsiyet != animals.cows[y].cinsiyet):
                            animals.cows.append(chicken(randomX,randomY,random.choice(["erkek","dişi"])))
                    elif type=="Wolf":
                        if (animals.wolfs[i].cinsiyet != animals.wolfs[y].cinsiyet):
                            animals.wolfs.append(chicken(randomX,randomY,random.choice(["erkek","dişi"])))
                    elif type=="Lion":
                        if (animals.lions[i].cinsiyet != animals.lions[y].cinsiyet):
                            animals.lions.append(chicken(randomX,randomY,random.choice(["erkek","dişi"])))
def clearList(forx,fory):
    forx.clear()
    fory.clear()
def createListChicken(forx,fory):
    for i in range(len(animals.chickens)):
        forx.append(animals.chickens[i].xKoordinat)
        fory.append(animals.chickens[i].yKoordinat)
def createListShip(forx,fory):
    for i in range(len(animals.ships)):
        forx.append(animals.ships[i].xKoordinat)
        fory.append(animals.ships[i].yKoordinat)
def createListCow(forx,fory):
    for i in range(len(animals.cows)):
        forx.append(animals.cows[i].xKoordinat)
        fory.append(animals.cows[i].yKoordinat)
def createWolfList(forx,fory):
    for i in range(len(animals.wolfs)):
        forx.append(animals.wolfs[i].xKoordinat)
        fory.append(animals.wolfs[i].yKoordinat)
def createLionList(forx,fory):
    for i in range(len(animals.lions)):
        forx.append(animals.lions[i].xKoordinat)
        fory.append(animals.lions[i].yKoordinat)
def chickenList(forx,fory):
    clearList(forx, fory)
    createListChicken(forx, fory)
    born(forx,fory,"Chicken")
    clearList(forx, fory)
    createListChicken(forx, fory)
    hunter(4, forx, fory, "Chicken")
    clearList(forx, fory)
    createListChicken(forx, fory)
    hunter(8, forx, fory, "Chicken")
def shipList(forx,fory):
    clearList(forx, fory)
    createListShip(forx, fory)
    born(forx,fory,"Ship")
    clearList(forx, fory)
    createListShip(forx, fory)
    hunter(4, forx, fory, "Ship")
    clearList(forx, fory)
    createListShip(forx, fory)
    hunter(5, forx, fory, "Ship")
    clearList(forx, fory)
    createListShip(forx, fory)
    hunter(8, forx, fory, "Ship")
def cowList(forx,fory):
    clearList(forx, fory)
    createListCow(forx, fory)
    born(forx,fory,"Cow")
    clearList(forx, fory)
    createListCow(forx, fory)
    hunter(5, forx, fory, "Cow")
    clearList(forx, fory)
    createListCow(forx, fory)
    hunter(8, forx, fory, "Cow")
def wolfList(forx,fory):
    clearList(forx, fory)
    createWolfList(forx,fory)
    born(forx,fory,"Wolf")
    clearList(forx, fory)
    createWolfList(forx,fory)
    hunter(8, forx, fory, "Wolf")
def lionList(forx,fory):
    clearList(forx, fory)
    createLionList(forx, fory)
    born(forx,fory,"Lion")
    clearList(forx, fory)
    createLionList(forx, fory)
    hunter(8, forx, fory, "Lion")
def main():
    global move
    forx = []   #X Koordinatı
    fory = []   #Y Koordinatı
    list=["Hunter","Chicken","Wolf","Cow","Lion","Ship"]
    while move < 1000:
        for i in list:
            moving(i)
        chickenList(forx, fory)
        shipList(forx, fory)
        cowList(forx, fory)
        wolfList(forx, fory)
        lionList(forx, fory)
if __name__ == "__main__":
    move = 0
    print("Başlangıçtaki Tavuk ve Horoz sayısının toplamı =" + str(len(animals.chickens)))
    print("Başlangıçtaki Koyun Sayısı = " + str(len(animals.ships)))
    print("Başlangıçtaki Kurt Sayısı = " + str(len(animals.wolfs)))
    print("Başlangıçtaki İnek Sayısı = " + str(len(animals.cows)))
    print("Başlangıçtaki Aslan Sayısı = " + str(len(animals.lions)))
    main()
    print("Bin hareketten sonra Tavuk ve Horoz sayısının toplamı =" + str(len(animals.chickens)))
    print("Bin hareketten sonra Koyun Sayısı = " + str(len(animals.ships)))
    print("Bin hareketten sonra Kurt Sayısı = " + str(len(animals.wolfs)))
    print("Bin hareketten sonra İnek Sayısı = " + str(len(animals.cows)))
    print("Bin hareketten sonra Aslan Sayısı = " + str(len(animals.lions)))
