from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ тєαм ɾιყα 

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏʀ ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ 3 ɢᴄ ᴍᴀɪ ᴀᴅᴅ ᴋᴀʀ ᴋᴇ 

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ ᴋᴏ ᴅᴏ ғɪʀ ʀᴇᴘᴏ ᴍɪʟ sᴀᴋᴛɪ ʜᴀɪ 

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("♡ α∂∂ иσω ♡", url=f"https://t.me/Jani_Music_Robot?start=help")
        ],
        [
          InlineKeyboardButton("ѕυρρσɾƚ", url="https://t.me/+AaI_GATiYwQ5NjU1"),
          InlineKeyboardButton("‷𓆩᪵⟶͇̽[ɪ⃪ϻ̱̱֯༏𐏓⃪꯭𓆩꯭𝗝꯭ᴀ꯭፝֟͠ɴ꯭ɪ꯭꯭ ꯭꯭꯭꯭꯭꯭𔘓꯭𓃭͜ ⃟⛦⃕ ̶꯭𝅥ͦ𝆬 ⃪͢,", url="http://t.me/Jani_RP_Lover"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/Jani_RP"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/+AaI_GATiYwQ5NjU1"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/5aj1rl.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
