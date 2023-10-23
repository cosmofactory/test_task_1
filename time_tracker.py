class DailyStat:
    """Some time tracker for various tasks."""

    def __init__(self):
        self._tasks = {}

    def set_task(self, task_name: str, time_spent: int):
        if task_name in self._tasks:
            self._tasks[task_name] += time_spent
        else:
            self._tasks[task_name] = time_spent

    def get_task(self, task_name: str) -> int:
        return self._tasks.get(task_name, 0)

    def get_all(self) -> str:
        return "\n".join(f"{task}: {time}" for task, time in self._tasks.items())
