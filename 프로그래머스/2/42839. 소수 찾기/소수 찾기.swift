import Foundation

func solution(_ numbers: String) -> Int {
    var nums = Array(numbers) // 문자열 -> 배열로 변경
    var candidates = Set<Int>() // 정답 저장할 셋
    
    func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num == 2 { return true }
        if num % 2 == 0 { return false }
        let limit = Int(sqrt(Double(num)))
        for i in stride(from: 3, through: limit, by: 2) {
            if num % i == 0 {
                return false
        }
    }
    return true
}


    func permute(_ arr: [Character], _ visited: inout [Bool], _ current: String) {
        if !current.isEmpty {
            if let number = Int(current) {
                candidates.insert(number)
            }
        }
        if current.count == arr.count { return }

        for i in 0..<arr.count {
            if visited[i] { continue }
            visited[i] = true
            permute(arr, &visited, current + String(arr[i]))
            visited[i] = false
        }
    }

    var visited = Array(repeating: false, count: nums.count)
    permute(nums, &visited, "")

    return candidates.filter { isPrime($0) }.count
}
