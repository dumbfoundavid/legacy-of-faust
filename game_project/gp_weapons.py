'''
Created on May 21, 2015

@author: David Nickolo
'''
import pygame


class Knife(pygame.sprite.Sprite):
    
    level = None
    player = None
    
    # -- Attributes
    # Set speed vector of knife
    change_x = 0
    
    # This holds all the images for the knife
    knife_frame_l = None
    knife_frame_r = None
    
    # What direction is the knife initially facing?
    knife_dir = "R"
    
    # has the knife hit something yet?
    knife_collide = False

  

    """ This class represents the knife weapon . """
    def __init__(self):
        
        """ Constructor. Pass in a handle to player. Needed for when determining
            how the weapon launches relative to the player. """
        
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        right_knife = pygame.image.load("knife.png").convert()
        left_knife = pygame.transform.flip(right_knife, True, False)
        
        self.knife_frame_l = left_knife
        self.knife_frame_r = right_knife
    
        
        # set the initial knife frame the player starts out with (right_knife)

        self.image = self.knife_frame_r
        
        
        # Set the color that should be transparent
        self.image.set_colorkey(pygame.Color(255, 255, 255)) 

        self.rect = self.image.get_rect()


    def update(self):
        
        """ Move the knife. """
        
        
        
        # if the player is facing right, launch the knife to the right
        if self.knife_dir == "R":
             
            self.change_x = 6
            self.rect.x += self.change_x
             
        # if the player is facing left, left- flip the knife sprite launch the knife to the left
        elif self.knife_dir == "L":
            
            self.image = self.knife_frame_l
            
            # Set the color that should be transparent
            self.image.set_colorkey(pygame.Color(255, 255, 255)) 
             
            self.change_x = -6
            self.rect.x += self.change_x
            
        # check if the weapon hurts an enemy
        
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
             
        for baddie in enemy_hit_list:
            
            baddie.hp -= 1
            
            print(baddie.hp)
           
            if (baddie.hp == 0):
                
                baddie.die()
                print(baddie.direction)
                
            if (baddie.direction == "D" and baddie.hp < 0):
                self.level.enemy_list.remove(baddie)
                self.knife_collide = True
                
                
