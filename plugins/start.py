from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Canal", url="https://t.me/BotsDeAyuda")],
        [InlineKeyboardButton(
            "Reporta fallos 😊", url="https://t.me/DKzippO")]
    ])
    welcomed = f"¡Hola! <b>{message.from_user.first_name}</b>\nEscribe /help para más información"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
