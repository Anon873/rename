from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 1484670284))
bot_username = os.environ.get("BOT_USERNAME","GangsterBaby_renamer_BOT")
log_channel = int(os.environ.get("LOG_CHANNEL", ""))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ Good morning sweetheart ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 Good afternoon my Love 🤍'
else:
    wish = '🦋 Good evening baby 🦋'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""✨ нєу ʙᴀʙʏ {message.from_user.first_name }🥀 \n
➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. 
➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ. 
➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀɴᴅ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ. 
➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.""" 
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("•ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs•", callback_data='help')
        ],[
        InlineKeyboardButton('•ᴜᴘᴅᴀᴛᴇs•', url='https://t.me/All_Hindi_Anime'),
        InlineKeyboardButton('•sᴜᴩᴩᴏʀᴛ•', url='https://t.me/shadowsupportx')
        ],[
        InlineKeyboardButton('ᴀʙᴏᴜᴛ ᴜꜱ 🥀', callback_data='about')
    ]]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                              [[InlineKeyboardButton("🔺 Support Group 🔺", url="https://t.me/ShadowSupportX")],
                                      [InlineKeyboardButton("Developer", url='https://t.me/it_was_abhi')]
                                      ]))
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 100MB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 1073741824
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	Hello {wish} {message.from_user.first_name }\n\n
	__I am file renamer bot, Please send any telegram 
	**Document Or Video** and enter new filename to rename it__
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Support Group 🔺", url="https://t.me/ShadowSupportX")],
                                      [InlineKeyboardButton("Developer", url='https://t.me/it_was_abhi')]
                                      ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__You are not subscribed my channel__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #SHADOW_LOGS 🦋,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Use About cmd first /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"Hello dear {message.from_user.first_name}  **we are currently working on this issue**\n\nPlease try to rename files from your another account.\nBecause this BOT can't rename file sent by some ids.\n\nIf you are an **ADMIN** Don't worry ! here we have a solution for you dear {message.from_user.first_name }.\n\nPlease use \n👉 `/addpremium your_other_userid` 👈 to use premium feautres\n\n",
                                  reply_markup=InlineKeyboardMarkup(
                                                                [[InlineKeyboardButton("🔺 Support Group 🔺", url="https://t.me/ShadowSupportX")],
                                                                [InlineKeyboardButton("Developer", url='https://t.me/it_was_abhi')]
                                                                ]))
        await message.reply_text(text=f"🦋")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 600
    else:
        LIMIT = 50
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% of daily {humanbytes(limit)} data quota exhausted.\n\n  File size detected {humanbytes(file.file_size)}\n  Used Daily Limit {humanbytes(used)}\n\nYou have only **{humanbytes(remain)}** left on your Account.\nIf U Want to Rename Large File Upgrade Your Plan ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daily Limit {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Can't upload files bigger than 2GB ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))

        elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ", callback_data="custom")
                ],[
                InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="thumb"),
                InlineKeyboardButton("ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ", callback_data="rename")
                ],[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "start")
	    ]])
        )
	    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "start")
            ]])            
        )
	    elif data == "rename":
        await query.message.edit_text(
            text=Txt.REX_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])          
                                    )
    elif data == "thumb":
        await query.message.edit_text(
            text=Txt.RET_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])          
                                     )
    elif data == "custom":
        await query.message.edit_text(
            text=Txt.REX2_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "help")
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

class Txt(object):
    # part of text configuration
    START_TXT = "✨ нєу ʙᴀʙʏ {} 🥀 \n\n➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. \n➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ. \n➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀɴᴅ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ. \n➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛᴀɪɴ."

    ABOUT_TXT = "➻ ᴍʏ ɴᴀᴍᴇ : {} \n➻ ᴍʏ ᴅᴀᴅ :<a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> \n➻ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ :<a href='https://t.me/botsupportx'>ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ</a> \n\n⚜ ꜰᴏʀ ᴀɴɪᴍᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ : \n\n➻ ᴀɴɪᴍᴇ ɪɴ ʜɪɴᴅɪ : <a href='https://t.me/All_Hindi_Anime'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ ʜɪɴᴅɪ : <a href='https://t.me/Anime_In_Hindi_Dub_Only'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ʙᴜʀᴏᴛᴏ ɪɴ ʜɪɴᴅɪ : <a href='https://t.me/Buroto_In_Hindi_Dub'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ᴢᴇᴇ ᴄᴀꜰᴇ ɪɴ ʜɪɴᴅɪ :<a href='https://t.me/ZEE_CAFE_HINDI_OFFICIAL'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n\n𝗔𝗡𝗜𝗠𝗘 𝗥𝗜𝗩𝗔𝗟𝗦 ⚡️: <a href='https://t.me/Rivals_Anime_Group'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n𝗔𝗡𝗜𝗠𝗘 𝗔𝗥𝗢𝗫𝗫 ⚡️: <a href='https://t.me/Aroxx_network'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a> \n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ᴄᴜꜱᴛᴏᴍ ʙᴏᴛ ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ <a href=https://t.me/it_was_abhi>ᴍʏ ᴅᴀᴅ</a>"

    START1_TXT = "✨ нєу ʙᴀʙʏ {} 🥀 \n\n➻ ꜱᴏ ʟᴇᴛ ᴍᴇ ᴇxᴘʟᴀɪɴ ɪ ᴀᴍ ᴀɴ ᴀɴᴅᴀᴠᴀɴᴄᴇᴅ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. \n➻ ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ, ᴠɪᴅᴇᴏꜱ, ᴍᴜꜱɪᴄ, ᴇᴛᴄ.... \n➻ ɪ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ. \n➻ ɪ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\nꜱᴏ ᴛʜᴇ ʙᴏᴛ ɪꜱ ɴᴏᴛ ꜰʀᴇᴇ ɪᴛ'ꜱ ᴘᴀɪᴅ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴘᴀʏ ᴜꜱ ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜱᴜʙɪꜱᴄʀɪᴘᴛɪᴏɴ. \n\nꜱᴜʙɪꜱᴄʀɪᴘᴛɪᴏɴ ɪꜱ ʙᴀꜱᴇᴅ ᴏɴ : \n1ᴅᴀʏ - ₹2 \n1ᴍᴏɴᴛʜ - ₹20 \n\nᴡʜʏ ʏᴏᴜ ꜱʜᴏᴜʟᴅ ᴜꜱᴇ ᴛʜɪꜱ ᴘᴀɪᴅ ʙᴏᴛ ɪɴꜱᴛᴇᴀᴅ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ꜰʀᴇᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ. \n\n• ᴡᴇ ᴅᴇᴘʟᴏʏᴇᴅ ᴏɴ ᴠᴘꜱ, ꜱᴏ ɪᴛ'ꜱ ꜱᴜᴘᴇʀ ꜰᴀꜱᴛ. \n• ʙᴏᴛ ɪꜱ ᴘʀɪᴠᴀᴛᴇ ꜱᴏ  ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ 2ɢʙ ꜰɪʟᴇ ɪɴ 1-2 ᴍɪɴꜱ . \n• ɪᴛ'ꜱ ꜱᴏ ᴄʜᴇᴀᴘ ʏᴏᴜ ᴄᴀɴ ᴀꜰꜰᴏʀᴅ ᴇᴀꜱɪʟʏ."

    APK_TXT = "ᴏɴʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ ᴛᴏ ɢᴇᴛ ꜱᴜʙɪꜱᴄʀɪᴘᴛɪᴏɴ. \n\n<a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> \n<a href=https://t.me/Minato_Bruh>ᴍɪɴᴀᴛᴏ</a> \n\nɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪꜱ ʙᴏᴛ ᴋɪɴᴅʟʏ ᴀꜱᴋ <a href=https://t.me/it_was_abhi>ᴍʏ ᴅᴀᴅ</a>"
  
    HELP_TXT = "ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](https://t.me/Botsupportx)\n\nᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`"

    PROGRESS_BAR = """<b>\n 
➻ ᴘʀᴏɢʀᴇss ʙᴀʀ 
» Sɪᴢᴇ: {1} | {2}
» Dᴏɴᴇ : {0}%
» 🚀 Sᴩᴇᴇᴅ: {3}/s
» ⏰️ Eᴛᴀ: {4} </b>"""

    REX_TXT = "✏️ ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴀ ꜰɪʟᴇ  \n\nꜱᴇɴᴅ ᴀɴʏ ꜰɪʟᴇ ᴀɴᴅ ᴛʏᴘᴇ ɴᴇᴡ ꜰɪʟᴇ ɴᴀᴍᴇ. \n\nᴀɴᴅ ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ꜰᴏʀᴍᴀᴛ [ ᴅᴏᴄᴜᴍᴇɴᴛ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ ]."
    REX2_TXT = "📑ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\n/set_caption : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\n/see_caption : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\n/del_caption : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. \n\nᴇxᴀᴍᴘʟᴇ -  \n/set_caption 📕 ꜰɪʟᴇ ɴᴀᴍᴇ : {ꜰɪʟᴇɴᴀᴍᴇ} \n💾 ꜱɪᴢᴇ : {ꜰɪʟᴇꜱɪᴢᴇ} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ: {ᴅᴜʀᴀᴛɪᴏɴ}"

