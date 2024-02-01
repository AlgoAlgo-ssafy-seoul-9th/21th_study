import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

left, right = 0, 0
max_len = 0
num_set = set()
# nums[right] in nums[left:right]를 사용하여 중복을 확인하면 시간 복잡도가 O(N)이므로 
# 입력이 100,000개의 숫자로 이루어져 있을 때 시간 초과

# 중복을 효율적으로 확인하기 위해 집합(Set) 사용
# Set은 중복된 값을 허용하지 않으며, 검색 연산(contains)의 시간 복잡도가 O(1)이기 때문에 더 효율적 

while right < N:
    # 들어오는 수가 구간에 없으면
    if nums[right] not in num_set:
        num_set.add(nums[right])
        right += 1
        max_len = max(max_len, right - left)
    # 들어오는 수가 구간에 있으면
    else:
        num_set.remove(nums[left])
        left += 1

print(max_len)
