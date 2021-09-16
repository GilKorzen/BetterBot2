class FourInLine:
  def __init__(self, players,game_board, board_message,first,second):
    self.players = players
    self.game_board = game_board
    self.board_message = board_message
    self.first = first
    self.second = second
  def players(self):
    return self.players
  def game_board(self):
    return self.game_board
  def board_message(self):
    return self.board_message


  def swap(self):
    for key in self.players:
      self.players[key]=not self.players[key]
      print(self.players)
    for key in self.players:
      if self.players[key]:
        if key==str(self.first.id):
          return self.first
        return self.second
  def over(self):
    for key in self.players:
      self.players[key]=False 
  def check_if_over(self):
    for i in range(self.game_board.shape[0]):
      for j in range(self.game_board.shape[1]-3):
        if self.game_board[i][j]==':green_circle:' and self.game_board[i][j]==self.game_board[i][j+1] and self.game_board[i][j]==self.game_board[i][j+2] and self.game_board[i][j]==self.game_board[i][j+3]:
          return 'green'
        elif self.game_board[i][j]==':red_circle:' and self.game_board[i][j]==self.game_board[i][j+1] and self.game_board[i][j]==self.game_board[i][j+2] and self.game_board[i][j]==self.game_board[i][j+3]:
          return 'red'
    for j in range(self.game_board.shape[1]):
      for i in range(self.game_board.shape[0]-3):
        if self.game_board[i][j]==':green_circle:' and self.game_board[i][j]==self.game_board[i+1][j] and self.game_board[i][j]==self.game_board[i+2][j] and self.game_board[i][j]==self.game_board[i+3][j]:
          return 'green'
        elif self.game_board[i][j]==':red_circle:' and self.game_board[i][j]==self.game_board[i+1][j] and self.game_board[i][j]==self.game_board[i+2][j] and self.game_board[i][j]==self.game_board[i+3][j]:
          return 'red'
    for i in range(self.game_board.shape[0]-3):
      for j in range(self.game_board.shape[1]-3):
        if self.game_board[i][j]==':green_circle:' and self.game_board[i][j]==self.game_board[i+1][j+1] and self.game_board[i][j]==self.game_board[i+2][j+2] and self.game_board[i][j]==self.game_board[i+3][j+3]:
          return 'green'
        elif self.game_board[i][j]==':red_circle:' and self.game_board[i][j]==self.game_board[i+1][j+1] and self.game_board[i][j]==self.game_board[i+2][j+2] and self.game_board[i][j]==self.game_board[i+3][j+3]:
          return 'red'
    for i in range(self.game_board.shape[0]-1,2,-1):
      for j in range(self.game_board.shape[1]-3):
        if self.game_board[i][j]==':green_circle:' and self.game_board[i][j]==self.game_board[i-1][j+1] and self.game_board[i][j]==self.game_board[i-2][j+2] and self.game_board[i][j]==self.game_board[i-3][j+3]:
          return 'green'
        elif self.game_board[i][j]==':red_circle:' and self.game_board[i][j]==self.game_board[i-1][j+1] and self.game_board[i][j]==self.game_board[i-2][j+2] and self.game_board[i][j]==self.game_board[i-3][j+3]:
          return 'red'
    return 'no'

  def playing(self,row):
    found=False
    print('checking progress')
    for i in range(self.game_board.shape[0]-1,-1,-1):
      print(self.game_board[i][row])
      if self.game_board[i][row]==':white_circle:':
        found=True
        if list(self.players.values())[0]:
          self.game_board[i][row]=':green_circle:'
        else:
          self.game_board[i][row]=':red_circle:'
        break
    board_message_str=''
    for array in self.game_board:
      board_message_str+='\n'
      for element in array:
        board_message_str+=element
    return board_message_str,found      