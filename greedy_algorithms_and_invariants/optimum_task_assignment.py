from collections import namedtuple

def optimum_task_assignment(tasks_duration):
    PairedTasks = namedtuple('PairedTasks', ('task1', 'task2'))
    res = []
    start, end = 0, len(tasks_duration) - 1
    tasks_duration.sort()
    while start < end :
        res.append(PairedTasks(tasks_duration[start], tasks_duration[end]))
        start, end = start+1, end-1
    return res

if __name__ == "__main__":
    tasks_duration = [5,2,1,6,4,4]
    print(optimum_task_assignment(tasks_duration))