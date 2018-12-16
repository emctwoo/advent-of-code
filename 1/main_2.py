

with open('input.txt', 'r') as f:
    input_data = f.readlines()

signs = [freq[0:1] for freq in input_data]
frequency_changes = [freq[1:len(freq)] for freq in input_data]

current_frequency = 0
seen_frequencies = set()
seen_frequencies.add(current_frequency)
duplicate_found = False

while not duplicate_found:
    for sign, freq in zip(signs, frequency_changes):
        assert sign in ['+', '-'], 'Sign must be one of + and -.'
        frequency_change = int(freq) if sign == '+' else -int(freq)
        current_frequency += frequency_change
        if current_frequency not in seen_frequencies:
            seen_frequencies.add(current_frequency)
        else:
            duplicate_found = True
            break

print(current_frequency)

