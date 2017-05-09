from telegram.ext import Updater, CommandHandler
from bs4 import BeautifulSoup
import requests

rankingPage = requests.get('https://www.basketplan.ch/showRankingForLeague.do?leagueHoldingId=5621')

rankingPageTextContent = rankingPage.text
soup = BeautifulSoup(rankingPageTextContent, 'html.parser')

rankings = soup.findAll("tr", {"onmouseout":"resetThisRowColor(this)"})


def start(bot, update):
    update.message.reply_text('Welcome ! \nSend me /ranking to get the ranking of Morges Basket\'s group!')

def ranking(bot, update):
    categories = ['Rank', 'Team', 'Games', 'Win', 'Loose', 'FF', 'Scored', 'Encaissé','Score', 'Points']
    update.message.reply_text('Rankings:')

    

    for rank in rankings:
        rank = rank.text.split('\n')
        rank = [x for x in rank if x]
        text = ""
        
        for i in range(len(categories)) :          

            text += "%s : %s " % (categories[i], rank[i])

        update.message.reply_text(text)
def table(bot, update):
    button_list = [
    InlineKeyboardButton("col 1", ...),
    InlineKeyboardButton("col 2", ...),
    InlineKeyboardButton("row 2", ...)
    ]
    reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))


updater = Updater('388939599:AAEEarbs86EH7_jCmhQY2WAzzJa-6Wg0hrk')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ranking', ranking))
updater.dispatcher.add_handler(CommandHandler('table', table))

updater.start_polling()