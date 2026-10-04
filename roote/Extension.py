state = "studying"

while True:
    if state == 'studying':
        print ("You are studying right now!")
        feeling = input("how are you feeling? (exhausted, hungry, bored)")

        if feeling == "exhausted":
            state = "sleeping"
        elif feeling == "hungry":
            state = "eating"
        elif feeling == "bored":
            state = "chilling"
        else:
            print(" That's not one of the feeling listed, staying in current state.")

    elif state == "sleeping":
        print (" you are dozing off and are asleep now")
        feeling = input("how are you feeling (awake, hungry)" )

        if feeling == "awake":
            state = "studying"
        elif feeling == "hungry":
            state = "eating"
        else:
            print("That's not one of the feeling listed, staying in current state")

    elif state == "eating":
        print (" You are eating food now")
        feeling = input ("how are you feeling (full, hungry)")

        if feeling == "full":
            state = "studying"
        elif feeling == "hungry":
            state = "eating"
        else:
            print("That's not one of the feeling listed, staying in current state")

    elif state == "chilling":
        print ("You are relaxing/chilling now")
        feeling = input ("how are you feeling (bored, exhausted)" )

        if feeling == "bored":
            state = "chilling"
        elif feeling == "exhausted":
            state = "sleeping"
        else:
            print("That's not one of the feeling listed, staying in current state")

