state = "studying"

while True:

    if state == "studying":
        print("You are studying!")
        feeling = input("How are you feeling? (tired/hungry/bored) ")

        if feeling == "tired":
            state = "sleeping"
        elif feeling == "hungry":
            state = "eating"
        elif feeling == "bored":
            state = "relaxing"
        else:
            print("That's not a correct feeling, staying in the same state.")

    elif state == "eating":
        print("You are eating!")
        feeling = input("How are you feeling? (full/hungry) ")

        if feeling == "full":
            state = "studying"
        elif feeling == "hungry":
            state = "eating"
        else:
            print("That's not a correct feeling, staying in the same state.")

    elif state == "sleeping":
        print("You are sleeping!")
        feeling = input("How are you feeling? (awake/tired) ")

        if feeling == "awake":
            state = "studying"
        elif feeling == "tired":
            state = "sleeping"
        else:
            print("That's not a correct feeling, staying in the same state.")

    elif state == "relaxing":
        print("You are relaxing!")
        feeling = input("How are you feeling? (bored/tired) ")

        if feeling == "bored":
            state = "studying"
        elif feeling == "tired":
            state = "sleeping"
        else:
            print("That's not a valid feeling, staying in the same state.")