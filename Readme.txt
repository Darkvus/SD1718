Autores:
	-Alejandro Jose Caraballo Garcia
	-Alejandro Segovia Gallardo

Readme:
	Bot que obtiene las estadisticas del Clash Royale con tecnologia RabbitMQ y 		lenguaje Python
	Para poner en marcha el bot debemos de enviar un mensaje directo a twitter con 		nuestro tagID
	del juego. Este lo procesaremos por una api para obtener las estadisticas.
	El bot obtendra una grafica y la subira a dropbox y te proporciona un txt 		donde encontramos el
	enlace para descargar nuestra gráfica de estadisticas.

Tecnologias:
	-RabbitMQ--> para crear el servicio de cola.
	-Python
	

Librerias:
	-Pillow --> Para el tratamiento de las imagenes
	-Dropbox --> Para la subida y descarga de la gráfica
	-Matplotlib --> para la creación de gráficas
	-Tweepy--> para el procesamiento de los mensajes directo
	-Pika: Para establecer la conexión con el servidor de colas RabbitMQ
	
