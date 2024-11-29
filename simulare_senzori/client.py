import requests
import json
import time
import random
import datetime


def generareDate (tip_senzor):
    valoare = None

    match tip_senzor:
        case 'temperatura':
            valoare = random.uniform(17.0, 25.8)
        case 'umiditate_a':
            valoare = random.uniform(35.0, 72.0)
        case 'umiditate_s':
            valoare = random.uniform(30.0, 89.0)

    timp = datetime.datetime.now().ctime()

    date_senzor = {
        'valoare': valoare,
        'timp': timp
    }

    return json.dumps(date_senzor)

def trimitePeriodic ():
    try:
        while True:
            tip_senzor = random.choice(["temperatura", "umiditate_a", "umiditate_s"])
            date_senzor = generareDate(tip_senzor)

            print("Date de trimis:", date_senzor)

            sectiune_aleasa = random.choice([1, 2, 3])
            url_generat = f"http://192.168.12.7:8000/{sectiune_aleasa}/{tip_senzor}"
            print("La adresa URL:", url_generat)

            server_response = requests.post(url_generat, date_senzor)
            print("Raspuns server:", server_response.status_code, end='\n---------------\n')

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nS-a oprit trimiterea periodica")


if __name__ == "__main__":
    trimitePeriodic()
