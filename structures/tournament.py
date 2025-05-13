import random
from structures.stack import Stack
from structures.queue import Queue
from structures.singly_linked_list import SinglyLinkedList
from structures.doubly_linked_list import DoublyLinkedList
from structures.double_circular_list import DoubleCircularList

class Tournament:
    def __init__(self, players):
        self.players = players
        self.wins = {p: Stack() for p in players}
        self.history = {p: SinglyLinkedList() for p in players}
        self.duels = DoublyLinkedList()
        self.matches = DoubleCircularList()
        self.rounds = []

    def start(self):
        queue = Queue()
        for p in self.players:
            queue.enqueue(p)

        current_round = 1
        while len(self.players) > 1:
            round_pairs = []
            next_round = []
            while not queue.is_empty():
                p1 = queue.dequeue()
                p2 = queue.dequeue()
                if p2:
                    winner = random.choice([p1, p2])
                    loser = p2 if winner == p1 else p1
                    self.wins[winner].push(f"won against {loser}")
                    self.history[winner].add(f"Round {current_round}: beat {loser}")
                    self.history[loser].add(f"Round {current_round}: lost to {winner}")
                    self.duels.add((p1, p2))
                    self.matches.add((p1, p2))
                    next_round.append(winner)
                    round_pairs.append((p1, p2))
            self.players = next_round
            for p in next_round:
                queue.enqueue(p)
            self.rounds.append(round_pairs)
            current_round += 1

    def show(self):
        for player, stack in self.wins.items():
            print(f"{player}:")
            for item in stack.to_list():
                print("  ", item)