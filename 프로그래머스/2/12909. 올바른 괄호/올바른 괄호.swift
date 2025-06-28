import Foundation

func solution(_ s:String) -> Bool {
    var stack: [Character] = [] // 문자
    for p in s {
        if stack.isEmpty || p == "(" {
            stack.append(p)
        } else {
            let popped = stack.popLast()
        }
    }
    if !stack.isEmpty {
        return false
    }
    return true
}