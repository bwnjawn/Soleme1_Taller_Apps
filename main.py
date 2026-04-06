from datetime import datetime

import ntplib
from fastapi import FastAPI

app = FastAPI()


def obtener_hora_ntp():
    """Obtiene la hora oficial desde el servidor NTP del SHOA."""
    client = ntplib.NTPClient()
    try:
        # Consultamos al servidor oficial ntp.shoa.cl
        response = client.request('ntp.shoa.cl', version=3, timeout=5)

        # Convertimos el timestamp de la red a un objeto datetime local
        # Usamos la hora local del sistema donde corre el contenedor
        dt = datetime.fromtimestamp(response.tx_time)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        # Si el servidor NTP no responde, retornamos None para usar el respaldo
        return None


@app.get('/time')
async def get_time():
    hora_oficial = obtener_hora_ntp()

    # Si falla la conexión NTP, usamos la hora del sistema como respaldo
    if not hora_oficial:
        hora_oficial = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return {'current_time': hora_oficial}
