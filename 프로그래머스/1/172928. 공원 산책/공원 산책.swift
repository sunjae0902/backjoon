import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    let move = [
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0),
    ]
    var park = park.map { Array($0) }
    let w = park[0].count
    let h = park.count
    var s: (Int, Int) = (0, 0)
    for i in 0..<h {
        for j in 0..<w {
            if park[i][j] == "S" {
                s = (i, j)
            }
        }
    }
    
    for route in routes {
        let items = route.split(separator: " ")
        let dir = String(items[0])
        guard let cnt = Int(items[1]) else { return [] }
        var canMove = true
        if let dist = move[dir] {
            var nx = s.0
            var ny = s.1
            for i in 0..<cnt {
                nx += dist.0
                ny += dist.1
                if !(0..<h).contains(nx) || !(0..<w).contains(ny) {
                    canMove = false
                    break
                }
                if park[nx][ny] == "X" {
                    canMove = false
                    break
                }
            }
            if canMove {
                s = (nx, ny)
            }
        }
    }

    return [s.0, s.1]
}