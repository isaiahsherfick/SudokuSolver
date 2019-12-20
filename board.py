class board:
	#Creates a n-dimensional board filled with -1s
	def __init__(self, n):
		self.width = n
		self.height = n
		newboard = []
		for i in range(n):
			newlst = []
			for j in range(n):
				newlst += [-1]
			newboard += newlst
		self.board = newboard

	def print(self):	
		print(self.board)

b = board(3)
b.print()
