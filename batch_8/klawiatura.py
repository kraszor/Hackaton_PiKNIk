import keyboard
import pyttsx3
import time


def play_sound_regular(letter, text):
    engine = pyttsx3.init()
    beginning = f'{letter} jak'
    engine.say(beginning)
    engine.runAndWait()
    time.sleep(0.1)
    engine.say(text)
    engine.runAndWait()


def play_sound_numeric(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


while True:
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
        play_sound_regular('i', "?Ile za most do poloneza")
    if keyboard.is_pressed('j'):
        play_sound_regular('j', "Jaka parówa wariacie")
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
        play_sound_regular('p', "Pierdole te studia")
    if keyboard.is_pressed('r'):
        play_sound_regular('r', "rruuhhaanniee")
    if keyboard.is_pressed('s'):
        play_sound_regular('s', "s")
    if keyboard.is_pressed('t'):
        play_sound_regular('t', "To jest. kurwa. dramat.")
    if keyboard.is_pressed('u'):
        play_sound_regular('u', "u")
    if keyboard.is_pressed('q'):
        play_sound_regular('q', "KU KU KURWA")
    if keyboard.is_pressed('w'):
        play_sound_regular('w', "Wale wiadro")
    if keyboard.is_pressed('v'):
        play_sound_regular('v', "v")
    if keyboard.is_pressed('x'):
        play_sound_regular('x', "x")
    if keyboard.is_pressed('y'):
        play_sound_regular('y', "yyy Piwo")
    if keyboard.is_pressed('z'):
        play_sound_regular('z', "Zjebani jesteśmy.. nie musicie nam mówić")

    if keyboard.is_pressed('0'):
        play_sound_numeric("Nie ma piwa")
    if keyboard.is_pressed('1'):
        play_sound_numeric("Jedno piwo")
    if keyboard.is_pressed('2'):
        play_sound_numeric("Dwa piwa")
    if keyboard.is_pressed('3'):
        play_sound_numeric("Trzy piwa")
    if keyboard.is_pressed('4'):
        play_sound_numeric("Cztery piwa")
    if keyboard.is_pressed('5'):
        play_sound_numeric("Pięć piw")
    if keyboard.is_pressed('6'):
        play_sound_numeric("Sześć piw")
    if keyboard.is_pressed('7'):
        play_sound_numeric("Siedem piw")
    if keyboard.is_pressed('8'):
        play_sound_numeric("Osiem piw")
    if keyboard.is_pressed('9'):
        play_sound_numeric("Dziewięć piw. zgon")

    if keyboard.is_pressed('~'):
        play_sound_regular('~', "Cycki")
    if keyboard.is_pressed('-'):
        play_sound_regular('-', "Cycki")
    if keyboard.is_pressed('='):
        play_sound_regular('=', "Cycki")
    if keyboard.is_pressed('['):
        play_sound_regular('[', "Cycki")
    if keyboard.is_pressed(']'):
        play_sound_regular(']', "Cycki")
    if keyboard.is_pressed(';'):
        play_sound_regular(';', "Cycki")
    if keyboard.is_pressed(','):
        play_sound_regular(',', "Cycki")
    if keyboard.is_pressed('.'):
        play_sound_regular('.', "Cycki")
    if keyboard.is_pressed('/'):
        play_sound_regular('/', "Cycki")
    if keyboard.is_pressed('*'):
        play_sound_regular('*', "Cycki")

