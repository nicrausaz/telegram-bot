from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

rankingPage = requests.get('https://www.basketplan.ch/showRankingForLeague.do?leagueHoldingId=5621')

rankingPageTextContent = rankingPage.text
soup = BeautifulSoup(rankingPageTextContent, 'html.parser')

rankings = soup.findAll("tr", {"onmouseout":"resetThisRowColor(this)"})

categories = {'Rank', 'Team', 'Games', 'Win', 'Loose', 'FF', 'Scored', 'Encaissé','Score', 'Points'}

def start(bot, update):
    update.message.reply_text('Welcome ! Send me /ranking to get the ranking of Morges Basket!')

def ranking(bot, update):
    update.message.reply_text('Rankings:')
    for rank in rankings:
        update.message.reply_text(rank.text)
 

updater = Updater('388939599:AAEEarbs86EH7_jCmhQY2WAzzJa-6Wg0hrk')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ranking', ranking))

updater.start_polling()