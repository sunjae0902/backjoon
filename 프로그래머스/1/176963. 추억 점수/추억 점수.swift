import Foundation
func getScore(_ arr: [Int]) -> Int {
    return arr.reduce(0) {sum, num in return sum + num}
}
func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var score: [String: Int] = [:]
    for i in 0..<name.count {
        score[name[i]] = yearning[i]
    }
    var answer: [Int] = []
    for people in photo {
        var scoreArr: [Int] = []
        for name in people {
            scoreArr.append(score[name, default: 0])
        }
        answer.append(getScore(scoreArr))
    }
    return answer
}