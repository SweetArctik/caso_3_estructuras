import json
import os
from system.player import Player
from system.tournament import Tournament

class TournamentManager:
    def __init__(self):
        self.players = []

    def menu(self):
        while True:
            print("\n=== Tournament System ===")
            print("1. Enter players")
            print("2. Start tournament")
            print("3. Show saved champion")
            print("4. Exit")
            choice = input("Option: ")

            if choice == "1":
                self.players.clear()
                print("Type 'end' to finish input.")
                while True:
                    name = input("Player name: ")
                    if name.lower() == "end":
                        break
                    self.players.append(Player(name))
                if len(self.players) < 2 or len(self.players) % 2 != 0:
                    print("Enter even number of players (at least 2).")
                    self.players.clear()

            elif choice == "2":
                if not self.players:
                    print("No players entered.")
                    continue
                tournament = Tournament(self.players.copy())
                tournament.run()
                tournament.show_results()
                self.save_champion(tournament.champion)

            elif choice == "3":
                self.load_champion()

            elif choice == "4":
                break

    def save_champion(self, champion, folder="data"):
        os.makedirs(folder, exist_ok=True)
        data = {"champion": champion.name, "skill": champion.skill}
        with open(os.path.join(folder, "champion.json"), "w") as f:
            json.dump(data, f)

    def load_champion(self, folder="data"):
        path = os.path.join(folder, "champion.json")
        if not os.path.exists(path):
            print("No saved champion.")
            return
        with open(path, "r") as f:
            data = json.load(f)
        print(f"Last Champion: {data['champion']} (Skill: {data['skill']})")