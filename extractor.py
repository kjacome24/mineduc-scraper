import requests
from bs4 import BeautifulSoup

import re
import time

def extraer_por_region_comuna(region_id, comuna_id, nombre_region, nombre_comuna):

    # Headers que un navegador real enviaría
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Referer": "https://mi.mineduc.cl/mime-web/mvc/mime/busqueda_avanzada",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Endpoint de búsqueda
    search_url = "https://mi.mineduc.cl/mime-web/mvc/mime/busqueda_avanzada"



    # Región de Coquimbo / La Serena
    payload = {
        "reg": region_id,
        "com": comuna_id,
        "region": region_id,
        "comuna": comuna_id,
        "dep": "0",
        "dependencia": "0",
        "npar": "0",
        "nbas": "0",
        "nmed": "0",
        "sep": "0",
        "tens": "0",
        "esp": "0",
        "sec": "0",
        "espec": "0",
        "rbd1": "",
        "idParvularia": "0",
        "idBasica": "0",
        "idMedia": "0",
        "tipoEns": "0",
        "sectorEco": "0",
        "especialidad": "0",
        "nEspecial": "0"
    }


    session = requests.Session()
    session.get(search_url)  # Obtener cookies
    resp = session.post(search_url, data=payload, headers=headers)

    # Parsear HTML
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.select("table tbody tr")

    resultados = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 4:
            continue

        nombre_rbd = cols[1].get_text(strip=True)
        nombre = re.sub(r"\s*\[\d+\]", "", nombre_rbd)
        rbd_match = re.search(r"\[(\d+)\]", nombre_rbd)
        if not rbd_match:
            continue
        rbd = rbd_match.group(1)


        # Ir a la ficha individual
        ficha_url = "https://mi.mineduc.cl/mime-web/mvc/mime/ficha"
        ficha_payload = {"rbd": rbd}

        try:
            ficha_resp = session.post(ficha_url, headers=headers, data=ficha_payload, timeout=30)
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la ficha del RBD {rbd}: {e}")
            continue



        # Guardar la ficha para debug SIEMPRE
        # with open(f"debug_ficha_{rbd}.html", "w", encoding="utf-8") as f:
        #     f.write(ficha_resp.text)

        # Validar que tenga contenido útil (mínimo la palabra "Dirección")
        if "Dirección" not in ficha_resp.text:
            print(f"⚠️ Ficha posiblemente incompleta para RBD {rbd}")
            continue


        ficha_soup = BeautifulSoup(ficha_resp.text, 'html.parser')

        # Encuentra la primera tabla con clase "tabla_form"
        tabla_info = ficha_soup.find_all("table", class_="tabla_form")[0]

        def get_dato(label):
            filas = tabla_info.find_all("tr")
            for fila in filas:
                tds = fila.find_all("td")
                if len(tds) >= 2 and label in tds[0].get_text(strip=True):
                    return tds[1].get_text(strip=True)
            return ""


        direccion = get_dato("Dirección")
        telefono = get_dato("Teléfono")
        correo = get_dato("E-mail contacto")
        pagina_web = get_dato("Página web")
        director = get_dato("Director(a)")
        sostenedor = get_dato("Sostenedor")



        resultados.append({
            "RBD": rbd,
            "Nombre": nombre,
            "Dirección": direccion,
            "Teléfono": telefono,
            "Correo": correo,
            "Página web" : pagina_web,
            "Director(a)" : director,
            "Sostenedor" : sostenedor,
            "Región" : nombre_region,
            "Comuna" : nombre_comuna
        })
        print(len(resultados))
        time.sleep(1.0)
    return resultados




# Guardar a CSV
# df = pd.DataFrame(extraer_por_region_comuna(1, 1101, "DE TARAPACÁ", "IQUIQUE"))
# df.to_csv("establecimientos_iquique.csv", index=False, encoding='utf-8-sig')
# print(" Datos guardados en establecimientos_iquique.csv")