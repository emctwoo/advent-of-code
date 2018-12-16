import numpy as np

with open('input.txt', 'r') as f:
    claims = f.readlines()

canvas = np.zeros(shape=(1000, 1000))
for claim in claims:
    claim_components = claim.split()
    claim_start = claim_components[2]
    claim_start = claim_start[0:len(claim_start) - 1].split(',')
    claim_start_x, claim_start_y = int(claim_start[0]), int(claim_start[1])

    claim_shape = claim_components[3].split('x')
    claim_shape_x, claim_shape_y = int(claim_shape[0]), int(claim_shape[1])

    canvas[
        claim_start_x: claim_start_x + claim_shape_x,
        claim_start_y: claim_start_y + claim_shape_y] += 1

print(np.sum(canvas > 1))

