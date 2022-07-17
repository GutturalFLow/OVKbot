from vk import types
from vk.bot_framework.dispatcher import Blueprint
from vk.types.conversation import Conversation
from vk.types.responses.messages import (
    GetConversationsById,
    GetConversationsByIdResponse,
)
from utils import get_api, user_is_chat_admin
import os
import re
from aiofile import AIOFile, LineReader, Writer
bp = Blueprint()
api = get_api()


@bp.message_handler(commands=["clear"])
async def clear_base(message: types.Message, _):
    conversation: GetConversationsById = await api.messages.get_conversations_by_id(
        peer_ids=message.peer_id, extended=True
    )
    response: GetConversationsByIdResponse = conversation.response

    if not response.items:
                await message.answer(
            "только администраторам чата"
            )
    chat: Conversation = response.items[0]
    if chat.peer.type == "user":
        message_ = "Команда доступна только в чатах"
        await api.messages.send(
            peer_id=message.from_id, message=message_, random_id=0
        )
    if user_is_chat_admin(chat, message.from_id):
        delmes=message.text
        if len(message.text.split()) == 1:
            os.remove(f"dialogs/dialogs{message.peer_id}.txt")
            await message.answer(
            "База слов успешно удалена"
           )
        else:
            async with AIOFile(f"dialogs/dialogs{message.peer_id}.txt", "r+", encoding="utf-8") as f:
                   delmes=message.text
                   delmes=delmes.lower()
                   delmes = delmes.replace("/clear ",'')
                   text = await f.read()
                   text=text.lower()
                   text = text.replace(delmes,'')
                   if "  ,\n" in text:
                       text=text.replace("  ,\n","")
                   f.close()
            async with AIOFile(f"dialogs/dialogs{message.peer_id}.txt", "w", encoding="utf-8") as f:
                   await f.write(text)
                   await message.answer("Фраза "+delmes+" успешно удалена")
    if not user_is_chat_admin(chat, message.from_id):
                await message.answer(
            "Команда доступна только администраторам чата"
           )




