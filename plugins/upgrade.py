"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 30GB
	Price Rs 20  ind /🌎 0.5$ per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 300GB
	Price Rs 50  ind /🌎 1$ per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 1000GB 
	Price Rs 100  ind /🌎 2$ per Month
	
	
	Pay Using Upi I'd ```abhidarkside01@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mRiderDM"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ab0hii")], 
        			[InlineKeyboardButton("Paytm",url = "Contact admin for payment"),
        			InlineKeyboardButton("Btc",url = "Contact admin for payment")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 20  ind /🌎 0.5$ per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 300GB
	Price Rs 50  ind /🌎 1$ per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 100  ind /🌎 2$ per Month
	
	
	Pay Using Upi I'd ```(kindly contact admin)```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mRiderDM"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ab0hii")], 
        			[InlineKeyboardButton("Paytm",url = "Contact admin for payment"),
        			InlineKeyboardButton("Btc",url = "Contact admin for payment")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
