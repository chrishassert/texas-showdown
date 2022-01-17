'''
Gamebox.py made by Luther Tychonievich

Game Made By: Christopher Hassert (ch8jd) and Mattias Pinto (mep3dr)

Game Name: Texas Showdown

[Two Players Simultaneously] Our game is a 1v1 shooter between two players on a 2D space.
[Music/Sound Effects] There will be western music and shooting sound effects
The players can move in all 4 directions and shoot bullets at eachother.
Player1 has "WASD" movement and Player2 has arrow key movement.
Player1 shoots using the spacebar and Player2 shoots using the forward slash key.
[Health Meter] Each player has 3 lives and can only shoot when they don't have one of their bullets on screen
If the players touch the left or right walls, they lose a life
[Timer] There is a timer at the top, at 5 seconds the walls will start moving towards eachother.

'''

import pygame
import gamebox

# URLs of Images
pillarurl = "https://i.imgur.com/6s2m5OZ.png"
player1url = "https://i.imgur.com/6xG9lBs.png"
player2url = "https://i.imgur.com/Pny7Fzg.png"
bulleturl = "https://i.imgur.com/xfxSMep.png"

# Variable Definitions
game_on = False
splash_screen = True
score = 0
ticks = 0
player1life = 3
player2life = 3
bullet1collide = False
bullet2collide = False
camera = gamebox.Camera(1200, 600)

# Creating Sprites
player1 = gamebox.from_image(200,300, player1url)
player1.scale_by(0.4)
player2 = gamebox.from_image(1000,300, player2url)
player2.scale_by(0.4)
bullet1 = gamebox.from_color(-300,200,'red',40,5)
bullet2 = gamebox.from_color(-300,500,'red',40,5)
player1end = gamebox.from_text(camera.x, camera.y, "Player2 Won!", "Times New Roman", 50,'Red', bold=True)
player2end = gamebox.from_text(camera.x, camera.y, "Player1 Won!", "Times New Roman", 50, 'Red', bold=True)
leftwall = gamebox.from_image(0,0, pillarurl)
rightwall = gamebox.from_image(1200,0, pillarurl)
topwall = gamebox.from_image(600, 0, pillarurl)
topwall.rotate(90)
botwall = gamebox.from_image(600, 600, pillarurl)
botwall.rotate(90)

# Loading Music and Sound Files
try:
    music = gamebox.load_sound("Texas_Showdown_Music.ogg")
    shot = gamebox.load_sound("Gun Sound.ogg")
    musicplayer = music.play(-1)
except ValueError:
    print("Couldn't find sound file. Is it in the same directory as game.py?")


# Splash Screen Function
def splash(keys):
    global splash_screen

    camera.clear('Red')

    # Splash Screen Sprites
    logo = gamebox.from_image(camera.x, camera.y, "https://i.imgur.com/q1u5NY8.png")
    directions = gamebox.from_text(camera.x, camera.y, "Press space to play the game!", "Times New Roman", 30, 'white', bold=True)
    directions.top = logo.bottom
    directionsplayer1 = gamebox.from_image(150,300, 'https://i.imgur.com/oU7fAvQ.png')
    directionsplayer1.scale_by(0.4)
    directionsplayer2 = gamebox.from_image(1050,300, 'https://i.imgur.com/Ww59MAV.png')
    directionsplayer2.scale_by(0.4)
    programmers = gamebox.from_text(600,25,'Game made by Christopher Hassert (ch8jd) and Mattias Pinto (mep3dr)','Times New Roman',30,'White',bold=True)

    # Drawing Sprites
    camera.draw(logo)
    camera.draw(directions)
    camera.draw(directionsplayer1)
    camera.draw(directionsplayer2)
    camera.draw(programmers)

    if pygame.K_SPACE in keys:
        splash_screen = False

    camera.display()

def tick(keys):
    global ticks
    global score
    global game_on
    global bullet1collide
    global bullet2collide
    global player1life
    global player2life
    global shot

    ticks += 1

    if splash_screen:
        splash(keys)
        return
    camera.clear('White')

    # Start Game Mechanism
    if pygame.K_SPACE in keys and not game_on:
        game_on = True
        ticks = 0

    if game_on:
        # Status Sprites
        time = gamebox.from_text(600, 25, str(ticks // 30), 'Times New Roman', 40, 'Red', bold=True)
        life1 = gamebox.from_text(300, 25,"Player1 Lives: "+str(player1life),'Times New Roman', 40, 'Red', bold=True)
        life2 = gamebox.from_text(900, 25, "Player2 Lives: "+str(player2life),'Times New Roman', 40, 'Red', bold=True)

        # Drawing Players and Walls
        camera.draw(player1)
        camera.draw(player2)
        camera.draw(leftwall)
        camera.draw(rightwall)
        camera.draw(topwall)
        camera.draw(botwall)
        camera.draw(bullet1)
        camera.draw(bullet2)

        # Left and Right Walls Move at 5 Seconds
        if (ticks//30) > 5:
            leftwall.move(0.2,0)
            rightwall.move(-0.2,0)

        # Player-Player Collision
        if player1.touches(player2):
            player1.move(-20,0)
            player2.move(20,0)

        # Bullet Collisions
        if bullet1.touches(rightwall):
            bullet1.speedx = 0
            bullet1.move(-2000, 200)
            bullet1collide = False
        if bullet2.touches(leftwall):
            bullet2.speedx = 0
            bullet2.move(-2000,200)
            bullet2collide = False
        if bullet1.touches(player2):
            bullet1.speedx = 0
            bullet1.move(2000,200)
            player2life -= 1
            bullet1collide = False
        if bullet2.touches(player1):
            bullet2.speedx = 0
            bullet2.move(2000,200)
            player1life -= 1
            bullet2collide = False

        # Wall Collisions
        if player1.touches(leftwall):
            player1.move(100,0)
            player1life -= 1
        if player1.touches(rightwall):
            player1.move(-100,0)
            player1life -= 1
        if player2.touches(leftwall):
            player1.move(100,0)
            player2life -= 1
        if player2.touches(rightwall):
            player2.move(-100,0)
            player2life -= 1
        if player1.touches(topwall):
            player1.move_to_stop_overlapping(topwall, 0, 0)
        if player1.touches(botwall):
            player1.move_to_stop_overlapping(botwall, 0, 0)
        if player2.touches(topwall):
            player2.move_to_stop_overlapping(topwall, 0, 0)
        if player2.touches(botwall):
            player2.move_to_stop_overlapping(botwall, 0, 0)

        # Player 1 Shooting Mechanism
        if pygame.K_SPACE in keys and not bullet1collide and (ticks > 30):
            musicplayer1 = shot.play()
            bullet1.center = player1.center
            bullet1.y = (player1.y - 28)
            bullet1.speedx = 60
            bullet1.speedy = 0
            bullet1collide = True
        bullet1.move_speed()

        # Player 2 Shooting Mechanism
        if pygame.K_SLASH in keys and not bullet2collide and (ticks > 30):
            musicplayer1 = shot.play()
            bullet2.center = player2.center
            bullet2.y = (player2.y - 28)
            bullet2.speedx = -75
            bullet2.speedy = 0
            bullet2collide = True
        bullet2.move_speed()

        # Player 1 Movement
        if pygame.K_w in keys:
            player1.move(0,-10)
        if pygame.K_s in keys:
            player1.move(0,10)
        if pygame.K_a in keys:
            player1.move(-10,0)
        if pygame.K_d in keys:
            player1.move(10,0)

        # Player 2 Movement
        if pygame.K_UP in keys:
            player2.move(0,-10)
        if pygame.K_DOWN in keys:
            player2.move(0,10)
        if pygame.K_LEFT in keys:
            player2.move(-10,0)
        if pygame.K_RIGHT in keys:
            player2.move(10,0)

        # Tells the Walls to Move
        leftwall.move_speed()
        rightwall.move_speed()

        # Draws Timer
        camera.draw(time)

        # End Game Conditions
        if player1life == 0:
            life1 = gamebox.from_text(300, 25, "Player1 Lives: 0", 'Times New Roman', 40, 'Red',bold=True)
            camera.draw(player1end)
            gamebox.pause()
        elif player2life == 0:
            life2 = gamebox.from_text(900, 25, "Player2 Lives: 0", 'Times New Roman', 40, 'Red', bold=True)
            camera.draw(player2end)
            gamebox.pause()

        # Draws Life Status'
        camera.draw(life1)
        camera.draw(life2)

    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
