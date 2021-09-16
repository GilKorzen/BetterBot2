class TicTacToe:
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
      for j in range(self.game_board.shape[1]-2):
        if self.game_board[i][j]==':o:' and self.game_board[i][j]==self.game_board[i][j+1] and self.game_board[i][j]==self.game_board[i][j+2]:
          return 'o'
        elif self.game_board[i][j]==':x:' and self.game_board[i][j]==self.game_board[i][j+1] and self.game_board[i][j]==self.game_board[i][j+2]:
          return 'x'
    for j in range(self.game_board.shape[1]):
      for i in range(self.game_board.shape[0]-2):
        if self.game_board[i][j]==':o:' and self.game_board[i][j]==self.game_board[i+1][j] and self.game_board[i][j]==self.game_board[i+2][j]:
          return 'o'
        elif self.game_board[i][j]==':x:' and self.game_board[i][j]==self.game_board[i+1][j] and self.game_board[i][j]==self.game_board[i+2][j]:
          return 'x'
    for i in range(self.game_board.shape[0]-2):
      for j in range(self.game_board.shape[1]-2):
        if self.game_board[i][j]==':o:' and self.game_board[i][j]==self.game_board[i+1][j+1] and self.game_board[i][j]==self.game_board[i+2][j+2]:
          return 'o'
        elif self.game_board[i][j]==':x:' and self.game_board[i][j]==self.game_board[i+1][j+1] and self.game_board[i][j]==self.game_board[i+2][j+2]:
          return 'x'
    for i in range(self.game_board.shape[0]-1,1,-1):
      for j in range(self.game_board.shape[1]-2):
        if self.game_board[i][j]==':o:' and self.game_board[i][j]==self.game_board[i-1][j+1] and self.game_board[i][j]==self.game_board[i-2][j+2]:
          return 'o'
        elif self.game_board[i][j]==':x:' and self.game_board[i][j]==self.game_board[i-1][j+1] and self.game_board[i][j]==self.game_board[i-2][j+2]:
          return 'x'
    for i in range(self.game_board.shape[0]):
      for j in range(self.game_board.shape[1]):
        if not self.game_board[i][j] in ':o:x:':
          return 'no'
    return 'yes'

  def playing(self,num):
    found=False
    if not self.game_board[num//3][num%3] in ':x:o:':
      found=True
      if list(self.players.values())[0]:
        self.game_board[num//3][num%3]=':x:'
      else:
        self.game_board[num//3][num%3]=':o:'
    board_message_str=''
    for array in self.game_board:
      board_message_str+='\n\n'
      for element in array:
        board_message_str+=element+'          '
    return board_message_str,found      