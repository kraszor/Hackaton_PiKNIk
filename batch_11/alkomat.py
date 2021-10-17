
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


def alkomat():
    while True:
        print("\n\nBreathalyser\n")
        print("1. Woman\n2. Man\n\n")
        sex = enter_val("sex (number)", True, 2)

        weight = enter_val("your weight (in kg)", False, 0)

        amount_of_alcohol = 0
        number_of_promille = 0
        soberity_time = 0
        while True:
            print("Specify the type and amount of alcohol consumed\n")
            print("1. Beer\n2. Wine\n3. Champagne\n4. Strong alcohol\n5. Amarena")
            alco_type = enter_val("type (number)", True, 5)

            quantity = enter_val("quantity (in millilitres)", False, 0)

            if alco_type == 1:
                percentage = 0.06

            elif alco_type == 2:
                percentage = 0.15

            elif alco_type == 3 or alco_type == 5:
                percentage = 0.12

            else:
                percentage = enter_val("precentage (in %)", False, 0)/100
                if percentage < 0:
                    percentage = 0
                elif percentage > 1:
                    percentage = 1

            print("\n1. Add another items\n2. Show result\n3. Exit")
            option = enter_val("option (number)", True, 3)

            amount_of_alcohol += quantity * percentage

            if option == 1:
                continue

            elif option == 2:
                break

            else:
                return

        if sex == 1:
            number_of_promille = (amount_of_alcohol * 0.8) / (0.6 * weight)
            soberity_time = (number_of_promille - 0.2) / 0.15

        elif sex == 2:
            number_of_promille = (amount_of_alcohol * 0.8) / (0.7 * weight)
            soberity_time = (number_of_promille - 0.2) / 0.15

        if number_of_promille < 0.2:
            print(f"\n\nCongratulations you can now drive :)")
            print(f"You have {'{:.2f}'.format(number_of_promille)} promille of alcohol in your blood")
            print("Good luck !!!\n\n")

        elif number_of_promille >= 0.2:
            print("\n\nStop !!!")
            print(f"You have {'{:.2f}'.format(number_of_promille)} promille of alcohol in your blood !!!")
            formatted_hours = int(soberity_time//1)
            formatted_minutes = round(((soberity_time % 1) * 60) // 1)

            print(f"You will be able to drive in {formatted_hours} hours {formatted_minutes} minutes\n\n")

        print("Do you want to continue?")
        print("1. Yes\n2. No")
        decision = enter_val("decision (number)", True, 2)

        if decision == 1:
            continue

        else:
            return


alkomat()

