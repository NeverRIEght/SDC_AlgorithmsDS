from collections import deque, defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Using modified Dijkstra's algorithm
        # F + C * log(F) where F is the number of flights and C is the number of cities

        graph = defaultdict(list)
        for source, target, cost in flights:
            graph[source].append((target, cost))

        queue = [(src, 0, 0)]

        # (node, stops) -> total_cost
        min_cost = defaultdict()
        min_cost[(src, 0)] = 0

        while queue:
            cost, current_city, stops = heappop(queue)

            if current_city == dst:
                return cost

            if stops > k:
                continue

            for neighbor, price in graph[current_city]:
                new_cost = cost + price
                if new_cost < min_cost[(neighbor, stops + 1)]:
                    min_cost[(neighbor, stops + 1)] = new_cost
                    heappush(queue, (new_cost, neighbor, stops + 1))

        return -1