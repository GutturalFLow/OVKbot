import vk_api
from vk_api import VkUpload
import mc
import os
from aiofile import AIOFile
from utils import USUAL_SYNTAX, TOKEN, get_api
import random
from PIL import Image, ImageDraw, ImageFont
from vk_api.longpoll import VkLongPoll
import textwrap
import re
from transformers import GPT2LMHeadModel, GPT2Tokenizer #GPT2
import numpy as np
import torch
import json


np.random.seed()
torch.manual_seed

vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
vk.get_api()
longpoll = VkLongPoll(vk, 176680702)
vkt=vk.get_api()

tok, model = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2"), GPT2LMHeadModel.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2").cuda()


async def write_words(*args):
    text, file = args
    if len(text.split()) <= 1:
        print("меньше")
        return
    else:
        async with AIOFile(file, "a", encoding="utf-8") as f:
            text = text.replace("\n", ". ").replace("\n\n", ". ")
            await f.write(text + ",\n") #ставить ли разделители в документе


async def send_and_gen_sentence(*args):
    file, peer_id = args
    if not os.path.exists(file):
        message = "База слов для этой беседы ещё не существует"
        await get_api().messages.send(
            peer_id=peer_id, message=message, random_id=0
        )
        return
    async with AIOFile(file, encoding="utf-8") as f:
        text = await f.read()
        text_model = [sample.strip() for sample in text.split(",")]
    generator = mc.StringGenerator(samples=text_model)
    message = generator.generate_string(
        attempts=40, # Количество проходов для проверки
        validator=mc.validators.words_count(minimal=2, maximal=15), # Мин и макс проверяймых слов
        formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )
    with open('dsetting.json', 'r') as f: # Считывание команды
        data = json.load(f)
        gtp_setting = str(*dict(*data[str(peer_id)]).values()) # Проверка команды доп генерации
    if random.randint(0, 1) == 1 and gtp_setting == '1': #GPT2
        def generate(
            model, tok, text,
            do_sample=True, max_length=50, repetition_penalty=2.0,
            top_k=40, top_p=0.95, temperature=2.0,
            num_beams=None,
            no_repeat_ngram_size=3
            ):
            input_ids = tok.encode(text, return_tensors="pt").cuda()
            out = model.generate(
                input_ids.cuda(),
                max_length=max_length,
                repetition_penalty=repetition_penalty,
                do_sample=do_sample,
                top_k=top_k, top_p=top_p, temperature=temperature,
                num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size
                )
            return list(map(tok.decode, out))

        generated = generate(model, tok, message, num_beams=10)         
        message = generated[0]
        message = re.sub("[A-Za-z0-9&;]", "", message)
    if not message:
        message = "База слов слишком мала для генерации"
    await get_api().messages.send(
        peer_id=peer_id, message=message, random_id=0 
    )
   
async def memes(*args):
    file, peer_id = args
    
    ran=random.randint(1, 20)

    async with AIOFile(file, encoding="utf-8") as f:
        text = await f.read()
        text_model = [sample.strip() for sample in text.split(",")]
    generator = mc.StringGenerator(samples=text_model)
    memtext =[ generator.generate_string(
        attempts=20, # Количество проходов для проверки
        validator=mc.validators.words_count(minimal=2, maximal=10), # Мин и макс проверяймых слов
        formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    ) for i in range(4) ]

    memimage=Image.open(F'Memes/Mem{ran}.jpg')   
    draw_text=ImageDraw.Draw(memimage)
    font = ImageFont.truetype("impact.ttf", 30, encoding='UTF-8')    
    formatted=[textwrap.fill(memtext[i], width=25) for i in range(len(memtext))] #длина переноса

    d = { 1:[60,50], 2:[70, 50], 3:[70, 20], 4:[150, 300], 5:[75, 400], 6:[90, 425], 7:[90, 425], 8:[90, 400], 9:[90, 425], 10:[90, 425], 
    11:[75, 175, 75, 425], 12:[50, 75, 50, 400], 13:[50, 100, 75, 400], 14:[150, 125, 150, 425], 15:[50, 150, 150, 400], 
    16:[20, 275, 200, 75], 17:[10, 400, 200, 200], 18:[10, 120, 270, 150], 19:[10, 340, 250, 400], 20:[30, 30, 200, 10, 250, 150, 200, 300]}
    count = 0
    for i in range(int(len(d[ran])/2)):
        draw_text.text(
            (d[ran][count:count+2]), 
            formatted[i],
            font=font,
            fill=('Darkorange'),
            stroke_width=3, stroke_fill='black'
            )
        count+=2
    watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))  #Ватермарк
    memimage.paste(watermark, (425, 425),mask=watermark)
    memimage.save("result.jpeg", "JPEG")
    image="result.jpeg" 

    upload=VkUpload(vk)
    attachment =[]
    upload_image = upload.photo_messages(photos=image)[0]
    attachment.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']) )
    await get_api().messages.send(
        peer_id=peer_id, message='', random_id=0, attachment=attachment
    )

async def cout_word(*args):
    file, peer_id = args
    c_word=0
    with open(file, 'rb') as f:
        for line in f:
            c_word = c_word + 1
            ci=("Я знаю " + str(c_word) +" строк")
    await get_api().messages.send(
        peer_id=peer_id, message=ci, random_id=0 
    )


async def bugurt(*args):
    file, peer_id = args

    ran=random.randint(4, 10)
    bug=[]
    async with AIOFile(file, encoding="utf-8") as f:
        text = await f.read()
        text_model = [sample.strip() for sample in text.split(",")]
    for i in range(5):
        generator = mc.StringGenerator(samples=text_model)
        bug1 = generator.generate_string(
            attempts=20, # Количество проходов для проверки
            validator=mc.validators.words_count(minimal=2, maximal=10), # Мин и макс проверяймых слов
            formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )   
        
        bug.append(bug1)
        bug.append("\n@\n")
    del bug[ran:]
    stri = "" 
    stri= " ".join(bug)
    stri=stri.upper()
    stri=stri.rstrip('\n@\n')
    stri=stri.replace("ID","id")
    stri=stri.replace("CLUB","club") 
    await get_api().messages.send(
                peer_id=peer_id, message=stri, random_id=0 
            )   



    

