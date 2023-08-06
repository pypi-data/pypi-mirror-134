

class Cells:
      #function to create list of rows
      def makeList(self,min,max,rows):
           #initialize variables
           global myBoard 
           myBoard =list() 
           global row
           row=list()
           for cell in range(min,max):
                  row.append(cell)
                  if cell%rows==0:
                        myBoard.append(row)
                        row=list()
      def drawBoard(self):
          for row in myBoard:
            s=('''
             _____   _____   _____   _____   _____   _____
            |     | |     | |     | |     | |     | |     |
            | %02d  | | %02d  | | %02d  | |  %02d | |  %02d | |  %02d | 
            |_____| |_____| |_____| |_____| |_____| |_____|
            '''%(row[0],row[1],row[2],row[3],row[4],row[5]))
            print(s,end="")



cells=Cells()
# cells.makeList(1,31,6)
# cells.drawBoard()





