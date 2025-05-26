import Foundation

func solution(_ order: [Int]) -> Int {
    var answer = 0
    var mainBelt = Array((1...order.count).reversed())
    var subBelt: [Int] = []
    
    for o in order {
        if let last = mainBelt.last, last == o { // if-let: 옵셔널이 아닐 경우 실행
            mainBelt.removeLast() // 배열 마지막 요소 제거, 시간복잡도 O(1)
            answer += 1
        } else if let last = subBelt.last, last == o {
            subBelt.removeLast()
            answer += 1
        } else {
            while let last = mainBelt.last, last != o {
                subBelt.append(mainBelt.removeLast()) // 배열 추가: append
            }
            if let last = mainBelt.last, last == o {
                mainBelt.removeLast()
                answer += 1
            } else if let last = subBelt.last, last == o {
                subBelt.removeLast()
                answer += 1
            } else {
                break
            }
        }
    }
    
    return answer
}
