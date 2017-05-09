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
    for i in range(0,5) :
        rank = rankings[i].text.split('\n')
        rank = [x for x in rank if x]

        print(rank)

    # test = ['', '1', '', 'Morges TEAM COSMO U19', '', '9', '8', '1', '0', '778', '490', '288', '17', '']
    # test.pop(0)
    # print(test)

    #for rank in rankings:
        # print(rank.text)
        # print(rank.text.split('\n'))
        # rank.pop(0)
        # print(rank.text)
    #     rank.pop(2)
    #     rank.pop(13)
    #     print(rank)
    #     update.message.reply_text(categories[i] + " : " + rank.text)
    #     i += 1

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