
from workers.task import execute_bead_task




def dispatch_convoy(convoy):
    task_ids = []

    for bead in convoy:
        task = execute_bead_task.delay(bead)
        task_ids.append(task.id)

    return task_ids