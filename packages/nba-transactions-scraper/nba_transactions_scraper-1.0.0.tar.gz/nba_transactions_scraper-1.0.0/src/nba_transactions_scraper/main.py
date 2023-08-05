import pandas as pd
import requests
import re

from bs4 import BeautifulSoup

from nba_api.stats.static import teams

class ProSports_Scraper():
    """ Scraper for Pro sports Transactions Website """
    
    def __init__(self):
        self.url = 'https://www.prosportstransactions.com/basketball/Search/SearchResults.php?'
        self.params = {}
        self.trades_df = pd.DataFrame(columns=['Date', 'Team', 'Acquired', 'Relinquished', 'Notes'])
        self.num_trades_df = pd.DataFrame(columns=['Team', 'Number of Transactions'])
        self.nba_teams= [x['nickname'] for x in teams.get_teams() ]
        
    def get_teams(self):
        # Read in the names of all NBA Teams
        
        self.nba_teams = [x['nickname'] for x in teams.get_teams() ]

    def extract_names(self, in_names):
        in_names = in_names.get_text(strip=True).split('•')
        out_names = []
        for n in in_names:
            #TODO: Add "'". Ex. D'Angelo. Also Add \. for Jr. or D.J.
            reg = re.findall('[A-Z//][\w-]*', n)
            reg = [x for x in reg if x not in self.nba_teams and x != '']
            if reg:
                out_names.append(' '.join(reg))

        if len(out_names) == 0:
            return ''
        elif len(out_names) == 1:
            return out_names[0].split('/')[0]
        else:
            #return ', '.join(out_names)
            return out_names
        
    def run(self, team, start, end=None, ):

        self.params['Player'] = None
        
        if team == 'Trail Blazers':
            self.params['Team'] = 'Blazers'
        else:
            self.params['Team'] = team
            
        self.params['BeginDate'] = start
        self.params['EndDate'] = end
        self.params['PlayerMovementChkBx'] = 'yes'
        self.params['Submit'] = 'Search'
        self.params['start'] = 0
        status_code = 200
        num_transactions = 0
        
        self.get_teams()

        self.num_trades_df['Team'] = self.nba_teams
        self.num_trades_df = self.num_trades_df.set_index('Team')
        

        try:
            while(status_code == 200):
                r = requests.get(self.url, self.params)

                status_code = r.status_code
                soup = BeautifulSoup(r.content, 'html.parser')
                table = soup.find('table')

                rows = table.find_all('tr')
                data = []
                flags = ['coach', 'president', 'executive', 'scout', 'coordinator', \
                            'director', 'trainer', 'manager', 'therapist']
                for row in rows:
                    cols = row.find_all('td')
                    
                    cols[2], cols[3] = self.extract_names(cols[2]), self.extract_names(cols[3])

                    cols = [x.get_text(strip=True).replace('•', '') 
                            if not isinstance(x, str) and not isinstance(x, list)
                            else x for x in cols]
                    
                    #Checks Notes index for non-player flags
                    skip = any(x in cols[-1] for x in flags)
                    if not skip:
                        data.append(cols) 

                num_transactions += len(data)

                if len(data) == 1: 
                    break

                temp_df = pd.DataFrame.from_records(data[1:], columns=data[0])
                self.trades_df = pd.concat([self.trades_df, temp_df], ignore_index=True)
                self.trades_df = self.trades_df.explode('Acquired').explode('Relinquished')
                self.params['start'] += 25

        
        except:
            print("Error on:", team)
            raise

        return self.trades_df


