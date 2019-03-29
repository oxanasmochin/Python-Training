class lotteryPlayer() :
    def __init__(self, name):
        self.name = name
        self.numbers = (12, 10, 34, 81, 5)

    def total(self):
        return sum(self.numbers)

player_one = lotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 4, 6, 7, 8)  #change the tuple numbers of player_one
player_two = lotteryPlayer("John")

print(player_one == player_two)
print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)
