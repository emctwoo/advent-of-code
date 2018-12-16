



import numpy as np


class Task:

    def __init__(self, task, time_needed):
        self.task = task
        self.dependencies = set()
        self.time_needed = time_needed

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.task == other.task
        else:
            return False

    def __hash__(self):
        return hash(self.task)

    def __lt__(self, other):
        if isinstance(other, Task):
            return self.task < other.task

def get_init_task(tasks):
    return (sorted(
        [tasks[t] for t in tasks if len(tasks[t].dependencies) ==0])
        .pop(0))

def get_next_task(tasks, executed_tasks):
    next_tasks = list()
    for t in tasks:
        all_dependencies_done = \
            np.all([d in executed_tasks for d in tasks[t].dependencies])
        if all_dependencies_done or len(tasks[t].dependencies) == 0:
            next_tasks.append(tasks[t])
    return sorted(next_tasks).pop(0)  # Sorts based on task name to get first.


with open('input.txt', 'r') as f:
    instructions = f.readlines()
    tasks = [i.split(' ') for i in instructions]
    task_names = [t[7] for t in tasks]
    dependencies = [t[1] for t in tasks]

ASCII_CHARACTERS = map(chr, range(65, 91))
TIMES = 60 + np.array(range(1, 27))
time_per_task = dict(zip(ASCII_CHARACTERS, TIMES))

tasks = dict()
for t in task_names + dependencies:
    if t not in tasks:
        tasks[t] = Task(t, time_per_task[t])

for t, d in zip(task_names, dependencies):
    tasks[t].dependencies.add(tasks[d])

init_task = get_init_task(tasks)
execution_order = [init_task]
tasks.pop(init_task.task)

progress = set([init_task])
while len(tasks) > 0:
    next_task = get_next_task(tasks, progress)
    tasks.pop(next_task.task)
    execution_order.append(next_task)
    progress.add(next_task)

# TODO: Treat as matrix and iterate row by row, column is worker and row is
# time.

print(''.join([t.task for t in execution_order]))

