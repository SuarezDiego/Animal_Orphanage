# Animal Orphanage

Un proyecto de ejemplo en Django para una página web que administra la adopción de animales.

## Instrucciones para correr en Windows

### Crear y activar el entorno virtual
1. Crear el entorno virtual con Python 3.8:
   ```bash
   py -3.8 -m venv env
   ```

2. Activar el entorno virtual:
   ```bash
   .\env\Scripts\activate
   ```

### Instalar dependencias
1. Instalar los requerimientos:
   ```bash
   pip install -r requirements.txt
   ```

### Configuración del proyecto
1. En la carpeta `animal_orphanage`, ejecutar los siguientes comandos:
   ```bash
   python manage.py collectstatic
   python manage.py migrate
   ```

### Ejecutar el servidor
1. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```


