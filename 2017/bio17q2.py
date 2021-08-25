class Game():
    
    def __init__(self, p1, m1, p2, m2, t):
        self.board = Board()
        self.board.squares[0].owner
        self.players = [Player(p1,m1, 0), Player(p2,m2, 1)]
        self.turns = t
        
    def run(self):
        currentTurn = 0
        for i in range(self.turns):
            # t<=60 so move is always available
            # Player.move() not only makes move but returns True/False for whether square has been won
            if not self.players[currentTurn].move(self.board):
                currentTurn += 1
                currentTurn %= 2
        self.result()
                
    def result(self):
        s = ""
        i = 0
        for square in self.board.squares:                
            s += square.owner
            if i%5 == 4:
                s += "\n"
            i += 1
        print(s)
        print(len(self.players[0].wonSquares),len(self.players[1].wonSquares))
        if all(self.board.squares[i].owner=="O" for i in range(25)):
            return True
        else: return False
                
        

class Board():
    
    def __init__(self):
        self.squares = []
        for i in range(25):
            self.squares.append(Square())

    def __str__(self):
        return str([self.squares[i].sides for i in range(25)])


class Square():
    def __init__(self):
        # [[right, top, left, bottom]]
        self.sides = [0,0,0,0]
        self.owner = "*"
        
    def completeSquare(self,turn):
        if all(x==1 for x in self.sides):
            if turn == 0:
                self.owner = "X"
            else: self.owner = "O"
            return True
 
class Player():
    def __init__(self, position, modifier, playerNum):
        self.position = position
        self.modifier = modifier
        self.wonSquares = []
        self.playerNum = playerNum

    def move(self, board):
        
        self.position += self.modifier
        while True:
            if self.position > 36:
                self.position %= 36        
            P = self.position - 1
            column = P % 6
            row = P // 6

            if self.playerNum == 1:
                
                ### Upwards line
                if row == 0: pass
                else:
                    if column == 5:
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif column == 0:
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                new = True
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

                # If on the left, cannot go left
                ### Left line
                if column == 0: pass
                else:
                    if row == 0:
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                return True
                            return False
                    # Drawing a left line at the bottom edge
                    elif row == 5:
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                new = True
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

                # If on the bottom , cannot go bottom
                ### Downwards line
                if row == 5: pass
                else:
                    if column == 0:
                        sq = board.squares[row*5 + column]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif column == 5:
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                new = True
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

                ### Line to the right
                # Cant draw a line from right edge
                if column == 5: pass
                else:
                    # Drawing a right line at the top edge
                    if row == 0:
                        sq = board.squares[row*5 + column]
                        sq.sides
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif row == 5:
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                new = True
                        sq = board.squares[row*5 + column]
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

            else:
                ### Upwards line
                if row == 0: pass
                else:
                    if column == 5:
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif column == 0:
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                new = True
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

                ### Line to the right
                # Cant draw a line from right edge
                if column == 5: pass
                else:
                    # Drawing a right line at the top edge
                    if row == 0:
                        sq = board.squares[row*5 + column]
                        sq.sides
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif row == 5:
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column - 5]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5)
                                new = True
                        sq = board.squares[row*5 + column]
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

                # If on the bottom , cannot go bottom
                ### Downwards line
                if row == 5: pass
                else:
                    if column == 0:
                        sq = board.squares[row*5 + column]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif column == 5:
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column]
                        if sq.sides[2] == 0:
                            sq.sides[2] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column)
                                new = True
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[0] == 0:
                            sq.sides[0] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False

                # If on the left, cannot go left
                ### Left line
                if column == 0: pass
                else:
                    if row == 0:
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                return True
                            return False
                    # Drawing a right line at the bottom edge
                    elif row == 5:
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                return True
                            return False
                    # Drawing a line in the centre
                    else:
                        new = False
                        changed = False
                        sq = board.squares[row*5 + column - 1]
                        if sq.sides[1] == 0:
                            sq.sides[1] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 1)
                                new = True
                        sq = board.squares[row*5 + column - 5 - 1]
                        if sq.sides[3] == 0:
                            sq.sides[3] = 1
                            changed = True
                            if sq.completeSquare(self.playerNum):
                                self.wonSquares.append(row * 5 + column - 5 - 1)
                                new = True
                        if new:
                            return True
                        if changed:
                            return False
                
                


            self.position += 1
            
            
def c():
    ans = 0
    for p in range(1,37):
        for m in range(1,36):
            game = Game(p, m, p, m, 60)
            game.run()
            if game.result():
                ans += 1
    print(ans)

if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    p1, m1, p2, m2, t = input().split()
    game = Game(int(p1), int(m1), int(p2), int(m2), int(t))
    game.run()
