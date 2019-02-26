import os
from file_reader import read_file

class PizzaSlicer:
    def __init__(self, header, rows):
        self.rows = header['rows']
        self.cols = header['cols']
        self.min_ingredients = header['minIngredients']
        self.maxCellsPerClice = header['maxCellsPerSlice']
        self.rows = []
        for row in rows:
            self.rows.append(row['row'])


example_file = os.path.join('data', 'a_example.in')
small_file = os.path.join('data', 'b_small.in')
medium_file = os.path.join('data', 'c_medium.in')
big_file = os.path.join('data', 'd_big.in')

example = read_file(example_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])
small = read_file(small_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])
medium = read_file(medium_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])
big = read_file(big_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])

exampleSlicer = PizzaSlicer(example['header'], example['rows'])
smallSlicer = PizzaSlicer(small['header'], small['rows'])
mediumSlicer = PizzaSlicer(medium['header'], medium['rows'])
bigSlicer = PizzaSlicer(big['header'], big['rows'])

