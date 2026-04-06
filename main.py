from datetime import datetime

import ntplib
from fastapi import FastAPI

app = FastAPI()


def obtener_hora():
    client = ntplib.NTPClient()
    try:
        response = client.request('ntp.shoa.cl', version=3, timeout=5)
        dt = datetime.fromtimestamp(response.tx_time)
        dt = dt.strftime('%Y-%m-%d %H:%M:%S')
        return dt
    except Exception:
        return None


@app.get('/time')
async def get_time():
    hora_oficial = obtener_hora()

    if not hora_oficial:
        hora_oficial = datetime.now()
        hora_oficial = hora_oficial.strftime('%Y-%m-%d %H:%M:%S')

    return {'hora_actual': hora_oficial}
