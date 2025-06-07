class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return "Name: "+str(self.name)+"\nAge: "+str(self.age)+"\nPosition: "+str(self.position)

class Team:
 
    def __init__(self, team_name, trainer_name):
        self.team_name = team_name
        self.trainer = trainer_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print("Игрок "+str(player.name)+" добавлен в команду "+str(self.team_name))

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print("Игрок "+str(player.name) +" удален из команды "+str(self.team_name))
        else:
            print("Текущего игрока нет в команде")

    def list_players(self):
        print("")
        print("Trainer: "+str(self.trainer))
        for player in self.players:
                print(player,end=" \n---\n")
        print("")


# Пример использования
if __name__ == "__main__":
    # Создаем игроков
    player1 = Player("Иванов", 25, "Нападающий")
    player2 = Player("Петров", 30, "Полузащитник")
    player3 = Player("Сидоров", 28, "Защитник")

    # Создаем команды
    team1 = Team("Красные", "Краснов")
    team2 = Team("Синие", "Синёв")

    # Добавляем игроков в команды
    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    # Выводим список игроков в командах
    team1.list_players()
    team2.list_players()

    # Удаляем игрока из команды
    team1.remove_player(player2)

    # Выводим обновленный список игроков
    team1.list_players()