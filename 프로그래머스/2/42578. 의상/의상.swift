import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var clotheMap: [String: [String]] = [:]
    for clothe in clothes {
        clotheMap[clothe[1], default: []].append(clothe[0])
    }
    var cnt = 1
    for val in clotheMap.values {
        cnt *= val.count + 1
    }
    return cnt-1
}