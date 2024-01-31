import requests
from telegram import ParseMode
from telegram.ext import CommandHandler
import random
from MukeshRobot import dispatcher
 

def waifu(update, context):
    try:
        msg = update.effective_message
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        text = f'''
<b>Name :</b> <code>{result['Character_Name']}</code>
        
<b>Anime :</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)


WAIFUINFO_HANDLER = CommandHandler('waifuinfo', waifu, run_async=True)
dispatcher.add_handler(WAIFUINFO_HANDLER)

__mod_name__ = 'Waifus'
__help__ = '''
*Get waifu images*

   ➢ `/waifu`*:* Sends limited but best Waifu image. *RECOMMENDED*
   ➢ `/waifuinfo`*:* Gives random image of waifu with info. 
   ➢ `/waifus`*:* Sends Random Waifu image.
   ➢ `/swaifu`*:* Sends Random Waifu image.

   *NSFW CONTENT*
   ➢ `/nsfwwaifu`
   ➢ `/nwaifu`  
'''

# DON'T EDIT
__handlers__ = [WAIFUINFO_HANDLER]
