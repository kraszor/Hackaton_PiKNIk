import time
import winsound
import os


def enter_val(text, is_option, value_range):
    while True:
        try:
            value = int(input(f"Please enter {text}: "))
            if is_option:
                if value in range(1, value_range+1):
                    break
                else:
                    print(f"Number out of range")
            else:
                break
        except:
            print(f"Incorrect value, {text} must be int")
    return value


def timer():
    print("TIMER")
    print("Enter values \n")

    hours = enter_val("hours", False, 0)
    minutes = enter_val("minutes", False, 0)
    seconds = enter_val("seconds", False, 0)

    initial_time = hours * 3600 + minutes * 60 + seconds

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Choose option\n")
    print("1. Start\n2. Exit")
    option = enter_val("option", True, 2)

    if option == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"TIME: {hours}: {minutes}: {seconds}\n\n")
        for i in range(1, initial_time+1):
            current_time = initial_time - i
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"TIME: {current_time // 3600}: {(current_time % 3600) // 60}: {((current_time % 3600) % 60)}\n\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("End of time")
        winsound.PlaySound("song.wav", winsound.SND_FILENAME)

    elif option == 2:
        return


def stopwatch():
    print("Stopwatch\n")
    print("Choose option\n")
    print("1. Start\n2. Exit")
    print("\nTo stop press CTRL+C")
    option = enter_val("option", True, 2)
    if option == 1:
        start_time = time.time()
        pause_time = 0
        while True:
            try:
                time.sleep(0.02)
                current_time = time.time() - start_time - pause_time
                print(current_time)
                formated_hours = '{:.0f}'.format(int('{:.0f}'.format(current_time)) // 3600)
                formated_minutes = '{:.0f}'.format((int('{:.0f}'.format(current_time)) % 3600) // 60)
                formated_seconds = '{:.0f}'.format(((int('{:.0f}'.format(current_time)) % 3600) % 60))
                formated_mseconds = str('{:.2f}'.format(current_time))[-2:]
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"TIME: {formated_hours}:{formated_minutes}:{formated_seconds}:{formated_mseconds}\n\n")

            except KeyboardInterrupt:
                start_pause_time = time.time()
                while True:
                    print('Pause\n')
                    print(f"TIME: {formated_hours}:{formated_minutes}:{formated_seconds}:{formated_mseconds}\n\n")
                    print("1. To exit write e and press ENTER\n2. To continue press only ENTER")

                    decision = input("Decision: ")
                    if decision == "e":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Total Time: {formated_hours}:{formated_minutes}:{formated_seconds}:{formated_mseconds}\n\n")
                        return
                    pause_time += time.time() - start_pause_time
                    break

    elif option == 2:
        return

    pass


def clock():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Select type of clock\n")
        print("1. Timer\n2. Stopwatch\n")
        option = enter_val("type (number)", True, 2)
        os.system('cls' if os.name == 'nt' else 'clear')

        if option == 1:
            timer()
        else:
            stopwatch()

        print("Do you want to continue?")
        print("1. Yes\n2. No")
        decision = enter_val("decision (number)", True, 2)

        if decision == 1:
            continue

        elif decision == 2:
            return


clock()