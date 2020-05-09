from copy import deepcopy
import sys

sys.setrecursionlimit(1000000)


def dfs(lst, path, adj_, target):
    adj = deepcopy(adj_)
    if len(path) != 1:
        adj[path[-2]].pop(adj[path[-2]].index(path[-1]))
    if len(path) == target:
        if path not in lst:
            lst.append(path)
        return
    if path[-1] not in adj:
        return
    else:
        for i in range(len(adj[path[-1]])):
            adj_node = adj[path[-1]][i]
            dfs(lst, path+[adj_node], adj, target)
        return


def solution(tickets):
    adj = {}
    target = len(tickets) + 1
    for ticket in tickets:
        start, end = ticket
        if start in adj:
            adj[start].append(end)
        else:
            adj[start] = [end]
    need_visit = []
    lst = []
    path = ["ICN"]
    dfs(lst, path, adj, target)
    return(sorted(lst)[0])
    # return answer


print(solution([["ICN", "COO"], ["ICN", "BOO"],
                ["COO", "ICN"], ["BOO", "DOO"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], [
#       "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
