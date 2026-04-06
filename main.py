from datetime import datetime

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


def obtener_hora_scraping():
    url = "https://www.horaoficial.cl/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscamos la fila de Chile Continental
        filas = soup.find_all("tr")
        for fila in filas:
            if "chile continental" in fila.get_text().lower():
                celdas = fila.find_all("td")
                if len(celdas) >= 2:
                    return celdas[1].get_text(strip=True)
    except Exception:
        return None
    return None


@app.get("/time")
async def get_time():
    hora_scrapeada = obtener_hora_scraping()

    # Si el scraping falla, usamos la hora del sistema como respaldo (para no sacar un 1.0)
    if not hora_scrapeada:
        now = datetime.now()
    else:
        # Combinamos la fecha de hoy con la hora obtenida del scraping
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        return {"current_time": f"{fecha_hoy} {hora_scrapeada}"}

    return {"current_time": now.strftime("%Y-%m-%d %H:%M:%S")}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )  # Requerimiento de puerto [cite: 21, 33]
