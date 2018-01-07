import os
# Python Techdegree Project 01 - Soccer Team - Lukas Straumann


def import_raw_data():
    with open('soccer_players.csv',newline='') as csvfile:
        lines = csvfile.readlines()
    header = lines[0].split(',')
    del lines[0] #delete header from the list of lines    

    soccer_players = []
    for line in lines: # loop through line to add players
        player = {}
        index = 0
        words_in_line = line.split(',')
        for key in header:
            player.update({key.replace('\r\n',''):words_in_line[index].replace('\r\n','')})
            index += 1
        soccer_players.append(player)
    return soccer_players


def split_list(soccer_players):
    experienced_players = []
    inexperienced_players = []
    for soccer_player in soccer_players:
        if soccer_player['Soccer Experience']=='YES':
            experienced_players.append(soccer_player)
            number_of_exp_players = len(experienced_players)
        elif soccer_player['Soccer Experience']=='NO':
            inexperienced_players.append(soccer_player)
    return experienced_players, inexperienced_players

def assign_players(experienced_players,inexperienced_players):
    soccer_players_assigned = []
    team_index = 0
    while len(experienced_players) > 0:
        if team_index == len(teams):  # reset the index
            team_index = 0
        player = experienced_players[0] 
        player.update({'Team':teams[team_index]})  # add to one of of three teams
        soccer_players_assigned.append(player)
        del experienced_players[0]
        team_index += 1
    team_index = 0
    while len(inexperienced_players) > 0:
        if team_index == len(teams):
            team_index = 0
        player = inexperienced_players[0]
        player.update({'Team':teams[team_index]})
        soccer_players_assigned.append(player)
        del inexperienced_players[0]
        team_index += 1
    return soccer_players_assigned
 
# write to file
def writing_to_file(league,teams,soccer_players_assigned):  # Write a list of the teams
    f = open('teams.txt', 'w')
    f.write('{}:\n\n'.format(league))
    for team in teams:
        f.write('Team: {}\n'.format(team))
        for player in soccer_players_assigned:
            if player['Team'] == team:
                f.write('{}, {}, {}\n'.format(player['Name'],
                                              player['Soccer Experience'],
                                              player['Guardian Name(s)']))
        f.write('\n')
    f.close()

def create_a_folder(rel_path):
    try:
        if not os.path.exists(rel_path):
            os.makedirs(rel_path)
    except OSError:
        print('Error: Creating path '.format(path))

def writing_files(soccer_players_assigned):  # Create invite letter files
    rel_path = './letters/'
    create_a_folder(rel_path)
    for player in soccer_players_assigned:
        path = os.path.join(rel_path,'{}.txt'.format(player['Name'].lower().replace(' ','_')))
        f = open(path, 'w')
        f.write('Dear {}\n\n'.format(player['Name']))
        f.write('''Welcome to this year's soccer season. We're going
to have a great time. You will be strengthening
the {} team.

Please be ready for the first practice at the 66 Star
soccer field on the 6th of June at 6 pm.

We look forward to playing great scoccer with you and polishing
our skills.

Your trainer,
Lukas'''.format(player['Team']))
        f.close()
        
    
# main
if __name__ == "__main__":
    league = 'League Roster'
    teams = ['Dragons','Sharks','Raptors']
    soccer_players = import_raw_data()
    experienced_players,inexperienced_players = split_list(soccer_players)
    soccer_players_assigned = assign_players(experienced_players,inexperienced_players)
    writing_to_file(league,teams,soccer_players_assigned)

    writing_files(soccer_players_assigned)  # Extra Credits
    
    

