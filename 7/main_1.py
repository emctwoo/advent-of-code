import numpy as np


class Task:

    def __init__(self, task, depends_on):
        self.task = task
        if depends_on is None:
            self.dependencies = list()
        else:
            self.dependencies = [depends_on]

    def __repr__(self):
        return self.task

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

def get_init_tasks(tasks):
    return {tasks[t] for t in tasks if len(tasks[t].dependencies) == 0}

def update_tasks(tasks, executed_tasks):
    _ = [tasks.pop(t.task) for t in executed_tasks]

def get_next_task(tasks, executed_tasks):
    next_tasks = list()
    for t in tasks:
        all_dependencies_done = \
            np.all([d in executed_tasks for d in tasks[t].dependencies])
        if all_dependencies_done:
            next_tasks.append(tasks[t])
    print(f'candidates: {next_tasks}')
    next_task = sorted(next_tasks).pop(0)
    print(f'next_task: {next_task}')
    return next_task


with open('input.txt', 'r') as f:
    instructions = f.readlines()
    tasks = [i.split(' ') for i in instructions]
    task_names = [t[7] for t in tasks]
    dependencies = [t[1] for t in tasks]

seen_tasks = set()
tasks = dict()

for t, d in zip(task_names, dependencies):
    if d not in seen_tasks:
        seen_tasks.add(d)
        nd = Task(d, None)
        tasks[d] = nd
    else:
        nd = tasks[d]

    if t not in seen_tasks:
        seen_tasks.add(t)
        nt = Task(t, nd)
        tasks[t] = nt
    else:
        nt = tasks[t]
        nt.dependencies.append(nd)

for t in list(tasks):
    print(tasks[t].task)
    print(tasks[t].dependencies)
    pass

execution_order = list()
init_tasks = get_init_tasks(tasks)
progress = set(init_tasks)
execution_order = sorted(list(init_tasks))

update_tasks(tasks, init_tasks)
while len(tasks) > 0:
    next_task = get_next_task(tasks, progress)
    update_tasks(tasks, [next_task])
    execution_order.append(next_task)
    progress.add(next_task)

print('executed tasks:')
print(progress)

print('execution_order')
print(execution_order)
print(''.join([t.task for t in execution_order]))

