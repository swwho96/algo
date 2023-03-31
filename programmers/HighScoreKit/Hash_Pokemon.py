# 가져갈 수 있는 포켓몬 중 최대한 많은 종류의 포켓몬을 가져가야 한다
# 가져갈 수 있는 포켓몬의 수가 포켓몬의 종류보다 많다면 모든 종류를 가져갈 수 있다
# 포켓몬의 종류가 가져갈 수 있는 포켓몬의 수보다 많다면 가져갈 수 있는 만큼의 포켓몬 종류를 가져갈 수 있다

def solution(nums):
    kinds = len(set(nums))
    can_take_num = len(nums) // 2
    return min(kinds, can_take_num)