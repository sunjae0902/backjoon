import Foundation

func solution(_ n:Int, _ roads:[[Int]], _ sources:[Int], _ destination:Int) -> [Int] {
    var graph = Array(repeating: [Int](), count: n+1)
    for road in roads {
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    }
    
    var distance = Array(repeating: -1, count: n+1)
    distance[destination] = 0

    var queue = [destination] //큐
    var index = 0
    
    while index < queue.count {
        let current = queue[index]
        index += 1
        
        for neighbor in graph[current] {
            if distance[neighbor] == -1 {
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
            }
        }
    }

    return sources.map { distance[$0] }
}