

class football_players:
    """
    """
    def __init__(self, name, team, goals, assists, world_cups=[]):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.world_cups = world_cups
    
    def __str__(self):
        return f'{self.name} plays for {self.team} and has scored {self.goals} and assisted {self.assists} times. But will play in {self.world_cups} world cup.'
    