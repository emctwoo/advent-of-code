def is_reactive(x, y):
    return ((x.lower() == y.lower()) and
            (x.islower() != y.islower()))

def reduction(polymer):
    potentially_reducible = True  # Input is assumed to be reducible.
    while potentially_reducible:
        reduction_found = False  # Current iteration.
        for i_unit in range(len(polymer)):
            if i_unit + 1 >= len(polymer):
                # at last index, needed since size changes.
                break
            elif is_reactive(polymer[i_unit], polymer[i_unit + 1]):
                reduction_found = True
                polymer = react(polymer, i_unit, i_unit + 1)
        potentially_reducible = reduction_found  # At least one reduction was found.
    return polymer

def react(polymer, start, end):
    return polymer[:start] + polymer[end + 1:]


with open('input.txt', 'r') as f:
    polymer = f.readline().split('\n')[0]

print('Before ({})): '.format(len(polymer)))
print(polymer + '\n')
reduced = reduction(polymer)
print('After ({}): '.format(len(reduced)))
print(reduced)

