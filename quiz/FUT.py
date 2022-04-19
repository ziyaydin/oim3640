PLAYERS = {
    'Karim Benzema': 93, # player's name: his rating
    'Robert Lewandowski': 94,
    'Kylian Mbappe': 97,
    'Luka Modric': 90,
    'Pedri': 93,
    'Pique': 88,
}

LEGENDARIES = {
    'Lionel Messi': (98, 1.1), # legendary player's name: (his rating, his chemistry booster value)
    'Cristiano Ronaldo': (97, 1.05),
}


class Team:
    """FIFA Ultimate Team"""

    def __init__(self, name, initial_players=None):
        """Initialize team and update squad and information if initial_players is provided
        name: string
        initial_players: a list of strings representing initial players in this team.
        """
        # self.name = name
        # self.squad = PLAYERS.keys()
        # self.rating = sum(PLAYERS.values())/len(PLAYERS)
        # if self.squad == None:
        #     self.squad = []
        #     self.rating = 0
        # else:
        #     for key, value in PLAYERS.items():
        #         self.squad[value] = key
        self.name = name
        self.squad = PLAYERS.keys()
        self.rating = sum(PLAYERS.values())/len(PLAYERS)
        if initial_players != None:
            self.initial_players = initial_players

    def __str__(self):
        """Return a string representation of this team, including team name and squad."""
        # return self.name
        t = [ self.name + 'has']
        if self.squad == []:
            return "no player yet."
        else:
            for obj in self.squad:
                s = '    ' + object.__str__(obj)
                t.append(s)
            return '\n'.join(t)


    def choose(self, player):
        """choose one player from PLAYERS and update team's rating which is the average rating of entire current squad.
        player: string
        """
        self.squad.append(player)
        if player in PLAYERS.keys():
            pass



    def choose_legendary(self, player):
        """choose one player from LEGENDARIES and update team's rating which is the average rating of entire current squad multiplied by legendary's booster.
        player: string
        """
        self.squad.append(player)
        if player in LEGENDARIES.keys():
            pass

    def __greaterthan__(self, other):
        if self.rating > other.rating:
            return True
        else:
            return False
#############################################
# Please DO NOT change code in main function!
#############################################
def main():
    real_madrid = Team('Real Madrid', initial_players=['Karim Benzema'])
    barcelona = Team('Barcelona')
    print('Before choosing squad:')
    print(real_madrid)
    print(barcelona)
    print()
    print('After choosing squad:')
    real_madrid.choose('Luka Modric')
    real_madrid.choose('Kylian Mbappe')
    barcelona.choose('Pique')
    barcelona.choose('Pedri')
    barcelona.choose('Robert Lewandowski')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)
    print()
    print('After choosing legendary:')
    real_madrid.choose_legendary('Cristiano Ronaldo')
    barcelona.choose_legendary('Lionel Messi')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)


if __name__ == '__main__':
    main()