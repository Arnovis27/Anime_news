from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time,os
#from Credencial import TOKENKEY


TOKENKEY= os.getenv("TOKENKEY")#Esta linea es para heroku, comentala y decomenta la de arriba

def start(update, context):
    user = update.message.from_user #datos de usuario
    update.message.reply_text("Hola "+user['first_name']+" "+ user['last_name']+", Bienvenido al sistemas de noticias para OTAKUS, espero el bot te sirva, muchas gracias por usarlo")


def funcion2(fecha,anime,links,text,update,context,zelda):  
    links= list()
    anime= list()
    fecha= list()
    aux3=0
    contador=0
    req = Request(zelda, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    busqueda(fecha,anime,links,webpage)
    dehoy(fecha,anime,links,text,update,context,contador)


def funcion1(update, context):
    text= update.message.text
    links= list()
    anime= list()
    fecha= list()
    zelda= "https://somoskudasai.com/categoria/noticias/anime/"
    funcion2(fecha,anime,links,text,update,context,zelda)
    return ConversationHandler.END

def funcion3(update, context):
    text= update.message.text
    links= list()
    anime= list()
    fecha= list()
    zelda= "https://somoskudasai.com/categoria/cultura-otaku/"
    funcion2(fecha,anime,links,text,update,context,zelda)
    return ConversationHandler.END

def funcion4(update, context):
    text= update.message.text
    links= list()
    anime= list()
    fecha= list()
    zelda= "https://somoskudasai.com/categoria/noticias/manga/"
    funcion2(fecha,anime,links,text,update,context,zelda)
    return ConversationHandler.END

def busqueda(fecha,anime,links,webpage):
    soup= BeautifulSoup(webpage)
    ani= soup.find_all("h2", class_="ar-title white-co mab fz4 lg-fz5")
    tags = soup.find_all('a', {"aria-label": True}) # get all the a tag
    reloj= soup.find_all("span",class_="db op5")
    #imagen= soup.find_all("img")
    aux=0
    aux2=0
    aux3=0

    for i in ani:
        anime.append(i.text)
    
    for i in range(len(tags)):
        aux=tags[i]
        aux2=aux['aria-label']
        for i in range(len(anime)):
            if aux2==anime[i]:
                links.append(aux["href"])

    for i in reloj:
        fecha.append(i.text)
        
    return (fecha,anime,links)

def dehoy(fecha,anime,links,text,update,context,contador):
    aux3=fecha[0]
    #noticias de hoy
    for i in range(len(fecha)):
        if fecha[i]==aux3:
            contador+=1
    update.message.reply_text(aux3.upper())
    for i in range(contador):
        update.message.reply_text("\n"+anime[i].upper()+"\n"+links[i])

def comando2_Command_Handler(update,context):

    update.message.reply_text("Este bot sigue en desarrollo, si tienes sugerencias comunicate conmigo Att: @Yagyu27")
    return ConversationHandler.END

if __name__ == '__main__':

    updater= Updater(token=TOKENKEY, use_context=True)
    
    dp= updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('anime',funcion1),
            CommandHandler('cultura',funcion3),
            CommandHandler('manga',funcion4),
            CommandHandler('info',comando2_Command_Handler)

        ],
        states={
            #INPUT_TEXT:[MessageHandler(Filters.text, input_text)]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    print("Bot Running")
    updater.idle()
