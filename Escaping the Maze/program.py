def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
        
while not at_goal():
    if right_is_clear():
        turn_right()
        if not wall_in_front():
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if not wall_in_front():
            move()
    



    

