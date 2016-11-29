'''
Created on May 16, 2015

@author: David Nickolo
'''

"""
Module for managing monsters.
"""
import pygame

from game_project.gp_spritesheet_functions import SpriteSheet


# These constants define our monster types:
#   Name of sprite sheet image
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite



#RED_FIEND = (73, 7, 50, 60) # the first monster

# Load sound fx
pygame.init()
monster_sound = pygame.mixer.Sound('monster_cry.ogg')
axe_cry = pygame.mixer.Sound('axe_cry.ogg')
player_damage = pygame.mixer.Sound('player_damage.ogg')

class Monster(pygame.sprite.Sprite):
    """ Monster that the user fights """

    def __init__(self, sprite_sheet_data):
        """ Monster constructor. """
        
        pygame.sprite.Sprite.__init__(self)



class BlueSkeleton(Monster):
    """ This is the first enemy type, a blue skeleton. """
    
    

    
    # -- Attributes
    # Set speed vector of monster
    change_x = 0
    change_y = 0
    hp = 40
    
    
    death = False
    
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0 # determines how far a monster goes left
    boundary_right = 0 # determines how far a monster goes right 

    # This holds all the images for the animated walk left/right
    # of the monster
    walking_frames_l = []
    walking_frames_r = []
    
    death_frame = []
    
    # What direction is the monster facing?
    direction = "R"

    # List of sprites monster can bump against
    level = None
    player = None 
    
    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("BlueSkel.png")
        
        
        # Load all the left facing images into a list
        image = sprite_sheet.get_image(22, 17, 51, 76)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(73, 14, 41, 80)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(113, 14, 29, 79)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(142, 16, 46, 77)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(187, 14, 38, 78)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(224, 16, 55, 76)
        self.walking_frames_l.append(image)
        
        # Load all the left facing images, then flip them
        # to face right.
        image = sprite_sheet.get_image(22, 17, 51, 76)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(73, 14, 41, 80)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(113, 14, 29, 79)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(142, 16, 46, 77)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(187, 14, 38, 78)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(224, 16, 55, 76)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        
        # set death frame (blood)
        
        #self.death_frame = pygame.image.load("blood_splatter.png").convert()
        
        death_sheet = SpriteSheet("blood_splatter.png")
        
        image = death_sheet.get_image(0, 0, 49, 40)
        self.death_frame.append(image)
 
   
        # Set the image the monster starts with
        self.image = self.walking_frames_l[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
    
    

    def update(self):
        """ Move the monster.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            monster shoves a player into another object. Make sure
            moving monsters have clearance to push the player around
            or add code to handle what happens if they don't. """
 

        # Move left/right
        
        self.rect.x += self.change_x
        
        pos = self.rect.x
        
        if self.direction == "R":
        #if pos < self.boundary_right:
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
            
           
        elif self.direction == "L":
        #elif pos > self.boundary_left:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
        elif self.direction == "D":

            frame = (pos // 30) % len(self.death_frame)
            self.image = self.death_frame[frame]
            
 

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
            
            print("Damaged player")
            
            print(self.player.life)
            
            self.player.life -= 1
            player_damage.play()

            # If player is moving right, set player's right side
            # to the left side of the monster we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
              
            else:
                # Otherwise if player us moving left, do the opposite.
                self.player.rect.left = self.rect.right
               
                
                


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
                


        # Check the boundaries and see if we need to reverse
        # direction.
        
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        
        #if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
        
        if cur_pos < self.boundary_left: # if left boundary is reached
            
           
            
            self.change_x *= -1
            
            self.direction = "R" # code to change where the monster is facing
            
            
        elif cur_pos > self.boundary_right: # if right boundary is reached
            
             
            
            self.change_x *= -1
            
            self.direction = "L" # code to change where the monster is facing 
         
                  
        #code below not used yet    
        # Monster movement:
    def go_left(self):
        """ Monster moves left. """
  
    
        self.change_x = -2
        self.direction = "L"
        # return self.change_x
        
       

    def go_right(self):
        """ Monster moves right. """
    
        
        self.change_x = 2
        self.direction = "R"
        #return self.change_x
    

    def calc_grav(self): # NOTE: does it even work properly? 
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            
    def set_direction(self, direction):
        
        self.direction = direction
        
    def die(self):
        
        

        print("die() accessed")
    
        
        monster_sound.play()


        self.change_x = 0
        self.change_y = 0

        self.direction = "D"
        
        
class AxeLord(Monster):
    """ This is the second enemy type, an axe knight. """
    
    

    
    # -- Attributes
    # Set speed vector of monster
    change_x = 0
    change_y = 0
    hp = 120
    
    
    death = False
    
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0 # determines how far a monster goes left
    boundary_right = 0 # determines how far a monster goes right 

    # This holds all the images for the animated walk left/right
    # of the monster
    walking_frames_l = []
    walking_frames_r = []
    
    death_frame = []
    
    # What direction is the monster facing?
    direction = "R"

    # List of sprites monster can bump against
    level = None
    player = None 
    
    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("axearmor.png")
        
        
        # Load all the left facing images into a list
        image = sprite_sheet.get_image(56, 48, 101, 153)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(171, 47, 111, 154)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(304, 48, 98, 154)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(426, 48, 112, 153)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(561, 49, 135, 152)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)

        
        # Load all the left facing images, then flip them
        # to face right.
        image = sprite_sheet.get_image(56, 48, 101, 153)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(171, 47, 111, 154)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(304, 48, 98, 154)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(426, 48, 112, 153)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(561, 49, 135, 152)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        
        # set death frame (blood)
        
        
        
        death_sheet = SpriteSheet("blood_splatter.png")
        
        image = death_sheet.get_image(0, 0, 49, 40)
        self.death_frame.append(image)
 
   
        # Set the image the monster starts with
        self.image = self.walking_frames_l[0]


        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
    
    

    def update(self):
        """ Move the monster.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            monster shoves a player into another object. Make sure
            moving monsters have clearance to push the player around
            or add code to handle what happens if they don't. """
 

        # Move left/right
        
        self.rect.x += self.change_x
        
        pos = self.rect.x
        
        if self.direction == "R":
        #if pos < self.boundary_right:
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
            
           
        elif self.direction == "L":
        #elif pos > self.boundary_left:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
        elif self.direction == "D":

            frame = (pos // 30) % len(self.death_frame)
            self.image = self.death_frame[frame]
            
 

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
            
            print("Damaged player")
            print(self.player.life)
            
            self.player.life -= 2
            player_damage.play()

            # If player is moving right, set player's right side
            # to the left side of the monster we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
              
            else:
                # Otherwise if player us moving left, do the opposite.
                self.player.rect.left = self.rect.right
               
                
                


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
                


        # Check the boundaries and see if we need to reverse
        # direction.
        
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        
        #if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
        
        if cur_pos < self.boundary_left: # if left boundary is reached
            
           
            
            self.change_x *= -1
            
            self.direction = "R" # code to change where the monster is facing
            
            
        elif cur_pos > self.boundary_right: # if right boundary is reached
            
             
            
            self.change_x *= -1
            
            self.direction = "L" # code to change where the monster is facing 
         
                  
     
        
    def die(self):
        
        

        print("die() accessed")
    
        
        axe_cry.play()

        self.change_x = 0
        self.change_y = 0

        self.direction = "D"

class Frankenstein(Monster):
    """ This is the third (last) enemy type, Dr. Frankenstein's monster. """
    
    

    
    # -- Attributes
    # Set speed vector of monster
    change_x = 0
    change_y = 0
    hp = 400
    
    
    death = False
    
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0 # determines how far a monster goes left
    boundary_right = 0 # determines how far a monster goes right 

    # This holds all the images for the animated walk left/right
    # of the monster
    walking_frames_l = []
    walking_frames_r = []
    
    death_frame = []
    
    # What direction is the monster facing?
    direction = "R"

    # List of sprites monster can bump against
    level = None
    player = None 
    
    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("frankenstein.png")
        
        
        # Load all the left facing images into a list
        image = sprite_sheet.get_image(0, 0, 221, 460)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(235, 0, 393, 466)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(637, 1, 479, 460)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(1163, 5, 164, 461)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(1407, 7, 208, 460)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(1633, 6, 173, 461)
        image.set_colorkey(pygame.Color(255, 255, 255))
        self.walking_frames_l.append(image)

        
        # Load all the left facing images, then flip them
        # to face right.
        image = sprite_sheet.get_image(0, 0, 221, 460)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(235, 0, 393, 466)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(637, 1, 479, 460)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(1163, 5, 164, 461)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(1407, 7, 208, 460)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(1633, 6, 173, 461)
        image.set_colorkey(pygame.Color(255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        
        # set death frame (blood)
        
       
        
        death_sheet = SpriteSheet("blood_splatter.png")
        
        image = death_sheet.get_image(0, 0, 49, 40)
        self.death_frame.append(image)
 
   
        # Set the image the monster starts with
        self.image = self.walking_frames_l[0]


        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
    
    

    def update(self):
        """ Move the monster.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            monster shoves a player into another object. Make sure
            moving monsters have clearance to push the player around
            or add code to handle what happens if they don't. """
 

        # Move left/right
        
        self.rect.x += self.change_x
        
        pos = self.rect.x
        
        if self.direction == "R":
        #if pos < self.boundary_right:
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
            
           
        elif self.direction == "L":
        #elif pos > self.boundary_left:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
        elif self.direction == "D":

            frame = (pos // 30) % len(self.death_frame)
            self.image = self.death_frame[frame]
            
 

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
            
            print("Damaged player")
            
            print(self.player.life)
            
            self.player.life -= 4
            player_damage.play()

            # If player is moving right, set player's right side
            # to the left side of the monster we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
              
            else:
                # Otherwise if player us moving left, do the opposite.
                self.player.rect.left = self.rect.right
               
                
                


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
                


        # Check the boundaries and see if we need to reverse
        # direction.
        
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        
        #if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
        
        if cur_pos < self.boundary_left: # if left boundary is reached
            
           
            
            self.change_x *= -1
            
            self.direction = "R" # code to change where the monster is facing
            
            
        elif cur_pos > self.boundary_right: # if right boundary is reached
            
             
            
            self.change_x *= -1
            
            self.direction = "L" # code to change where the monster is facing 
         
                  
     
        
    def die(self):
        
        

        print("die() accessed")
    
        
        axe_cry.play()
          

        self.change_x = 0
        self.change_y = 0

        self.direction = "D"          
        
  
