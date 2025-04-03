def solution(words):
    trie = {}
    answer = 0

    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {"#": 0} 
            node = node[char]
            node["#"] += 1
    
    for word in words:
        node = trie
        for i, char in enumerate(word):
            node = node[char]
            if node["#"] == 1:  
                answer += i + 1
                break
        else:
            answer += len(word)

    return answer
