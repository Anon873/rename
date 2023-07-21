import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"➻ ᴍʏ ɴᴀᴍᴇ :<a href=https://t.me/ab0hii>ᴀʙʜɪ</a \n➻ ᴍʏ ᴅᴀᴅ :<a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> \n➻ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ :<a href='https://t.me/Shadowupportx'>ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ</a> \n\n⚜ ꜰᴏʀ ᴀɴɪᴍᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ : \n\n➻ ᴀɴɪᴍᴇ ɪɴ ʜɪɴᴅɪ : <a href='https://t.me/All_Hindi_Anime'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ ʜɪɴᴅɪ : <a href='https://t.me/Anime_In_Hindi_Dub_Only'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ʙᴜʀᴏᴛᴏ ɪɴ ʜɪɴᴅɪ : <a href='https://t.me/Buroto_In_Hindi_Dub'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n➻ ᴢᴇᴇ ᴄᴀꜰᴇ ɪɴ ʜɪɴᴅɪ :<a href='https://t.me/ZEE_CAFE_HINDI_OFFICIAL'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n\n𝗔𝗡𝗜𝗠𝗘 𝗥𝗜𝗩𝗔𝗟𝗦 ⚡️: <a href='https://t.me/Rivals_Anime_Group'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a>\n𝗔𝗡𝗜𝗠𝗘 𝗔𝗥𝗢𝗫𝗫 ⚡️: <a href='https://t.me/Aroxx_network'>ᴄʟɪᴄᴋ ᴛᴏ ᴊᴏɪɴ</a> \n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ᴄᴜꜱᴛᴏᴍ ʙᴏᴛ ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ <a href=https://t.me/it_was_abhi>ᴍʏ ᴅᴀᴅ</a>")
