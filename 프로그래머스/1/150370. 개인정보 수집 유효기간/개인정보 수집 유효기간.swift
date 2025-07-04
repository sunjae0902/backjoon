import Foundation

func getExpiredDate(_ from: String, _ duration: Int) -> String {
    let splited = from.split(separator: ".")
    guard var y = Int(splited[0]),
          var m = Int(splited[1]),
          var d = Int(splited[2]) else { return "" }

    // 일 보정
    if d == 1 {
        d = 28
        m -= 1
        if m == 0 {
            m = 12
            y -= 1
        }
    } else {
        d -= 1
    }

    // 전체 개월 수 계산
    let totalMonths = m + duration
    y += (totalMonths - 1) / 12
    m = totalMonths % 12
    if m == 0 { m = 12 }

    return "\(y).\(String(format: "%02d", m)).\(String(format: "%02d", d))"
}


func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    let duration = terms.reduce(into: [String: Int]()) { dict, term in // 지금까지 누적된 변수, 현재 변수
    let typeAndDur = term.split(separator: " ")
    if typeAndDur.count == 2, let months = Int(typeAndDur[1]) {
        dict[String(typeAndDur[0])] = months
    }
}
    var expireDates: [String] = []
    for privacy in privacies {
        let items = privacy.split(separator: " ")
        if let months = duration[String(items[1])] {
             expireDates.append(getExpiredDate(String(items[0]), months))
        }
    }

    let dateFormatter = DateFormatter()
    dateFormatter.dateFormat = "yyyy.MM.dd"
    
    guard let todayDate = dateFormatter.date(from: today) else { return [] }

    var answer: [Int] = []
    for (i, dateStr) in expireDates.enumerated() {
        if let expireDate = dateFormatter.date(from: dateStr), todayDate > expireDate {
            answer.append(i+1)
        }
    }

    return answer
}