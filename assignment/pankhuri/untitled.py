import sys
import os
from time import process_time 
print(sys.version)

from typing import List
from time import process_time

        
# class exam:
#     def __init__(
#         self,
#         grid: "List[List[str]",
#         n: "int",
#         islands: "list of list of int",
#         work: "List of size 1",
#         show: "boolean",
#     ):
#         self._grid = grid
#         self._n = n  # 4 or 8 Direction to explore
#         self._islands = islands  # Must Fill
#         self._work = work  # Must Fill
#         self._show = show
#         self._row = len(self._grid)
#         self._col = len(self._grid[0])

#         # Tou can have any number of data structures here
#         self._visitedArr = [ [False] * len(grid[0])]*len(grid)

#         # MUST WRITE THIS ROUTINE
#         self._alg()
        

#     def _increment_work(self):
#         self._work[0] = self._work[0] + 1

#     ############################################################
#     # WRITE CODE BELOW
#     ###########################################################
    
#     def _visited(self, x,y):
#         print([x,y])
#         if x < 0 or x >= self._row or y < 0 or y >= self._col or self._visitedArr[x][y]:
#             return []
#         if self._visitedArr[x][y] == False and self._grid[x][y] != "1":
#             self._visitedArr[x][y] = True
#             return []
#         if self._visitedArr[x][y] == False and self._grid[x][y] == "1":
#             self._visitedArr[x][y] = True
#             print(self._grid[x][y])
#             if self._n == 4:
#                 return [x,y] + self._visited(x-1,y) + self._visited(x,y-1)+ self._visited(x+1,y)+ self._visited(x,y+1)
#             elif self._n ==8:
#                 return [x,y] + self._visited(x-1,y) + self._visited(x,y-1)+ self._visited(x+1,y)+ self._visited(x,y+1) + self._visited(x-1,y-1) + self._visited(x-1,y+1)+ self._visited(x+1,y-1)+ self._visited(x+1,y+1)
#         return []        
        
#     def _travel(self):
#         for x in range(self._row):        
#             for y in range(self._col):
#                 # values = self._visited(x,y)
#                 print("ytytyuty",self._visited(x,y))
#                 # if len([00]) > 0:
#                 #     self._islands.append(self._visited(x,y))    
#                 print()
#             print()
#         s = examTest()
#         print(s._print_matrix(self._visitedArr))
        
#     def _alg(self):
#         if self._n == 4 or self._n == 8:
#             self._travel()

class exam:
    def __init__(
        self,
        grid: "List[List[str]]",
        n: "int",
        islands: "List[List[int]]",
        work: "List[int]",
        show: "bool",
    ):
        self._grid = grid
        self._n = n  # 4 or 8 Direction to explore
        self._islands = islands  # Must Fill
        self._work = work  # Must Fill
        self._show = show
        self._visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        # Directions based on n
        if n == 4:
            self._directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        elif n == 8:
            self._directions = [
                (0, 1), (1, 0), (0, -1), (-1, 0),  # right, down, left, up
                (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonals
            ]
        
        self._alg()

    def _increment_work(self):
        self._work[0] += 1

    def _dfs(self, r, c, island):
        stack = [(r, c)]
        while stack:
            row, col = stack.pop()
            if self._visited[row][col]:
                continue
            self._visited[row][col] = True
            island.append((row, col))
            self._increment_work()
            
            for dr, dc in self._directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(self._grid) and 0 <= nc < len(self._grid[0]) and not self._visited[nr][nc] and self._grid[nr][nc] == "1":
                    stack.append((nr, nc))

    def _alg(self):
        for r in range(len(self._grid)):
            for c in range(len(self._grid[0])):
                if self._grid[r][c] == "1" and not self._visited[r][c]:
                    island = []
                    self._dfs(r, c, island)
                    self._islands.append(island)
            

class examTest:
    def __init__(self):
        self._show = True
        self._num = 0
        self._mark = 0
        # self._test()

    def _print_matrix(self, grid: "List[List[str]"):
        if self._show:
            for arow in grid:
                for e in arow:
                    print(e, sep="", end="")
                print()
            print()

    def _test1(self, grid: "List[List[str]", n: int, eans: "int"):
        self._num = self._num + 1
        print(
            "______________________Problem",
            self._num,
            "---------------------------------",
        )
        print("Input grid is shown below. You must find all islands for n = ", n)
        self._print_matrix(grid)
        work = [0]
        islands = []
        # return list of listq
        p = exam(grid, n, islands, work, self._show)
        num = len(islands)
        if num:
            if work[0] == 0:
                print("How did you solve the problem witj no work?")
                assert False
            else:
                print("WORK = ", work[0])

    def _marks(self, n:'int'):
      self._mark += n
      print("At this point You got", self._mark, "marks")

    def _test(self):
        self._show = True
        
        grid = [
            ["1", "1", "0"],
            ["0", "1", "0"],
            ["1", "0", "0"]         
        ]
        n = 4
        e = 5 #wrong
        self._test1(grid, n, e)

        n = 8
        e = 4 #WRONG
        self._test1(grid, n, e)
        self._marks(10)
        # print("Let us see how many tests passes after I give you hidden tests")


############################################################
# main
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
    print("Testing examTest Starts")
    s = examTest()
    s._test()
    print("Testing examTest ENDS")
    

if (__name__    == '__main__'):
    main()