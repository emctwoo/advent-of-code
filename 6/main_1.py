import pandas as pd
import numpy as np
from collections import Counter


class Point: def __init__(self, x, y):
        self.x = x
        self.y = y

    def man_dist(self, other):
        assert isinstance(other, Point), 'Must be point'
        return np.abs(self.x - other.x) + np.abs(self.y - other.y)

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.man_dist(other) == 0
        else:
            False

    def __hash__(self):
        return hash((self.x, self.y))


with open('input.txt', 'r') as f:
    _ = [c.split(',') for c in f.readlines()]
    coordinates_list = list(zip(
        [int(c[0]) for c in _],
        [int(c[1].strip()) for c in _]))
    coordinates_df = pd.DataFrame({
        'x': [c[0] for c in coordinates_list],
        'y': [c[1] for c in coordinates_list]})

x_min, x_max = np.min(coordinates_df.x), np.max(coordinates_df.y)
y_min, y_max = np.min(coordinates_df.y), np.max(coordinates_df.y)
coordinates_df.loc[:, 'p'] = \
        coordinates_df.apply(lambda c: Point(c['x'], c['y']), axis=1)

print(coordinates_df.head())

print('Canvas')
print(f'x: ({x_min}, {x_max})')
print(f'y: ({y_min}, {y_max})')

x_range = range(x_min, x_max)
y_range = range(y_min, y_max)

boundary_points = list()
canvas = dict()

from tqdm import tqdm
for x in tqdm(x_range):
    for y in y_range:
        coordinates_df_copy = coordinates_df.copy()
        p = Point(x, y)
        coordinates_df_copy['c'] = p
        coordinates_df_copy.loc[:, 'd'] = coordinates_df_copy.apply(lambda x: x['c'].man_dist(x['p']), axis=1)
        min_distance = coordinates_df_copy.d.min()
        points = list(coordinates_df_copy.loc[coordinates_df_copy.d == min_distance, 'p'])
        canvas[p] = points if len(points) == 1 else None

appearances = list()
for p in list(canvas):
    if canvas[p] is not None:
        appearances += canvas[p]

print(Counter(appearances))

