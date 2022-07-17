from vk import types
from vk.bot_framework.dispatcher import Blueprint
from utils import get_api, TOKEN
from neuron import cout_word, bugurt, memes, send_and_gen_sentence
import vk_api
from vk_api import VkUpload
import random
import mc
import os
import textwrap
import wget
import requests
from utils import USUAL_SYNTAX
from PIL import Image, ImageFont, ImageDraw
import pyttsx3
from aiofile import AIOFile
import numpy as np
import cv2
bp = Blueprint()
api = get_api()

vk = vk_api.VkApi(token=TOKEN)
@bp.message_handler(commands=["g", "gen", "generate"])
async def generate(message: types.Message, _):
    await send_and_gen_sentence(
        f"dialogs/dialogs{message.peer_id}.txt", message.peer_id
    )
   

@bp.message_handler(commands=["mem", "meme"])
async def generate(message: types.Message, _):
 
    await memes(
        f"dialogs/dialogs{message.peer_id}.txt", message.peer_id
    )

@bp.message_handler(commands=["w", "word"])
async def generate(message: types.Message, _):
 
    await cout_word(
        f"dialogs/dialogs{message.peer_id}.txt", message.peer_id
    )

@bp.message_handler(commands=["b","b \d"])
async def generate(message: types.Message, _):
 
    await bugurt(
f"dialogs/dialogs{message.peer_id}.txt", message.peer_id
)

@bp.message_handler(commands=["c"])
async def generate(message: types.Message, _):
        if len(message.text.split()) == 1:
            async with AIOFile( f"dialogs/dialogs{message.peer_id}.txt", encoding="utf-8") as f:
                text = await f.read()
                text_model = [sample.strip() for sample in text.split(",")]
            generator = mc.StringGenerator(samples=text_model)
            memtext = generator.generate_string(
                attempts=15, # Количество проходов для проверки
                validator=mc.validators.words_count(minimal=5, maximal=15), # Мин и макс проверяймых слов
                formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
                )
        else:
            memtext=message.text
            memtext=memtext.replace("/c", "")
        peer_id=message.peer_id
        h=[]
        attachment =[]
        h=message.attachments
        memtext=memtext.upper()
        url = h[0].photo.sizes[-1].url
        wget.download(url, f"files/create.jpeg")    #Скачиваниие
        hwimage = cv2.imread(f"files/create.jpeg")
        x = np.size(hwimage, 0)
        y = np.size(hwimage, 1)
        img = Image.new('RGB', (x*2, y//6), color='#000000')
        user_img = Image.open(f"files/create.jpeg")
        user_img.paste(img, (0, 0))
        draw_text=ImageDraw.Draw(user_img)
        font = ImageFont.truetype("impact.ttf", 30, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=35)
        draw_text.text(
            (5,5),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=1, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((100, 100))
        img=user_img 
        img.paste(watermark, (1150, 1000),mask=watermark)
        img.save(f'files/done.jpeg')
        img=f'files/done.jpeg'
        upload=VkUpload(vk)
        attachment =[]
        upload_image = upload.photo_messages(photos=img)[-1]
        attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']) )
        os.remove(f"files/create.jpeg")
        await get_api().messages.send(
        peer_id=peer_id, message='', random_id=0, attachment=attachment
    )

@bp.message_handler(commands=["h"])
async def hate(message: types.Message, _):
    hate_id=""
    hate_id=message.text
    hate_id=hate_id.replace("/h", "")
    async with AIOFile(f"dialogs/hate.txt", encoding="utf-8") as f:
        text = await f.read()
        text_model = [sample.strip() for sample in text.split(",")]
        generator = mc.StringGenerator(samples=text_model)
        hate = generator.generate_string(
            attempts=100, # Количество проходов для проверки
            validator=mc.validators.words_count(minimal=5, maximal=45), # Мин и макс проверяймых слов
            formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )   
    
        await get_api().messages.send(
        peer_id=message.peer_id, message=hate_id+" "+hate, random_id=0 
    )
vk = vk_api.VkApi(token=TOKEN)

@bp.message_handler(commands=["hs", "speak"])
async def HateSpeak(message: types.Message, _):
    peer_id=message.peer_id   
    
    async with AIOFile(f"dialogs/hate.txt", encoding="utf-8") as f:
        text = await f.read()
        text_model = [sample.strip() for sample in text.split(",")]
        generator = mc.StringGenerator(samples=text_model)
        hate = generator.generate_string(
            attempts=100, # Количество проходов для проверки
            validator=mc.validators.words_count(minimal=5, maximal=45), # Мин и макс проверяймых слов
            formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )     
    hate_id=""
    hate_id=message.text    
    hate_id=hate_id.replace("/hs", "")   
    engine = pyttsx3.init()
    rlist=(0,3,4,5,6,7,8)
    r1=random.randint(100, 200)
    r2=random.choice(rlist)
    engine.setProperty ('rate', r1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r2].id)

    engine.save_to_file(hate_id+hate, 'ggg.ogg')
    engine.runAndWait()
    name="ggg.ogg"

    upload = vk.method("docs.getMessagesUploadServer", {"type": "audio_message", "peer_id": peer_id})
    jsn = requests.post(upload["upload_url"], files={'file': open(name, 'rb')}).json()
    save = vk.method("docs.save", {"file": jsn["file"]})   
    send = 'doc{}_{}'.format(save["audio_message"]["owner_id"], save["audio_message"]["id"])

    await get_api().messages.send(
    peer_id=peer_id, message='', random_id=0, attachment=send
    )

