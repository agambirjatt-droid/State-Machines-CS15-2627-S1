state = "coding"

while True:

    if state == "coding":
        print("You are coding!")
        feeling = input("How are you feeling? (tired/hungry/happy) ")

        if feeling == "tired":
            state = "sleeping"
        elif feeling == "hungry":
            state = "eating"
        elif feeling == "happy":
            state = "coding"
        else:
            print("That's not a valid feeling, staying in the same state.")

    elif state == "eating":
        print("You are eating!")
        feeling = input("How are you feeling? (hungry/full/tired) ")

        if feeling == "hungry":
            state = "eating"
        elif feeling == "full":
            state = "coding"
        elif feeling == "tired":
            state = "sleeping"
        else:
            print("That's not a valid feeling, staying in the same state.")

    elif state == "sleeping":
        print("You are sleeping!")
        feeling = input("How are you feeling? (tired/awake/hungry) ")

        if feeling == "tired":
            state = "sleeping"
        elif feeling == "awake":
            state = "coding"
        elif feeling == "hungry":
            state = "eating"
        else:
            print("That's not a valid feeling, staying in the same state.")