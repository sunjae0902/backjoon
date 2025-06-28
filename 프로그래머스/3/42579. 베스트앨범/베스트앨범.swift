import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    let n = genres.count
    var genreToSongs: [String: [(count: Int, number: Int)]] = [:]
    
    for i in 0..<n {
        genreToSongs[genres[i], default: []].append((plays[i], i)) // 디폴트 값 명시하기
    }
    
    let genreTotalPlays = genreToSongs.mapValues { songs in songs.reduce(0) { $0 + $1.count} }
    let sortedGenres = genreTotalPlays.sorted { $0.value > $1.value }.map {$0.key} // 총 재생 수가 많은대로 정렬된 장르 배열
    
    var answer: [Int] = []
    
    for genre in sortedGenres {
        let sortedSongs = genreToSongs[genre]!.sorted { 
            if ($0.count == $1.count) {
                return $0.number < $1.number
            } 
            return $0.count > $1.count
        }
        let songsCnt = min(2, sortedSongs.count)
        answer.append(contentsOf: sortedSongs[0..<songsCnt].map { $0.number }) // 요소를 개별로 추가
    }
    
    return answer
}