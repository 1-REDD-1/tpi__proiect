import json
import time
import threading

import requests
import streamlit as st


GLOBAL_lista_grafice_temperatura = {}
GLOBAL_lista_tabele_temperatura = {}
GLOBAL_lista_fire_executie = []



def obtineDateSectiuneTipSenzor (sectiune_aleasa, tip_senzor):
    raspuns_server = requests.get(f"http://192.168.12.7:8000/{sectiune_aleasa}/{tip_senzor}")

    lista_date_senzori = raspuns_server.json()
    return lista_date_senzori


def creeazaContinutSectiune (tab_sectiune, numar_sectiune):
    global GLOBAL_lista_tabele_temperatura

    # tab_sectiune.download_button("Descarcă datele", json.dumps(date), key=cheie)
    # tab_sectiune.write("Temperatura curentă: " + str(ultima_temperatura))
    GLOBAL_lista_grafice_temperatura[numar_sectiune] = tab_sectiune.empty()

    expander = tab_sectiune.expander("Afișează tabelul", icon=":material/info:")
    GLOBAL_lista_tabele_temperatura[numar_sectiune] = expander.empty()

if __name__ == "__main__":
    lista_tab_sectiuni = st.tabs(["Secțiunea 1", "Secțiunea 2", "Secțiunea 3"])
    lista_resurse_endpoint = [1, 2, 3]

    i = 0
    for tab_sectiune in lista_tab_sectiuni:
        creeazaContinutSectiune(tab_sectiune, lista_resurse_endpoint[i])
        i += 1


    while True:
        for sectiune in lista_resurse_endpoint:
            lista_date_senzori = obtineDateSectiuneTipSenzor(sectiune, "temperatura")

            GLOBAL_lista_grafice_temperatura[sectiune].line_chart(lista_date_senzori, x="timp", y="valoare")
            GLOBAL_lista_tabele_temperatura[sectiune].table(lista_date_senzori)

        time.sleep(5)