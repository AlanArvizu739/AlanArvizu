#alan arvizu

bball_weight = 5.25

ball_circumference = 9.20

ball_color = "white"

stitching_color = "red"

ball_shape = "sphere"

ball_thrown = True

max_capacity = 18.0

current_capacity = 16.0


def throw_bball(in_hand):
    if in_hand:
        print("you can throw ball")
    else:
        print("you can't throw ball")

def catch_bball(ball_thrown):
    if ball_thrown:
        print("the ball has been thrown, catch it if you can")
    else:
       print("you cant catch a ball that has not been thrown")

def fill_ball(air_amount, current_capacity):
    if current_capacity >= 18.0:
        print("You can't put anymore air in.")

    else:
        current_capacity = current_capacity + air_amount
        return current_capacity
                  
