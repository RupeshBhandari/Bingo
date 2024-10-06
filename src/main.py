import random
class Board:
    BOARD_SIZE: int = 5
    RANGES: dict[int, range] = {
        0: range(1,15),#'B'
        1:range(16,30),#'I'
        2:range(31,45),#'N'
        3:range(46,60),#'G'
        4:range(61,75) #'O'        
        }
    
    MIDDLE_SQUARE = (2, 2)
    
    def __init__(self):
        self.board: list[list[int | str]] = [[0] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.grid = self.generate_board()
            
            
    def generate_board(self):
         # Generate numbers for each column
        for col_index in range(len(self.board)):
            # Get the range for the current column
            column_range = self.RANGES[col_index]
            
            # Randomly select 5 unique numbers for this column
            numbers = random.sample(column_range, len(self.board))
            
            # Assign these numbers to the board, but skip the middle square
            for row_index in range(len(self.board)):
                if (row_index, col_index) == self.MIDDLE_SQUARE:
                    self.board[row_index][col_index] = 0  # Free space
                else:
                    self.board[row_index][col_index] = numbers[row_index]

    def print_board(self) -> None|str:
        """Prints the Bingo board in Markdown table format."""
        print('| B     | I     | N     | G     | O     |')
        print('|-------|-------|-------|-------|-------|')
        for row in self.board:
            print('| ' + ' | '.join(f"{str(num):<5}" for num in row) + ' |')

            
    def mark_number(self, number:int) -> None:
        # Mark the number on the board if it exists
        for row_index, row_value in enumerate(iterable=self.board):
            for col_index, col_value in enumerate(iterable=row_value):
                if self.board[row_index][col_index] != number:
                    continue
                self.board[row_index][col_index] = f"({number})"
    
    def check_win(self) -> bool:
        """Check if there's a winning condition (row, column, or diagonal)."""
        # Check rows
        for row_index, row_value in enumerate(self.board):
            if all(isinstance(num, str) and num.startswith("(") and num.endswith(")") for num in row_value):
                print(f'Player won on row {row_index + 1}')
                self.print_board()
                return True

        # Check columns
        for col_index in range(len(self.board[0])):
            if all(isinstance(self.board[row_index][col_index], str) and 
                   self.board[row_index][col_index].startswith("(") and 
                   self.board[row_index][col_index].endswith(")") for row_index in range(len(self.board))):
                print(f'Player won on column {col_index + 1}')
                self.print_board()
                
                return True

        # Check diagonals
        if all(isinstance(self.board[i][i], str) and 
               self.board[i][i].startswith("(") and 
               self.board[i][i].endswith(")") for i in range(len(self.board))):
            print('Player won on the main diagonal')
            self.print_board()
            
            return True

        if all(isinstance(self.board[i][len(self.board) - 1 - i], str) and 
               self.board[i][len(self.board) - 1 - i].startswith("(") and 
               self.board[i][len(self.board) - 1 - i].endswith(")") for i in range(len(self.board))):
            print('Player won on the anti-diagonal')
            self.print_board()
            
            return True

        return False


                
                
class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.board = Board() 
    
    def mark_number(self, number: int):
        # Mark the number on the player's board
        self.board.mark_number(number)
    
    def has_won(self) -> bool:
        # Check if the player has a winning board
        return self.board.check_win()

class Game:
    def __init__(self, num_players: int):
        # Initialize players and the game state
        self.players = [Player(player_id=i) for i in range(num_players)]
        self.drawn_numbers: set[int] = set()
    
    
    def start_game(self):
        # Main game loop: keep drawing numbers and updating player boards
        while len(self.drawn_numbers) < 75:
            number = self.draw_number()
            print(f"Number drawn: {number}")
            self.update_players(number)
            if self.check_for_winner():
                break
        if len(self.drawn_numbers) == 75:
            print("No winner, all numbers drawn.")

    
    def draw_number(self) -> int:
        # Draw a unique number between 1 and 75 that hasn’t been drawn yet
        available_numbers = set(range(1, 76)) - self.drawn_numbers
        if not available_numbers:
            raise ValueError("No more numbers to draw!")
        number = random.choice(list(available_numbers))
        self.drawn_numbers.add(number)
        return number

    
    def update_players(self, number: int) -> None:
        # Notify all players of the drawn number
        for player in self.players:
            player.mark_number(number=number)
            
    def check_for_winner(self) -> bool:
        # Check if any player has won
        for player in self.players:
            if player.has_won():
                print(f"Player {player.player_id+1} wins!")
                return True
        return False

if __name__ == '__main__':
    num_players = int(input("Enter number of players -> "))
    game = Game(num_players=num_players)
    game.start_game()