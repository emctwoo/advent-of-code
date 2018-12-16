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

def get_units(polymer):
    units_lower = list(set(polymer.lower()))
    units_upper = [unit.upper() for unit in units_lower]
    return list(zip(units_lower, units_upper))

def filter_char(string, char):
    return ''.join(string.split(char))


with open('input.txt', 'r') as f:
    polymer = f.readline().split('\n')[0]

units = get_units(polymer)
units.sort()

reduced_size = list()
for small_unit, big_unit in units:
    print(f'Filter: ({small_unit}, {big_unit})')
    _ = filter_char(polymer, small_unit)
    polymer_filtered = filter_char(_, big_unit)
    reduced = reduction(polymer_filtered)
    reduced_size.append(len(reduced))

print(min(reduced_size))

