import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpltlb

class interactiveGraphCreator:
    def setText(self, s):
        plt.title(s, fontsize=16)
        plt.draw()
        
    def createGraph(self):  
        def press(event):
            if event.key==None:
                return
            if event.key not in keys and not (48<=ord(event.key)<=57):
                return
        
            nonlocal curr1
            nonlocal curr2
            nonlocal first
            nonlocal directed
            
            if event.key.isalpha():
                if event.key=='n':
                    first = False
                    self.setText(f'Second vertice: {curr2}, to add an edge click \'a\'')
                elif event.key=='backspace':
                    if first:
                        curr1//=10
                        self.setText(f'First vertice: {curr1}, to choose second vertice click \'n\'')
                    else:
                        curr2//=10
                        self.setText(f'Second vertice: {curr2}, to add an edge click \'a\'')     
                elif event.key=='a':
                    if curr1>len(pts)-1:
                        self.setText(f'First vertice: {curr1} cannot be bigger than points number')
                        return
                    elif curr2>len(pts)-1:
                        self.setText(f'Second vertice: {curr2} cannot be bigger than points number')
                        return
                    if curr1 == curr2:
                        curr1=0
                        curr2=0
                        first=True
                        return
                    if len(pts)<curr1 or len(pts)<curr2:
                        curr1=0
                        curr2=0
                        first=True
                        return
                    edges.append((curr1,curr2))
                    if directed:
                        line = plt.annotate("", xy=(pts[curr2][0], pts[curr2][1]), xytext=(pts[curr1][0], pts[curr1][1]), arrowprops=dict(arrowstyle="->", linewidth=2, mutation_scale=20))
                        lineStack.append((line,(curr1,curr2)))
                    else:
                        line = plt.plot([pts[curr1][0], pts[curr2][0]], [pts[curr1][1], pts[curr2][1]], linewidth=2, color = "black")
                        lineStack.append((line[0],(curr1,curr2)))
                    plt.draw()
                    curr1=0
                    curr2=0
                    first=True
                    self.setText(f'First vertice: {curr1}, to choose second vertice click \'n\'')
                elif event.key=='b':
                    curr2=0
                    first=True
                    self.setText(f'First vertice: {curr1}, to choose second vertice click \'n\'')
                elif event.key=='z':
                    if len(lineStack)==0:
                        return
                    lineToDelete, coordsToDelete = lineStack.pop()
                    edges.remove(coordsToDelete)
                    lineToDelete.remove()
                    plt.draw()
                elif event.key=='d':
                    #we set directed graph mode on or off
                    directed = not directed
            else:  
                if first==True and -1<int(event.key)<10:
                    curr1*=10
                    curr1+=int(event.key)
                    self.setText(f'First vertice: {curr1}, to choose second vertice click \'n\'')
                elif first==False and -1<int(event.key)<10:
                    curr2*=10
                    curr2+=int(event.key)
                    self.setText(f'Second vertice: {curr2}, to add an edge click \'a\'')

        curr1 = 0
        curr2 = 0
        first = True
        directed = False
        lineStack = []
        keys=['z','b','a','n','d','backspace']
        
        fig=plt.figure(frameon=False)
        fig.canvas.manager.set_window_title("Graph creator")
        fig.canvas.mpl_connect('key_press_event', press)
        mpltlb.rcParams['toolbar'] = 'None'
        
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)

        #results
        pts=[]
        edges=[]

        while len(pts) < 2:
            self.setText('Choose vertices\'s coordinates')
            pts = np.asarray(plt.ginput(-1, timeout=-1))
  
        plt.clf()    
    
        ph = plt.scatter(pts[:, 0], pts[:, 1], c='blue', zorder=5, s=50)
        for i in range(len(pts)):
            plt.annotate(f'{i}', (pts[:, 0][i], pts[:, 1][i]))

        self.setText(f'First vertice: {curr1}, to choose second vertice click \'n\'')
    
        plt.show()

        plt.scatter(pts[:, 0], pts[:, 1], c='blue', zorder=5, s=50)

        for i in range(len(pts)):
            plt.annotate(f'{i}', (pts[:, 0][i], pts[:, 1][i]))
        for i1, i2 in edges:
            plt.plot([pts[i1][0], pts[i2][0]], [pts[i1][1], pts[i2][1]], linewidth=2, color = "black")

        self.setText('Final Graph')
        plt.show()

        return pts, edges