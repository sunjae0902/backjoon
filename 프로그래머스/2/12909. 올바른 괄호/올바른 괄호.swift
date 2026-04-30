import Foundation

func solution(_ s:String) -> Bool
{
    var st: [Character] = []
    for ch in s {
        if ch == "(" {
            st.append(ch)
        } else {
            if st.isEmpty { return false }
            st.removeLast()
        }
    }
    return st.isEmpty
}