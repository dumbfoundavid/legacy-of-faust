"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.

"""
import pygame

import game_project.gp_constants as constants

from game_project.gp_spritesheet_functions import SpriteSheet
from game_project.gp_platforms import MovingPlatform

# Load sound fx
pygame.init()
player_damage = pygame.mixer.Sound('player_damage.ogg')



class Player(pygame.sprite.Sprite):
    
    """ This class represents the main character the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0
    
    # is the player already walking (handle sprinting)
    
    walking = False
    
    life = 150

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    
    # holds images for animated jump left/right of our player
    
    walking_frames_lj = []
    walking_frames_rj = []
    
    # holds images for animated attack left/right of our player
    
    attack_frames_l = []
    attack_frames_r = []
    
    # holds images for animated attack left/right of our player
    
    damaged_frames_l = []
    damaged_frames_r = []

    # What direction is the player facing?
    direction = "R"
    
    # What direction is the player attacking 
    att_direction = "R"

    # List of sprites we can bump against
    level = None
    
    # tracks how many monsters the enemy has killed
    slain = 0

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("hanz_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(487, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(542, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(597, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(660, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(730, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(801, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(852, 104, 57, 100)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(918, 104, 57, 100)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(487, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(542, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(597, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(660, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(730, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(801, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(852, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(918, 104, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        
        # Load all the jumping images
        
        # facing right
        
        image = sprite_sheet.get_image(224, 718, 57, 100)
        self.walking_frames_rj.append(image)
        
        # facing left
        
        image = sprite_sheet.get_image(224, 718, 57, 100)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_lj.append(image)
        
        # Load all the attacking frames
        
        
        # facing right

        image = sprite_sheet.get_image(118, 2, 85, 100)
        self.attack_frames_r.append(image)
        
        # facing left
        

        image = sprite_sheet.get_image(118, 2, 85, 100)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()


    def update(self):
        """ Move the player. """
        

    
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        
        pos = self.rect.x + self.level.world_shift
        
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
           
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
            
        # jump left/right
        
        elif self.direction == "LJ":
            frame = (pos // 30) % len(self.walking_frames_lj)
            self.image = self.walking_frames_lj[frame]
            #self.rect = self.image.get_rect()
        
        elif self.direction == "RJ":
            frame = (pos // 30) % len(self.walking_frames_rj)
            self.image = self.walking_frames_rj[frame]
            #self.rect = self.image.get_rect()
            
        # attack left/right
        
        elif self.direction == "LA":
            frame = (pos // 30) % len(self.attack_frames_l)
            self.image = self.attack_frames_l[frame]
            
        elif self.direction == "RA":
            frame = (pos // 30) % len(self.attack_frames_r)
            self.image = self.attack_frames_r[frame]
            
            

        #See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        self.level.platform_list
 
        # Check and see if we hit anything (platforms)
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
                
                
                
        # Check and see if we hit anything (enemies)
        # True in third parameter removes any enemy we touch
         
#          
#           
#         enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
#            
#         for baddie in enemy_hit_list:
#             self.life -= 1
#             player_damage.play()
#             
# 
#             print('curr hp:', str(self.life))
#              
#         
#                 
         

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """
        
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
        
        if self.direction == "R":
            self.direction = "RJ" # right-facing jump
            
        elif self.direction == "L":
            self.direction = "LJ" # left-facing jump

    # Player-controlled movement:
    
    def attack(self):
        
        """ Called when the user hits the 'a' keystroke. """
        
        if self.direction == "L":
            self.direction = "LA"
            
        elif self.direction == "R":
            self.direction = "RA"

    def go_left(self):
        
        
        
        """ Called when the user hits the left arrow. """
        
    
    
        self.change_x = -3
        self.direction = "L"
        
        self.walking = True
        
       

    def go_right(self):
        """ Called when the user hits the right arrow. """
        
     
        
        self.change_x = 3
        self.direction = "R"
        
        self.walking = True
        
    def sprint(self):
        """ Makes the player run faster. """
        
        if(self.direction == "R" and self.change_y == 0 and self.walking == True):
            self.change_x = 6
        
        elif(self.direction == "L" and self.change_y == 0 and self.walking == True): # if going left
            self.change_x = -6
    
    def normal_speed(self):
        """ Makes the player run at a normal pace. """
        
        if(self.direction == "R"):
            self.change_x = 3
        
        elif(self.direction == "L"): # if going left
            self.change_x = -3    
  

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        
        # reset the walking boolean to False
        
        self.walking = False
        
    def reset_animation(self):
        
        if self.direction == "LA" or self.direction == "LJ":
            self.direction = "L"
        elif self.direction == "RA" or self.direction == "RJ":
            self.direction = "R"
        
    
