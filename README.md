# Anime_News
Proyecto python para Telegram usando Webscraping creacion de agente virtual para saber noticias animes segun su categoria

## Instalación
Puedes intalarlo clonando el repositorio con ```$ git clone url```

## Como se usa
Para iniciar el programa debes abrir desde el CMD el archivo ```app.py```

### Conexion
Se solicita la creacion del agente virtual de telegram para generar el token de validacion, al mismo tiempo se analiza la estructura de la pagina web en HTML para poder acceder mediante scraping

### Proceso
Mediante las etiquetas contruidas por el HTML de la pagina destino, podremos acceder a los datos que requerimos de esa pagina para mostrar al usuario.

### Servidor
Heroku es una plataforma que nos montar en un servidor por cierto limite de forma gratuita mensualmente, para subirlo necesitamos crear un archivo con ```pip freeze > requirements.txt``` , el cual es usado para que heroku instale las librerias usadas al momento de montar el proyecto, del mismo modo creamos un archivo llamado **Procfile** que es un mecanismo para declarar qué comandos ejecuta su aplicación en la plataforma Heroku
