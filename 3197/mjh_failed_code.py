import sys
from collections import deque

sys.setrecursionlimit(10**8)

class Swan:
    area_number = 0
    area_root = []
    day = 0
    swans = []
    blocks = deque()
    water_coming_blocks = deque()

    def __init__(self, arr):
        self.arr = arr

    def change_water_to_number(self, x, y):
        arr = self.arr
        shift_r = (-1, 0, 0, 1)
        shift_c = (0, -1, 1, 0)
        visited = set()
        queue = deque()
        queue.append((x, y))
        visited.add((x, y))
        while queue:
            r, c = queue.popleft()
            if arr[r][c] == 'L':
                self.swans.append(self.area_number)
            arr[r][c] = self.area_number
            for i in range(4):
                rs = r + shift_r[i]
                cs = c + shift_c[i]
                if 0 <= rs and rs < len(arr) \
                and 0 <= cs and cs < len(arr[rs]) \
                and (rs, cs) not in visited:
                    if arr[rs][cs] == '.' or arr[rs][cs] == 'L':
                        queue.append((rs, cs))
                        visited.add((rs, cs))

    # public
    def set_number_in_water_area(self):
        arr = self.arr
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == '.' or arr[i][j] == 'L':
                    self.change_water_to_number(i, j)
                    self.increase_area_number()
                elif arr[i][j] == 'X':
                    if self.is_water_coming(i, j):
                        self.append_water_coming_block(i, j)
                    else:
                        self.append_block(i, j)
    
    def is_water_coming(self, r, c) -> bool:
        arr = self.arr
        shift_r = (-1, 0, 0, 1)
        shift_c = (0, -1, 1, 0)
        for i in range(4):
            rs = r + shift_r[i]
            cs = c + shift_c[i]
            if 0 <= rs and rs < len(arr) \
            and 0 <= cs and cs < len(arr[rs]) \
            and (type(arr[rs][cs]) is int or arr[rs][cs] == '.'):
                return True
        return False

    def melt(self) -> bool:
        arr = self.arr
        shift_r = (-1, 0, 0, 1)
        shift_c = (0, -1, 1, 0)

        while self.water_coming_blocks:
            r, c = self.pop_water_coming_block()
            mixing_waters = []
            for i in range(4):
                rs = r + shift_r[i]
                cs = c + shift_c[i]
                if 0 <= rs and rs < len(arr) \
                and 0 <= cs and cs < len(arr[rs]) \
                and type(arr[rs][cs]) is int:
                    mixing_waters.append(arr[rs][cs])
            if self.area_root[self.swans[0]] in mixing_waters and self.area_root[self.swans[1]] in mixing_waters:
                return True
            min_num = min(mixing_waters)
            for num in mixing_waters:
                if num > min_num:
                    root_num = self.find_root(num)
                    root_min_num = self.find_root(min_num)
                    self.area_root[root_num] = self.area_root[root_min_num]
            arr[r][c] = self.area_root[min_num]

        return False
    
    def find_water_coming_blocks(self):
        new_blocks = deque()
        while self.blocks:
            r, c = self.pop_block()
            if self.is_water_coming(r, c):
                self.append_water_coming_block(r, c)
            else:
                new_blocks.append((r, c))
        self.blocks = new_blocks

    # public
    def the_time_goes_on(self):
        swans = self.swans
        if swans[0] == swans[1]:
            return self.day
        while True:
            # self.print_arr()
            self.increase_day()
            if self.melt():
                return self.day
            self.find_water_coming_blocks()
    
    def increase_area_number(self):
        self.area_root.append(self.area_number)
        self.area_number += 1

    def increase_day(self):
        self.day += 1

    def append_block(self, x, y):
        self.blocks.append((x, y))
    
    def pop_block(self):
        return self.blocks.popleft()
    
    def append_water_coming_block(self, x, y):
        self.water_coming_blocks.append((x, y))
    
    def pop_water_coming_block(self):
        return self.water_coming_blocks.popleft()
    
    def find_root(self, num):
        if self.area_root[num] == num:
            return num
        self.area_root[num] = self.find_root(self.area_root[num])
        return self.area_root[num]

    # FOR DEBUG
    def print_arr(self):
        arr = self.arr
        print()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(arr[i][j], end=' ')
            print()

def main():
    R, C = map(int, sys.stdin.readline().split())
    arr = [0 for _ in range(R)]

    for i in range(R):
        arr[i] = [*sys.stdin.readline().strip()]

    swan = Swan(arr)
    swan.set_number_in_water_area()
    print(swan.the_time_goes_on())

main()