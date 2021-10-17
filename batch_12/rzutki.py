def createLeaderboard(participants):
    participants_info = []
    for participant in participants:
        splitted = participant.split(" ")
        suma = 0
        for number in splitted[1:]:
            suma += int(number)
        participants_info.append((splitted[0], str(suma)))
    participants_info.sort(key=lambda x: x[1])
    participants_info = participants_info[::-1]
    miejsce = 1
    for i in range(0, len(participants_info)):
        if i != 0 and int(participants_info[i-1][1]) ==  int(participants_info[i][1]):
            print(f"Miejsce: {miejsce}, Imię: {participants_info[i][0]}, Wynik: {participants_info[i][1]} ")
        else:
            print(f"Miejsce: {i+1}, Imię: {participants_info[i][0]}, Wynik: {participants_info[i][1]} ")
        if i != 0:
            miejsce += 1


createLeaderboard([
"Adam 1 2 3 4 5",
"Basia 10 9 8 7 6",
"Czesio 10 10 0 10 10",
"Daria 0 0 10 4"
])