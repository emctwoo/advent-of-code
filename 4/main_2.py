import pandas as pd
import numpy as np
import datetime


class Guard:

    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.sleep_counter = np.zeros(shape=(1, 60)).flatten()

    def update_sleep_time(self, start_minute, end_minute):
        self.sleep_counter[start_minute: end_minute] += 1


TIME_FORMAT = '[%Y-%m-%d %H:%M]'

with open('input.txt', 'r') as f:
    schedule = f.readlines()

times = list()
for event in schedule:
    time = event[0: 18]
    time = datetime.datetime.strptime(time, TIME_FORMAT)
    times.append(time)

schedule = [x for _, x in sorted(zip(times, schedule))]  # Sort based on other.

guards = dict()
for event in schedule:
    time = event[0: 18]
    event_name = event[19: len(event) - 1]
    time = datetime.datetime.strptime(time, TIME_FORMAT)
    if event_name[0] == 'G':
        # Get the guard.
        guard_id = event_name.split()[1][1:]
        if guard_id in list(guards):
            guard = guards[guard_id]
        else:
            guard = Guard(guard_id)
            guards[guard_id] = guard
    else:
        if event_name == 'wakes up':
            sleep_end_time = time.minute
            guard.update_sleep_time(sleep_start_time, sleep_end_time)
        elif event_name == 'falls asleep':
            sleep_start_time = time.minute

max_sleep = list()
minute_with_max_sleep = list()
guard_ids = list(guards)
for guard_id in guard_ids:
    guard = guards[guard_id]
    max_sleep.append(np.max(guard.sleep_counter))
    minute_with_max_sleep.append(np.argmax(guard.sleep_counter))

print(int(guard_ids[np.argmax(max_sleep)]) *
        minute_with_max_sleep[np.argmax(max_sleep)])

