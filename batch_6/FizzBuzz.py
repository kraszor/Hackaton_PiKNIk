import pyttsx3
from tqdm import tqdm  # trzeba pobrać
import time

# Ma być kreatywnie (czyli śmiesznie :) ) więc zmieniliśmy nazwy:
# FizzBuzz -> Denaturat
# Fizz -> Wóda
# Buzz -> Piwo

# koniecznie z dźwiękiem

def open_music(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


fizzbuzz_text = 'Denaturat'
buzz_text = 'Wóda'
fizz_text = 'Piwo'


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0 and i != 0:
            open_music(fizzbuzz_text)
            time.sleep(0.7)
        elif i % 3 == 0 and i != 0:
            open_music(fizz_text)
            time.sleep(0.7)
        elif i % 5 == 0 and i != 0:
            open_music(buzz_text)
            time.sleep(0.7)
        else:
            open_music(str(i))
            time.sleep(0.7)

print("Zaczynamy za")
for j in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):
    time.sleep(0.5)
print("Jazda!!!!")
open_music("Następna stacja")
time.sleep(0.3)
open_music("Wpierdol")
fizzbuzz(32)
