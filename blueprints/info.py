from vk import types
from vk.bot_framework.dispatcher import Blueprint


bp = Blueprint()



@bp.message_handler(commands=["info"])
async def info(message: types.Message, _):
    await message.answer(
        "Доступные команды:\n/gen или /g - генерация текста\n"
        "/clear - очистка базы текста для данной беседы\n"
        "/mem - генерация мема\n"
        "/w - количество выученных строк"
        "\n /b - бугурт"
        "\n /h + текст - бот ругается"
        "\n /hs + текст - бот ругается в голосовом"        
        "\n /c (АНГЛИЙСКАЯ) + изображение  - генерация мема, можно вписать свой текст"
        "\n /gtp 0 Отключить дополнительную генерацию, 1 - включить"
    )
