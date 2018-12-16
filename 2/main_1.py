

with open('input.txt', 'r') as f:
    input_data = f.readlines()

character_triplets = 0
character_duplicates = 0

for box_id in input_data:
    box_dict = dict()
    for char in box_id:
        if char not in list(box_dict):
            box_dict[char] = 0
        box_dict[char] += 1

    char_counts = [box_dict[char_key] for char_key in list(box_dict)]

    if 2 in char_counts:
        character_duplicates += 1
    if 3 in char_counts:
        character_triplets += 1

print(character_duplicates * character_triplets)

