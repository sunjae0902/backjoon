#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> form(int i, int n) {
    if (i == 0) { return {0}; }
    vector<int> res;
    while (i > 0) {
        res.push_back(i%n);
        i /= n;
    }
    reverse(res.begin(), res.end());
    return res;
}
string solution(int n, int t, int m, int p) {
    string answer = "";
    string total = "";
    for (int i=0; i < t*m; i++) {
        for (int x: form(i, n)) {
            if (x > 9) {
                total += x-10 + 'A';
            } else {
                total += x + '0';
            }
        }
    }
    for (int i = 0; i < t*m; i++) {
        if (i%m == p-1) {
            answer += total[i];
        }
    }
    return answer;
}