import os
import glob
import matplotlib.pyplot as plt

digit_count = {}

with open('FGNET.txt', 'r') as file:
    for line in file:
        columns = line.split()
        if len(columns) >= 2:
            second_column = columns[1]
            for char in second_column:
                if char.isdigit():
                    num = int(char)
                    print(num)