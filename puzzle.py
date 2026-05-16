import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#0 means no number in cell
numbers = [
	[0,0,21,0,0,0,0,0,0],
	[21,0,0,0,27,0,0,25,0],
	[0,27,0,0,0,15,0,0,9],
	[0,0,0,0,0,0,0,0,0],
	[25,0,0,27,0,45,0,0,9],
	[0,0,0,0,0,0,0,0,0],
	[9,0,0,63,0,0,0,45,0],
	[0,63,0,0,9,0,0,0,288],
	[0,0,0,0,0,0,35,0,0]
]

#1 means green, 0 means white
colors = [
	[1,0,0,1,0,1,0,1,0],
	[0,0,0,1,0,0,1,0,1],
	[1,0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,0,0,1],
	[1,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,1,1],
	[0,0,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0,0],
	[0,1,0,0,1,0,1,0,1]
]

#tl means topleft, br means bottom right, tr means top right, bl means bottom left, na means none
curves = [
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"],
	["na","na","na","na","na","na","na","na","na"]
]

numbers = [[3,0,9,0],
		   [0,0,0,6],
		   [8,0,0,0],
		   [0,6,0,24]]

colors = [[0,1,0,1],
		  [0,0,0,0],
		  [0,1,0,1],
		  [0,0,0,0]]

curves = [["tr","na","tr","na"],
		  ["tl","tr","br","bl"],
		  ["bl","na","bl","na"],
		  ["na","tr","tl","na"]]


class board(object):
	def __init__(self,numbers,colors,curves):
		self.board = []
		for i in range(len(numbers)):
			temp = []
			for j in range(len(numbers[i])):
				color = (0.7,1,0.7) if colors[i][j] == 1 else "white"
				num = None if numbers[i][j] == 0 else numbers[i][j]
				curve = curves[i][j]
				temp.append({"curve":curve, "color": color, "number":num})
			self.board.append(temp)

	def updateCurve(self,i,j,newCurve):
		self.board[i][j]['curve'] = newCurve                  



def drawArch(arch,i,j,cell_size):
	if arch == "tl":
		a = 180
		x,y = (j+1)*cell_size,(i+1)*cell_size
	elif arch == "tr":
		a = 270
		x,y = (j)*cell_size,(i+1)*cell_size
	elif arch == "bl":
		a = 90
		x,y = (j+1)*cell_size,(i)*cell_size
	elif arch == "br":
		a = 0
		x,y = (j)*cell_size,(i)*cell_size
	return patches.Arc((x,y),cell_size*2,cell_size*2,angle=a,theta1=0,theta2=90,lw=2)




def visual(arr,num_rows=4,num_cols=4,cell_size=16,cell_color='white',edge_color='black'):
	ax = plt.gca()
	archs = []
	for i in range(num_rows):
		for j in range(num_cols):
			rect = plt.Rectangle([i*cell_size, j*cell_size], cell_size, cell_size, facecolor=arr[i][j]['color'], edgecolor=edge_color)
			ax.add_patch(rect)
			plt.text(i*cell_size+cell_size/2,j*cell_size+cell_size/2, arr[i][j]['number'],fontsize="40",weight=500,ha="center",va="center")
			if arr[i][j]["curve"] != "na":
				arch = drawArch(arr[i][j]["curve"],i,j,cell_size)
				archs.append(arch)
	for arch in archs:
		ax.add_patch(arch)

	ax.axis('off')
	ax.autoscale_view()
	ax.invert_yaxis()
	ax.set_aspect('equal', 'box')
	ax.xaxis.set_major_locator(plt.NullLocator())
	ax.yaxis.set_major_locator(plt.NullLocator())
	plt.show()


<<<<<<< HEAD
b = board(numbers,colors,curves)
visual(b.board)
=======
def possibleArch(final_board):
    for i in range(len(final_board)):
        for j in range(len(final_board[0])):
            if(final_board[i][j]['val'] != 0):
                print(final_board[i][j]['val'])

visual(final_board)
>>>>>>> 0f9a744be64bffa81e599bd58164c850551ed8ac










