import random
import time
from turtle import Turtle,Screen
is_race_on=False
screen=Screen()
screen.setup(900,600)
screen.bgcolor("black")
screen.title("Turtle Race")
screen.tracer(0)

#background
particles=[]
shapes=["circle","square","triangle","classic"]
def create_particles(n=200):
    for _ in range(n):
        p=Turtle()
        p.shape(random.choice(shapes))
        p.color("white")
        p.penup()
        p.shapesize(0.15)
        p.goto(random.randint(-440,440),random.randint(-290,290))
        particles.append(p)

def animate_particles():
    for p in particles:
        p.sety(p.ycor()-1)
        if p.ycor()<-300:
            p.goto(random.randint(-440,440),290)

    screen.update()
    screen.ontimer(animate_particles, 30)

create_particles()
animate_particles()

#intro
intro_turtle=Turtle()
intro_turtle.hideturtle()
intro_turtle.color("#00FFAA")
intro_turtle.penup()
intro_turtle.goto(0,150)
ascii_art = r"""
████████╗██╗   ██╗████████╗████████╗██╗███████╗
╚══██╔══╝██║   ██║╚══██╔══╝╚══██╔══╝██║██╔════╝
   ██║   ██║   ██║   ██║      ██║   ██║█████╗  
   ██║   ██║   ██║   ██║      ██║   ██║██╔══╝  
   ██║   ╚██████╔╝   ██║      ██║   ██║███████╗
   ╚═╝    ╚═════╝    ╚═╝      ╚═╝   ╚═╝╚══════╝
"""
intro_turtle.write(ascii_art,align="center",font=("Courier",14,"bold"))
screen.textinput("Start Game","Press ENTER  to begin the game")

#start button apply
start_button=Turtle()
start_button.hideturtle()
start_button.color("white")
start_button.penup()
start_button.goto(0,-10)
start_button.write("CLICK ANYWHERE TO START THE RACE",align="center",font=("Arial",16,"bold"))
#wait for click
clicked=False
def start_game(x,y):
    global clicked
    clicked=True
screen.onclick(start_game)

while not clicked:
    screen.update()



#Turtle Race game starts

colors = [
    "Red",  # Red-Orange
    "Green",  # Lime Green
    "Blue",  # Bright Blue
    "Yellow",  # Yellow
    "Purple",  # Purple
    "Teal",  # Teal
]
all_turtles=[]
winner=None
y_positions=[-70,-40,-10,20,50,80]

def start_game(x,y):
    screen.onclick(None)
    intro_turtle.clear()
    start_button.clear()
    #screen.update()
    global user_bet
    user_bet=screen.textinput("Welcome to the turtle zoo","Which turtle will win the race?enter the colour : ")
    if user_bet:
        user_bet.strip().lower()
    else:
        user_bet=""
    #create turtles
    for i in range(0,6):
        t=Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(-400,y_positions[i])
        all_turtles.append(t)
    start_race_step()

def start_race_step():
    global race_running,winner

    race_running=True

    for t in all_turtles:
        step=random.randint(1,12)
        t.forward(step)
        if t.xcor()>380 and winner is None:
            winner=t.pencolor()
    screen.update()

    if winner is None:
        screen.ontimer(start_race_step,50)
    else:
        race_running=False
        end_race()

def end_race():
    for t in all_turtles:
        t.hideturtle()
    screen.update()

    announcer=Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.color("white")
    announcer.goto(0,0)
    if user_bet and winner.lower()==user_bet.lower():
        announcer.write(f"🎉YOU WON! {winner.upper()} turtle wins!",align="center",font=("Courier",28,"bold"))
    else:
        announcer.write(f"🎉YOU LOST! {winner.upper()} turtle wins!", align="center", font=("Courier", 28, "bold"))
    screen.update()

screen.onclick(start_game)
screen.mainloop()