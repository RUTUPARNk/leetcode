class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (priority, userId)
            heapq.heappush(self.heap, (-priority, -taskId, userId))
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_map[taskId][1]
        self.task_map[taskId] = (newPriority, userId)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))
        

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]
        

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, userId = self.heap[0]
            taskId = -negTaskId
            if taskId not in self.task_map:
                heapq.heappop(self.heap)
                continue
            current_priority, current_user = self.task_map[taskId]
            if current_priority == -priority and current_user == userId:
                heapq.heappop(self.heap)
                del self.task_map[taskId]
                return userId
            else:
                heapq.heappop(self.heap)
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()