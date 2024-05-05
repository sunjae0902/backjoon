let N = Int(readLine()!)!
typealias myTuple = (age:Int, name:String)
var arr: Array<myTuple> = []

for _ in 0..<N {
    let strArr = readLine()!.split(separator: " ")
    let person = myTuple(age: Int(strArr[0])!, name: String(strArr[1]))
    arr.append(person)
}

let sortedArr = arr.sorted {
    if $0.0 > $1.0 {
        return $0.0 < $1.0
    }
    else if $0.0 == $1.0 {
        return $0.0 > $1.0
    }
    return true
}
var i = 1
while i <= N {
    print(sortedArr[i-1].age, sortedArr[i-1].name)
    i += 1
}