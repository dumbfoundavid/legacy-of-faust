'''
Created on Apr 29, 2015

@author: David Nickolo Perez
'''
from game_project.gp_levels import Level

"""

GAME PROJECT FOR CS332L, SPRING 2015
TAUGHT BY: KEENAN KNAUR

Main module for platform scroller game project.

SPRITES, MUSIC, SOUND EFFECTS TAKEN FROM:

castlevaniadungeon.net
opengameart.org
freesound.org
soundfxcenter.com

ALL RIGHTS GO TO THEIR RESPECTIVE CREATORS

GAME PROJECT CREATED FOR EDUCATIONAL PURPOSES

"""

import pygame
from pygame.locals import *

import game_project.gp_constants as constants
import game_project.gp_levels as levels

from game_project.gp_player import Player

from game_project.gp_weapons import Knife

# Set the height and width of the screen
size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)



def draw_text(SCREEN, text, x, y):
    WHITE = pygame.Color(255, 255, 255)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    rendered = font.render(text, True, WHITE)
    SCREEN.blit(rendered, [x, y])
    



def health_bars(player_health):
    """Tracks the health of the player"""
    
    
    if player_health > 75:
        player_health_color = constants.GREEN
    
    elif player_health > 50:
        player_health_color = constants.YELLOW
    
    else:
        player_health_color = constants.RED
        
    if player_health > 0:
        
        pygame.draw.rect(screen, player_health_color, (40, 5, player_health, 15), 0)
        

    
       

def main():
    """ Main Program """
    pygame.mixer.pre_init(22050, 16, 2, 4096) # prevents sound effect delay
    
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Legacy of Faust")

    # Create the player
    player = Player()
    
    
    
    # List of each knife
    knife_list = pygame.sprite.Group()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player)) # append the player to the level
    
 

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    
    # initial position of the player
    player.rect.x = 400
    player.rect.y = 300
    #player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    

   
    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Load sound fx
    #step_sound = pygame.mixer.Sound('footstep.ogg')
    knife_sound = pygame.mixer.Sound('knife_throw.ogg')
 
    

    #Load background music
    pygame.mixer.music.load('stage01.ogg')
    pygame.mixer.music.set_endevent(USEREVENT)
    pygame.mixer.music.play(-1) # -1 means plays in a loop
  
    
    game_over = False
    
    # check if we killed all the monsters in the game
    


    # -------- Main Program Loop -----------
    while not done:
        
       
        

        enemy_counter = len(current_level.enemy_list)
        
        # print("driver", str(enemy_counter))
        
        # if the user falls off the platforms, he dies
        
        if player.rect.y == constants.SCREEN_HEIGHT - player.rect.height:
            game_over = True
        
        if enemy_counter == 0:
            game_over = True
        
        
        
        

        # handle the game over screen
        while game_over:
        

            
            # load a custom game_over.png
            
            """NOTE: To play again after GAME OVER screen, press 'r' 
                     to quit press 'q'
            """

            game_over_image = pygame.image.load("game_over.png").convert()
            imagerect = game_over_image.get_rect()
            

            # Set the color that should be transparent
            
            game_over_image.set_colorkey(pygame.Color(0, 0, 0))
            
            screen.blit(game_over_image, imagerect)
            
            pygame.display.flip() # update the screen and show the game over message
            
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
                        game_over = False
                        
                    if event.key == pygame.K_r: # RESET ALL VARIABLES HERE
                        #main()
                        
                        # Create the player
                        player = Player()
                        
                        
                        
                        # List of each knife
                        knife_list = pygame.sprite.Group()
                    
                        # Create all the levels
                        level_list = []
                        level_list.append(levels.Level_01(player)) # append the player to the level
                        
                     
                    
                        # Set the current level
                        current_level_no = 0
                        current_level = level_list[current_level_no]
                    
                        active_sprite_list = pygame.sprite.Group()
                        player.level = current_level
                        
                        # initial position of the player
                        player.rect.x = 400
                        player.rect.y = 300
                        #player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
                        active_sprite_list.add(player)
                        
                    
                       
                        #Loop until the user clicks the close button.
                        done = False
                    
                        # Used to manage how fast the screen updates
                        clock = pygame.time.Clock()
                        
                        # Load sound fx
                        #step_sound = pygame.mixer.Sound('footstep.ogg')
                        knife_sound = pygame.mixer.Sound('knife_throw.ogg')
                     
                        
                    
                        #Load background music
                        pygame.mixer.music.load('stage01.ogg')
                        pygame.mixer.music.set_endevent(USEREVENT)
                        pygame.mixer.music.play(-1) # -1 means plays in a loop
                      
                        
                        game_over = False
    
            
        
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    
                    player.go_left()
                    
                if event.key == pygame.K_RIGHT:
                   
                    player.go_right()
                    
                if event.key == pygame.K_a:
                    
                    knife_sound.play()
                    
                    player.attack()
                    
                    knife = Knife()
                    
                    # add the knife to the sprite lists
                    
                    active_sprite_list.add(knife)
                    knife_list.add(knife)
                    
                            

        
                    if player.direction == "RA" or player.direction == "RJ":
                        knife.knife_dir = "R"
                        print(knife.knife_dir)
                        
                    elif player.direction == "LA" or player.direction == "LJ":
                        knife.knife_dir = "L"

                    knife.level = current_level # assign the knife to the current level
                    
                    # Set the knife so it is where the player is
                    
                    if knife.knife_dir == "R":
                    
                        knife.rect.x = player.rect.x + 10
                        knife.rect.y = player.rect.y - 15
                        
                    elif knife.knife_dir == "L":
                        knife.rect.x = player.rect.x - 80
                        knife.rect.y = player.rect.y - 15
                               
                

                            

                if event.key == pygame.K_UP:
                    player.jump()
                   
                    
                    
                if event.key == pygame.K_SPACE:
                    player.sprint()
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                   
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                    
                    
                if event.key == pygame.K_SPACE:
                    player.stop()
               
                    
                if event.key == pygame.K_UP:
                    player.reset_animation()
           
                    
                if event.key == pygame.K_a:
                    
                    player.reset_animation()
                    
        # if player HP reaches 0 or less, game over            
            
        if player.life <= 0:
            game_over = True
            
    
      
                    
        # Remove the knife once it kills something
                    
        for weapon in knife_list:
            if weapon.knife_collide == True:
                              
                knife_list.remove(weapon)
                             
                active_sprite_list.remove(weapon)
                              
                               
                print("knife has killed")

        # remove knife if it goes off-screen (left or right side)
                
        for weapon in knife_list:
            
                if weapon.rect.x >= 700 or weapon.rect.x <= 20:
                    knife_list.remove(weapon)
                    active_sprite_list.remove(weapon)
                    

                    
        if event.type == USEREVENT:
            pygame.mixer.music.play()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)



        # set up HUD over here
    
        draw_text(screen, 'HP', 0, 0)
        
        draw_text(screen, "ENEMY COUNT: " + str(enemy_counter), 0, 25)
            
        # show the health bars
        
        player_health = player.life
        
        health_bars(player_health)
        


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()

