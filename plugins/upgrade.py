"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 10GB
	(Free hai sur)
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 50GB
	Price ₹20 inr /🌎 0.5$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 100GB
	Price ₹40 inr /🌎 1$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 500GB (Unlimited)
	Price ₹69 inr /🌎 2$  per Month
	
        Contact Admin for payment <a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> <a href=https://t.me/Minato_Bruh>ᴍɪɴᴀᴛᴏ</a>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ab0hii")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 10GB
	(Free hai sur)
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 50GB
	Price ₹20 inr /🌎 0.5$ per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 100GB
	Price ₹40 inr /🌎 1$ per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 500GB (Unlimited)
	Price ₹69 inr /🌎 2$  per Month
	
	Contact Admin for payment <a href=https://t.me/it_was_abhi>ᴀʙʜɪ</a> <a href=https://t.me/Minato_Bruh>ᴍɪɴᴀᴛᴏ</a>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ab0hii")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
