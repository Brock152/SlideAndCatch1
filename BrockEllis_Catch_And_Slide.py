# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:07:15 2024

@author: uball
"""
import pygame, random, simpleGE

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(25, 25)
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.scene.screen.get_width())
        self.dy = random.randint(4, 8)

    def checkBounds(self):
        if self.bottom > self.scene.screen.get_height():
            self.reset()

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Card.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("blackjack.jpg")
        self.charlie = Charlie(self)
        self.coins = [Coin(self) for _ in range(10)]
        self.sprites = [self.charlie] + self.coins

    def process(self):
        for coin in self.coins:
            if self.charlie.collidesWith(coin):
                coin.reset()

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
