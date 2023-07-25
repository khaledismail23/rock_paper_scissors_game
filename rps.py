import random
import sys


class Player:
    moves = ["rock", "paper", "scissors"]

    def __init__(self):
        self.score = 0

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(self.moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        while True:
            try:
                move = input("Rock, paper, scissors? ").lower()
                if move in self.moves:
                    return move
                if move == "quit":
                    sys.exit()
            except BaseException:
                sys.exit()


class ReflectPlayer(Player):
    '''
    ReflectPlayer class that remembers what move
    the opponent played last round,
    and plays that move this round.
    '''
    def __init__(self):
        super().__init__()
        self.their_move = random.choice(self.moves)

    def move(self):
        return self.their_move


class CyclePlayer(Player):
    '''
    CyclePlayer class that remembers what move
    it played last round, and cycles through the different moves.
    '''
    def __init__(self):
        super().__init__()
        self.my_move = self.moves[2]

    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        elif self.my_move == self.moves[2]:
            return self.moves[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def beats(self, one, two):
        return (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
        )

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        if self.beats(move1, move2):
            self.p1.score += 1
            print("** PLAYER ONE WINS **")
            print(f"Score: Player One {self.p1.score},")
            print(f"Player Two {self.p2.score}")
        elif move1 == move2:
            self.p1.score = self.p1.score
            self.p2.score = self.p2.score
            print("** TIE **")
            print(f"Score: Player One {self.p1.score},")
            print(f"Player Two {self.p2.score}")
        else:
            self.p2.score += 1
            print("** PLAYER TWO WINS **")
            print(f"Score: Player One {self.p1.score},")
            print(f"Player Two {self.p2.score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        rounds = 5
        print("Game start!")
        print(f"The Game is {rounds} rounds,")
        print("player with the higher score is the winner")
        print('to exit, type "quit" or press ctrl + c')
        print()
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(f"Congratulation, You Won")
        elif self.p2.score > self.p1.score:
            print("Game over!, Player Two Won")
        else:
            print("It's a Tie")
        print("final score:")
        print(f"player one: {self.p1.score}")
        print(f"player two: {self.p2.score}")


def chose_player():
    strategies = {1: Player(), 2: RandomPlayer(),
                  3: ReflectPlayer(), 4: CyclePlayer()}

    while True:
        try:
            print('1) Rock Player')
            print('2) Random Player')
            print('3) Reflect Player')
            print('4) Cycle Player')
            player = int(input('select the player you want to play against: '))
            if player in [1, 2, 3, 4]:
                return strategies[player]
        except BaseException:
            sys.exit()


if __name__ == "__main__":
    game = Game(HumanPlayer(), chose_player())
    game.play_game()
