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

vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
vk.get_api()
longpoll = VkLongPoll(vk, 176680702)
vkt=vk.get_api()


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
    memtext = generator.generate_string(
        attempts=20, # Количество проходов для проверки
        validator=mc.validators.words_count(minimal=2, maximal=10), # Мин и макс проверяймых слов
        formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )
    memtext2 = generator.generate_string(
        attempts=20, # Количество проходов для проверки
        validator=mc.validators.words_count(minimal=2, maximal=10), # Мин и макс проверяймых слов
        formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )
    memtext3 = generator.generate_string(
        attempts=20, # Количество проходов для проверки
        validator=mc.validators.words_count(minimal=2, maximal=10), # Мин и макс проверяймых слов
        formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )
    memtext4 = generator.generate_string(
        attempts=20, # Количество проходов для проверки
        validator=mc.validators.words_count(minimal=2, maximal=10), # Мин и макс проверяймых слов
        formatter=mc.formatters.usual_syntax if USUAL_SYNTAX else None,
    )
    if ran == 1:  #мужик на пляже  
        memimage=Image.open(F'Memes/Mem1.jpg')   
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 72, encoding='UTF-8')    
        formatted=textwrap.fill(memtext, width=25) #длина переноса
        draw_text.text(
            (80,65), 
            formatted,
            font=font,
            fill=('Darkorange'),
            stroke_width=6, stroke_fill='black'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (880, 850),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"      
    if ran == 2: # олень
        memimage=Image.open(f'Memes//Mem2.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=20)
        formatted2=textwrap.fill(memtext2, width=20)
        draw_text.text(
            (70,100),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=6, stroke_fill='black'
            )
        draw_text.text(
            (70,600),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=6, stroke_fill='black'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((55, 55))
        memimage.paste(watermark, (560, 25),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 3: #stonks
        memimage=Image.open(f'Memes/Mem3.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 35, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=15)
        draw_text.text(
            (100,100),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='black'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((50, 50))
        memimage.paste(watermark, (10, 10),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 4: #Сквидвард
        memimage=Image.open(f'Memes/Mem4.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=20)
        draw_text.text(
            (350,60),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (885, 640),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 5: #уверенно подошел
        memimage=Image.open(f'Memes/Mem5.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 45, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=35)
        draw_text.text(
            (120,600),
            formatted,
            font=font,
            fill=('white'),
            stroke_width=4, stroke_fill='black'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (680, 20),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 6: # В ноги к тян
        memimage=Image.open(f'Memes/Mem6.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=15)
        draw_text.text(
            (530,40),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (885, 900),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 7: # тупые смеются над умным
        memimage=Image.open(f'Memes/Mem7.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 35, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=20)
        formatted2=textwrap.fill(memtext2, width=20)
        draw_text.text(
            (350,80),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        draw_text.text(
            (85,250),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((50, 50))
        memimage.paste(watermark, (13, 13),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 8: # Плачут и не плачут
        memimage=Image.open(f'Memes/Mem8.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 70, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=25)
        formatted2=textwrap.fill(memtext2, width=25)
        draw_text.text(
            (400,450),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        draw_text.text(
            (400,1050),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=5, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((70, 70))
        memimage.paste(watermark, (1180, 30),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 9: # Солдаты держат остров
        memimage=Image.open(f'Memes/Mem9.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 90, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=15)
        formatted2=textwrap.fill(memtext2, width=25)
        draw_text.text(
            (400,350),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        draw_text.text(
            (80,1050),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=5, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((80, 80))
        memimage.paste(watermark, (1030, 60),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 10: # 2 doge
        memimage=Image.open(f'Memes/Mem10.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 30, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=15)
        formatted2=textwrap.fill(memtext2, width=15)
        draw_text.text(
            (15,370),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (400,370),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((50, 50))
        memimage.paste(watermark, (590, 24),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 11: # 2 froge
        memimage=Image.open(f'Memes/Mem11.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 30, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=25)
        formatted2=textwrap.fill(memtext2, width=25)
        draw_text.text(
            (80,37),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (80,290),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((50, 50))
        memimage.paste(watermark, (430, 330),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 12: #Степанова
        memimage=Image.open(f'Memes/Mem12.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=20)
        draw_text.text(
            (70,300),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((60, 60))
        memimage.paste(watermark, (650, 400),mask=watermark)
        memimage.save("result.jpeg", "JPEG")

        image="result.jpeg"
    if ran == 13: #Голубь и пёс
        memimage=Image.open(f'Memes/Mem13.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=20)
        draw_text.text(
            (100,32),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (850, 600),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 14: # 2 longdog
        memimage=Image.open(f'Memes/Mem14.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=25)
        formatted2=textwrap.fill(memtext2, width=30)
        draw_text.text(
            (80,37),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (80,790),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (650, 950),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 15: # собеседование
        memimage=Image.open(f'Memes/Mem15.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 35, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=15)
        formatted2=textwrap.fill(memtext2, width=15)
        formatted3=textwrap.fill(memtext3, width=15)
        formatted4=textwrap.fill(memtext4, width=15)
        draw_text.text(
            (40,40),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (505,38),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (470,240),
            formatted3, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (315,485),
            formatted4, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (650, 700),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 16:  #аниме плачет 
        memimage=Image.open(f'Memes/Mem16.jpg')   
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 55, encoding='UTF-8')    
        formatted=textwrap.fill(memtext, width=35) #длина переноса
        draw_text.text(
            (70,930), 
            formatted,
            font=font,
            fill=('Darkorange'),
            stroke_width=6, stroke_fill='black'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (880, 980),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"     
    if ran == 17: # 2 Обмен
        memimage=Image.open(f'Memes/Mem17.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=15)
        formatted2=textwrap.fill(memtext2, width=15)
        draw_text.text(
            (70,250),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (450,250),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (650, 950),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 18: # 2  злой добрый
        memimage=Image.open(f'Memes/Mem18.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 45, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=25)
        formatted2=textwrap.fill(memtext2, width=25)
        draw_text.text(
            (50,550),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (620,550),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (60, 9),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 19: # 2  
        memimage=Image.open(f'Memes/Mem19.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 60, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=25)
        formatted2=textwrap.fill(memtext2, width=20)
        draw_text.text(
            (50,150),
            formatted, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        draw_text.text(
            (550,550),
            formatted2, 
            font=font,
            fill=('darkorange'),
            stroke_width=3, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((75, 75))
        memimage.paste(watermark, (60, 9),mask=watermark)
        memimage.save("result.jpeg", "JPEG")
        image="result.jpeg"
    if ran == 20: #Кчау
        memimage=Image.open(f'Memes/Mem20.jpg')
        draw_text=ImageDraw.Draw(memimage)
        font = ImageFont.truetype("impact.ttf", 50, encoding='UTF-8')
        formatted=textwrap.fill(memtext, width=20)
        draw_text.text(
            (70,250),
            formatted,
            font=font,
            fill=('darkorange'),
            stroke_width=4, stroke_fill='darkblue'
            )
        watermark = Image.open(f'Memes/OVK2.png').resize((60, 60))
        memimage.paste(watermark, (10, 10),mask=watermark)
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



    

