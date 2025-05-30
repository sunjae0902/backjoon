import Foundation

func toStr(_ time: Int) -> String {
    let h = time / 3600
    let m = time % 3600 / 60
    let s = time % 60
    return String(format: "%02d:%02d:%02d", h, m, s)
}   

func toSec(_ time: String) -> Int {
    let parts = time.split(separator: ":").map { Int($0)! }
    return 3600 * parts[0] + 60 * parts[1] + parts[2]
}

func solution(_ play_time:String, _ adv_time:String, _ logs:[String]) -> String {
    let playSec = toSec(play_time)
    let advSec = toSec(adv_time)

    var count = [Int](repeating: 0, count: playSec+2)
    
    for log in logs {
        let parts = log.split(separator: "-").map { String($0) }
        let start = toSec(parts[0])
        let end = toSec(parts[1])
        count[start] += 1
        count[end] -= 1
    }
    
    for i in 1..<playSec {
        count[i] += count[i-1]
    }
    for i in 1..<playSec {
        count[i] += count[i-1]
    }
    
    var max_time: Int = 0
    var answer: String = ""
    for start in 0...(playSec-advSec) {
        let end = start + advSec - 1
        let total = count[end] - (start > 0 ? count[start - 1] : 0)
        if max_time < total {
            max_time = total
            answer = toStr(start)
        }
    }
    return answer
}