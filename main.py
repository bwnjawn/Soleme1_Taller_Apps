from datetime import datetime

import ntplib
from fastapi import FastAPI

app = FastAPI()


def obtener_hora_ntp():
    client = ntplib.NTPClient()
    try:
        response = client.request('ntp.shoa.cl', version=3, timeout=5)

        dt = datetime.fromtimestamp(response.tx_time)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return None


@app.get('/time')
async def get_time():
    hora_oficial = obtener_hora_ntp()

    if not hora_oficial:
        hora_oficial = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return {'current_time': hora_oficial}
