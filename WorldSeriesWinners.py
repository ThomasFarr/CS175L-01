#Thomas Farrell
#CS 175L 01
#World_Series

file = open('WorldSeriesWinners.txt','r')
teams_won = []
for line in file:
    line = line.rstrip('\n')
    teams_won.append(line)

team_names = [*set(teams_won)]
print (team_names)
        
def search():
    team = input('Enter the name of a team: ')
    series_winners = [item for item in teams_won if item.lower() == team.lower()]
    win_count = (len(series_winners))
    
    if win_count > 0:
        print('The '+team+' won the world series '+str(win_count)+' times between 1903 and 2009.')
    else:
        print ('Team not found')
        
    repeat()

def repeat():
    again = input('Enter continue or quit: ')

    if again == 'quit' or again == 'Quit':
        print ('Bye')
    elif again == 'continue' or again == 'Continue':
        search()
    else:
        print ('Invalid response, please enter continue or quit: ')

if __name__ == '__main__':
    search()




