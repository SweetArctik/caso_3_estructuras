class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.loser = None

    def play(self):
        if self.player1.skill >= self.player2.skill:
            self.winner = self.player1
            self.loser = self.player2
        else:
            self.winner = self.player2
            self.loser = self.player1
        self.winner.add_win(self.loser)
        self.winner.add_event(f"Beat {self.loser.name}")
        self.loser.add_event(f"Lost to {self.winner.name}")