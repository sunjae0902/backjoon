import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var answer = 0
    var dict: [String: [String]] = [:]
    for item in clothes {
        dict[item[1], default: []].append(item[0])
    }
    
    answer = dict.reduce(1) { acc, cur in
        acc * (cur.value.count + 1)
    }
    return answer-1
}