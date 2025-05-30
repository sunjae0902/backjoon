import Foundation

func solution(_ scores: [[Int]]) -> Int {
    var answer = 0
    var indexedScores = scores.enumerated().map { (i, score) in return [i, score[0], score[1], 0] }
    indexedScores.sort {
        if $0[1] != $1[1] { // 내림 차순
            return $0[1] > $1[1]
        } else {
            return $0[2] < $1[2] // 오름 차순
        }
    }

    var disqualified = Set<Int>()
    var maxB = -1
    for score in indexedScores {
        if score[2] < maxB {
            disqualified.insert(score[0])
        } else {
            maxB = max(maxB, score[2])
        }
    }

    if disqualified.contains(0) {
        return -1
    }

    var rankList = indexedScores.filter { !disqualified.contains($0[0]) }
    rankList.sort { // 점수 정렬
        $0[1] + $0[2] > $1[1] + $1[2]
    }

    rankList[0][3] = 1
    for i in 1..<rankList.count {
        if rankList[i][1] + rankList[i][2] == rankList[i-1][1] + rankList[i-1][2] {
            rankList[i][3] = rankList[i-1][3]
        } else {
            rankList[i][3] = i + 1
        }
    }

    for score in rankList {
        if score[0] == 0 {
            answer = score[3]
            break
        }
    }

    return answer
}
