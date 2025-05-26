import Foundation

func isPrime(_ n: Int) -> Bool {
    if n == 2 {
        return true
    } 
    if n < 2 || n % 2 == 0 {
        return false
    } 
    // 단순 순회의 경우 for i in a...b 사용
    for i in stride(from: 3, through: Int(Double(n).squareRoot()), by: 2) {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func toKBase(_ n: Int, _ k: Int) -> [String] {
    if n == 0 {
        return ["0"]
    }
    var n = n
    var arr: [String] = []
    while n > 0 {
        arr.append(String(n % k))
        n /= k
    }
    return arr.reversed()
}

func solution(_ n: Int, _ k: Int) -> Int {
    let based = toKBase(n, k)
    let joined = based.joined() // 배열을 문자열로 합침
 
    // Substring type -> String 타입으로 변환
    let parts = joined.split(separator: "0").map { String($0) }
    
    var answer = 0
    for part in parts {
        if let num = Int(part), isPrime(num) {
            answer += 1
        }
    }
    return answer
}