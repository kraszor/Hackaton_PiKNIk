from abc import ABC, abstractmethod
from copy import deepcopy


class Piece(ABC):

    def __init__(self, id, color, pose, name, first_move, status):
        self.id = id
        self.color = color
        self.pose = pose
        self.name = name
        self.first_move = first_move
        self.status = status

    def move(self, picked_pose):
        self.pose = picked_pose

    @abstractmethod
    def possible_moves(self):
        pass


class Pawn(Piece):

    def __init__(self, id, color,
                 pose, name, first_move=True,
                 status=False, en_passant=()):
        super().__init__(id, color, pose, name, first_move, status)
        self.symbol = "P"
        self.points = 10
        self.en_passant = en_passant

    def possible_moves(self,
                       current_pose,
                       current_board,
                       prevboard=[[]],
                       possible_for_enemy=[[]]):
        possible_moves = []
        if self.color == "white":
            if current_pose[0] == 6:
                if current_board[current_pose[0] - 1][current_pose[1]] == "" and \
                        current_board[current_pose[0] - 2][current_pose[1]] == "":
                    possible_moves.append((current_pose,
                                          (current_pose[0] - 2,
                                           current_pose[1]), False))
            if current_board[current_pose[0] - 1][current_pose[1]] == "":
                possible_moves.append((current_pose,
                                      (current_pose[0] - 1,
                                       current_pose[1]), False))

            try:
                if current_board[current_pose[0] - 1][current_pose[1] + 1].color == "black":
                    possible_moves.insert(0, (current_pose,
                                              (current_pose[0] - 1,
                                               current_pose[1] + 1), False))
                if current_board[current_pose[0] - 1][current_pose[1] + 1].color == "white":
                    current_board[current_pose[0] - 1][current_pose[1] + 1].status = True
            except Exception:
                pass

            try:
                if current_board[current_pose[0] - 1][current_pose[1] - 1].color == "black":
                    possible_moves.insert(0, (current_pose,
                                              (current_pose[0] - 1,
                                               current_pose[1] - 1), False))
                if current_board[current_pose[0] - 1][current_pose[1] - 1].color == "White":
                    current_board[current_pose[0] - 1][current_pose[1] - 1].status = True
            except Exception:
                pass

            # en passant for white
            if current_pose[0] == 3:
                try:
                    if current_board[3][current_pose[1] + 1].color == "black" and \
                       current_board[3][current_pose[1] + 1].symbol == "P" and \
                       prevboard[1][current_pose[1] + 1].id == current_board[3][current_pose[1] + 1].id:
                        possible_moves.insert(0, (current_pose,
                                                  (2, current_pose[1] + 1),
                                                  False))
                        self.en_passant = (2, current_pose[1] + 1)
                except Exception:
                    pass

                try:
                    if current_board[3][current_pose[1] - 1].color == "black" and \
                       current_board[3][current_pose[1] - 1].symbol == "P" and \
                       prevboard[1][current_pose[1] - 1].id == current_board[3][current_pose[1] - 1].id:
                        possible_moves.insert(0, (current_pose,
                                                  (2, current_pose[1] - 1),
                                                  False))
                        self.en_passant = (2, current_pose[1] - 1)
                except Exception:
                    pass

        if self.color == "black":
            if current_pose[0] == 1:
                if current_board[current_pose[0] + 1][current_pose[1]] == \
                        "" and current_board[current_pose[0] + 2][current_pose[1]] == "":
                    possible_moves.append((current_pose,
                                           (current_pose[0] + 2,
                                            current_pose[1]), False))
            if current_board[current_pose[0] + 1][current_pose[1]] == "":
                possible_moves.append((current_pose,
                                       (current_pose[0] + 1,
                                        current_pose[1]), False))

            try:
                if current_board[current_pose[0] + 1][current_pose[1] + 1].color == "white":
                    possible_moves.insert(0, (current_pose,
                                              (current_pose[0] + 1,
                                               current_pose[1] + 1), False))
                if current_board[current_pose[0] + 1][current_pose[1] + 1].color == "black":
                    current_board[current_pose[0] + 1][current_pose[1] + 1].status = True
            except Exception:
                pass

            try:
                if current_board[current_pose[0] + 1][current_pose[1] - 1].color == "white":
                    possible_moves.insert(0, (current_pose,
                                              (current_pose[0] + 1,
                                               current_pose[1] - 1), False))
                if current_board[current_pose[0] + 1][current_pose[1] - 1].color == "black":
                    current_board[current_pose[0] + 1][current_pose[1] - 1].status = True
            except Exception:
                pass

            # en passant for black
            if current_pose[0] == 4:
                try:
                    if current_board[4][current_pose[1] + 1].color == "white" and \
                       current_board[4][current_pose[1] + 1].symbol == "P" and \
                       prevboard[6][current_pose[1] + 1].id == current_board[4][current_pose[1] + 1].id:
                        possible_moves.insert(0, (current_pose,
                                                  (5, current_pose[1] + 1),
                                                  False))
                        self.en_passant = (5, current_pose[1] + 1)
                except Exception:
                    pass

                try:
                    if current_board[4][current_pose[1] - 1].color == "white" and \
                       current_board[4][current_pose[1] - 1].symbol == "P" and \
                       prevboard[6][current_pose[1] - 1].id == current_board[4][current_pose[1] - 1].id:
                        possible_moves.insert(0, (current_pose,
                                                  (5, current_pose[1] - 1),
                                                  False))
                        self.en_passant = (5, current_pose[1] - 1)
                except Exception:
                    pass
        return possible_moves


class King(Piece):

    def __init__(self, id, color, pose, name, first_move=True, status=False):
        super().__init__(id, color, pose, name, first_move, status)
        self.symbol = "K"
        self.points = 900
        if color == "black":
            castle = "kq"
        else:
            castle = "KQ"
        self.castle = castle

    def possible_moves(self, current_pose,
                       current_board, prevboard=[[]],
                       possible_for_enemy=[]):
        possible_moves = []
        for i in range(-1, 2):
            for n in range(-1, 2):
                if self.color == "white":
                    if current_pose[0] + i >= 0 and current_pose[1] + n >= 0:
                        if current_pose[0] + i != current_pose[0] or \
                           current_pose[1] + n != current_pose[1]:

                            try:
                                if possible_for_enemy[current_pose[0] + i][current_pose[1] + n] == "" and \
                                        current_board[current_pose[0] + i][current_pose[1] + n] == "" or \
                                        possible_for_enemy[current_pose[0] + i][current_pose[1] + n] == "x" and \
                                        current_board[current_pose[0] + i - 1][current_pose[1] + n].symbol == "P":
                                    possible_moves.append((current_pose,
                                                           (current_pose[0] + i,
                                                            current_pose[1] + n),
                                                           False))
                            except Exception:
                                pass

                            try:
                                if current_board[current_pose[0] + i][current_pose[1] + n].color == "black" and \
                                   current_board[current_pose[0] + i][current_pose[1] + n].status is False:
                                    possible_moves.insert(0, (current_pose,
                                                              (current_pose[0] + i,
                                                               current_pose[1] + n),
                                                              False))
                                if current_board[current_pose[0] + i][current_pose[1] + n].color == "white":
                                    current_board[current_pose[0] + i][current_pose[1] + n].status = True
                            except Exception:
                                pass

                            try:
                                if (current_pose, (current_pose[0] + i, current_pose[1] + n), False) in possible_moves:
                                    for a in range(-1, 2):
                                        for b in range(-1, 2):
                                            if current_pose[0] + i + a >= 0 and current_pose[1] + n + b >= 0:

                                                try:
                                                    if current_board[current_pose[0] + i + a][current_pose[1] + n + b].\
                                                        name == "King" and \
                                                       current_board[current_pose[0] + i + a][current_pose[1] + n + b].\
                                                            color == "black":
                                                        possible_moves.remove((current_pose,
                                                                               (current_pose[0] + i,
                                                                                current_pose[1] + n),
                                                                               False))
                                                except Exception:
                                                    pass
                            except Exception:
                                pass
                if self.color == "black":
                    if current_pose[0] + i >= 0 and current_pose[1] + n >= 0:
                        if current_pose[0] + i != current_pose[0] or current_pose[1] + n != current_pose[1]:

                            try:
                                if possible_for_enemy[current_pose[0] + i][current_pose[1] + n] == "" and \
                                        current_board[current_pose[0] + i][current_pose[1] + n] == "" or \
                                        possible_for_enemy[current_pose[0] + i][current_pose[1] + n] == "x" and \
                                        current_board[current_pose[0] + i + 1][current_pose[1] + n].symbol == "P":
                                    possible_moves.append((current_pose,
                                                           (current_pose[0] + i,
                                                            current_pose[1] + n),
                                                           False))
                            except Exception:
                                pass

                            try:
                                if current_board[current_pose[0] + i][current_pose[1] + n].color == "white" and \
                                   current_board[current_pose[0] + i][current_pose[1] + n].status is False:
                                    possible_moves.insert(0, (current_pose,
                                                              (current_pose[0] + i,
                                                               current_pose[1] + n),
                                                              False))
                                if current_board[current_pose[0] + i][current_pose[1] + n].color == "black":
                                    current_board[current_pose[0] + i][current_pose[1] + n].status = True
                            except Exception:
                                pass

                            try:
                                if (current_pose, (current_pose[0] + i, current_pose[1] + n), False) in possible_moves:
                                    for a in range(-1, 2):
                                        for b in range(-1, 2):
                                            if current_pose[0] + i + a >= 0 and current_pose[1] + n + b >= 0:

                                                try:
                                                    if current_board[current_pose[0] + i + a][current_pose[1] + n + b].\
                                                        name == "King" and \
                                                       current_board[current_pose[0] + i + a][current_pose[1] + n + b].\
                                                            color == "white":
                                                        possible_moves.remove((current_pose,
                                                                               (current_pose[0] + i,
                                                                                current_pose[1] + n),
                                                                               False))
                                                except Exception:
                                                    pass
                            except Exception:
                                pass
        if self.color == "white":
            try:
                if self.first_move is False or type(current_board[7][7]) == str or \
                   current_board[7][7].symbol != "R" or current_board[7][7].first_move is False:
                    self.castle = self.castle[1:]
                if self.first_move is True and \
                   current_board[7][7] != "" and \
                   possible_for_enemy[7][5] == "" and current_board[7][5] == "" and \
                   possible_for_enemy[7][6] == "" and current_board[7][6] == "" and \
                   possible_for_enemy[7][4] != 'x':
                    if current_board[7][7].symbol == "R" and current_board[7][7].first_move is True:
                        possible_moves.append((current_pose, (7, 6), False))
            except Exception:
                pass

            try:
                if self.first_move is False or type(current_board[7][0]) == str or \
                   current_board[7][0].symbol != "R" or current_board[7][0].first_move is False:
                    self.castle = self.castle[:-1]
                if self.first_move is True and \
                   possible_for_enemy[7][3] == "" and current_board[7][3] == "" and \
                   possible_for_enemy[7][2] == "" and current_board[7][2] == "" and \
                   current_board[7][1] == "" and \
                   current_board[7][0] != "" and \
                   possible_for_enemy[7][4] != 'x':
                    if current_board[7][0].symbol == "R" and current_board[7][0].first_move is True:
                        possible_moves.append((current_pose, (7, 2), False))
            except Exception:
                pass

        if self.color == "black":
            try:
                if self.first_move is False or type(current_board[0][7]) == str or \
                   current_board[0][7].symbol != "R" or current_board[0][7].first_move is False:
                    self.castle = self.castle[1:]
                if self.first_move is True and \
                   possible_for_enemy[0][5] == "" and current_board[0][5] == "" and \
                   possible_for_enemy[0][6] == "" and current_board[0][6] == "" and \
                   current_board[0][7] != "" and \
                   possible_for_enemy[0][4] != 'x':
                    if current_board[0][7].symbol == "R" and current_board[0][7].first_move is True:
                        possible_moves.append((current_pose, (0, 6), False))
            except Exception:
                pass

            try:
                if self.first_move is False or type(current_board[0][0]) == str or \
                   current_board[0][0].symbol != "R" or current_board[0][0].first_move is False:
                    self.castle = self.castle[:-1]
                if self.first_move is True \
                   and possible_for_enemy[0][3] == "" and current_board[0][3] == "" and \
                   possible_for_enemy[0][2] == "" and current_board[0][2] == "" and \
                   current_board[0][1] == "" and \
                   current_board[0][0] != "" and \
                   possible_for_enemy[0][4] != 'x':
                    if current_board[0][0].symbol == "R" and current_board[0][0].first_move is True:
                        possible_moves.append((current_pose, (0, 2), False))
            except Exception:
                pass
        return possible_moves

    def check_status(self, possible_for_enemy=[[]]):
        if possible_for_enemy[self.pose[0]][self.pose[1]] == "x":
            return True
        else:
            return False

    def checkmate_status(self, check_status, possible_for_ally=[[]]):
        if check_status is True and len(possible_for_ally) == 0:
            return True
        else:
            return False

    def stalemate(self, check_status, possible_for_ally=[[]]):
        if check_status is False and len(possible_for_ally) == 0:
            return True
        else:
            return False


class Queen(Piece):

    def __init__(self, id, color, pose, name, first_move=True, status=False):
        super().__init__(id, color, pose, name, first_move, status)
        self.symbol = "Q"
        self.points = 90

    def possible_moves(self, current_pose, current_board,
                       prevboard=[[]], possible_for_enemy=[[]]):

        w_rook_to_queen = Rook(1, "white", (10, 10), "wR3")
        b_rook_to_queen = Rook(1, "black", (10, 10), "bR3")
        w_bishop_to_queen = Bishop(1, "white", (10, 10), "wB3")
        b_bishop_to_queen = Bishop(1, "black", (10, 10), "bB3")

        if self.color == "white":
            options_1 = w_rook_to_queen.possible_moves(current_pose,
                                                       current_board)
            options_2 = w_bishop_to_queen.possible_moves(current_pose,
                                                         current_board)
            return options_1 + options_2

        if self.color == "black":
            options_1 = b_rook_to_queen.possible_moves(current_pose,
                                                       current_board)
            options_2 = b_bishop_to_queen.possible_moves(current_pose,
                                                         current_board)
            return options_1 + options_2


class Knight(Piece):

    def __init__(self, id, color, pose, name, first_move=True, status=False):
        super().__init__(id, color, pose, name, first_move, status)
        self.symbol = "N"
        self.points = 30

    def possible_moves(self, current_pose, current_board,
                       prevboard=[[]], possible_for_enemy=[[]]):
        possible_moves = []
        for i in range(-2, 5, 4):
            for n in range(-1, 2, 2):
                try:
                    if current_pose[0] + i >= 0 and current_pose[1] + n >= 0:
                        if current_board[current_pose[0] + i][current_pose[1] + n] == "":
                            possible_moves.append((current_pose,
                                                   (current_pose[0] + i,
                                                    current_pose[1] + n),
                                                   False))
                        if current_board[current_pose[0] + i][current_pose[1] + n].color != self.color:
                            possible_moves.insert(0, (current_pose,
                                                      (current_pose[0] + i,
                                                       current_pose[1] + n),
                                                      False))
                        if current_board[current_pose[0] + i][current_pose[1] + n].color == self.color:
                            current_board[current_pose[0] + i][current_pose[1] + n].status = True
                except Exception:
                    pass

                try:
                    if current_pose[0] + n >= 0 and current_pose[1] + i >= 0:
                        if current_board[current_pose[0] + n][current_pose[1] + i] == "":
                            possible_moves.append((current_pose, (current_pose[0] + n, current_pose[1] + i), False))
                        if current_board[current_pose[0] + n][current_pose[1] + i].color != self.color:
                            possible_moves.insert(0, (current_pose, (current_pose[0] + n, current_pose[1] + i), False))
                        if current_board[current_pose[0] + n][current_pose[1] + i].color == self.color:
                            current_board[current_pose[0] + n][current_pose[1] + i].status = True
                except Exception:
                    pass
        return possible_moves

    def move(self, picked_pose):
        self.pose = picked_pose


class Bishop(Piece):

    def __init__(self, id, color, pose, name, first_move=True, status=False):
        super().__init__(id, color, pose, name, first_move, status)
        self.symbol = "B"
        self.points = 30

    def possible_moves(self, current_pose, current_board, prevboard=[[]], possible_for_enemy=[[]]):
        possible_moves = []
        occur_1 = False
        occur_2 = False
        occur_3 = False
        occur_4 = False
        for i in range(1, 8):
            if occur_1 is False:
                try:
                    if current_board[current_pose[0] + i][current_pose[1] + i] == "":
                        possible_moves.append((current_pose, (current_pose[0] + i, current_pose[1] + i), False))
                    elif current_board[current_pose[0] + i][current_pose[1] + i] == "x" or \
                            current_board[current_pose[0] + i][current_pose[1] + i].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0] + i, current_pose[1] + i), False))
                        occur_1 = True
                    elif current_board[current_pose[0] + i][current_pose[1] + i].color == self.color:
                        current_board[current_pose[0] + i][current_pose[1] + i].status = True
                        occur_1 = True
                except Exception:
                    pass

            if occur_2 is False and current_pose[0] - i >= 0 and current_pose[1] - i >= 0:
                try:
                    if current_board[current_pose[0] - i][current_pose[1] - i] == "":
                        possible_moves.append((current_pose, (current_pose[0] - i, current_pose[1] - i), False))
                    elif current_board[current_pose[0] - i][current_pose[1] - i] == "x" or \
                            current_board[current_pose[0] - i][current_pose[1] - i].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0] - i, current_pose[1] - i), False))
                        occur_2 = True
                    elif current_board[current_pose[0] - i][current_pose[1] - i].color == self.color:
                        current_board[current_pose[0] - i][current_pose[1] - i].status = True
                        occur_2 = True
                except Exception:
                    pass

            if occur_3 is False and current_pose[1] - i >= 0:
                try:
                    if current_board[current_pose[0] + i][current_pose[1] - i] == "":
                        possible_moves.append((current_pose, (current_pose[0] + i, current_pose[1] - i), False))
                    elif current_board[current_pose[0] + i][current_pose[1] - i] == "x" or \
                            current_board[current_pose[0] + i][current_pose[1] - i].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0] + i, current_pose[1] - i), False))
                        occur_3 = True
                    elif current_board[current_pose[0] + i][current_pose[1] - i].color == self.color:
                        current_board[current_pose[0] + i][current_pose[1] - i].status = True
                        occur_3 = True
                except Exception:
                    pass

            if occur_4 is False and current_pose[0] - i >= 0:
                try:
                    if current_board[current_pose[0] - i][current_pose[1] + i] == "":
                        possible_moves.append((current_pose, (current_pose[0] - i, current_pose[1] + i), False))
                    elif current_board[current_pose[0] - i][current_pose[1] + i] == "x" or \
                            current_board[current_pose[0] - i][current_pose[1] + i].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0] - i, current_pose[1] + i), False))
                        occur_4 = True
                    elif current_board[current_pose[0] - i][current_pose[1] + i].color == self.color:
                        current_board[current_pose[0] - i][current_pose[1] + i].status = True
                        occur_4 = True
                except Exception:
                    pass
        return possible_moves


class Rook(Piece):

    def __init__(self, id, color, pose, name, first_move=True, status=False):
        super().__init__(id, color, pose, name, first_move, status)
        self.symbol = "R"
        self.points = 50

    def possible_moves(self, current_pose, current_board, prevboard=[[]], possible_for_enemy=[[]]):
        possible_moves = []
        occurance_1 = False
        occurance_2 = False
        occurance_3 = False
        occurance_4 = False
        for i in range(1, 8):
            try:
                if occurance_1 is False:
                    if current_board[current_pose[0] + i][current_pose[1]] == "":
                        possible_moves.append((current_pose, (current_pose[0] + i, current_pose[1]), False))
                    elif current_board[current_pose[0] + i][current_pose[1]] == "x" or \
                            current_board[current_pose[0] + i][current_pose[1]].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0] + i, current_pose[1]), False))
                        occurance_1 = True
                    elif current_board[current_pose[0] + i][current_pose[1]].color == self.color:
                        current_board[current_pose[0] + i][current_pose[1]].status = True
                        occurance_1 = True
            except Exception:
                pass

            try:
                if occurance_2 is False and current_pose[0] - i >= 0:
                    if current_board[current_pose[0] - i][current_pose[1]] == "":
                        possible_moves.append((current_pose, (current_pose[0] - i, current_pose[1]), False))
                    elif current_board[current_pose[0] - i][current_pose[1]] == "x" or \
                            current_board[current_pose[0] - i][current_pose[1]].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0] - i, current_pose[1]), False))
                        occurance_2 = True
                    elif current_board[current_pose[0] - i][current_pose[1]].color == self.color:
                        current_board[current_pose[0] - i][current_pose[1]].status = True
                        occurance_2 = True
            except Exception:
                pass

            try:
                if occurance_3 is False:
                    if current_board[current_pose[0]][current_pose[1] + i] == "":
                        possible_moves.append((current_pose, (current_pose[0], current_pose[1] + i), False))
                    elif current_board[current_pose[0]][current_pose[1] + i] == "x" or \
                            current_board[current_pose[0]][current_pose[1] + i].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0], current_pose[1] + i), False))
                        occurance_3 = True
                    elif current_board[current_pose[0]][current_pose[1] + i].color == self.color:
                        current_board[current_pose[0]][current_pose[1] + i].status = True
                        occurance_3 = True
            except Exception:
                pass

            try:
                if occurance_4 is False and current_pose[1] - i >= 0:
                    if current_board[current_pose[0]][current_pose[1] - i] == "":
                        possible_moves.append((current_pose, (current_pose[0], current_pose[1] - i), False))
                    elif current_board[current_pose[0]][current_pose[1] - i] == "x" or \
                            current_board[current_pose[0]][current_pose[1] - i].color != self.color:
                        possible_moves.insert(0, (current_pose, (current_pose[0], current_pose[1] - i), False))
                        occurance_4 = True
                    elif current_board[current_pose[0]][current_pose[1] - i].color == self.color:
                        current_board[current_pose[0]][current_pose[1] - i].status = True
                        occurance_4 = True
            except Exception:
                pass
        return possible_moves


class Board():
    def __init__(self):
        self.w_king_pose = (7, 4)
        self.b_king_pose = (0, 4)
        self.turn = "white"
        self.gameover = False
        self.draw = False
        self.check = False
        self.board = self.starting_board()
        self.FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.half_moves = 0
        self.half_moves_no_pawn_no_capture = 0
        self.made_moves = []
        self.previous_state = {'board': deepcopy(self.board),
                               'w_king': self.w_king_pose,
                               'b_king': self.b_king_pose,
                               'turn': self.turn,
                               'FEN': self.FEN,
                               'half_moves': self.half_moves}

    # creating a starting board which contains objects of the individual pieces classes
    def starting_board(self):
        wp1 = Pawn(1, "white", (6, 0), "wP1")
        wp2 = Pawn(2, "white", (6, 1), "wP2")
        wp3 = Pawn(3, "white", (6, 2), "wP3")
        wp4 = Pawn(4, "white", (6, 3), "wP4")
        wp5 = Pawn(5, "white", (6, 4), "wP5")
        wp6 = Pawn(6, "white", (6, 5), "wP6")
        wp7 = Pawn(7, "white", (6, 6), "wP7")
        wp8 = Pawn(8, "white", (6, 7), "wP8")
        bp1 = Pawn(9, "black", (1, 0), "bP1")
        bp2 = Pawn(10, "black", (1, 1), "bP2")
        bp3 = Pawn(11, "black", (1, 2), "bP3")
        bp4 = Pawn(12, "black", (1, 3), "bP4")
        bp5 = Pawn(13, "black", (1, 4), "bP5")
        bp6 = Pawn(14, "black", (1, 5), "bP6")
        bp7 = Pawn(15, "black", (1, 6), "bP7")
        bp8 = Pawn(16, "black", (1, 7), "bP8")
        wr1 = Rook(17, "white", (7, 0), "wR1")
        wr2 = Rook(18, "white", (7, 7), "wR2")
        br1 = Rook(19, "black", (0, 0), "bR1")
        br2 = Rook(20, "black", (0, 7), "bR2")
        wb1 = Bishop(21, "white", (7, 2), "wB1")
        wb2 = Bishop(22, "white", (7, 5), "wB2")
        bb1 = Bishop(23, "black", (0, 2), "bB1")
        bb2 = Bishop(24, "black", (0, 5), "bB2")
        wn1 = Knight(25, "white", (7, 1), "wN1")
        wn2 = Knight(26, "white", (7, 6), "wN2")
        bn1 = Knight(27, "black", (0, 1), "bN1")
        bn2 = Knight(28, "black", (0, 6), "bN2")
        wq = Queen(29, "white", (7, 3), "wQ1")
        bq = Queen(29, "black", (0, 3), "bQ1")
        wk = King(100, "white", (7, 4), "wK1")
        bk = King(101, "black", (0, 4), "bK1")

        starting_board = [[br1, bn1, bb1, bq, bk, bb2, bn2, br2],
                          [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
                          [wr1, wn1, wb1, wq, wk, wb2, wn2, wr2]]

        return starting_board

    def possible_for_enemies(self, color):
        enemy_possibilities = []
        for elem in self.board:
            for i in elem:
                if type(i) != str:
                    if i.color != color:
                        possible_for_enemy = i.possible_moves(i.pose,
                                                              self.board)
                        enemy_possibilities += possible_for_enemy

        return enemy_possibilities

    def possible_to_board(self, possible):
        possible_board = [["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""]]
        for elem in possible:
            space_1 = possible_board[elem[0][0]][elem[0][1]]
            space_2 = possible_board[elem[1][0]][elem[1][1]]
            if space_1 == "":
                possible_board[elem[0][0]][elem[0][1]] = self.board[elem[0][0]][elem[0][1]]
                possible_board[elem[0][0]][elem[0][1]].status = False
            if type(space_2) != str:
                possible_board[elem[1][0]][elem[1][1]].status = True
            else:
                possible_board[elem[1][0]][elem[1][1]] = 'x'

        return possible_board

    def possible_for_allies(self, possible_for_enemy, isAI):
        ally_possibilities = []
        for elem in self.board:
            for i in elem:
                if type(i) != str and \
                   i.color == self.turn:
                    if i.symbol == "K" and len(possible_for_enemy) > 0 and \
                            len(possible_for_enemy) != 8 and len(possible_for_enemy[0]) != 8:
                        possible_for_enemy = self.possible_to_board(possible_for_enemy)
                    possible_for_ally = \
                        i.possible_moves(i.pose,
                                         self.board,
                                         possible_for_enemy=possible_for_enemy)
                    if len(possible_for_ally) == 0:
                        continue
                    possible_for_ally = self.legal_moves(possible_for_ally)
                    if len(possible_for_ally) > 0 and not isAI:
                        return possible_for_ally
                    ally_possibilities += possible_for_ally

        return list(set(ally_possibilities))


    def board_status_reset(self):
        for row in self.board:
            for elem in row:
                if type(elem) != str:
                    elem.status = False

    def legal_moves(self, possible_for_ally):
        illegal_moves = []
        if self.turn == "white":
            king_pose = self.w_king_pose
            x, y = king_pose
            king = self.board[x][y]
        elif self.turn == "black":
            king_pose = self.b_king_pose
            x, y = king_pose
            king = self.board[x][y]
        p_test = Pawn(1000, self.turn, (10, 10), "TP1")
        for elem in possible_for_ally:
            x, y = king_pose
            if elem[2] is True:
                continue
            else:
                if elem[0] == (x, y):
                    p_test = king
                    x, y = elem[1]
                piece = self.board[elem[0][0]][elem[0][1]]
                picked = self.board[elem[1][0]][elem[1][1]]
                self.board[elem[1][0]][elem[1][1]] = p_test
                self.board[elem[0][0]][elem[0][1]] = ""
                enemy_possible = self.possible_for_enemies(self.turn)
                if p_test == king:
                    self.board[elem[0][0]][elem[0][1]] = ""
                    self.board[elem[1][0]][elem[1][1]] = ""
                    additional_possiblities = self.possible_for_enemies(self.turn)
                    self.board[elem[1][0]][elem[1][1]] = p_test
                    enemy_possible = list(set(enemy_possible + additional_possiblities))
                for item in enemy_possible:
                    pawn_cond = abs(item[1][0] - item[0][0]) == 1 and \
                               item[1][1] == item[0][1] and self.board[item[0][0]][item[0][1]].symbol == "P"
                    if item[1] == (x, y) and item[2] is False and not pawn_cond:
                        illegal_moves.append(elem)
                self.board[elem[0][0]][elem[0][1]] = piece
                self.board[elem[1][0]][elem[1][1]] = picked
        legal_moves = list(set(possible_for_ally) - set(illegal_moves))

        return legal_moves

    def FEN_calculations(self, capture, piece):
        FEN = ""
        cords = ()
        for a, row in enumerate(self.board):
            empty_spaces = 0
            for b, elem in enumerate(row):
                if type(elem) != str:
                    if empty_spaces != 0:
                        FEN += str(empty_spaces)
                        empty_spaces = 0
                    if elem.symbol == "P" and elem.color == self.turn:
                        if elem.en_passant != ():
                            cords = elem.en_passant
                    if elem.color == "black":
                        FEN += elem.symbol.lower()
                        if elem.symbol == "K":
                            elem.possible_moves(elem.pose, self.board)
                            black_castle = self.board[a][b].castle
                    else:
                        FEN += elem.symbol
                        if elem.symbol == "K":
                            elem.possible_moves(elem.pose, self.board)
                            white_castle = self.board[a][b].castle
                else:
                    empty_spaces += 1
            if empty_spaces != 0:
                FEN += str(empty_spaces)
            FEN += "/"
            b = -1
        if self.turn == "white":
            turn = "w"
        else:
            turn = "b"
        if cords != ():
            space_symbol = chr(ord("a") + cords[1]) + str(8 - cords[0])
        else:
            space_symbol = "-"
        moves = self.half_moves // 2 + 1
        if piece.symbol == "P" or capture:
            self.half_moves_no_pawn_no_capture = 0
        else:
            self.half_moves_no_pawn_no_capture = self.half_moves_no_pawn_no_capture + 1
        if white_castle == "" and black_castle == "":
            black_castle = "-"
        FEN = FEN[:-1]
        FEN = FEN + f' {turn} {white_castle}{black_castle} {space_symbol} {self.half_moves_no_pawn_no_capture} {moves}'
        self.FEN = FEN

    def set_prev_state(self):
        self.previous_state = {
                               'board': deepcopy(self.board),
                               'w_king': self.w_king_pose,
                               'b_king': self.b_king_pose,
                               'turn': self.turn,
                               'FEN': self.FEN,
                               'half_moves': self.half_moves}

    def switch_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

    def calc_game_status(self, possible_for_enemy, possible_for_ally):
        checkmate = False
        stalemate = False
        king = self.w_king_pose if self.turn == "white" else self.b_king_pose
        check = self.board[king[0]][king[1]].check_status(possible_for_enemy)
        if check:
            checkmate = self.board[king[0]][king[1]].checkmate_status(check, possible_for_ally)
        else:
            stalemate = self.board[king[0]][king[1]].stalemate(check, possible_for_ally)
        self.check = check
        self.gameover = checkmate
        self.draw = stalemate

        return check, checkmate, stalemate

    def move(self, current_pose, picked_pose, promo=None):
        enemy = "black" if self.turn == "white" else "white"
        self.set_prev_state()
        self.made_moves.append(deepcopy(self.previous_state))
        moving_piece = self.board[current_pose[0]][current_pose[1]]
        moving_piece.first_move = False
        if moving_piece.symbol == "K" and \
           (picked_pose[1] + 2 == current_pose[1]
                or picked_pose[1] - 2 == current_pose[1]):
            self.board[picked_pose[0]][picked_pose[1]] = moving_piece
            self.board[current_pose[0]][current_pose[1]] = ""
            if picked_pose[1] == 6:
                self.board[picked_pose[0]][picked_pose[1] + 1].pose = \
                    (current_pose[0], current_pose[1] + 1)
                self.board[current_pose[0]][current_pose[1] + 1] = \
                    self.board[picked_pose[0]][picked_pose[1] + 1]
                self.board[picked_pose[0]][picked_pose[1] + 1] = ""
            elif picked_pose[1] == 2:
                self.board[picked_pose[0]][picked_pose[1] - 2].pose = \
                    (current_pose[0], current_pose[1] - 1)
                self.board[current_pose[0]][current_pose[1] - 1] = \
                    self.board[picked_pose[0]][picked_pose[1] - 2]
                self.board[picked_pose[0]][picked_pose[1] - 2] = ""
        elif moving_piece.symbol == "P" and \
            self.board[picked_pose[0]][picked_pose[1]] == "" and \
                (picked_pose[1] + 1 == current_pose[1] or
                    picked_pose[1] - 1 == current_pose[1]):
            self.board[picked_pose[0]][picked_pose[1]] = moving_piece
            self.board[current_pose[0]][current_pose[1]] = ""
            if self.board[picked_pose[0] + 1][picked_pose[1]] == "":
                self.board[picked_pose[0] - 1][picked_pose[1]] = ""
            elif self.board[picked_pose[0] - 1][picked_pose[1]] == "":
                self.board[picked_pose[0] + 1][picked_pose[1]] = ""
        else:
            if self.board[current_pose[0]][current_pose[1]].symbol == "P" and \
                picked_pose[0] in (0, 7):
                moving_piece = Queen(1000, self.turn, (picked_pose[0], picked_pose[1]), "PQ1")
            self.board[picked_pose[0]][picked_pose[1]] = moving_piece
            self.board[current_pose[0]][current_pose[1]] = ""
        moving_piece.move(picked_pose)
        if moving_piece.symbol == 'K':
            if moving_piece.color == 'white':
                self.w_king_pose = picked_pose
            else:
                self.b_king_pose = picked_pose
        self.half_moves += 1
        self.switch_turn()
        self.board_status_reset()
        possible_for_enemy = self.possible_for_enemies(enemy)
        possible_for_enemy = self.possible_to_board(possible_for_enemy)
        possible_for_ally = self.possible_for_allies(possible_for_enemy, False)
        self.calc_game_status(possible_for_enemy, possible_for_ally)

    def undo_move(self):
        self.previous_state = self.made_moves.pop()
        self.board = self.previous_state['board']
        self.b_king_pose = self.previous_state['b_king']
        self.w_king_pose = self.previous_state['w_king']
        self.turn = self.previous_state['turn']
        self.half_moves = self.previous_state['half_moves']
        self.FEN = self.previous_state['FEN']
        self.previous_state = self.made_moves[-1]


class Game():
    def __init__(self):
        self.board = Board()
        self.history = [deepcopy(self.board.board)]
        self.FEN_list = []

    def highlight(self, possible_moves, terminal_board):
        for elem in possible_moves:
            if terminal_board[elem[1][0]][elem[1][1]] == "   ":
                terminal_board[elem[1][0]][elem[1][1]] = " o "
            if terminal_board[elem[1][0]][elem[1][1]] != "   ":
                if terminal_board[elem[1][0]][elem[1][1]][0] == "b" and self.board.turn == "white" or \
                    terminal_board[elem[1][0]][elem[1][1]][0] == "w" and self.board.turn == "black":
                    terminal_board[elem[1][0]][elem[1][1]] = " x "
        self.draw_board(terminal_board)

    def del_highlight(self):
        self.draw_board(self.board.board)

    def highlight_calc(self, cords):
        row, col = cords
        piece = self.board.board[row][col]
        possible_for_enemies = self.board.possible_for_enemies(self.board.turn)
        if piece.symbol == 'K':
            possible_for_enemies = self.board.possible_to_board(possible_for_enemies)
        possible_moves = piece.possible_moves(piece.pose, self.board.board,
                                              self.board.previous_state['board'],
                                              possible_for_enemies)
        possible_moves = self.board.legal_moves(possible_moves)

        return possible_for_enemies, possible_moves

    def find_piece(self, name, board):
        cords = None
        for x, row in enumerate(board):
            for y, col in enumerate(row):
                if col == name:
                    cords = (x, y)
        return cords

    def draw_board(self, board, possible_moves=[], check=False, mate=False):
        terminal_board = deepcopy(board)
        for x, row in enumerate(board):
            for y, elem in enumerate(row):
                if type(elem) != str:
                    terminal_board[x][y] = elem.name
                elif elem == "":
                    terminal_board[x][y] = "   "
        print("-" * 56)
        for n, row in enumerate(terminal_board):
            row = f'{row} {8 - n}'
            print(row)
            print("-" * 56)
        print("   a      b      c      d      e      f      g      h")
        return terminal_board
        
    def play(self):
        text =  """
        Chess game
        x in possible moves means capture
        o in possible moves means normal move
        pick piece by entering its name
        pick move by calling a position e.g e4
        """
        print(text)
        FEN_cond = 0
        capture = False
        moved_piece = None
        picked = False
        promotion = False
        promo_piece = None
        positions = {"a": 0, "b": 1, "c": 2,
                     "d": 3, "e": 4, "f": 5,
                     "g": 6, "h": 7}
        terminal = self.draw_board(self.board.board)
        while True:
            if FEN_cond == 0 and self.board.half_moves != 0:
                self.board.FEN_calculations(capture, moved_piece)
                FEN_cond = 1
                self.FEN_list.append(self.board.FEN[:-2].rstrip()[:-2].rstrip())
            if self.FEN_list.count(self.board.FEN[:-2].rstrip()[:-2].rstrip()) == 3:
                self.board.draw = True
            if self.board.draw or self.board.gameover:
                if self.board.draw:
                    print("Draw")
                    break
                if self.board.gameover:
                    if self.board.turn == "black":
                        print("White wins!")
                        break
                    else:
                        print("Black wins!")
                        break
            while True:
                print(f'Turn: {self.board.turn}')
                piece = input("Choose piece to move: ")
                if piece[0] == "w" and self.board.turn == "black" or \
                    piece[0] == "b" and self.board.turn == "white":
                    print("It is not turn of this piece!")
                elif self.find_piece(piece, terminal) is None:
                    print("There is no such a piecie!")
                else:
                    cords = self.find_piece(piece, terminal)
                    possible_enemy, possible = self.highlight_calc(cords)
                    if len(possible) == 0:
                        print("This peice can't move. Choose other piece!")
                    else:
                        self.highlight(possible, terminal)
                        break
            while True:
                move = input("Choose where to move: ")
                try:
                    print(move[0])
                    print(move[1])
                    y = positions[move[0]]
                    print(y)
                    x = 8 - int(move[1])
                    print(x)
                    print(terminal[x][y])
                    if terminal[x][y] != " x " and terminal[x][y] != " o ":
                        print("Inocorrect move!")
                    else:
                        # self.del_highlight()
                        moved_piece = self.board.board[cords[0]][cords[1]]
                        self.board.move(cords, (x, y))
                        FEN_cond = 0
                        if type(self.board.previous_state['board'][x][y]) == str:
                            capture = False
                        else:
                            capture = True
                        moves_to_draw = self.board.FEN[:-2].rstrip()
                        if int(moves_to_draw[-2:] == 50):
                            self.board.draw = True
                        terminal = self.draw_board(self.board.board)
                        break
                except Exception:
                    print("Inocorrect move!")
            if True in (self.board.gameover, self.board.draw):
                if self.board.draw:
                    print("Draw")
                    break
                if self.board.gameover:
                    if self.board.turn == "black":
                        print("White wins!")
                        break
                    else:
                        print("Black wins!")
                        break


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()