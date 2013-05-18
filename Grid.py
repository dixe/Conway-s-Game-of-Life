from Cell import *
class Grid():
    def __init__(self,screen,rows,cols,cell_image):
        self.rows=rows
        self.cols=cols
        self.cells=[[Cell(screen,False,(i*10,j*10),cell_image) for i in range(rows)] for j in range(cols)]
        self.cellstmp=[[Cell(screen,False,(i*10,j*10),cell_image) for i in range(rows)] for j in range(cols)]

    def getCell(self,row,col):
        return self.cells[row][col]

    def setCell(self,i,j,alive):
        if alive:
            self.cells[i][j].spawn()
            self.cellstmp[i][j].spawn()
        else:
            self.cells[i][j].kill()
            self.cellstmp[i][j].kill()

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getNaborNumber(self,i,j):
        number=0
        if i<1 or j<1 or j>self.cols-2 or i>self.rows-2:
            return 0
        if self.cells[i-1][j-1].getStatus():
            number = number+1
        if self.cells[i-1][j].getStatus():
            number = number+1
        if self.cells[i][j-1].getStatus():
            number = number+1
        if self.cells[i+1][j-1].getStatus():
            number = number+1
        if self.cells[i+1][j+1].getStatus():
            number = number+1
        if self.cells[i+1][j].getStatus():
            number = number+1
        if self.cells[i][j+1].getStatus():
            number = number+1
        if self.cells[i-1][j+1].getStatus():
            number = number+1
        return number

    def updateCells(self):
        for i in range(self.rows):
            for j in range(self.cols):
                nabor= self.getNaborNumber(i,j)
                if nabor < 2:
                    self.cellstmp[i][j].kill()
                if nabor >3:
                    self.cellstmp[i][j].kill()
                elif nabor==3:
                    self.cellstmp[i][j].spawn()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cellstmp[i][j].getStatus():
                    self.cells[i][j].spawn()
                else:
                    self.cells[i][j].kill()