from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Actualmente el bot sólo es compatible con YouTube  (No lista de reproducción) Simplemente envía el link de YouTube ☺️"
    await message.reply_text(helptxt)
