import keyboard
import pyttsx3
import time

# dla lepszych efektów trzeba mieć polską wersję systemu


def play_sound_regular(letter, text):
    engine = pyttsx3.init()
    beginning = f'{letter} jak'
    engine.say(beginning)
    engine.runAndWait()
    time.sleep(0.1)
    engine.say(text)
    engine.runAndWait()


def play_sound_special(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def funny_keyboard():
    while True:
        try:
            if keyboard.is_pressed('a'):
                play_sound_regular('a', "Alkohol")
            if keyboard.is_pressed('b'):
                play_sound_regular('b', "Bimber")
            if keyboard.is_pressed('c'):
                play_sound_regular('c', "Cycki")
            if keyboard.is_pressed('d'):
                play_sound_regular('d', "Dużo piwa")
            if keyboard.is_pressed('e'):
                play_sound_regular('e', "EEEEEEEwa Stróżyna")
            if keyboard.is_pressed('f'):
                play_sound_regular('f', "Fujjj.       dziewczyna")
            if keyboard.is_pressed('g'):
                play_sound_regular('g', "Góóóra fety")
            if keyboard.is_pressed('h'):
                play_sound_regular('h', "Huj. z tym. wszystkim")
            if keyboard.is_pressed('i'):
                play_sound_regular('i', "Idziemy przysmażyć płucko?")
            if keyboard.is_pressed('j'):
                play_sound_regular('j', "Jak to jest być skrybą, dobrze? A, wie pan, moim zdaniem to nie ma tak, że dobrze, albo że niedobrze. Gdybym miał powiedzieć, co cenię w życiu najbardziej, powiedziałbym, że ludzi. Ludzi, którzy podali mi pomocną dłoń, kiedy sobie nie radziłem, kiedy byłem sam, i co ciekawe, to właśnie przypadkowe spotkania wpływają na nasze życie. Chodzi o to, że kiedy wyznaje się pewne wartości, nawet pozornie uniwersalne, bywa, że nie znajduje się zrozumienia, które by tak rzec, które pomaga się nam rozwijać. Ja miałem szczęście, by tak rzec, ponieważ je znalazłem, i dziękuję życiu! Dziękuję mu; życie to śpiew, życie to taniec, życie to miłość! Wielu ludzi pyta mnie o to samo: ale jak ty to robisz, skąd czerpiesz tę radość? A ja odpowiadam, że to proste! To umiłowanie życia. To właśnie ono sprawia, że dzisiaj na przykład buduję maszyny, a jutro – kto wie? Dlaczego by nie – oddam się pracy społecznej i będę, ot, choćby, sadzić... doć— m-marchew...")
            if keyboard.is_pressed('k'):
                play_sound_regular('k', "Kurwa pryncypałki")
            if keyboard.is_pressed('l'):
                play_sound_regular('l', "Lepiej hujem trzeć po żwirze niż studiować na Airze")
            if keyboard.is_pressed('m'):
                play_sound_regular('m', "Miałeś kurwo złoty róg")
            if keyboard.is_pressed('n'):
                play_sound_regular('n', "Nowy passat od szwagra")
            if keyboard.is_pressed('o'):
                play_sound_regular('o', "Olo Solo")
            if keyboard.is_pressed('p'):
                play_sound_regular('p', "Pan Zbyszek obraca się trzymając walizkę")
            if keyboard.is_pressed('r'):
                play_sound_regular('r', "rruuhhaanniee")
            if keyboard.is_pressed('s'):
                play_sound_regular('s', "Student debil")
            if keyboard.is_pressed('t'):
                play_sound_regular('t', "To jest. kurwa. dramat.")
            if keyboard.is_pressed('u'):
                play_sound_regular('u', "Ufff. Na szczęście zdążyłem")
            if keyboard.is_pressed('q'):
                play_sound_regular('q', "KU KU KURWA")
            if keyboard.is_pressed('w'):
                play_sound_regular('w', "Wale wiadro")
            if keyboard.is_pressed('v'):
                play_sound_regular('v', "Wyrzuć ją! Wypierdol!")
            if keyboard.is_pressed('x'):
                play_sound_regular('x', "X.D")
            if keyboard.is_pressed('y'):
                play_sound_regular('y', "yyy Piwo")
            if keyboard.is_pressed('z'):
                play_sound_regular('z', "Zjebani jesteśmy.. nie musicie nam mówić")

            if keyboard.is_pressed('0'):
                play_sound_special("Nie ma piwa")
            if keyboard.is_pressed('1'):
                play_sound_special("Jedno piwo")
            if keyboard.is_pressed('2'):
                play_sound_special("Dwa piwa")
            if keyboard.is_pressed('3'):
                play_sound_special("Trzy piwa")
            if keyboard.is_pressed('4'):
                play_sound_special("Cztery piwa")
            if keyboard.is_pressed('5'):
                play_sound_special("Pięć piw")
            if keyboard.is_pressed('6'):
                play_sound_special("Sześć piw")
            if keyboard.is_pressed('7'):
                play_sound_special("Siedem piw")
            if keyboard.is_pressed('8'):
                play_sound_special("Osiem piw")
            if keyboard.is_pressed('9'):
                play_sound_special("Dziewięć piw. zgon")

            if keyboard.is_pressed('`'):
                play_sound_special("Ajir wspaniały tylko Dawid Huj")
            if keyboard.is_pressed('-'):
                play_sound_special("Białasy")
            if keyboard.is_pressed('='):
                play_sound_special("Kroplóweczka pyszniutka")
            if keyboard.is_pressed('['):
                play_sound_special("Pyszniutka kroplóweczka")
            if keyboard.is_pressed(']'):
                play_sound_special("Piwem kaca wyleczysz")
            if keyboard.is_pressed(';'):
                play_sound_special("Uśmiechnijmy się do siebie")
            if keyboard.is_pressed(','):
                play_sound_special("A gdyby tak wszystkie marchewki zamienić na grzyby?")
            if keyboard.is_pressed('.'):
                play_sound_special("Macierz Dżejsona")
            if keyboard.is_pressed('/'):
                play_sound_special("Tępe huje")
            if keyboard.is_pressed('*'):
                play_sound_special("Wielki Tomek Aligator")
            if keyboard.is_pressed('!'):
                return
        except:
            break


funny_keyboard()