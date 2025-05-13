from structures.stack import Stack
from structures.queue import Queue
from structures.singly_linked_list import SinglyLinkedList
from structures.doubly_linked_list import DoublyLinkedList
from structures.double_circular_list import DoubleCircularList
from system.match import Match

class Tournament:
    def __init__(self, players):
        self.players = players
        self.stack_wins = {p.name: Stack() for p in players}
        self.history = {p.name: SinglyLinkedList() for p in players}
        self.duels = DoublyLinkedList()
        self.matches = DoubleCircularList()
        self.rounds = []
        self.champion = None

    def run(self):
        queue = Queue()
        for player in self.players:
            queue.enqueue(player)

        while len(self.players) > 1:
            next_round = []
            round_matches = []
            while not queue.is_empty():
                p1 = queue.dequeue()
                p2 = queue.dequeue()
                if not p2:
                    next_round.append(p1)
                    continue
                match = Match(p1, p2)
                match.play()
                self.stack_wins[match.winner.name].push(f"won against {match.loser.name}")
                self.history[match.winner.name].add(f"Beat {match.loser.name}")
                self.history[match.loser.name].add(f"Lost to {match.winner.name}")
                self.duels.add((p1.name, p2.name))
                self.matches.add((p1.name, p2.name))
                next_round.append(match.winner)
                round_matches.append((p1.name, p2.name))
            self.players = next_round
            for p in next_round:
                queue.enqueue(p)
            self.rounds.append(round_matches)
        self.champion = self.players[0]

    def show_results(self):
        for name, stack in self.stack_wins.items():
            print(f"{name}:")
            for win in stack.to_list():
                print("  ", win)
        print(f"Champion: {self.champion.name} with skill {self.champion.skill}")