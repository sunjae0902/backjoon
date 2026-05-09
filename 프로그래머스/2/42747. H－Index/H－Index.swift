import Foundation

func solution(_ citations:[Int]) -> Int {
    for h in stride(from: 1000, to: 0, by: -1) {
        var cnt = 0
        for c in citations {
            if c >= h { cnt += 1}
        }
        if cnt >= h { return h }
    }
    return 0
}