# mineduc-scraper
# 📊 Extractor de Datos de Establecimientos Educacionales – MINEDUC Chile

Este proyecto es un scraper automatizado que recorre **todas las regiones y comunas de Chile**, accediendo al buscador del Ministerio de Educación (MINEDUC) para extraer información detallada de los establecimientos educacionales, como:

- Nombre
- Dirección
- Teléfono
- Correo electrónico
- Página web
- Director(a)
- Sostenedor
- Región y Comuna

## 🚀 ¿Para qué sirve?

Este script permite generar una base de datos completa y actualizada con información pública de todos los establecimientos educacionales del país. Útil para análisis, segmentaciones, contacto institucional, o uso en herramientas internas.

---

## 📦 Estructura del Proyecto

Extractor_data_miniedu/
---------- extractor.py 
---------- run_scraper.py 
---------- requirements.txt 
---------- establecimientos_iquique.csv

extractor.py # Contiene la lógica para acceder a las fichas por región y comuna
run_scraper.py # Script principal que recorre todas las comunas y genera el CSV final
requirements.txt # Librerías necesarias
establecimientos_iquique.csv # Archivo de salida con los datos (puede cambiar el nombre)

---

## 🧩 ¿Cómo funciona?

1. `run_scraper.py` recorre cada combinación región–comuna definida en el diccionario.
2. Por cada combinación, consulta el buscador de MINEDUC.
3. Extrae todos los RBD (identificadores únicos de los colegios).
4. Por cada RBD, accede a su ficha individual.
5. Extrae los campos clave y los guarda en una lista.
6. Finalmente, genera un archivo CSV con toda la información recolectada.

---

## 🛠️ Instrucciones de instalación y uso

### 1. Clona o descarga el repositorio

```bash
git clone https://github.com/tuusuario/extractor-mineduc.git
cd extractor-mineduc 
```

### 2. Instala Python (si no lo tienes)

Descárgalo desde: [https://www.python.org/downloads/](https://www.python.org/downloads/)

> 💡 Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"**.

---

### 3. Instala las librerías necesarias

Desde la terminal, dentro de la carpeta del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

Si no tienes un archivo requirements.txt, también puedes instalar manualmente:

```bash
pip install requests beautifulsoup4 pandas
```

### 4. Ejecuta el scraper
```bash
python run_scraper.py
```

## ⏳ Tiempo de ejecución

En promedio, el scraper tarda entre **7 a 9 horas** en completar las más de **13.000 escuelas**.  
Mucho mejor que las **~219 horas que tomaría a un humano** recopilar esta información manualmente. 😅

---

## ⚠️ Consideraciones Técnicas

- Cada solicitud tiene un `timeout=30` segundos.
- Se implementó `time.sleep(1.0)` entre peticiones para evitar bloqueo por parte del servidor del MINEDUC.
- En caso de que alguna ficha no cargue o el sitio esté inestable, el error se omite y el programa continúa.
- El scraper **no fuerza scraping agresivo ni evasión de seguridad**.

---

## 📁 Ejemplo de salida

```csv
RBD,Nombre,Dirección,Teléfono,Correo,Página web,Director(a),Sostenedor,Región,Comuna
12635,ACADEMIA IQUIQUE,Bulnes 767,2247188,ytrujillo@academiaiquique.cl,www.academiaiquique.cl,Yerka Verónica Trujillo Butler,Sociedad Comercial Ceva Tres Spa,DE TARAPACÁ,IQUIQUE
