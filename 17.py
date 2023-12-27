'''
new graph
vertices: (row, col, last_dir, steps from that dir)
edges
(row, col, 'r', steps) -> (row, col + 1, 'r', steps+1), assuming steps < 3 weight: map[row][col+1]
(row, col, 'r', steps) -> (row+1, col, 'l', 1)
...
'''