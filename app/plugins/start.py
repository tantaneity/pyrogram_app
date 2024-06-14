from pyrogram import filters, types
from app.bot import Bot as app


async def get_start(message) -> types.Message:
    start_message = "qq"
    return await message.reply(start_message)

@app.on_message(filters.command(['start'], prefixes=['!', '/', '']))
async def new_welcome(_, message):
    await get_start(message)
    