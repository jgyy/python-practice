"""
Alarm Clock - A simple clock where it plays a sound after
X number of minutes/seconds or at a particular time.
"""
import time
import os


def sound():
    """Number of repeats, beats and how long between beeps"""
    for _ in range(2):  # Number of repeats

        for _ in range(9):  # Number of beeps
            print("Message Beep")

        time.sleep(2)  # How long between beeps


def alarm(n_sec):
    """:param n_sec: Waits 'n' seconds before playing sound"""
    print()
    print("Wait time:", n_sec, "seconds.")
    time.sleep(n_sec)

    sound()


def input_destinations(user_input):
    """:param user_input: input from the terminal"""
    if user_input == '1':

        user_input = int(input("Enter the desired hours: "))

        wait_time = (user_input * 60) * 60
        alarm(wait_time)

    elif user_input == '2':

        user_input = int(input("Enter the desired minutes: "))

        wait_time = user_input * 60
        alarm(wait_time)

    elif user_input == '3':

        user_input = int(input("Enter the desired seconds: "))

        wait_time = user_input
        alarm(wait_time)

    elif user_input == '4':

        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))

        wait_time = ((hours * 60) * 60) + (minutes * 60) + seconds
        print(wait_time)
        alarm(wait_time)

    else:

        try:
            os.system('cls')  # If OS is Windows
            main()

        except IOError:
            os.system('clear')  # If OS is Linux or Mac
            main()


def main():
    """Runs the main script"""
    print("What unit of time do you want to wait?\n "
          "(1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
    main_input = input(": ")

    input_destinations(main_input)


if __name__ == "__main__":
    main()
