import heapq

class MaxHeapJobScheduler:
    def __init__(self):
        self._heap = []

    def add_job(self, priority, job_name):
        heapq.heappush(self._heap, (-priority, job_name))
        print(f"\nAdded job: {job_name} with priority {priority}")
        self.print_heap_tree()

    def process_job(self):
        if not self._heap:
            print("No jobs to process.")
            return None
        priority, job_name = heapq.heappop(self._heap)
        print(f"\nProcessing job: {job_name} (Priority: {-priority})")
        self.print_heap_tree()
        return (job_name, -priority)

    def has_jobs(self):
        return len(self._heap) > 0

    def print_heap_tree(self):
        n = len(self._heap)
        if n == 0:
            print("Heap is empty!")
            return
        
        def get_left(i):
            return 2 * i + 1
        
        def get_right(i):
            return 2 * i + 2
        
        print("\nHeap Tree Structure:")
        for i in range(n):
            val, name = self._heap[i]
            left = get_left(i)
            right = get_right(i)
            line = f"[{name}:{-val}]"
            if left < n:
                lval, lname = self._heap[left]
                line += f" --> Left -> [{lname}:{-lval}]"
            if right < n:
                rval, rname = self._heap[right]
                line += f" --> Right -> [{rname}:{-rval}]"
            print(line)
        print()

# Example usage
scheduler = MaxHeapJobScheduler()
scheduler.add_job(50, "JobA")
scheduler.add_job(30, "JobB")
scheduler.add_job(40, "JobC")
scheduler.add_job(10, "JobD")
scheduler.add_job(20, "JobE")

while scheduler.has_jobs():
    scheduler.process_job()

