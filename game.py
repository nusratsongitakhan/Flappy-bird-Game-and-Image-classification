################################----Fahad Molla 18-37548-1-----################################

from tkinter import *
import random
import os
# declaresion of varialbe for use
Start_FRAMERATE=40
FRAMERATE = Start_FRAMERATE
BIRD_Y = 200
PIPE_X = 550
PIPE_HOLE = 0
NOW_PAUSE = False
BEST_SCORE = 0
jump_Limit = 0
endRectangle = endBest = endScore = endGame = None
SCORE=-1
# creating tk inter object
main = Tk()
# for fix window size
main.resizable(width=False, height=False)
# giving window title
main.title("Flappy Bird")
#giving window width and length
main.geometry('550x700')
#creating canvas on the window
w = Canvas(main, width=550, height=700, background="#4e6fca", bd=0, highlightthickness=0)
w.pack()
# get the image from folder
backgroundImg = PhotoImage(file="images/b3.png")
#set the background image on canvas
background = w.create_image(0,0,image=backgroundImg)
#create bird add in a positon
birdImg = PhotoImage(file="images/bird.png")
# add bird on the canvas
bird = w.create_image(100, BIRD_Y, image=birdImg)
#creating upper pip in PIPE_X with width of 100 px  and hight to pIPE_HOLE
pipeUp = w.create_rectangle(PIPE_X, 0, PIPE_X + 100, PIPE_HOLE, fill="#63390c", outline="#74BF2E")
#creating Down pip in PIPE_X with width of 100 px  and hight to pIPE_HOLE+200
pipeDown = w.create_rectangle(PIPE_X, PIPE_HOLE + 200, PIPE_X + 100, 700, fill="#63390c", outline="#74BF2E")
# show live score on the top left corner
score_w = w.create_text(15, 45, text="0", font='Impact 60', fill='#ffffff', anchor=W)
def generatePipeHole():
    # get the global variable in here
    global PIPE_HOLE
    global SCORE
    global FRAMERATE
    #score increase by 1
    SCORE += 1
    #update the score of top left corner
    w.itemconfig(score_w, text=str(SCORE))
    # generate random random varialbe between 50 and 500 PIPE_HOLE for generating random hole position of pipe
    PIPE_HOLE = random.randint(50, 500)
    # decrease FRAMERATE variable by 1 means increase frame speed  by 1ms after every 7 score is increased
    if SCORE + 1 % 7 == 0 and SCORE != 0:
        FRAMERATE-=1
# called generatePipeHole() function to start it
generatePipeHole()



################################----NUSRAT SONGITA KHAN 18-37518-1-----################################



# move the pip in left size of the screen
def pipesMotion():
    global PIPE_X
    global PIPE_HOLE
    global NOW_PAUSE
    # move 5 pixel left every time the function is called
    PIPE_X -= 5
    # move the pipeUp using coords
    w.coords(pipeUp, PIPE_X, 0, PIPE_X + 100, PIPE_HOLE)
    # move the pipeDown using coords
    w.coords(pipeDown, PIPE_X, PIPE_HOLE + 200, PIPE_X + 100, 700)
    # if  the pipe if out of the screen from left then it will start from 550 pixel means right out side of the screen as screen with is 550
    if PIPE_X < -100:
        PIPE_X = 550
        # generatePipeHole() function is called to update live score and frame speed and to create random hole in between pipeUp and pipeDown
        generatePipeHole()
    # check the screen is pause or not by boolean variable NOW_PAUSE
    if not NOW_PAUSE:
        #if screen is not paused then call the after() function . This function callback funcion call pipesMotion after FRAMERATE ms time
        main.after(FRAMERATE, pipesMotion)
# birdUp to move the bird up when the function is called

def birdUp(event=None):
    global BIRD_Y
    global jump_Limit
    global NOW_PAUSE
    # check pause or not
    if not NOW_PAUSE:
        # decrease BIRD_Y by 20 pixel means move the bird up by  20 pixel
        BIRD_Y -= 20
        # check BIRD_Y is less or equale to zero means outof the screen or not
        if BIRD_Y <= 0:
            #if outof the screen then stay on Y axis zero position
            BIRD_Y = 0
        w.coords(bird, 100, BIRD_Y)
        #check jump_Limit is less than 5 or not
        if jump_Limit < 5:
            # increase jump_Limit by 1
            jump_Limit += 1
            # if less then 5 then call the main after callback function which call BirdUp 5 times for the condition jump_Limit < 5
            main.after(FRAMERATE, birdUp)
        # if jump_Limit < 5 not then convert jump_Limit to zero
        else:
            jump_Limit = 0
    # if the game is paused then if the birdUp function is called this will call the restartGame() function
    else:
        restartGame()


###################---------ADIT AHNAF KHAN 18-37491-1---------###################


# birdDown to move the bird Down when the function is called
def birdDown():
    global BIRD_Y
    global NOW_PAUSE
    # increase BIRD_Y by 8 every time the function is called means move down by 8 pixel.
    BIRD_Y += 8
    #BIRD_Y >= 700 because window hight is 700 so if the bird is outof the screen from dawn it will stay on that posion
    if BIRD_Y >= 700:
        BIRD_Y = 700
        # by NOW_PAUSE = True the game is paused because the game is over when bird touch bottom screen
        NOW_PAUSE = True
        # As game is over so engGameScreen() function is called
        engGameScreen()
    #To update the bird using coords() function
    w.coords(bird, 100, BIRD_Y)
    # if the game is not paused then call  the after callback function which will call birdDown
    if not NOW_PAUSE:
        main.after(FRAMERATE,birdDown)

# when the game is over when bird is crashed on pipes or down
def engGameScreen():
    global endRectangle
    global endScore
    global endBest
    global endGame
    #Create Rectangle for the whole screen so to show end screen
    endRectangle = w.create_rectangle(0, 0, 550, 700, fill='#4EC0CA')
    # show final score
    endScore = w.create_text(100, 400, text="Your score: " + str(SCORE), font='Impact 50', fill='#ffffff', anchor=W)
    #show GAME OVER text
    endGame = w.create_text(130, 300, text="GAME OVER ", font='Impact 50', fill='#ffffff', anchor=W)


##################--------------------Md. Abu Zehad Foysal 18-37514-1 ---------------##################


# check the collision of bird and pipes
def detectCollision():
    global NOW_PAUSE
    global BEST_SCORE
    #check x axis and y axis of pipes and birds if the cross each other
    if (PIPE_X < 130 and PIPE_X + 100 >= 55) and (BIRD_Y < PIPE_HOLE+45 or BIRD_Y > PIPE_HOLE + 175):
        # if cross each other then make NOW_PAUSE = True to end the game and call engGameScreen() function to show end screen
        NOW_PAUSE = True
        engGameScreen()
        # if the game is not paused then after callback funcion call detectCollision() again and again
    if not NOW_PAUSE:
        main.after(FRAMERATE, detectCollision)


# for the start the game again
def restartGame():
    global PIPE_X
    global BIRD_Y
    global SCORE
    global NOW_PAUSE
    global FRAMERATE
    global Start_FRAMERATE
    # bird start position
    BIRD_Y = 200
    # pipe start position
    PIPE_X = 550
    SCORE = -1
    # FRAMERATE start frame speed
    FRAMERATE = Start_FRAMERATE
    # as game restarted so make NOW_PAUSE = False
    NOW_PAUSE = False
    # delete end score object as the game is restarted it is no longer needed
    w.delete(endScore)
    # delete endGame object as the game is restarted it is no longer needed
    w.delete(endGame)
    # delete endRectangle object as the game is restarted it is no longer needed and clear the screen to see the game
    w.delete(endRectangle)
    # generatePipeHole() function is called to update live score and frame speed and to create random hole in between pipeUp and pipeDown
    generatePipeHole()
    #  to start the call of birdDown() pipesMotion() detectCollision() functions
    main.after(FRAMERATE, birdDown)
    main.after(FRAMERATE, pipesMotion)
    main.after(FRAMERATE, detectCollision)

# to start the call of birdDown function
main.after(FRAMERATE, birdDown)
# binded with space buttion to when space is called then BirdUp is called
main.bind("<space>", birdUp)
main.after(FRAMERATE, pipesMotion)
main.after(FRAMERATE, detectCollision)
# this mainloop() function listen all the evens in the code when the window is on
main.mainloop()