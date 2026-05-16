import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

archs = ["none","topleft","topright","bottomleft","bottomright"]

board = [
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

final_board = []

for i in range(len(board)):
	temp_board = []
	for j in range(len(board[i])):
		color = (0.70,1,0.7) if colors[i][j] == 1 else "white"
		num = None if board[i][j] == 0 else board[i][j]
		temp_board.append({"cv":"none", "color": color, "val":num})
	final_board.append(temp_board)                      
	
	
print(final_board[0])




def drawArch(arch,i,j):

	if arch == "topleft":
		t1,t2 = 90,180
		x,y = (j+1)*16,(i+1)*16
	elif arch == "topright":
		t1,t2 = 180,270
		x,y = (j)*16,(i+1)*16 
	elif arch == "bottomleft":
		t1,t2 = 0,90
		x,y = (j+1)*16,(i)*16 
	elif arch == "bottomright":
		t1,t2 = 270,360
		x,y = (j)*16,(i)*16

	return patches.Arc((x,y),32,32,angle=90,theta1=t1,theta2=t2)

def visual(arr,num_rows=9,num_cols=9,cell_size=16,cell_color='white',edge_color='black'):
	ax = plt.gca()

	for i in range(num_cols):
		for j in range(num_rows):

			rect = plt.Rectangle([j*16, i*16], cell_size, cell_size,facecolor=arr[i][j]['color'],edgecolor=edge_color)
			ax.add_patch(rect)
			if not arr[i][j]["cv"] == "none":
				arch = drawArch(arr[i][j]["cv"],j,i)
				ax.add_patch(arch)
			# e1 = patches.Arc((1*16, 1*16),32,32,angle=90,theta1=90,theta2=180)
			# e2 = patches.Arc((0*16, 1*16),32,32,angle=90,theta1=180,theta2=270)
			# e3 = patches.Arc((1*16, 1*16),32,32,angle=90,theta1=270,theta2=360)
			# e4 = patches.Arc((1*16, 1*16),32,32,angle=90,theta1=0,theta2=90)
			
			# ax.add_patch(e1)
			# ax.add_patch(e2)
			# ax.add_patch(e3)
			# ax.add_patch(e4)
			plt.text(j*16+8,i*16+8, arr[i][j]['val'],fontsize="12",ha="center")

	ax.axis('off')
	ax.autoscale_view()
	ax.invert_yaxis()
	ax.set_aspect('equal', 'box')
	ax.xaxis.set_major_locator(plt.NullLocator())
	ax.yaxis.set_major_locator(plt.NullLocator())
	plt.show()


def possibleArch(final_board):
    for i in range(len(final_board)):
        for j in range(len(final_board[0])):
            if(final_board[i][j]['val'] != 0):
                print(final_board[i][j]['val'])

visual(final_board)










