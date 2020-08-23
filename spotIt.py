from PIL import Image, ImageDraw, ImageFilter
import os
import random



class Item:
    def __init__(self, imagePath, name = None):
        self.image = Image.open(imagePath)
        self.name = name
        if self.name is None:
            self.name = os.path.splitext(os.path.basename(imagePath))[0]
def pickSpotCardAB(itemList, totalItemNum = 7):
    target = random.choice(itemList)
    itemList.remove(target)
    cardA = [target,]
    for i in range(0, totalItemNum):
        cardAItem = random.choice(itemList)
        cardA.append(cardAItem) 
        itemList.remove(cardAItem)
    cardB = [target,]
    for i in range(0, totalItemNum):
        cardBItem = random.choice(itemList)
        cardB.append(cardBItem) 
        itemList.remove(cardBItem)
    return(cardA, cardB)


def createEmptyCard(size = 500, outline = None):
    if outline is None:
        outline = size / 100
    im = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.ellipse((size/20-outline, size/20-outline, 19*size/20+outline, 19*size/20+outline), fill=(0, 0, 0))
    draw.ellipse((size/20, size/20, 19*size/20, 19*size/20), fill=(255, 255, 255))
    return im


def pickRandomPoint(backgroundSize):
    return random.randint(0, backgroundSize)


def applyRandomRotation(image):
    return image.rotate(random.randint(0, 360), fillcolor='white')

def createSpotCard(itemList, emptyCard = createEmptyCard()):
    for item in itemList:
        emptyCard.paste(applyRandomRotation(item), (pickRandomPoint(emptyCard.size[0] - item.size[0]), pickRandomPoint(emptyCard.size[1] - item.size[1])))
    return emptyCard
    
itemList = []
for i in range(15):
    item = Image.open('image/tiger.png')     
    itemList.append(item)
spotCards = pickSpotCardAB(itemList, totalItemNum=7)
spotCardA = createSpotCard(spotCards[0])
spotCardB = createSpotCard(spotCards[1])

#TODO: Manage background of each item
# and enhance pickRandomPoint to provide proper layout in a single card