class BoardOwner:
  def __init__(self, id,game_board, board_message,location):
    self.id = id
    self.game_board = game_board
    self.board_message = board_message
    self.location = location
  def id(self):
    return self.id
  def game_board(self):
    return self.game_board

  def board_message(self):
    return self.board_message
  def location(self):
    return self.location

  def down(self):
    if self.location[0]==self.game_board.shape[0]-1:
      self.location[0]=0
    else:
      self.location[0]+=1
    for i in range(self.game_board.shape[0]):
      for k in range(self.game_board.shape[1]):
        self.game_board[i][k]=':white_large_square:'
    self.game_board[self.location[0],self.location[1]]=':smiley:'
    board_message_str=''
    for array in self.game_board:
      board_message_str+='\n'
      for element in array:
        board_message_str+=element
    return board_message_str

  def up(self):
    if self.location[0]==0:
      self.location[0]=self.game_board.shape[0]-1
    else:
      self.location[0]-=1
    for i in range(self.game_board.shape[0]):
      for k in range(self.game_board.shape[1]):
        self.game_board[i][k]=':white_large_square:'
    self.game_board[self.location[0],self.location[1]]=':smiley:'
    board_message_str=''
    for array in self.game_board:
      board_message_str+='\n'
      for element in array:
        board_message_str+=element
    return board_message_str   
  
  def right(self):
    if self.location[1]==self.game_board.shape[1]-1:
      self.location[1]=0
    else:
      self.location[1]+=1
    for i in range(self.game_board.shape[0]):
      for k in range(self.game_board.shape[1]):
        self.game_board[i][k]=':white_large_square:'
    self.game_board[self.location[0],self.location[1]]=':smiley:'
    board_message_str=''
    for array in self.game_board:
      board_message_str+='\n'
      for element in array:
        board_message_str+=element
    return board_message_str


  def left(self):
    if self.location[1]==0:
      self.location[1]=self.game_board.shape[1]-1
    else:
      self.location[1]-=1
    for i in range(self.game_board.shape[0]):
      for k in range(self.game_board.shape[1]):
        self.game_board[i][k]=':white_large_square:'
    self.game_board[self.location[0],self.location[1]]=':smiley:'
    board_message_str=''
    for array in self.game_board:
      board_message_str+='\n'
      for element in array:
        board_message_str+=element
    return board_message_str 
