from configuration import *
import pygame
import math

class Weapon(pygame.sprite.Sprite):
    def __init__(self, game, x,y):
        self.game=game
        self._layer=GROUND_LAYER
        self.groups=self.game.all_sprites, self.game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        
        self.width=TILESIZE
        self.height=TILESIZE
        
        self.image=self.game.weapon_spritesheet.get_image(447,353, self.width, self.height)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.animationCounter=1
        
    def animation(self):
        
        animate=[self.game.weapon_spritesheet.get_image(0,0,self.width,self.height),
                 self.game.weapon_spritesheet.get_image(32,0,self.width,self.height),
                 self.game.weapon_spritesheet.get_image(64,0,self.width,self.height)]
        
        self.image=animate[math.floor(self.animationCounter)]
        self.animationCounter+=0.06
        if self.animationCounter>=3:
            self.animationCounter=0
            
    def update(self):
        self.animation()
        
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.bullet_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = self.game.player.direction
        self.damagePoints=1
    
    def collide_block(self):
        collide=pygame.sprite.spritecollide(self, self.game.blocks,False)
        if collide:
            self.kill()
    
    def collide_enemy(self):
        collide=pygame.sprite.spritecollide(self, self.game.enemies,False)
        if collide:
            collide[0].damage(self.damagePoints)
            self.kill()

        
        
    def move(self):
        
        if self.direction =="right":
            self.rect.x += BULLET_STEPS
             
            
        if self.direction =="left":
            self.rect.x -= BULLET_STEPS        
            
        if self.direction =="up":
            self.rect.y -= BULLET_STEPS
            
        if self.direction =="down":
            self.rect.y += BULLET_STEPS
            
    def update(self):
        self.move()
        self.collide_block()
        self.collide_enemy()
        
class Enemy_Bullet(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.bullet_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = self.game.player.direction
        self.damage=1
    
    def collide_block(self):
        collide=pygame.sprite.spritecollide(self, self.game.blocks,False)
        if collide:
            self.kill()
    
    def collide_player(self):
        collide=pygame.sprite.spritecollide(self, self.game.mainPlayer,False)
        if collide:
            self.game.player.damage(self.damage)
            self.kill()

        
        
    def move(self):
        
        if self.direction =="right":
            self.rect.x += BULLET_STEPS
             
            
        if self.direction =="left":
            self.rect.x -= BULLET_STEPS        
            
        if self.direction =="up":
            self.rect.y -= BULLET_STEPS
            
        if self.direction =="down":
            self.rect.y += BULLET_STEPS
            
    def update(self):
        self.move()
        self.collide_block()
        self.collide_player()
        
   
        