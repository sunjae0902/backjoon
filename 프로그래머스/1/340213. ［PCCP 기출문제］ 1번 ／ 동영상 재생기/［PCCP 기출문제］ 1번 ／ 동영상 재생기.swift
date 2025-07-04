import Foundation

func toSec(_ pos: String) -> Int? {
    let components = pos.split(separator: ":")
    guard components.count == 2,
          let minutes = Int(components[0]),
          let seconds = Int(components[1]) else {
        return nil
    }
    return minutes * 60 + seconds
}

func toStr(_ sec: Int) -> String {
    return String(format: "%02d", Int(sec / 60)) + ":" + String(format: "%02d", sec % 60)
}

func solution(_ video_len:String, _ pos:String, _ op_start:String, _ op_end:String, _ commands:[String]) -> String {
    guard var curSec = toSec(pos) else { return "" }
    guard let totalSec = toSec(video_len) else { return "" }
    guard let start = toSec(op_start), let end = toSec(op_end), start <= end else { return "" }
    let opRange = start...end  

    if opRange.contains(curSec) {
        curSec = opRange.upperBound // 끝으로 이동
    }
    for command in commands {
        if command == "prev" {
            curSec = curSec <= 10 ? 0 : curSec-10
        } else if command == "next" {
            curSec = totalSec-curSec <= 10 ? totalSec : curSec+10
        }
        
        if opRange.contains(curSec) {
            curSec = opRange.upperBound // 끝으로 이동
        }
    }
    return toStr(curSec)
}