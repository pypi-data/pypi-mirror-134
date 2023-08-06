from queue import Queue
from time import sleep
from threading import Thread


class TaskQueue:
    def __init__(self, num_workers=4):
        self.num_workers = num_workers
        self.total_num_jobs = 0
        self.jobs_completed = 0
        self.answers_sent = 0
        self.jobs = Queue()
        self.results = Queue()
        # self.start_workers()

    def add_task(self, task, *args, **kwargs):
        args = args or ()
        kwargs = kwargs or {}
        self.total_num_jobs += 1
        self.jobs.put((task, args, kwargs))

    def start_workers(self):
        for _ in range(self.num_workers):
            t = Thread(target=self.worker)
            t.daemon = True
            t.start()

    def worker(self):
        while True:
            item, args, kwargs = self.jobs.get()
            item(*args, **kwargs)
            self.jobs_completed += 1
            self.jobs.task_done()

    def get_answers(self):
        while self.answers_sent < self.total_num_jobs or self.jobs_completed == 0:
            yield self.results.get()
            self.answers_sent += 1
            self.results.task_done()


def task(task_num, sleep_time, q):
    sleep(sleep_time)
    ans = "Task #{} sleeping {}".format(task_num, sleep_time)
    q.put((task_num, ans))


if __name__ == "__main__":
    h = TaskQueue(num_workers=4)
    q = h.results
    answers = {}
    curr_task = 1

    for t, s in zip([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1]):
        h.add_task(task, t, s, q)

    for task_num, ans in h.get_answers():
        answers[task_num] = ans
        if curr_task in answers:
            print(answers[curr_task])
            del answers[curr_task]
            curr_task += 1

    # Print remaining items (if any)
    for k, v in sorted(answers.items()):
        print(v)
