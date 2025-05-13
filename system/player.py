import random

class Player:
    def __init__(self, name):
        self.name = name
        self.skill = random.randint(1, 100)
        self.events = []
        self.wins = []

    def add_event(self, description):
        self.events.append(description)

    def add_win(self, opponent):
        self.wins.append(f"won against {opponent.name}")