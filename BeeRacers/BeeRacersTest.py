import beeRacers

scoring = False
beeScore = beeRacers.score

while(True):
    if beeScore != beeRacers.score:
        scoring = True

    if beeRacers.beeSprite.rect.colliderect(beeRacers.flowerSprite.rec):
        print("Overlapping flower")

