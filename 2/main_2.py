import pandas as pd


def differing_char_count(x, y):
    assert len(x) == len(y), 'strings must be same length'

    not_same_character_count = 0
    for char_pos in range(0, len(x)):
        if x[char_pos] != y[char_pos]:
            not_same_character_count += 1

    return not_same_character_count


with open('input.txt', 'r') as f:
    input_data = f.readlines()

box_id_df = pd.DataFrame({
    'box_id': [box_id[0:len(box_id) - 1] for box_id in input_data],
    '_key':1})

box_id_df_cross_join = pd.merge(box_id_df, box_id_df.copy(), on=['_key'])
box_id_df_cross_join.drop(columns=['_key'], inplace=True)

box_id_df_cross_join.loc[:, 'n_differing_char'] = (
    box_id_df_cross_join.apply(
        lambda row: differing_char_count(
            x=row['box_id_x'],
            y=row['box_id_y']),
            axis=1))

near_match_boxes = box_id_df_cross_join.loc[
    box_id_df_cross_join.n_differing_char == 1, :]

near_duplicate_word_x = near_match_boxes.head(1)['box_id_x'].values[0]
near_duplicate_word_y = near_match_boxes.head(1)['box_id_y'].values[0]

same_chars = list()
for i_char in range(0, len(near_duplicate_word_x)):
    assert isinstance(near_duplicate_word_x, str), f'must be string, is {type(near_duplicate_word_x)}'
    x = near_duplicate_word_x[i_char]
    y = near_duplicate_word_y[i_char]

    if x == y:
        same_chars.append(x)

print(''.join(same_chars))

