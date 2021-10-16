import copy
from tkinter import *


class GameOfLife:
    def __init__(self, size):
        self.root = Tk()
        self.root.title("GamOfLife")
        self.root.resizable(width=False, height=False)

        self.size = size
        self.map = []
        self.map_copy = []
        self.segments = []
        for i in range(size):
            self.map.append([0] * size)
            self.map_copy.append([0] * size)
            self.segments.append([None] * size)
            for j in range(size):
                self.segments[i][j] = Canvas(self.root, width=15, height=15, bg="#000000", highlightthickness=0)
                self.segments[i][j].grid(row=i, column=j)

    def set_positive(self, pos_x, pos_y):
        self.map_copy[pos_y][pos_x] = 1

    def set_negative(self, pos_x, pos_y):
        self.map_copy[pos_y][pos_x] = 0

    def overwrite_map(self):
        self.map = copy.deepcopy(self.map_copy)

    def adjacent(self, pos_x, pos_y):
        n = 0
        adjacent = [(pos_x - 1, pos_y - 1), (pos_x, pos_y - 1), (pos_x + 1, pos_y - 1), (pos_x - 1, pos_y),
                    (pos_x + 1, pos_y), (pos_x - 1, pos_y + 1), (pos_x, pos_y + 1), (pos_x + 1, pos_y + 1)]
        for i in range(8):
            for j in range(2):
                if adjacent[i][j] < 0 or adjacent[i][j] >= self.size:
                    adjacent[i] = "X"
                    n += 1
                    break

        for k in range(n):
            adjacent.remove("X")

        return adjacent

    def check_value(self, pos_x, pos_y):
        adjacent = self.adjacent(pos_x, pos_y)
        val = 0
        for i in adjacent:
            val += self.map[i[1]][i[0]]

        if val == 2 and self.map[pos_y][pos_x] == 1:
            self.set_positive(pos_x, pos_y)
        elif val == 3:
            self.set_positive(pos_x, pos_y)
        else:
            self.set_negative(pos_x, pos_y)

    def next_life_cycle(self):
        for i in range(self.size):
            for j in range(self.size):
                self.check_value(j, i)
        self.overwrite_map()

    def print_map(self):
        for i in self.map:
            print(i)
        print("=" * self.size)

    def update(self):
        self.next_life_cycle()
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == 1:
                    self.segments[i][j]["bg"] = "#ffffff"
                else:
                    self.segments[i][j]["bg"] = "#000000"
        self.root.update()

    def begin(self):
        while True:
            self.root.after(100, self.update())

    def create_glider(self, start_x, start_y):
        self.set_positive(start_x, start_y)
        self.set_positive(start_x + 1, start_y)
        self.set_positive(start_x + 2, start_y)
        self.set_positive(start_x, start_y + 1)
        self.set_positive(start_x + 1, start_y + 2)

    def create_glider_down(self, start_x, start_y):
        self.set_positive(start_x, start_y)
        self.set_positive(start_x, start_y - 1)
        self.set_positive(start_x, start_y - 2)
        self.set_positive(start_x - 1, start_y)
        self.set_positive(start_x - 2, start_y - 1)

    def create_dacotas_flight(self, start_x, start_y):
        self.set_positive(start_x, start_y)
        self.set_positive(start_x + 1, start_y)
        self.set_positive(start_x + 3, start_y)
        self.set_positive(start_x + 4, start_y)
        self.set_positive(start_x + 5, start_y)
        self.set_positive(start_x + 1, start_y - 1)
        self.set_positive(start_x + 2, start_y - 1)
        self.set_positive(start_x + 1, start_y + 1)
        self.set_positive(start_x + 2, start_y + 1)
        self.set_positive(start_x + 3, start_y + 1)
        self.set_positive(start_x + 4, start_y + 1)
        self.set_positive(start_x + 5, start_y + 1)
        self.set_positive(start_x + 2, start_y + 2)
        self.set_positive(start_x + 3, start_y + 2)
        self.set_positive(start_x + 4, start_y + 2)


if __name__ == "__main__":
    example = GameOfLife(30)
    example.create_glider(20, 20)
    example.create_glider(25, 20)
    example.create_glider(20, 25)
    example.create_glider_down(5, 5)
    example.create_glider_down(10, 5)
    example.create_glider_down(5, 10)
    example.create_dacotas_flight(15, 15)
    example.overwrite_map()
    example.update()
    example.root.after(500, example.begin())
    example.root.mainloop()
