'''
Created on Apr 29, 2015

@author: David Nickolo
'''

import pygame

import game_project.gp_constants as constants
from game_project import gp_platforms
from game_project.gp_monsters import BlueSkeleton, AxeLord, Frankenstein





class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
        
    enemy_counter = 0

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player): # should modify for bullets too?
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
       
        self.enemy_list = pygame.sprite.Group()
        self.player = player
      

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
       
        self.enemy_list.update()
        
        # track the current number of enemies
        
        self.enemy_counter = len(self.enemy_list)
        
        #print(self.enemy_counter) # print the amount of enemies in our game
   
             
            

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            #enemy.rect.x += shift_x
            enemy.rect.x += shift_x
            
            

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
    
    
    

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("level01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -5000
 
        # Array with type of platform, and x, y location of the platform.

        level = [ 
                 
                  
                  
                  [gp_platforms.ELEVATED, 350, 580],
                  
                                   
                  [gp_platforms.GROUND_TWO, 600, 545],
                  [gp_platforms.GROUND_TWO, 645, 545],
                  
                  [gp_platforms.GROUND_TWO, 800, 545],
                  [gp_platforms.GROUND_TWO, 845, 545],
                  [gp_platforms.GROUND_TWO, 800, 500],
                  [gp_platforms.GROUND_TWO, 845, 500],
                  
        
        

                  [gp_platforms.GROUND, 1000, 450],
                  
                  [gp_platforms.GROUND, 1250, 450],
                  [gp_platforms.GROUND, 1300, 450],
                  [gp_platforms.GROUND, 1400, 450],
                  [gp_platforms.GROUND, 1500, 450],
                  [gp_platforms.GROUND, 1600, 450],
                  [gp_platforms.GROUND, 1700, 450],
                  [gp_platforms.GROUND, 1800, 450],
                  [gp_platforms.GROUND, 1900, 450],
                  [gp_platforms.GROUND, 2000, 450],
                  
                  
                  [gp_platforms.GROUND, 1000, 230],
                  
                  [gp_platforms.GROUND, 1100, 230],
                  [gp_platforms.GROUND, 1100, 230],
                  [gp_platforms.GROUND, 1300, 230],
                  [gp_platforms.GROUND, 1400, 230],
                  [gp_platforms.GROUND, 1500, 230],
                  [gp_platforms.GROUND, 1600, 230],
                  [gp_platforms.GROUND, 1700, 230],
                  [gp_platforms.GROUND, 1800, 230],
                  [gp_platforms.GROUND, 1900, 230],
                  
                  [gp_platforms.SMALL_PLATFORM, 2130, 200],
                  
                  [gp_platforms.SMALL_PLATFORM, 2500, 200],
                  [gp_platforms.SMALL_PLATFORM, 2550, 250],
                  [gp_platforms.SMALL_PLATFORM, 2600, 300],
                  
                  [gp_platforms.SMALL_PLATFORM, 2650, 300],
                  [gp_platforms.SMALL_PLATFORM, 2700, 250],
                  [gp_platforms.SMALL_PLATFORM, 2750, 200],
                  
                  
                  
                  [gp_platforms.ELEVATED, 2900, 230],

                  [gp_platforms.ELEVATED, 3200, 230],
                  [gp_platforms.ELEVATED, 3300, 230],
                  [gp_platforms.ELEVATED, 3400, 230],
                  [gp_platforms.ELEVATED, 3500, 230],
                  [gp_platforms.ELEVATED, 3600, 230],
                  [gp_platforms.ELEVATED, 3700, 230],
                  [gp_platforms.ELEVATED, 3800, 230],
                  [gp_platforms.ELEVATED, 3900, 230],
                  [gp_platforms.ELEVATED, 3900, 170],
                  [gp_platforms.ELEVATED, 3900, 110],
                  [gp_platforms.ELEVATED, 3900, 50],
                  [gp_platforms.ELEVATED, 3900, -10],
                  
                  
                  
                  [gp_platforms.ELEVATED, 2900, 470],

                  [gp_platforms.ELEVATED, 3400, 470],
                  
                  [gp_platforms.SMALL_PLATFORM, 4250, 650],
                  [gp_platforms.SMALL_PLATFORM, 4300, 600],
                  [gp_platforms.SMALL_PLATFORM, 4350, 550],
                  

                  
                  [gp_platforms.ELEVATED, 4400, 530],
                  [gp_platforms.ELEVATED, 4500, 530],
                  [gp_platforms.ELEVATED, 4600, 530],
                  
                  [gp_platforms.ELEVATED, 4700, 530],
                  [gp_platforms.ELEVATED, 4800, 530],
                  [gp_platforms.ELEVATED, 4900, 530],
                  [gp_platforms.ELEVATED, 5000, 530],
                  [gp_platforms.ELEVATED, 5100, 530],
                  [gp_platforms.ELEVATED, 5200, 530],
                  [gp_platforms.ELEVATED, 5300, 530],
                  [gp_platforms.ELEVATED, 5400, 530],
                  [gp_platforms.ELEVATED, 5500, 530],
                  [gp_platforms.ELEVATED, 5600, 530],
                  [gp_platforms.ELEVATED, 5700, 530],
                  
                  
                  [gp_platforms.ELEVATED, 5700, 470],
                  [gp_platforms.ELEVATED, 5700, 410],
                  [gp_platforms.ELEVATED, 5700, 350],
                  [gp_platforms.ELEVATED, 5700, 290],
                  [gp_platforms.ELEVATED, 5700, 230],
                  [gp_platforms.ELEVATED, 5700, 170],
                  [gp_platforms.ELEVATED, 5700, 110],
                  [gp_platforms.ELEVATED, 5700, 50],
                  [gp_platforms.ELEVATED, 5700, -10],
                  

                
                  ]
        

        
 


        # Go through the array above and add platforms
        for platform in level:
            block = gp_platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        
            
        
        # Add a custom moving platform
        block1 = gp_platforms.MovingPlatform(gp_platforms.MOVING_PLATFORM)
        block1.rect.x = 2300
        block1.rect.y = 250
        block1.boundary_top = block1.rect.y
        block1.boundary_bottom = block1.rect.y + 250
        block1.change_y = 2
        block1.player = self.player
        block1.level = self
        
        block2 = gp_platforms.MovingPlatform(gp_platforms.MOVING_PLATFORM)
        block2.rect.x = 2320
        block2.rect.y = 250
        block2.boundary_top = block2.rect.y
        block2.boundary_bottom = block2.rect.y + 250
        block2.change_y = 2
        block2.player = self.player
        block2.level = self
        
        block3 = gp_platforms.MovingPlatform(gp_platforms.MOVING_PLATFORM)
        block3.rect.x = 3110
        block3.rect.y = 250
        block3.boundary_top = block3.rect.y
        block3.boundary_bottom = block3.rect.y + 450
        block3.change_y = 4
        block3.player = self.player
        block3.level = self
        
        # moves left and right
        
        block4 = gp_platforms.MovingPlatform(gp_platforms.MOVING_PLATFORM)
        block4.rect.x = 3150
        block4.rect.y = 650
        block4.boundary_left = block4.rect.x
        block4.boundary_right = block4.rect.x + 1000
        block4.change_x = 2
        block4.player = self.player
        block4.level = self
        
        self.platform_list.add(block1)
        self.platform_list.add(block2)
        self.platform_list.add(block3)
        self.platform_list.add(block4)
        
        
        

        
    #store all the pre-set blue_skeletons here, list holds their location in map
        
        blue_skeletons = [ [1300, 370],
                       [1500, 370],
                       [3200, 152],
                       [3220, 152],
                       [3240, 152],
                     ]  
        
        axe_lords = [ [1300, 80],
                     ] 
        
        s_blue_skeletons = [ [2700, 170],
                            ]   
        
        s_axe_lords = [ [2900, 320],
                        [3400, 320]
                      ]
        
        frankenstein = [ [4700, 70],
                        ]
         
        # Add the first enemy type (blue skeleton)
        # loop through the blue_skeletons container and add them to the level
        
        for f in frankenstein:
            
            frank = Frankenstein()
            frank.rect.x = f[0]
            frank.rect.y = f[1]
            frank.boundary_left = f[0]
            frank.boundary_right = f[0] + 600
            frank.change_x = 4
            frank.player = self.player
            frank.level = self
            self.enemy_list.add(frank)
            
         
        for bs in blue_skeletons:
             
            blueskel = BlueSkeleton()
            blueskel.rect.x = bs[0]
            blueskel.rect.y = bs[1]
            blueskel.boundary_left = bs[0]
            blueskel.boundary_right = bs[0] + 600
            blueskel.change_x = 2
            blueskel.player = self.player
            blueskel.level = self
            self.enemy_list.add(blueskel)
        
            
        for sbs in s_blue_skeletons: # stationary blue_skeletons
            
            blueskel = BlueSkeleton()
            blueskel.direction = "L"
            blueskel.hp = 100
            blueskel.rect.x = sbs[0]
            blueskel.rect.y = sbs[1]
            blueskel.boundary_left = sbs[0]
            blueskel.boundary_right = sbs[0]
            blueskel.direction = "L"
            blueskel.change_x = 0
            blueskel.player = self.player
            blueskel.level = self
            self.enemy_list.add(blueskel)
            
        for sal in s_axe_lords: 
                         
            axel = AxeLord()
            axel.rect.x = sal[0]
            axel.rect.y = sal[1]
            axel.boundary_left = sal[0]
            axel.boundary_right = sal[0] + 50
            axel.change_x = 1
            axel.player = self.player
            axel.level = self
            self.enemy_list.add(axel)
            
               
            
        for al in axe_lords:
            
                         
            axel = AxeLord()
            axel.rect.x = al[0]
            axel.rect.y = al[1]
            axel.boundary_left = al[0]
            axel.boundary_right = al[0] + 600
            axel.change_x = 4
            axel.player = self.player
            axel.level = self
            self.enemy_list.add(axel)
           
