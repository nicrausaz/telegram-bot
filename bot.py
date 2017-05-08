from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

rankingPage = requests.get('https://www.basketplan.ch/showRankingForLeague.do?leagueHoldingId=5621')

rankingPageTextContent = rankingPage.text
soup = BeautifulSoup(rankingPageTextContent, 'html.parser')
rankings = soup.findAll("td", { "class" : "txt8" })


def start(bot, update):
    update.message.reply_text('Welcome ! Send me /ranking to get the ranking of Morges Basket!')

def ranking(bot, update):
    categories = {'Rank', 'Team', 'Games', 'Win', 'Loose', 'FF', 'Scored', 'Encaissé','Score', 'Points'}
    update.message.reply_text('Rankings:')
    for rank in rankings :
        update.message.reply_text(rank.text)

    


# def ranksInfos():

 

updater = Updater('388939599:AAEEarbs86EH7_jCmhQY2WAzzJa-6Wg0hrk')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ranking', ranking))

updater.start_polling()

# exemple of recup                      
'''
<table border="0" cellspacing="0" cellpadding="2" width="740" class="forms">

            <tr onmouseover="highlightThisRowColor(this,'C0CDD6')" onmouseout="resetThisRowColor(this)">
                <td class="txt8"><SPAN class="margin">1</SPAN></td>
                <td class="txt8">
                    <a href="/findTeamById.do?teamId=321" class="a_txt8">Morges TEAM COSMO U19</a>
                </td>
                <td class="txt8">9</td>
                <td class="txt8">8</td>
                <td class="txt8">1</td>
                <td class="txt8">0</td>
                <td class="txt8">778</td>
                <td class="txt8">490</td>
                <td class="txt8">288</td>
                
                
                <td class="txt8">17</td>
            </tr>
        
        
        
        
        
    
        
        
            <tr onmouseover="highlightThisRowColor(this,'C0CDD6')" onmouseout="resetThisRowColor(this)">
                <td class="txt8"><SPAN class="margin">2</SPAN></td>
                <td class="txt8">
                    <a href="/findTeamById.do?teamId=1448" class="a_txt8">Blonay 2</a>
                </td>
                <td class="txt8">9</td>
                <td class="txt8">6</td>
                <td class="txt8">3</td>
                <td class="txt8">0</td>
                <td class="txt8">613</td>
                <td class="txt8">456</td>
                <td class="txt8">157</td>
                
                
                <td class="txt8">15</td>
            </tr>
        
        
        
        
        
    
        
        
            <tr onmouseover="highlightThisRowColor(this,'C0CDD6')" onmouseout="resetThisRowColor(this)">
                <td class="txt8"><SPAN class="margin">3</SPAN></td>
                <td class="txt8">
                    <a href="/findTeamById.do?teamId=1609" class="a_txt8">Vevey Riviera</a>
                </td>
                <td class="txt8">8</td>
                <td class="txt8">6</td>
                <td class="txt8">2</td>
                <td class="txt8">0</td>
                <td class="txt8">450</td>
                <td class="txt8">392</td>
                <td class="txt8">58</td>
                
                
                <td class="txt8">14</td>
            </tr>
        
        
        
        
        
    
        
        
            <tr onmouseover="highlightThisRowColor(this,'C0CDD6')" onmouseout="resetThisRowColor(this)">
                <td class="txt8"><SPAN class="margin">4</SPAN></td>
                <td class="txt8">
                    <a href="/findTeamById.do?teamId=4119" class="a_txt8">St Prex</a>
                </td>
                <td class="txt8">9</td>
                <td class="txt8">4</td>
                <td class="txt8">5</td>
                <td class="txt8">0</td>
                <td class="txt8">486</td>
                <td class="txt8">560</td>
                <td class="txt8">-74</td>
                
                
                <td class="txt8">13</td>
            </tr>
        
        
        
        
        
    
        
        
            <tr onmouseover="highlightThisRowColor(this,'C0CDD6')" onmouseout="resetThisRowColor(this)">
                <td class="txt8"><SPAN class="margin">5</SPAN></td>
                <td class="txt8">
                    <a href="/findTeamById.do?teamId=4116" class="a_txt8">Lausanne Ouest</a>
                </td>
                <td class="txt8">8</td>
                <td class="txt8">2</td>
                <td class="txt8">6</td>
                <td class="txt8">0</td>
                <td class="txt8">378</td>
                <td class="txt8">519</td>
                <td class="txt8">-141</td>
                
                
                <td class="txt8">10</td>
            </tr>
        
        
        
        
        
    
        
        
            <tr onmouseover="highlightThisRowColor(this,'C0CDD6')" onmouseout="resetThisRowColor(this)">
                <td class="txt8"><SPAN class="margin">6</SPAN></td>
                <td class="txt8">
                    <a href="/findTeamById.do?teamId=4118" class="a_txt8">Gland</a>
                </td>
                <td class="txt8">9</td>
                <td class="txt8">0</td>
                <td class="txt8">9</td>
                <td class="txt8">0</td>
                <td class="txt8">404</td>
                <td class="txt8">692</td>
                <td class="txt8">-288</td>
                
                
                <td class="txt8">9</td>
            </tr>
        
        
        
        
        
    
    
    
    
    <!-- Errors -->
        
</table>
'''