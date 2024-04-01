def solution(enroll, referral, seller, amount):
    n = len(enroll)
    tree = {}
    money = {}
    for i in range(n):
        tree[enroll[i]] = referral[i]  
        money[enroll[i]] = 0
        
    def dfs(name, benefit):
        if name == '-':
            return
        if int(benefit*0.1) >= 1:
            money[name] += benefit - int(benefit*0.1)
            dfs(tree[name], int(benefit*0.1))
        else:
            money[name] += benefit
            return
        
    for s, a in zip(seller, amount):
        dfs(s, a*100)
        
    return list(money.values())