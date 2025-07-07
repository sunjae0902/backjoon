import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    var visited: [Int] = Array(repeating: 0, count: n+1)
    var answer = 0
    for sn in section {
        if visited[sn] != 0 { continue }
        answer += 1
        for i in sn..<min(sn+m, n+1) {
            visited[i] = 1
        }
    }
    return answer
}