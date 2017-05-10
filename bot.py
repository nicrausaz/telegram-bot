import telegram
from telegram.ext import Updater, CommandHandler
from bs4 import BeautifulSoup
import requests

# Request and soup
rankingPage = requests.get('https://www.basketplan.ch/showRankingForLeague.do?leagueHoldingId=5621')
rankingPageTextContent = rankingPage.text
soup = BeautifulSoup(rankingPageTextContent, 'html.parser')
rankings = soup.findAll("tr", {"onmouseout":"resetThisRowColor(this)"})


def start(bot, update):
    chat_id = bot.get_updates()[-1].message.chat_id
    bot.send_message(chat_id=chat_id, text='Welcome ! \nSend me /ranking to get the ranking of Morges Basket\'s group!')

    
    
def ranking(bot, update):
    chat_id = bot.get_updates()[-1].message.chat_id
    
    bot.send_message(chat_id=chat_id, text='Classement:')
    categories = ['Place', 'Équipe', 'Matchs', 'Victoires', 'Défaites', 'FF', 'Marqué', 'Encaissé', 'Score', 'Points']

    for rank in rankings:
        rank = rank.text.split('\n')
        rank = [x for x in rank if x]
        text = ""

        for i in range(len(categories)) :          
            text += "*%s* : _%s_ \r\n" % (categories[i], rank[i])
        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)

    
def table(bot, update):
    button_list = [
    InlineKeyboardButton("col 1", ...),
    InlineKeyboardButton("col 2", ...),
    InlineKeyboardButton("row 2", ...)
    ]
    reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))


updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ranking', ranking))
updater.dispatcher.add_handler(CommandHandler('table', table))

updater.start_polling()
    
