from random import random

def getRandomInt(min=1000, max=9999):
  return round(random() * (max - min)) + min;
