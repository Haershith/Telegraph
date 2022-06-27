from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""𝐻𝐸𝑌 𝐻𝐸𝑅𝐸 𝑌𝑂𝑈 𝐶𝐴𝑁 𝐹𝐼𝑁𝐷 𝑇𝐻𝐸 𝐵𝐴𝑆𝐼𝐶 𝐶𝑂𝑀𝑀𝐴𝑁𝐷𝑆 𝑂𝐹 𝑀𝐼𝑁𝐸.𝐼𝐹 𝑌𝑂𝑈 𝐷𝑂𝑁'𝑇 𝐾𝑁𝑂𝑊 𝐻𝑂𝑊 𝑇𝑂 𝑈𝑆𝐸 𝐶𝑂𝑀𝑀𝐴𝑁𝐷 𝐽𝑂𝐼𝑁 𝑆𝑈𝑃𝑃𝑂𝑅𝑇 𝐺𝑅𝑂𝑈𝑃 𝐴𝑁𝐷 𝐴𝑆𝐾.

<b><u>COMMANDS</u></b>

◉ sᴇɴᴅ ᴄʜᴀɴɴᴇʟ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ
  ғᴏʀᴡᴇʀᴅ ᴛᴀɢ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ 

◉ /id - ʏᴏᴜʀ ᴛɢ ɪᴅ & ɪɴғᴏ

◉ /telegraph - ʀᴇᴘʟʏ ᴛᴏ ʙᴇʟᴏᴡ 𝟻Mʙ ᴍᴇᴅɪᴀ
  ᴛᴏ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ

◉ /stickerid - Rᴇᴘʟʏ Tᴏ Aɴʏ Sᴛɪᴄᴋᴇʀ ᴛᴏ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ

💞Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ Mᴇ💞
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🤖 𝐌𝐘 𝐁𝐎𝐓𝐒", callback_data="botz")
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ Telegraph 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖 ᴍʏ ɴᴀᴍᴇ : {bot.mention}
║┣⪼💞 ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/MutyalaHarshith>Mutyala Harshith</a>
║┣⪼💕 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : <a href=https://t.me/MHGcHaT>MHGcHaT</a>
║┣⪼🗣️ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ3</a>
║┣⪼📚 ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ ᴠᴇʀsɪᴏɴ : 1.0.3  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/MHGcHaT"),
                  InlineKeyboardButton("📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/MutyalaHarshith")
                  ],[            
                  InlineKeyboardButton("ℹ️ 𝐇𝐄𝐋𝐏", callback_data="help"),
                  InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
                  ],[
                  InlineKeyboardButton("👨‍💻 Delovepers 👨‍💻 ", callback_data="devs"),
                  InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
                  ]]
                  )
             )
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @MutyalaHarshith & @MHGcHaT ",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("💖 Updates Channel", url="https://t.me/MutyalaHarshith"),
                  InlineKeyboardButton("😜 Support Channel", url="https://t.me/Telugu_Robots")
                  ],[
                  InlineKeyboardButton("💞 Support Group", url="https://t.me/MHGcHaT"),
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUS TEST THIS COMMANDS 😉</u></b>

◉ /runs         
◉ /ikka      
◉ /dice     
◉ /arrow    
◉ /goal    
◉ /luck    
◉ /throw     
◉ /bowling  
◉ /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                 InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="🤖 This is My botz 😁",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("💞 Stylish Text BoT", url="https://t.me/StylishTextRoBoT"),
                     InlineKeyboardButton("🎵 Music BoT", url="https://t.me/MHYTdlBoT")
                     ],[
                     InlineKeyboardButton("💞 Group Management", url="https://t.me/GeethanjaliBoT")
                     ],[                   
                     InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                     InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























