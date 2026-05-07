import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var bridge: [(Int, Int)] = []
    var answer = 0
    var truck_weights = truck_weights
    while true {
        if truck_weights.count == 0 {
            break
        }
        answer += 1
        if !bridge.isEmpty && bridge[0].0 + bridge_length == answer {
            let _ = bridge.removeFirst()
        }
        let sum = bridge.reduce(0) { $0 + $1.1 }
        if bridge.count < bridge_length && sum + truck_weights.first! <= weight {
            let now = truck_weights.removeFirst()
            bridge.append((answer, now))
        }
   }
    if bridge.count != 0 {
        answer += bridge_length
    }
    return answer
}