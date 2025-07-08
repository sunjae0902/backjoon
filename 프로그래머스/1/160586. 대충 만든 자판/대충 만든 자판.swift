import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    var minCntMap: [Character: (n: Int, cnt: Int)] = [:]
    
    for (i, str) in keymap.enumerated() {
        let key = i + 1
        for (j, ch) in str.enumerated() {
            let cnt = j + 1
            if let chInfo = minCntMap[ch] {
                if cnt < chInfo.cnt {
                    minCntMap[ch] = (key, cnt)
                }
            } else {
                minCntMap[ch] = (key, cnt)
            }
        }
    }
    var answer: [Int] = []
    for target in targets {
        var total = 0
        var valid = true
        for ch in target { 
            if let chInfo = minCntMap[ch] {
                total += chInfo.cnt
            } else {
                valid = false
                break
            }
        }
        answer.append(valid ? total : -1 )
    }
    return answer
}