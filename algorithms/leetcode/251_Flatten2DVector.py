from typing import List

# class Vector2D:
    
#     def __init__(self, vec: List[List[int]]):
#         self.vec = vec
#         self.row = 0
#         self.col = 0
#         self.m = len(self.vec)
        
#     def hasNextRow(self, current_row):
#         return current_row + 1 < self.m
    
#     def getNextColCursor(self, current_row, current_col, incrementCursor = False):
#         r = self.vec[current_row]
#         if current_col+1 < len(r):
#             if incrementCursor:
#                 self.col+=1
#             return (current_row, current_col+1 )
#         else:
#             while self.hasNextRow(current_row):
#                 if len(self.vec[current_row + 1] ) != 0:
#                     if incrementCursor:
#                         self.row = current_row + 1
#                         self.col = 0
#                     return (current_row + 1, 0 )
#                 else:
#                      current_row += 1
#             return None
                    

#     def next(self) -> int:
#         cursor =  self.getNextColCursor(self.row, self.col)
#         print(cursor)
#         if cursor:
#             r,c = cursor[0], cursor[1]
#             return self.vec[r][c]
#             #increment cursor
#             self.getNextColCursor(self.row, self.col, True)
#         else:
#             return None
            
                

#     def hasNext(self) -> bool:
#         cursor =  self.getNextColCursor(self.row, self.col)
#         return cursor != None

class Vector2D:
    
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0
        self.m = len(self.vec)
        

    def getNextColCursor(self):
        while self.row < self.m and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0
                    

    def next(self) -> int:
        self.getNextColCursor()
        r = self.vec[self.row][self.col]
        self.col+=1
        return r
            
                

    def hasNext(self) -> bool:
        self.getNextColCursor()
        return self.row < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()