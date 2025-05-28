import Foundation

func correct(_ arr: [Character]) -> Bool {
    var stack: [Character] = []
    for s in arr {
        if "[({".contains(s) {
            stack.append(s)
        } else {
            if let last = stack.last { // 옵셔널
                let pair = String(last) + String(s) // string으로 변환 후 더하기
                if ["()", "[]", "{}"].contains(pair) {
                    stack.popLast()
                } else {
                    return false
                }
            } else {
                return false
            }
        }
    }
    return stack.isEmpty
}

func solution(_ s: String) -> Int {
    var answer = 0
    let arr = Array(s)
    let n = arr.count
    
    for i in 0..<n {
        let s1 = Array(arr[(i+1)..<n])
        let s2 = Array(arr[0...i])
        
        if correct(s1 + s2) {
            answer += 1
        }
    }
    
    return answer
}