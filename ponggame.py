import turtle
turtle.hideturtle()

score_a=0
score_b=0
#screen
s = turtle.getscreen()   
s.setup(1500,1000)
s.bgcolor("blue")
s.title("pong game")
s.tracer(0)


#left rectangle box
lb=turtle.Turtle()
lb.shape("square")
lb.color("white")
lb.penup()
lb.speed(0)
lb.shapesize(5,1)
lb.goto(-735,0)

#right rectangle box
rb=turtle.Turtle()
rb.shape("square")
rb.color("white")
rb.penup()
rb.speed(0)
rb.shapesize(5,1)
rb.goto(734,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(2,2)
ball.color("white")
ball.penup()
ball.dx=1
ball.dy=1



#box movement
def lb_up():
    lb.sety(lb.ycor()+20)

def lb_down():
    lb.sety(lb.ycor()-20)

def rb_up():
    rb.sety(rb.ycor()+20)

def rb_down():
    rb.sety(rb.ycor()-20)

#listen key
s.listen()
s.onkeypress(lb_up,'w')
s.onkeypress(lb_down,'s')
s.onkeypress(rb_up,'Up')
s.onkeypress(rb_down,'Down')

 #score
sc = turtle.Turtle()
sc.speed(0)
sc.color("white")
sc.penup()
sc.goto(0,460)
sc.hideturtle()
sc.clear()
sc.write("player A: {}  player B: {} ".format(score_a,score_b), align="center",font="Ariel")

#winner
win=turtle.Turtle()
win.speed(0)
win.hideturtle()
win.color("white")
win.penup()
win.goto(0,100)




while True:
    s.update()
  

  
     #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
 
    #top wall
    if ball.ycor() > 485:
        ball.sety(485)
        ball.dy *= -1

    #bottom wall
    if ball.ycor() < -480:
        ball.sety(-480)
        ball.dy *= -1

    #right wall
    if ball.xcor() > 735:
        ball.setx(735)
        ball.dx *= -1
        
        score_a +=1
        sc.clear()
        sc.write("player A: {}  player B: {} ".format(score_a,score_b), align="center",font="Ariel")
        

     #left wall
    if ball.xcor() < -740:
        ball.setx(-740)
        ball.dx *= -1

        score_b +=1
        sc.clear()
        sc.write("player A: {}  player B: {} ".format(score_a,score_b), align="center",font="Ariel")


    #collision with box
    if ball.xcor() >710 and rb.ycor()-50 <ball.ycor() < rb.ycor()+50:
        ball.setx(710)
        ball.dx *= -1

    if ball.xcor() <-710 and lb.ycor()-50 <ball.ycor() < lb.ycor()+50:
        ball.setx(-710)
        ball.dx *= -1

     #winner
    if score_a > 2:
        win.write(" player A is win", align="center",font="Ariel")
        ball.setpos(0,0)

    if score_b >2:
        win.write("player B is win", align="center",font="Ariel")
        ball.setpos(0,0)    

   
        

 




    
    
