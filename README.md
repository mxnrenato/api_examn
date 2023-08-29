
## 1.- Crear el entorno virtual
python -m venv nombredelentorno

## 2.- Activar el entonro virtual
source nombredelentorno/Scripts/activate (Windows)
source nombredelentorno/bin/activate (Linux)

## 3.- Instalar los paquetes desde requirements.txt
python -m pip install -r requirements.txt

## 4.- Ejecutar la app
python app.py

Se ejecuta en el entorno local (nube/ on premises)

http://127.0.0.1:5000/califications

### Recursos
En la carpeta src/ encontrarán el script para crear la base de datos en PostgresSQl
