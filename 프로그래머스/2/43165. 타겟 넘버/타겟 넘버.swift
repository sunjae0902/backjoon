import Foundation

extension String {
    subscript(_ i: Int) -> Character {
        self[index(startIndex, offsetBy: i)]
    }
}

func dfs(_ cur: String, _ n: Int) -> [String] {
    if cur.count == n {
        return [cur]
    }
    
    var combis: [String] = []
    
    combis += dfs(cur + "+", n)
    combis += dfs(cur + "-", n)
    
    return combis
}


func solution(_ numbers:[Int], _ target:Int) -> Int {
    var combi: [String] = []
    var answer = 0
    let n = numbers.count
    combi = dfs("", n)
    for comb in combi {
        var res = 0
        for i in 0..<n {
            if comb[i] == "+" {
                res += numbers[i]
            } else {
                res -= numbers[i]
            }
        }
        if res == target {
            answer += 1
        }
    }
    return answer
}