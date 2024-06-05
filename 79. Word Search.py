from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxX = len(board)
        maxY = len(board[0])
        i =0
        j=0
        z= 0
        value = [''] * len(word)
        while (i< maxX and j< maxY and z< len(word)):
            if (board[i][j].lower() == word[z].lower()):
                value[z] = board[i][j] 
                board[i][j] =''
                z+=1
                
                if (i+1 < maxX and z< len(word) and board[i+1][j].lower() == word[z].lower()):
                    i+=1
                elif (j+1 < maxY and z< len(word) and board[i][j+1].lower() == word[z].lower()):
                    j+=1
                
                elif (j-1 >= 0 and z< len(word) and board[i][j-1].lower() == word[z].lower()):
                    j-=1
                elif (i-1 >= 0 and z< len(word) and board[i-1][j].lower() == word[z].lower()):
                    i-=1
                elif (j+1 < maxY and i+1 <maxX and z< len(word) and board[i+1][j+1].lower() == word[z].lower()):
                    j+=1
                    i+=1
                elif (j-1 >= 0 and i+1 <maxX and z< len(word) and board[i+1][j-1].lower() == word[z].lower()):
                    maxY = j
                    j-=1
                    i+=1
                elif (j+1 < maxY and i-1 >0 and z< len(word) and board[i-1][j+1].lower() == word[z].lower()):
                    j+=1
                    i-=1
                elif (j-1 >0 and i-1 >0 and z< len(word) and board[i-1][j-1].lower() == word[z].lower()):
                    j-=1
                    i-=1
                elif z != len(word): 
                    value = [''] * len(word)
                    z= 0
            elif j<= maxY-1:
                if j+1 == maxY:
                    j= 0
                    i+=1
                else :
                    j+=1

        return "".join(value).lower() == word.lower()
    
value = Solution()
# print(value.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(value.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
# print(value.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCD"))
# print(value.exist([["a","b"],["c","d"]], "acdb"))
# print(value.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(value.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
print(value.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE"))


