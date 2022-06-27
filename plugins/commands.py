from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from helper.database import insert, getid
from helper.utils import not_subscribed
from variables import STAT_STICK, PICS, ADMIN, DELAY
import asyncio
import random

WAIT_MSG = """"<b>Processing ...</b>"""

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**⚠️Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)]
           ])
       )

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    insert(int(message.chat.id))
    await message.reply_chat_action("Typing")
    await asyncio.sleep(DELAY)
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(DELAY)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻\n𝙸 𝚊𝚖 𝙰 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚙𝚑 𝙱𝚘𝚝 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢 𝙷𝚊𝚛𝚜𝚑𝚒𝚝𝚑 𝙸 𝚌𝚊𝚗 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚙𝚑 𝙼𝚎𝚍𝚒𝚊 𝙻𝚒𝚔𝚎 𝙿𝚑𝚘𝚝𝚘 , 𝙼𝚞𝚜𝚒𝚌 & 𝚅𝚒𝚍𝚎𝚘𝚜 𝙵𝚘𝚛 𝙼𝚘𝚛𝚎 𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝙲𝚕𝚒𝚌𝚔 /help",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("💞 Support", url="https://t.me/MHGcHaT"),
            InlineKeyboardButton("💖 Updates", url="https://t.me/MutyalaHarshith")
            ],[            
            InlineKeyboardButton("😜 Help", callback_data="help"),
            InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
            ],[
            InlineKeyboardButton("😎 Develovepers", callback_data="devs"),
            InlineKeyboardButton("💔 About", callback_data="about")
            ]]
            )
        )
         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    await message.reply_text(
    text = f"""<i>
<u>👁️‍🗨️YOUR DETAILS</u>

○ ID : <code>{message.from_user.id}</code>
○ First Name : <code>{message.from_user.first_name}<code>
○ UserName : @{message.from_user.username}

Thank You For Using Me❣️</i>""")


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):    
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")
