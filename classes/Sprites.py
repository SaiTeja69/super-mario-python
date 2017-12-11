from classes.Spritesheet import Spritesheet
import pygame
from pygame.color import Color
from classes.Sprite import Sprite
from classes.Animation import Animation
import json
import pprint

class Sprites():
    def __init__(self):
        self.spriteCollection = self.loadSprites([  "./sprites/Mario.json",
                                                    "./sprites/Goomba.json",
                                                    "./sprites/Koopa.json",
                                                    "./sprites/AnimationSprites.json",
                                                    "./sprites/BackgroundSprites.json"])

    def loadSprites(self,urlList):
        resDict = {}
        for url in urlList:
            with open(url) as jsonData:
                data = json.load(jsonData)
                mySpritesheet = Spritesheet(data['spriteSheetURL'])
                dic = {}
                if(data['type'] == "background"):
                    for sprite in data['sprites']:
                        try: 
                            colorkey = sprite['colorKey']
                        except KeyError:
                            colorkey = None
                        dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey),sprite['collision'],None,sprite['redrawBg'])
                    resDict.update(dic)
                    continue
                elif data['type'] == "animation":
                    for sprite in data['sprites']:
                        images = []
                        for image in sprite['images']:
                            images.append(mySpritesheet.image_at(image['x'],image['y'],image['scale'],colorkey=-1))
                        dic[sprite['name']] = Sprite(None,True,animation = Animation(images,deltaTime = sprite["deltaTime"]),redrawBackground = sprite['redrawBackground'])
                    resDict.update(dic)
                    continue
                elif data['type'] == "character":
                    for sprite in data['sprites']:
                        try: 
                            colorkey = sprite['colorKey']
                        except KeyError:
                            colorkey = None
                        dic[sprite['name']] = Sprite(mySpritesheet.image_at(sprite['x'],sprite['y'],sprite['scalefactor'],colorkey,True,xTileSize=data['size'][0],yTileSize=data['size'][1]),sprite['collision'])
                    resDict.update(dic)
                    continue
        return resDict




            



