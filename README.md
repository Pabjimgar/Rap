# MusicStats

Proyecto personal para mejorar en la programación con **Python** y aprender **MongoDb**.
Se ha tratado de abarcar un ciclo completo de gestión del dato, desde su extracción de la web
mediante las librerias *requests* y *beautifoulSoup*, pasando por el procesamiento de los textos 
extraidos para conseguir estadísticas con que comparar los diferentes artistas y estilos y la 
consolidación de esta información en MongoDb.

La visualización de los datos se lleva a cabo mediante las librerias *matplotlib* y *seaborn*; mientras
que la generación de canciones se lleva a cabo a través de la librería *markovify*.

La ejecución del programa se realiza por consola siguiendo el siguiente patrón:

```bash
python3 main.py Artista Estilo
```
