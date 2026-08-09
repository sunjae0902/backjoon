from collections import defaultdict

def solution(record):
    answer = []
    info = defaultdict(str)
    log = [ ]
    for args in record:
        args = list(args.split(" "))
        cmd, user_id = args[:2]
        log.append((cmd, user_id))
        
        if len(args) == 3:
            info[user_id] = args[-1]
        
    for cmd, user_id in log:
        if cmd == 'Enter':
            answer.append(info[user_id] + "님이 들어왔습니다.")
        elif cmd == 'Leave':
            answer.append(info[user_id] + "님이 나갔습니다.")
    return answer