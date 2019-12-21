import sys
class board:
	#Creates an n-dimensional board filled with -1s
	def __init__(self, n):
		self.rows = n
		self.columns = n
		newboard = []
		for i in range(n):
			newlst = []
			for j in range(n):
				newlst.append(-1)
			newboard.append(newlst)
		self.board = newboard

	def print(self):	
		for i in range(self.rows):
			for j in range(self.columns):
				sys.stdout.write(str(self.board[i][j]) + " ")
		sys.stdout.write("\n\n")
b = board(9)
b.print()
