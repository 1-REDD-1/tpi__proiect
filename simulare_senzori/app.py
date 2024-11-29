import fastapi
import pydantic
import typing
import json


app = fastapi.FastAPI()

class DataSenzor (pydantic.BaseModel):
    valoare: float
    sectiune: int
    timp: str

class RawDataSenzor (pydantic.BaseModel):
    valoare: float
    timp: str


lista_date_senzori_temperatura = []
lista_date_senzori_umiditate_sol = []
lista_date_senzori_umiditate_aer = []


async def filtreazaDate (numar_sectiune, tip_data):
    lista_date_filtrate = []

    match tip_data:
        case "temperatura":
            for data_senzor in lista_date_senzori_temperatura:
                if (data_senzor.sectiune == numar_sectiune):
                    lista_date_filtrate.append(data_senzor)
        case "umiditate_s":
            for data_senzor in lista_date_senzori_umiditate_sol:
                if (data_senzor.sectiune == numar_sectiune):
                    lista_date_filtrate.append(data_senzor)
        case "umiditate_a":
            for data_senzor in lista_date_senzori_umiditate_aer:
                if (data_senzor.sectiune == numar_sectiune):
                    lista_date_filtrate.append(data_senzor)

    return lista_date_filtrate

@app.get("/{numar_sectiune}/{tip_data}", response_model=typing.List[DataSenzor])
async def getSectiune1 (numar_sectiune: int, tip_data: str):
    lista_date_senzori_sectiune = await filtreazaDate(numar_sectiune, tip_data)

    return lista_date_senzori_sectiune

@app.post("/{numar_sectiune}/{tip_data}", status_code=201)
async def postDataSenzorSectiune (raw_data_senzor: RawDataSenzor, numar_sectiune: int, tip_data: str):
    # data_senzor.sectiune = numar_sectiune
    print(raw_data_senzor)
    data_senzor = DataSenzor(
        valoare=raw_data_senzor.valoare,
        sectiune=numar_sectiune,
        timp=raw_data_senzor.timp
    )

    print(data_senzor)

    match tip_data:
        case "temperatura":
            lista_date_senzori_temperatura.append(data_senzor)
        case "umiditate_s":
            lista_date_senzori_temperatura.append(data_senzor)
        case "umiditate_a":
            lista_date_senzori_temperatura.append(data_senzor)