#!/usr/bin/env python
import pika
import time
import sys
import requests
from grafic import grafica

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='royalecola', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def porcentaje(partidas, total):
    #print(float(total))
    div = (float(partidas)/float(total))
    #print(div)
    port = div * 100
    print(port)
    return port



def callback(ch, method, properties, body):
    print(" [x] Buscando https://royaleapi.com/player/" + body)
    url = 'https://royaleapi.com/player/'+body
    tagId = body


    debug = {'verbose': sys.stderr}
    user_agent = {'User-agent': 'Mozilla/5.0'}
    http  = requests.get(url, headers = user_agent)
    
    datosVictorias1 = http.text.split('wins')
    victorias21 = datosVictorias1[1].split('<td class="right aligned">')
    victoriasF1 = victorias21[1].split('</td>')
    print( "El ususario tiene :" + victoriasF1[0] + " victorias")
    

    if len(victoriasF1[0]) > 3:
	victoriasFin1 = victoriasF1[0].split(',')
	victoriasFinal1 = victoriasFin1[0] + victoriasFin1[1]

    else:
	victoriasFinal1 = victoriasF1[0]
    
    datosVictorias = http.text.split('wins')
    victorias2 = datosVictorias[2].split('<td class="right aligned">')
    victoriasF = victorias2[1].split('</td>')
    print( "El ususario tiene :" + victoriasF[0] + " victorias de 3 coronas")
    
#Como tiene ',' si tiene mas de 3 digitos hay que reajustarlo para su conversion a int
    if len(victoriasF[0]) > 3:
	victoriasFin = victoriasF[0].split(',')
	victoriasFinal = victoriasFin[0] + victoriasFin[1]

    else:
	victoriasFinal = victoriasF[0]

    datosDerrotas = http.text.split('Losses')
    derrotas2 = datosDerrotas[1].split('<td class="right aligned">')
    derrotasF = derrotas2[1].split('</td>')
    print( "El ususario tiene : " + derrotasF[0] + " derrotas")
    
#Como tiene ',' si tiene mas de 3 digitos hay que reajustarlo para su conversion a int
    if len(derrotasF[0]) > 3:
	derrotasFin = derrotasF[0].split(',')
	derrotasFinal = derrotasFin[0] + derrotasFin[1]

    else:
	derrotasFinal = derrotasF[0]
	
    
    partidasJugadas = int(victoriasFinal1) + int(derrotasFinal)
    print("El usuario ha disputado: " + str(partidasJugadas) + " partidas (no se cuentan los empates)")
    
    winner = int(victoriasFinal1)
    print (winner)
    loser = int(derrotasFinal)
    #array[] = {victoriasFinal, derrotasFinal, partidasJugadas}
    porcientos = [porcentaje(winner,partidasJugadas),porcentaje(loser,partidasJugadas)]

    grafica(tagId,porcientos)
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=0) 
#prefetch_count=1-> don't dispatch a new message to a worker until it has processed and acknowledged the previous one
channel.basic_consume(callback,
                      queue='royalecola')

channel.start_consuming()




