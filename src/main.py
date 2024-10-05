import random

import numpy
class Board:
    BOARD = numpy.zeros(shape=[5,5], dtype=int)
    
    def __init__(self) -> None:
        self.max_number = 75
    
    @property
    def get_maxno(self) -> int:
        return self.max_number
    
    @get_maxno
    def set_maxno(self, maximum_number: int) -> None:
        self.max_number = maximum_number
        
    
class Player:
    PLAYER_LIST: list[int] = []
    def __init__(self, player_id:int) -> None:
        self.PLAYER_LIST.append(player_id)

class Game:
    def __init__(self, players: int) -> None:
        self.load_start_text()
        for i in range(players):
            i = Player(player_id=i)
    
    @staticmethod
    def load_start_text() -> None:
        print('Game Started')

if __name__ == '__main__':
    players:int = int(input('Enter no of players > '))
    Game(players=players)
    print(numpy.zeros(shape=[5,5], dtype=int))
    