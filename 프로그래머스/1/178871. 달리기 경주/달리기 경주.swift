import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var rank: [String: Int] = [:]
    var playerList = players
    for (i, player) in players.enumerated() {
        rank[player] = i // 0-
    }
    for name in callings {
        guard let curRank = rank[name] else { continue }
        let prevPlayer = playerList[curRank-1]
        rank[name] = curRank-1
        rank[prevPlayer] = curRank
        playerList.swapAt(curRank, curRank-1)
    }
    var sortedArr = rank.sorted { $0.value < $1.value }
    return sortedArr.map { $0.key }
}