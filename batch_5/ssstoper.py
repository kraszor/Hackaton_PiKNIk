import time
import winsound
import os


# wersja ogólna ale z nowym oknem
# os.system("fizzbuzz.mp3")

# wersja na windowsa ale działa idealnie
# winsound.PlaySound("USSR_beep.wav", winsound.SND_FILENAME)
# winsound.PlaySound("USSR_beep_bass.wav", winsound.SND_FILENAME)


def enter_val(text):
    while True:
        try:
            value = int(input(f"Please enter {text}: "))
            if text == "option":
                if value in (1, 2):
                    break
                else:
                    print(f"Number out of range")
            else:
                break
        except:
            print(f"Incorrect value, {text} must be int")
    return value


def timer():
    print("\nTIMER")
    print("Enter values \n")

    hours = enter_val("hours")
    minutes = enter_val("minutes")
    seconds = enter_val("seconds")

    initial_time = hours * 3600 + minutes * 60 + seconds

    print(f"\n\nTime: {hours}: {minutes}: {seconds}\n\n")
    print("Choose option\n")
    print("1. Start\n2. Exit")
    option = enter_val("option")

    current_time = initial_time
    if option == 1:
        # start_time = time.time()
        for i in range(1, initial_time+1):
            print(f"Timer")
            current_time = initial_time - i
            time.sleep(1)
            print(f"Time: {current_time // 3600}: {(current_time % 3600) // 60}: {((current_time % 3600) % 60)}\n\n")
        print("End of time")


        # while current_time > 0:
        #     print(f"Timer")
        #     time.sleep(1)
        #     current_time = round(initial_time - (time.time() - start_time))
        #     print(f"Hours: {current_time // 3600}, Minutes: {(current_time % 3600) // 60}, Seconds: {((current_time % 3600) % 60)}\n\n")
        # print("End of time")
        # # winsound.PlaySound("USSR_beep_bass.wav", winsound.SND_FILENAME)

    elif option == 2:
        return


def stopwatch():
    print("\nStopwatch")

    print("Choose option\n")
    print("1. Start\n2. Exit")
    print("\nTo stop press CTRL+C")
    option = enter_val("option")
    current_time = 0
    if option == 1:
        start_time = time.time()
        pause_time = 0
        while True:
            try:
                current_time = time.time() - start_time
                current_time = current_time - pause_time
                pause_time = 0
                formated_hours = '{:.0f}'.format(int('{:.0f}'.format(current_time)) // 3600)
                formated_minutes = '{:.0f}'.format((int('{:.0f}'.format(current_time)) % 3600) // 60)
                formated_seconds = '{:.0f}'.format(((int('{:.0f}'.format(current_time)) % 3600) % 60))
                formated_mseconds = str('{:.2f}'.format(current_time))[-2:]

            except KeyboardInterrupt:
                start_pause_time = time.time()
                while True:
                    print(chr(27) + "[2J")
                    print('Pause\n')
                    print(f"Time: {formated_hours}:{formated_minutes}:{formated_seconds}:{formated_mseconds}\n\n")
                    print("1. To exit write e and press ENTER\n2. To continue press only ENTER")

                    decision = input("Decision: ")
                    if decision == "e":
                        print(f"\n\nTotal Time: {formated_hours}:{formated_minutes}:{formated_seconds}:{formated_mseconds}\n\n")
                        return
                    pause_time = time.time() - start_pause_time
                    break

    elif option == 2:
        return

    pass


timer()
# stopwatch()