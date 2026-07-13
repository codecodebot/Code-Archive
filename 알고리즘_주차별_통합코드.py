# -*- coding: utf-8 -*-
"""
알고리즘 수업 주차별 통합 코드

- 각 Jupyter Notebook의 코드 셀을 하나의 Python 파일로 통합
- 각 자료는 2주 단위로 구분
- 원본에서 문법적으로 불완전한 코드 셀은 삭제하지 않고 주석 처리
"""


# ==============================================================================
# 1~2주차 | 알고리즘 성능 분석
# 원본 파일: 알고리즘_성능_분석_발표자료 (2) (2).ipynb
# ==============================================================================

# %% [1~2주차] 합이 k인 두 수 구하기
import time

nums = list(map(int, input("정수 입력: ").split()))
k = int(input("목표 합 k 입력: "))

# 브루트포스
start = time.time()

result1 = None
n = len(nums)

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == k:
            result1 = [i, j]
            break
    if result1 is not None:
        break

end = time.time()
time1 = end - start

# 최적화

start = time.time()

seen = {} # 본 숫자와 그 인덱스를 저장할 딕셔너리
result2 = None

for i in range(len(nums)): #리스트를 한번만 순회하여 최적화
    target = k - nums[i]

    if target in seen: #필요한 값이 이미 등장한적 있다면 정답 처리
        result2 = [seen[target], i]
        break

    seen[nums[i]] = i

end = time.time()
time2 = end - start

# 시간 비교
diff = abs(time1 - time2)

# 출력
print("브루트포스 결과:", result1)
print(f"브루트포스 시간: {time1:.8f}")

print("최적화 결과:", result2)
print(f"최적화 시간: {time2:.8f}")

print(f"시간 차이: {diff:.8f}")

if time1 > time2:
    print("브루트포스가 더 오래 걸림")
elif time2 > time1:
    print("최적화 풀이가 더 오래 걸림")
else:
    print("두 방법의 시간이 동일함")

# %% [1~2주차] 성적 상위 k명 뽑기
import time
import heapq

scores = list(map(int, input("점수 입력: ").split()))
k = int(input("k 입력: "))

# 브루트포스
start = time.time()

arr1 = scores[:]
result1 = []

for _ in range(k): # 전체를 순회하면서 가장 큰 값을 하나씩 추출
    max_score = max(arr1)
    result1.append(max_score)
    arr1.remove(max_score)

end = time.time()
time1 = end - start

print("브루트포스 결과:", result1)
print(f"브루트포스 시간: {time1:.8f}")

# 최적화
start = time.time()

heap = [] #HEAP형태로 저장해서
for score in scores:
    if len(heap) < k:
        heapq.heappush(heap, score)
    elif score > heap[0]:
        heapq.heapreplace(heap, score)

result2 = sorted(heap, reverse=True)

end = time.time()
time2 = end - start

print("최적화 결과:", result2)
print(f"최적화 시간: {time2:.8f}")

diff = abs(time1 - time2)
print(f"시간 차이: {diff:.8f}")

if time1 > time2:
    print("브루트포스가 더 오래 걸림")
else:
    print("최적화 풀이가 더 오래 걸림")

# %% [1~2주차] 4.계단 오르기
#O(N)풀이
import time

n = int(input("계단 수 입력: "))

if n == 1:
    result2 = 1
elif n == 2:
    result2 = 2
else:
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    result2 = b
print(result2)

# %% [1~2주차] 4.계단 오르기
#O(1) 풀이
import math

n = int(input("계단 수 입력: "))

phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2

result = round((phi ** (n + 1) - psi ** (n + 1)) / math.sqrt(5))

print(result)

# %% [1~2주차] 4.계단 오르기
import time
import matplotlib.pyplot as plt

ns = list(range(1, 1001))

times_iter = []
times_formula = []
time_diffs = []

for n in ns:
    total_time1 = 0
    total_time2 = 0

    for _ in range(5):
        # 방법 1: 반복문
        start = time.time()
        if n == 1:
            result1 = 1
        elif n == 2:
            result1 = 2
        else:
            a, b = 1, 2
            for _ in range(3, n + 1):
                a, b = b, a + b
            result1 = b
        total_time1 += time.time() - start

        # 방법 2: 수식
        start = time.time()
        result2 = round(
            pow((1 + 5**0.5) / 2, n + 1) / (5**0.5)
        )
        total_time2 += time.time() - start

    avg_time1 = total_time1 / 5
    avg_time2 = total_time2 / 5

    times_iter.append(avg_time1)
    times_formula.append(avg_time2)
    time_diffs.append(abs(avg_time1 - avg_time2))

plt.figure(figsize=(10, 6))
plt.plot(ns, times_iter, label="Method 1: Iterative")
plt.plot(ns, times_formula, label="Method 2: Formula")
plt.plot(ns, time_diffs, label="Time Difference")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Execution Time Comparison (Average of 5 Runs)")
plt.legend()
plt.grid(True)
plt.show()

# %% [1~2주차] 4.계단 오르기
import time
import matplotlib.pyplot as plt

ns = list(range(1, 1001))

times_iter = []
times_formula = []
time_diffs = []

for n in ns:
    # 방법 1: 반복문 (100회 평균)
    start = time.perf_counter()
    for _ in range(100):
        if n == 1:
            result1 = 1
        elif n == 2:
            result1 = 2
        else:
            a, b = 1, 2
            for _ in range(3, n + 1):
                a, b = b, a + b
            result1 = b
    avg_time1 = (time.perf_counter() - start) / 100

    # 방법 2: 수식 (100회 평균)
    start = time.perf_counter()
    for _ in range(100):
        result2 = round(
            pow((1 + 5**0.5) / 2, n + 1) / (5**0.5)
        )
    avg_time2 = (time.perf_counter() - start) / 100

    times_iter.append(avg_time1)
    times_formula.append(avg_time2)
    time_diffs.append(abs(avg_time1 - avg_time2))

plt.figure(figsize=(10, 6))
plt.plot(ns, times_iter, label="Method 1: Iterative")
plt.plot(ns, times_formula, label="Method 2: Formula")
plt.plot(ns, time_diffs, label="Time Difference")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Execution Time Comparison (Average of 100 Runs)")
plt.legend()
plt.grid(True)
plt.show()

# %% [1~2주차] 4.계단 오르기
import time
import matplotlib.pyplot as plt

ns = list(range(1, 1001))

times_iter = []
times_formula = []
time_diffs = []
digits_list = []

for n in ns:
    start = time.perf_counter()
    for _ in range(100):
        if n == 1:
            result1 = 1
        elif n == 2:
            result1 = 2
        else:
            a, b = 1, 2
            for _ in range(3, n + 1):
                a, b = b, a + b
            result1 = b
    avg_time1 = (time.perf_counter() - start) / 100

    start = time.perf_counter()
    for _ in range(500):
        result2 = round(pow((1 + 5**0.5) / 2, n + 1) / (5**0.5))
    avg_time2 = (time.perf_counter() - start) / 100

    times_iter.append(avg_time1)
    times_formula.append(avg_time2)
    time_diffs.append(abs(avg_time1 - avg_time2))
    digits_list.append(len(str(result1)))

plt.figure(figsize=(10, 6))
plt.plot(ns, times_iter, label="Method 1: Iterative")
plt.plot(ns, times_formula, label="Method 2: Formula")
plt.plot(ns, time_diffs, label="Time Difference")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Execution Time Comparison (Average of 100 Runs)")
plt.legend()
plt.grid(True)
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(ns, times_iter, label="Iterative Time")
ax1.set_xlabel("n")
ax1.set_ylabel("Execution Time (s)")

ax2 = ax1.twinx()
ax2.plot(ns, digits_list, label="Number of Digits")
ax2.set_ylabel("Digits of Fibonacci-like Value")

plt.title("Iterative Time and Number of Digits")
ax1.grid(True)
plt.show()

# %% [1~2주차] 4.계단 오르기
import time
import matplotlib.pyplot as plt

ns = list(range(1, 1001))

times_iter = []
bit_lengths = []

for n in ns:
    start = time.perf_counter()
    for _ in range(100):
        if n == 1:
            result1 = 1
        elif n == 2:
            result1 = 2
        else:
            a, b = 1, 2
            for _ in range(3, n + 1):
                a, b = b, a + b
            result1 = b
    avg_time1 = (time.perf_counter() - start) / 100

    times_iter.append(avg_time1)
    bit_lengths.append(result1.bit_length())

spikes = []
window = 5
threshold = 1.5

for i in range(window, len(times_iter) - window):
    left_avg = sum(times_iter[i - window:i]) / window
    right_avg = sum(times_iter[i + 1:i + 1 + window]) / window
    local_avg = (left_avg + right_avg) / 2

    if times_iter[i] > local_avg * threshold:
        spikes.append((ns[i], times_iter[i], bit_lengths[i]))

print("Spike 후보:")
for n, t, bits in spikes:
    print(f"n={n}, time={t:.8e}, bit_length={bits}")

plt.figure(figsize=(10, 6))
plt.plot(ns, times_iter, label="Iterative Time")
plt.scatter([x[0] for x in spikes], [x[1] for x in spikes], label="Spike Points")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Iterative Time with Spike Points (window=5)")
plt.legend()
plt.grid(True)
plt.show()

# %% [1~2주차] 4.계단 오르기
import sys
print(sys.int_info)
print(sys.int_info.bits_per_digit)

# %% [1~2주차] 가장 가까운 두 수
import time

nums = list(map(int, input("정수 입력: ").split()))
arr = nums[:]
arr.sort()#아래 코드는 O(n)이므로, arr.sort에 의해 시간복잡도 O(n log n)결정
min_diff2 = float('inf')
for i in range(1, len(arr)):
    diff = arr[i] - arr[i - 1]
    if diff < min_diff2:
        min_diff2 = diff
print(min_diff2)

# %% [1~2주차] 가장 가까운 두 수
#insertion_sort
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array

# %% [1~2주차] 가장 가까운 두 수
#timesort
def timsort(array):
    min_run = 32
    n = len(array)
    for i in range(0, n, min_run):#insertion_sort를 n/min_run번 호출
        insertion_sort(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:#merge_sort
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            array[start:start + len(merged_array)] = merged_array
        size *= 2#이 코드로 인해 log n

    return array

# %% [1~2주차] 섬의 개수 세기
from collections import deque

m, n = map(int, input("행 열 입력: ").split())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))

g2 = [row[:] for row in grid]

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if g2[x][y] == 0:
        return

    g2[x][y] = 0
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

count2 = 0
for i in range(m):#이 부분으로 인해 시간복잡도 O(mn)결정
    for j in range(n):
        if g2[i][j] == 1:
            count2 += 1
            dfs(i, j)

print(count2)


# ==============================================================================
# 3~4주차 | 해시 테이블
# 원본 파일: 해시테이블_발표_코드 (10).ipynb
# ==============================================================================

# %% [3~4주차] 나눗셈 해싱
class HashTableDivision():
  def __init__(self, size=7):
    self.size = size
    self.table = [None] * size

  def hash_fn(self, key):
    return key % self.size

  def insert(self, key, value):
    idx = self.hash_fn(key)
    self.table[idx] = (key, value)

  def search(self, key):
    if self.table[self.hash_fn(key)] is None:
      return "Null"
    return self.table[self.hash_fn(key)][1]

  def delete(self, key):
    idx = self.hash_fn(key)

    if self.table[idx] is None:
      print("삭제 실패: 해당 key 없음")
      return

    if self.table[idx][0] == key:
      self.table[idx] = None
      print("삭제 완료")
    else:
      print("삭제 실패: key 불일치")

  def display(self):
    print("\n[ 해시 테이블 상태 ]")
    for i, slot in enumerate(self.table):
      print(f" [{i}] {slot}")
    print()

# %% [3~4주차] 나눗셈 해싱
ht = HashTableDivision(size=7)

ht.insert(16, "apple")   # 16 % 7 = 2
ht.insert(5,  "daisy")   # 5  % 7 = 5

ht.display()

ht.delete(16)
ht.display()

print("search(16):", ht.search(16))

# %% [3~4주차] 자릿수 접기 해싱
class HashTableFolding():
    def __init__(self, size=7, group_size=2):
        self.size = size # 해시테이블 크기
        self.group_size = group_size #해시테이블을 몇개씩 접을지
        self.table = [None] * size # 테이블 생성

    def hash_fn(self, key):
        s = str(key) # 문자열로 변환
        total = 0
        for i in range(0, len(s), self.group_size): #시작부터 끝까지 2단위로 쪼개기
            total += int(s[i:i+self.group_size]) #i부터 i+2(g.p)까지 정수형으로 더하기
        return total % self.size # 테이블 크기에 대한 나머지로

    def insert(self, key, value):
      idx = self.hash_fn(key)
      if self.table[idx] is not None:
        print(f"충돌 발생! index {idx}: {self.table[idx]} -> ({key}, {value})") # 충돌발생이 자릿수 접기의 한계임
      self.table[idx] = (key, value) #덮어쓰기로 처리

    def delete(self, key):
      idx = self.hash_fn(key) #key에 해당하는 해시값
      if self.table[idx] is None: #해시테이블에 없을때 예외처리
        print("삭제 실패: 해당 key 없음")
        return
      if self.table[idx][0] == key: #
        self.table[idx] = None
        print("삭제 완료")
      else:
        print("삭제 실패: key 불일치")

    def search(self, key): #찾아서 반환
        idx = self.hash_fn(key)
        if self.table[idx] is not None and self.table[idx][0] == key:
            return self.table[idx][1]
        return None

    def display(self): # 모두 출력
        print(f"\n[ 자릿수 접기 해시 테이블 (Size: {self.size}) ]")
        for i, slot in enumerate(self.table):
            if slot is not None:
                print(f"  [{i}] {slot}")

# %% [3~4주차] 자릿수 접기 해싱
ht = HashTableFolding()

# 삽입
ht.insert(10, 'A')
ht.insert(20, 'B')
ht.insert(17, 'C')  # 충돌

# 출력
ht.display()

# 탐색
print("search(10):", ht.search(10))
print("search(20):", ht.search(20))
print("search(99):", ht.search(99))  # 없음

# 삭제
ht.delete(20)
ht.delete(99)  # 없음

# 최종 상태
ht.display()

# %% [3~4주차] 체이닝
class Node:
    def __init__(self, key, value):
        # 연결리스트
        self.key = key        # 저장할 key
        self.value = value    # key의 값
        self.next = None

class HashTableChaining:
    def __init__(self, size=7):
        self.size = size
        # 각 슬롯에는 데이터가 아니라 "연결 리스트의 시작 노드"가 들어감
        self.table = [None] * size

    def hash_fn(self, key):
        # 나눗셈 해싱
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_fn(key)

        # 이미 같은 key가 있는지 먼저 확인 (있으면 값만 업데이트)
        cur = self.table[idx]
        while cur:
            if cur.key == key:
                cur.value = value
                return
            cur = cur.next

        # 새로운 노드를 생성해서 "리스트의 맨 앞(head)"에 삽입
        new_node = Node(key, value)
        new_node.next = self.table[idx]
        self.table[idx] = new_node

    def search(self, key):
        idx = self.hash_fn(key)
        cur = self.table[idx]

        # 연결 리스트를 앞에서부터 순회하면서 key 탐색
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next

        # 찾는 값이 없으면 None 반환
        return None

    def delete(self, key):
        idx = self.hash_fn(key)
        cur = self.table[idx]
        prev = None

        # 연결 리스트를 순회하면서 삭제할 노드 탐색
        while cur:
            if cur.key == key:
                # 중간 노드 삭제
                if prev: #head가 아니면
                    prev.next = cur.next
                # 맨 앞(head) 노드 삭제
                else:
                    self.table[idx] = cur.next
                return True

            prev = cur
            cur = cur.next

        # 해당 key가 없을 경우
        return False
    def display(self):
      print("\n[ 해시 테이블 상태 ]")
      for i, slot in enumerate(self.table):
        cur = slot
        print(f"[{i}]", end=" ")
        while cur:
            print(f"({cur.key},{cur.value})", end=" -> ")
            cur = cur.next
        print("None")
      print()

# %% [3~4주차] 체이닝
ht = HashTableChaining()

ht.insert(10, "A")
ht.insert(17, "B")
ht.insert(24, "C")
ht.insert(31, "D")
ht.insert(38, "E")
ht.insert(45, "F")

print(ht.search(10))
print(ht.search(24))
print(ht.search(45))
print(ht.search(99))

ht.insert(24, "C_updated")
print(ht.search(24))

print(ht.delete(17))
print(ht.delete(99))

print(ht.search(17))

ht.insert(52, "G")
ht.insert(59, "H")
ht.insert(66, "I")

for i in range(ht.size):
    current = ht.table[i]
    chain = []
    while current:
        chain.append((current.key, current.value))
        current = current.next
    print(f"[{i}] {chain}")

# %% [3~4주차] BST + 체이닝
class BSTNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 삽입
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return BSTNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value

        return node

    # 검색
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # 삭제
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # case 1, 2 (자식 노드가 없거나 하나일 때)
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # case 3 (자식 노드가 둘일 때)
            min_node = self._min(node.right)
            node.key, node.value = min_node.key, min_node.value
            node.right = self._delete(node.right, min_node.key)

        return node

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    # 출력
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)


class HashTableBSTChaining():
    def __init__(self, size = 7):
        self.size = size
        self.table = [BST() for _ in range(size)]

    def hash_fn(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_fn(key)
        self.table[idx].insert(key, value)

    def search(self, key):
        idx = self.hash_fn(key)
        return self.table[idx].search(key)


    def delete(self, key):
      idx = self.hash_fn(key)
      if self.table[idx].search(key) is None:
        print("삭제 실패: 해당 key 없음")
        return False

      self.table[idx].delete(key)
      print("삭제 완료")
      return True

    def display(self):
        print("\n[ BST + 체이닝 해시 상태 ]")
        for i, bst in enumerate(self.table):
            print(f"[{i}] {bst.inorder()}")
        print()

# %% [3~4주차] BST + 체이닝
ht = HashTableBSTChaining()

ht.insert(10, "A")
ht.insert(17, "B")
ht.insert(24, "C")

print(ht.search(10))
print(ht.search(99))

ht.delete(17)
ht.delete(99)

ht.display()

# %% [3~4주차] Tombstone
DELETED = object()
# DELETED = ('DELETED', None)

# %% [3~4주차] 선형 탐사
class HashTableLinearProbing:

    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size

    def hash_fn(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_fn(key)
        start = idx

        while (self.table[idx] is not None and
               self.table[idx] != DELETED and
               self.table[idx][0] != key):

            idx = (idx + 1) % self.size
            if idx == start:
                print("해시 테이블이 가득참")
                return

        self.table[idx] = (key, value)

    def search(self, key):
        idx = self.hash_fn(key)
        start = idx

        while self.table[idx] is not None:
            if self.table[idx] != DELETED and self.table[idx][0] == key:
                return self.table[idx][1]

            idx = (idx + 1) % self.size
            if idx == start:
                break

        return None

    def delete(self, key):
        idx = self.hash_fn(key)
        start = idx

        while self.table[idx] is not None:
            if self.table[idx] != DELETED and self.table[idx][0] == key:
                self.table[idx] = DELETED
                return True

            idx = (idx + 1) % self.size
            if idx == start:
                break

        return False

    def display(self):
        print("\n[ 선형 탐사 상태 ]")
        for i, slot in enumerate(self.table):
            print(f"  [{i}] {slot}")
        print()

# %% [3~4주차] 선형 탐사
ht = HashTableLinearProbing()

data = [
    (7, "A"),
    (14, "B"),
    (21, "C"),
    (28, "D"),
    (8, "E"),
    (15, "F"),
    (22, "G"),
]

print("삽입 과정")
for k, v in data:
    idx = ht.hash_fn(k)
    print(f"insert({k}, '{v}') -> hash index = {idx}")
    ht.insert(k, v)

ht.display()

print("[ 검색 테스트 ]")
print("search(7)  =", ht.search(7))
print("search(14) =", ht.search(14))
print("search(21) =", ht.search(21))
print("search(28) =", ht.search(28))
print("search(8)  =", ht.search(8))
print("search(15) =", ht.search(15))
print("search(22) =", ht.search(22))
print("search(100) =", ht.search(100))   # 없는 값

ht.display()

# 테이블 가득 차는 테스트
print("\n[ 테이블 가득 참 테스트 ]")
ht.insert(22, "G")
ht.insert(29, "H") # 가득 찰 가능성 있음

ht.display()

# %% [3~4주차] 제곱 탐사
class HashTableQuadraticProbing:
    def __init__(self, size = 7):
        self.size = size
        self.table = [None] * size

    def hash_fn(self, key):
        return key % self.size

    def insert(self, key, value):
        h = self.hash_fn(key)
        i = 0

        while True:
            idx = (h + i * i) % self.size

            if (self.table[idx] is None or
                self.table[idx] == DELETED or
                self.table[idx][0] == key):

                self.table[idx] = (key, value)
                return

            i += 1
            h = idx

            if i == self.size:
                print("해시 테이블이 가득참")
                return

    def search(self, key):
        h = self.hash_fn(key)
        i = 0

        while True:
            idx = (h + i * i) % self.size

            if self.table[idx] is None:
                return None

            if self.table[idx] != DELETED and self.table[idx][0] == key:
                return self.table[idx][1]

            i += 1
            if i == self.size:
                return None

    def delete(self, key):
        h = self.hash_fn(key)
        i = 0

        while True:
            idx = (h + i * i) % self.size

            if self.table[idx] is None:
                return False

            if self.table[idx] != DELETED and self.table[idx][0] == key:
                self.table[idx] = DELETED
                return True

            i += 1
            if i == self.size:
                return False

    def display(self):
        print("\n[ 제곱 탐사 상태 ]")
        for i, slot in enumerate(self.table):
            print(f"  [{i}] {slot}")
        print()

# %% [3~4주차] 제곱 탐사
ht = HashTableQuadraticProbing()

data = [
    (7, "A"),
    (14, "B"),
    (21, "C"),
    (28, "D"),
    (8, "E"),
    (15, "F"),
    (22, "G"),
]

print("삽입 과정")
for k, v in data:
    idx = ht.hash_fn(k)
    print(f"insert({k}, '{v}') -> hash index = {idx}")
    ht.insert(k, v)

ht.display()

print("[ 검색 테스트 ]")
print("search(7)  =", ht.search(7))
print("search(14) =", ht.search(14))
print("search(21) =", ht.search(21))
print("search(28) =", ht.search(28))
print("search(8)  =", ht.search(8))
print("search(15) =", ht.search(15))
print("search(22) =", ht.search(22))
print("search(100) =", ht.search(100))   # 없는 값

ht.display()

print("\n[ 테이블 가득 참 테스트 ]")
ht.insert(22, "G")
ht.insert(29, "H")

ht.display()

# %% [3~4주차] Double Hashing
def findPrimeNum(n):
    for num in range(n - 1, 1, -1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            return num
    return 2

# %% [3~4주차] Double Hashing
class DoubleHashing():
    def __init__(self, size=7, method='division', group_size=2):
        self.size = size
        self.group_size = group_size
        self.table = [None] * size
        self.method = method
        self._prime = findPrimeNum(size)

    def hash_fn(self, key):
        if self.method == 'division':
            return key % self.size
        elif self.method == 'folding':
            s = str(key)
            total = 0
            for i in range(0, len(s), self.group_size):
                total += int(s[i:i+self.group_size])
            return total % self.size
        else:
            raise ValueError(f"{self.method}는 지원하지 않는 해싱 방법입니다.")

    def hash_fn2(self, key):
        return (key % self._prime) + 1

    def _probe(self, key):
        h1, h2 = self.hash_fn(key), self.hash_fn2(key)
        for i in range(self.size):
            yield (h1 + i * h2) % self.size

    def insert(self, key, value):
        first_deleted = None
        for idx in self._probe(key):
            slot = self.table[idx]
            if slot is None:
                self.table[first_deleted if first_deleted is not None else idx] = (key, value)
                return
            if slot is DELETED:
                if first_deleted is None:
                    first_deleted = idx
            elif slot[0] == key:
                self.table[idx] = (key, value)
                return

        if first_deleted is not None:
            self.table[first_deleted] = (key, value)
        else:
            print("해시 테이블이 가득 찼습니다.")

    def search(self, key):
        for idx in self._probe(key):
            slot = self.table[idx]
            if slot is None:
                return None
            if slot is not DELETED and slot[0] == key:
                return slot[1]
        return None

    def delete(self, key):
        for idx in self._probe(key):
            slot = self.table[idx]
            if slot is None:
                print("삭제 실패: 해당 key 없음")
                return
            if slot is not DELETED and slot[0] == key:
                self.table[idx] = DELETED
                print("삭제 완료")
                return
        print("삭제 실패: 해당 key 없음")

    def display(self):
        label = '나눗셈법' if self.method == 'division' else '자릿수 접기'
        print(f"\n[ 이중 해싱 테이블 ({label}, Size: {self.size}) ]")
        for i, slot in enumerate(self.table):
            if slot is DELETED:
                print(f"  [{i}] <삭제됨>")
            else:
                print(f"  [{i}] {slot}")
        print()

# %% [3~4주차] Test code
# ── division 방식 ──────────────────────────────────────────────
print("=" * 45)
print("  이중 해싱 테스트 — 나눗셈법 (Division)")
print("=" * 45)

dh_div = DoubleHashing(size=7, method='division')

print("\n▶ insert")
dh_div.insert(10, 'apple')
dh_div.insert(17, 'banana')   # 10 % 7 == 17 % 7 == 3 → 충돌
dh_div.insert(24, 'cherry')   # 24 % 7 == 3 → 또 충돌
dh_div.insert(5,  'date')
dh_div.display()

print("▶ search")
print(f"  key=10 → {dh_div.search(10)}")   # apple
print(f"  key=17 → {dh_div.search(17)}")   # banana
print(f"  key=24 → {dh_div.search(24)}")   # cherry
print(f"  key=99 → {dh_div.search(99)}")   # None (없는 키)

print("\n▶ delete → 탐묘석 확인")
dh_div.delete(17)                           # 삭제 완료
dh_div.delete(17)                           # 삭제 실패: 없음
print(f"  key=17 삭제 후 search → {dh_div.search(17)}")   # None
print(f"  key=24 체인 유지 확인  → {dh_div.search(24)}")  # cherry (체인 안 끊겨야 함)
dh_div.display()

print("▶ 중복 키 덮어쓰기")
dh_div.insert(10, 'avocado')
print(f"  key=10 → {dh_div.search(10)}")   # avocado
dh_div.display()


# ── folding 방식 ───────────────────────────────────────────────
print("=" * 45)
print("  이중 해싱 테스트 — 자릿수 접기 (Folding)")
print("=" * 45)

dh_fol = DoubleHashing(size=7, method='folding', group_size=2)

print("\n▶ insert")
dh_fol.insert(1234, 'lion')    # 12+34=46 → 46%7=4
dh_fol.insert(3412, 'tiger')   # 34+12=46 → 46%7=4 → 충돌
dh_fol.insert(5600, 'bear')    # 56+00=56 → 56%7=0
dh_fol.insert(1111, 'wolf')    # 11+11=22 → 22%7=1
dh_fol.display()

print("▶ search")
print(f"  key=1234 → {dh_fol.search(1234)}")  # lion
print(f"  key=3412 → {dh_fol.search(3412)}")  # tiger
print(f"  key=9999 → {dh_fol.search(9999)}")  # None

print("\n▶ delete → 탐묘석 확인")
dh_fol.delete(1234)
print(f"  key=1234 삭제 후 search → {dh_fol.search(1234)}")  # None
print(f"  key=3412 체인 유지 확인  → {dh_fol.search(3412)}") # tiger
dh_fol.display()

print("▶ 테이블 꽉 채우기")
dh_small = DoubleHashing(size=3, method='division')
dh_small.insert(1, 'a')
dh_small.insert(2, 'b')
dh_small.insert(3, 'c')
dh_small.insert(4, 'd')   # 가득 참 메시지 출력

# %% [3~4주차] Rehashing
class DoubleHashingWithRehashing(DoubleHashing):
  def __init__(self, size=7, method='division', group_size=2):
    super().__init__(size, method, group_size)

  def _rehash(self):
    old_table = self.table
    self.size *= 2
    self.table = [None] * self.size
    self._prime = findPrimeNum(self.size)
    for slot in old_table:
        if slot is not None and slot is not DELETED:
            self.insert(slot[0], slot[1])

  def insert(self, key, value):
      occupied = sum(1 for s in self.table if s is not None and s is not DELETED) + 1
      if occupied / self.size > 0.75:
          self._rehash()

      first_deleted = None
      for idx in self._probe(key):
          slot = self.table[idx]
          if slot is None:
              self.table[first_deleted if first_deleted is not None else idx] = (key, value)
              return
          if slot is DELETED:
              if first_deleted is None:
                  first_deleted = idx
          elif slot[0] == key:
              self.table[idx] = (key, value)
              return
      if first_deleted is not None:
        self.table[first_deleted] = (key, value)

# %% [3~4주차] Test code
# ── 기본 삽입 / 조회 ──────────────────────────────────────────
print("=" * 50)
print("  기본 삽입 / 조회")
print("=" * 50)

dh = DoubleHashingWithRehashing(size=7, method='division')
dh.insert(10, 'apple')
dh.insert(17, 'banana')  # 10 % 7 == 17 % 7 == 3 → 충돌
dh.insert(24, 'cherry')  # 24 % 7 == 3 → 또 충돌
dh.insert(5,  'date')
dh.display()

print(f"  search(10) → {dh.search(10)}")  # apple
print(f"  search(17) → {dh.search(17)}")  # banana
print(f"  search(24) → {dh.search(24)}")  # cherry
print(f"  search(99) → {dh.search(99)}")  # None


# ── 리해싱 트리거 (삭제 없이 삽입만으로 70% 초과) ────────────
print("\n" + "=" * 50)
print("  리해싱 트리거 — 삽입만으로 occupied > 70%")
print("=" * 50)

dh2 = DoubleHashingWithRehashing(size=10, method='division')
keys = [1, 2, 13, 4, 15, 6, 7, 8, 19, 20]  # 9번째 insert에서 리해싱

for k in keys:
    occupied_before = sum(1 for s in dh2.table if s is not None and s is not DELETED)
    size_before = dh2.size
    dh2.insert(k, f'val{k}')
    if dh2.size != size_before:
        print(f"  key={k} 삽입 시 리해싱 발생: size {size_before} → {dh2.size}")

dh2.display()
print("  리해싱 후 데이터 정합성 확인")
for k in keys:
    print(f"  search({k}) → {dh2.search(k)}")  # 전부 정상 조회


# ── 삭제 후 탐묘석 → 탐색 체인 유지 ─────────────────────────
print("\n" + "=" * 50)
print("  삭제 후 탐묘석 → 체인 유지 확인")
print("=" * 50)

dh3 = DoubleHashingWithRehashing(size=7, method='division')
dh3.insert(10, 'apple')
dh3.insert(17, 'banana')  # 충돌 → 프로브 체인에 삽입
dh3.insert(24, 'cherry')  # 충돌 → 프로브 체인에 삽입

dh3.delete(17)            # 체인 중간 삭제 → DELETED
print(f"  key=17 삭제 후 search(17) → {dh3.search(17)}")  # None
print(f"  체인 유지 확인 search(24) → {dh3.search(24)}")  # cherry (끊기면 None)
dh3.display()


# ── 삭제 후 재삽입 → 탐묘석 재활용 ──────────────────────────
print("=" * 50)
print("  탐묘석 슬롯 재활용 확인")
print("=" * 50)

dh4 = DoubleHashingWithRehashing(size=7, method='division')
dh4.insert(10, 'apple')
dh4.insert(17, 'banana')
dh4.delete(17)

idx_before = [i for i, s in enumerate(dh4.table) if s is DELETED]
dh4.insert(17, 'newbanana')
idx_after  = [i for i, s in enumerate(dh4.table) if s is DELETED]

print(f"  재삽입 전 DELETED 슬롯: {idx_before}")
print(f"  재삽입 후 DELETED 슬롯: {idx_after}")   # 재활용돼서 줄어야 함
print(f"  search(17) → {dh4.search(17)}")          # newbanana

# %% [3~4주차] Mixing
class RehashingMixin:
    th = 0.75

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self._prime = findPrimeNum(self.size)
        for slot in old_table:
            if slot is not None and slot is not DELETED:
                self.insert(slot[0], slot[1])

    def insert(self, key, value):
        occupied = sum(1 for s in self.table if s is not None and s is not DELETED) + 1
        if occupied / self.size > self.th:
            self._rehash()
        super().insert(key, value)

# %% [3~4주차] ReDouble
class ReDouble(RehashingMixin, DoubleHashing):
    pass

# %% [3~4주차] ReDouble
# ── 기본 삽입 / 조회 ──────────────────────────────────────────
print("=" * 50)
print("  기본 삽입 / 조회")
print("=" * 50)

dh = ReDouble(size=7, method='division')
dh.insert(10, 'apple')
dh.insert(17, 'banana')  # 10 % 7 == 17 % 7 == 3 → 충돌
dh.insert(24, 'cherry')  # 24 % 7 == 3 → 또 충돌
dh.insert(5,  'date')
dh.display()

print(f"  search(10) → {dh.search(10)}")  # apple
print(f"  search(17) → {dh.search(17)}")  # banana
print(f"  search(24) → {dh.search(24)}")  # cherry
print(f"  search(99) → {dh.search(99)}")  # None


# ── 리해싱 트리거 (삭제 없이 삽입만으로 70% 초과) ────────────
print("\n" + "=" * 50)
print("  리해싱 트리거 — 삽입만으로 occupied > 70%")
print("=" * 50)

dh2 = ReDouble(size=10, method='division')
keys = [1, 2, 13, 4, 15, 6, 7, 8, 19, 20]  # 9번째 insert에서 리해싱

for k in keys:
    occupied_before = sum(1 for s in dh2.table if s is not None and s is not DELETED)
    size_before = dh2.size
    dh2.insert(k, f'val{k}')
    if dh2.size != size_before:
        print(f"  key={k} 삽입 시 리해싱 발생: size {size_before} → {dh2.size}")

dh2.display()
print("  리해싱 후 데이터 정합성 확인")
for k in keys:
    print(f"  search({k}) → {dh2.search(k)}")  # 전부 정상 조회


# ── 삭제 후 탐묘석 → 탐색 체인 유지 ─────────────────────────
print("\n" + "=" * 50)
print("  삭제 후 탐묘석 → 체인 유지 확인")
print("=" * 50)

dh3 = ReDouble(size=7, method='division')
dh3.insert(10, 'apple')
dh3.insert(17, 'banana')  # 충돌 → 프로브 체인에 삽입
dh3.insert(24, 'cherry')  # 충돌 → 프로브 체인에 삽입

dh3.delete(17)            # 체인 중간 삭제 → DELETED
print(f"  key=17 삭제 후 search(17) → {dh3.search(17)}")  # None
print(f"  체인 유지 확인 search(24) → {dh3.search(24)}")  # cherry (끊기면 None)
dh3.display()


# ── 삭제 후 재삽입 → 탐묘석 재활용 ──────────────────────────
print("=" * 50)
print("  탐묘석 슬롯 재활용 확인")
print("=" * 50)

dh4 = ReDouble(size=7, method='division')
dh4.insert(10, 'apple')
dh4.insert(17, 'banana')
dh4.delete(17)

idx_before = [i for i, s in enumerate(dh4.table) if s is DELETED]
dh4.insert(17, 'newbanana')
idx_after  = [i for i, s in enumerate(dh4.table) if s is DELETED]

print(f"  재삽입 전 DELETED 슬롯: {idx_before}")
print(f"  재삽입 후 DELETED 슬롯: {idx_after}")   # 재활용돼서 줄어야 함
print(f"  search(17) → {dh4.search(17)}")          # newbanana

# %% [3~4주차] ReQuad
class ReQuad(RehashingMixin, HashTableQuadraticProbing):
    pass

# %% [3~4주차] ReQuad
ht = ReQuad()

data = [
    (7, "A"),
    (14, "B"),
    (21, "C"),
    (28, "D"),
    (8, "E"),
    (15, "F"),
    (22, "G"),
]

print("삽입 과정")
for k, v in data:
    idx = ht.hash_fn(k)
    print(f"insert({k}, '{v}') -> hash index = {idx}")
    ht.insert(k, v)

ht.display()

print("[ 검색 테스트 ]")
print("search(7)  =", ht.search(7))
print("search(14) =", ht.search(14))
print("search(21) =", ht.search(21))
print("search(28) =", ht.search(28))
print("search(8)  =", ht.search(8))
print("search(15) =", ht.search(15))
print("search(22) =", ht.search(22))
print("search(100) =", ht.search(100))   # 없는 값

ht.display()

# %% [3~4주차] ReLinear
class ReLinear(RehashingMixin, HashTableLinearProbing):
    th = 0.9

# %% [3~4주차] ReLinear
ht = ReLinear()

data = [
    (7, "A"),
    (14, "B"),
    (21, "C"),
    (28, "D"),
    (8, "E"),
    (15, "F"),
    (22, "G"),
]

print("삽입 과정")
for k, v in data:
    idx = ht.hash_fn(k)
    print(f"insert({k}, '{v}') -> hash index = {idx}")
    ht.insert(k, v)

ht.display()

print("[ 검색 테스트 ]")
print("search(7)  =", ht.search(7))
print("search(14) =", ht.search(14))
print("search(21) =", ht.search(21))
print("search(28) =", ht.search(28))
print("search(8)  =", ht.search(8))
print("search(15) =", ht.search(15))
print("search(22) =", ht.search(22))
print("search(100) =", ht.search(100))

ht.display()

# %% [3~4주차] 급식실 출석 확인
class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(size)]  # 체이닝 방식

    def hash_fn(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_fn(key)
        bucket = self.table[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:   # 이미 있으면 이름 수정
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def search(self, key):
        idx = self.hash_fn(key)
        bucket = self.table[idx]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self.hash_fn(key)
        bucket = self.table[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return True
        return False

    def display(self):
        print("\n[해시 테이블 상태]")
        for i in range(self.size):
            if self.table[i]:
                print(f"{i}: {self.table[i]}")


# -------------------------------
# 학기 초 전교생 명단 1회 등록
# -------------------------------
students = [
    (3506, "민동윤"),
    (3706, "권민성"),
    (3701, "김지안"),
    (3410, "김서현"),
    (3512, "주윤재"),
    (3213, "윤건하"),
    (3514, "최은수B"),
    (3604, "송연경"),
    (3507, "손원희"),
    (3616, "황현민"),
    (3108, "김종오"),
    (2509, "차마리"),
    (3310, "손승원")
]
ht = HashTable()

for sid, name in students:
    ht.insert(sid, name)

# -------------------------------
# 점심시간 출석 확인 시스템
# -------------------------------
while True:
    print("\n1. 출석 확인  2. 학생 삭제  3. 전체 보기  4. 전학(추가)  5. 종료")

    menu = input("메뉴 선택: ")

    if menu == "1":
        try:
            sid = int(input("학번 입력: "))
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        name = ht.search(sid)

        if name is None:
            print("잘못된 학번입니다. 출입을 금지합니다.")
        else:
            print(f"{name} 학생 확인 완료. 출입 가능합니다.")

    elif menu == "2":
        try:
            sid = int(input("삭제할 학번 입력: "))
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if ht.delete(sid):
            print("삭제 완료")
        else:
            print("해당 학번이 존재하지 않습니다.")

    elif menu == "3":
        ht.display()
    elif menu == "4":
      try:
        sid = int(input("학번 입력: "))
      except ValueError:
        print("숫자만 입력하세요.")
        continue

      name = input("이름 입력: ")
    # 이미 존재하는 학생인지 확인
      if ht.search(sid) is not None:
        print("이미 존재하는 학번입니다. 이름을 수정합니다.")

      ht.insert(sid, name)
      print(f"{name} 학생 등록 완료")

    elif menu == "5":
      print("시스템 종료")
      break

    else:
        print("올바른 메뉴를 입력하세요.")

# %% [3~4주차] 하지만 우리에겐? 해싱이 있다!
def solution(arr, target):
  ht = HashTableBSTChaining() # BST + 체이닝 방식 사용

  for num in arr:

    if ht.search(target - num) is not None:
      return True

    ht.insert(num, num)

  return False

# %% [3~4주차] 하지만 우리에겐? 해싱이 있다!
arr = list(map(int, input().split()))
target = int(input())

if solution(arr, target):
  print("True")
else:
  print("False")

# %% [3~4주차] 3-B
def solution(N, cards, M, queries):

    ht = ReDouble(size=1000003, method='division')
    m = M
    for card in cards:
      if card < 10_000_001 and card > -10_000_001:
        current = ht.search(card)
        if current is None:
            ht.insert(card, 1)
        else:
            ht.insert(card, current + 1)
      else:
        m = m-1
    print('최대 입력 가능 쿼리 개수: ',m)
    return [ht.search(q) or 0 for q in queries]

# %% [3~4주차] 3-B
while True:
  N = int(input("카드 개수: "))
  if N == 0:
    break
  cards = list(map(int, input("카드: ").split()))
  M = int(input("쿼리 개수: "))
  queries = list(map(int, input("쿼리: ").split()))
  result = solution(N, cards, M, queries)
  print(' '.join(map(str, result)))

# %% [3~4주차] 3-B
print("=" * 50)
print("  기본 예제")
print("=" * 50)
N = 5
cards = [6, 3, 2, 10, 10]
M = 4
queries = [10, 9, -5, 2]
result = solution(N, cards, M, queries)
print(f"  입력 카드:  {cards}")
print(f"  쿼리:       {queries}")
print(f"  출력:       {' '.join(map(str, result))}")
# 10 → 2장, 9 → 0장, -5 → 0장, 2 → 1장
# 기댓값: 2 0 0 1


print("\n" + "=" * 50)
print("  음수 카드")
print("=" * 50)
N = 4
cards = [-10_000_000, -10_000_000, -1, 0]
M = 3
queries = [-10_000_000, -1, 0]
result = solution(N, cards, M, queries)
print(f"  입력 카드:  {cards}")
print(f"  쿼리:       {queries}")
print(f"  출력:       {' '.join(map(str, result))}")
# 기댓값: 2 1 1


print("\n" + "=" * 50)
print("  카드가 아예 없는 숫자만 조회")
print("=" * 50)
N = 3
cards = [1, 2, 3]
M = 3
queries = [4, 5, 6]
result = solution(N, cards, M, queries)
print(f"  입력 카드:  {cards}")
print(f"  쿼리:       {queries}")
print(f"  출력:       {' '.join(map(str, result))}")
# 기댓값: 0 0 0


print("\n" + "=" * 50)
print("  카드 전부 동일한 숫자")
print("=" * 50)
N = 5
cards = [7, 7, 7, 7, 7]
M = 2
queries = [7, 1]
result = solution(N, cards, M, queries)
print(f"  입력 카드:  {cards}")
print(f"  쿼리:       {queries}")
print(f"  출력:       {' '.join(map(str, result))}")
# 기댓값: 5 0


print("\n" + "=" * 50)
print("  경계값 (±10,000,000)")
print("=" * 50)
N = 4
cards = [10_000_000, 10_000_000, -10_000_000, -10_000_000]
M = 3
queries = [10_000_000, -10_000_000, 0]
result = solution(N, cards, M, queries)
print(f"  입력 카드:  {cards}")
print(f"  쿼리:       {queries}")
print(f"  출력:       {' '.join(map(str, result))}")
# 기댓값: 2 2 0


# print("\n" + "=" * 50)
# print("  대량 입력 성능 테스트 (N=M=500,000)")
# print("=" * 50)
# import random, time
# random.seed(42)
# N = 500_000
# cards = [random.randint(-10_000_000, 10_000_000) for _ in range(N)]
# M = 500_000
# queries = [random.randint(-10_000_000, 10_000_000) for _ in range(M)]

# start = time.time()
# result = solution(N, cards, M, queries)
# elapsed = time.time() - start

# print(f"  카드 {N:,}개 삽입 + 쿼리 {M:,}개 조회")
# print(f"  소요 시간: {elapsed:.3f}초")
# print(f"  쿼리 결과 샘플 (앞 10개): {result[:10]}")


# ==============================================================================
# 5~6주차 | 동적 계획법
# 원본 파일: (공유문서)_3_동적_계획법 (5).ipynb
# ==============================================================================

# %% [5~6주차] 1. 계단 오르기
try:
    n = int(input())

    if n <= 0:
        print("잘못된 입력입니다. 계단 수는 1 이상의 정수만 입력할 수 있습니다.")

    else:
        dp = [0] * (n + 1)

        dp[1] = 1

        if n >= 2:
            dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp[n])

except ValueError:
    print("잘못된 입력입니다. 계단 수는 1 이상의 정수만 입력할 수 있습니다.")

# %% [5~6주차] 1. 계단 오르기
# [주의] 원본 노트북에서 문법적으로 불완전한 코드 셀입니다.
# 오류: IndentationError - expected an indented block after function definition on line 7
# 원본 보존을 위해 아래 코드는 주석 처리했습니다.
# n = int(input())
#
# memo = [-1] * (n-1)
# memo[1] = 1
# memo[2] = 1
#
# def upstairs(memo):

# %% [5~6주차] 2. 최장 공통 부분 수열 구현
def backtrack(dp, s1, s2, i, j):
    if i == 0 or j == 0:
        return {""}

    current = dp[i][j]

    result = set()

    # 위쪽과 값이 같으면 위쪽 탐색
    if dp[i - 1][j] == current:
        result.update(
            backtrack(dp, s1, s2, i - 1, j)
        )

    # 왼쪽과 값이 같으면 왼쪽 탐색
    if dp[i][j - 1] == current:
        result.update(
            backtrack(dp, s1, s2, i, j - 1)
        )

    # 위쪽, 왼쪽 모두 현재 값과 다르면
    # 문자가 일치한 경우이므로 대각선 이동
    if (
        dp[i - 1][j] != current
        and dp[i][j - 1] != current
    ):
        for lcs in backtrack(
            dp, s1, s2,
            i - 1, j - 1
        ):
            result.add(lcs + s1[i - 1])

    return result


print("=== 최장 공통 부분 수열(LCS) ===")

s1 = input("첫 번째 문자열을 입력하세요: ").strip()
s2 = input("두 번째 문자열을 입력하세요: ").strip()

if len(s1) == 0 or len(s2) == 0:
    print("문자열은 비어 있을 수 없습니다.")

else:
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # LCS 테이블 생성
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    print("\n[LCS 테이블]")

    print("   ", end="")
    for ch in s2:
        print(f"{ch:>3}", end="")
    print()

    for i in range(n + 1):

        if i == 0:
            print(" ", end="")
        else:
            print(s1[i - 1], end="")

        for j in range(m + 1):
            print(f"{dp[i][j]:>3}", end="")

        print()

    all_lcs = backtrack(
        dp,
        s1,
        s2,
        n,
        m
    )

    print("\nLCS 길이:", dp[n][m])

    print("\n가능한 모든 LCS")

    for idx, lcs in enumerate(
        sorted(all_lcs),
        start=1
    ):
        print(f"{idx}. {lcs}")

# %% [5~6주차] 2. 최장 공통 부분 수열 구현
def backtrack(dp, s1, s2, i, j):

    if i == 0 or j == 0:
        return {""}

    current = dp[i][j]

    result = set()

    # 위쪽과 값이 같으면 위쪽 탐색
    if dp[i - 1][j] == current:
        result.update(
            backtrack(dp, s1, s2, i - 1, j)
        )

    # 왼쪽과 값이 같으면 왼쪽 탐색
    if dp[i][j - 1] == current:
        result.update(
            backtrack(dp, s1, s2, i, j - 1)
        )

    # 위쪽, 왼쪽 모두 현재 값과 다르면
    # 문자가 일치한 경우이므로 대각선 이동
    if (
        dp[i - 1][j] != current
        and dp[i][j - 1] != current
    ):
        for lcs in backtrack(
            dp, s1, s2,
            i - 1, j - 1
        ):
            result.add(lcs + s1[i - 1])

    return result


print("=== 최장 공통 부분 수열(LCS) ===")

s1 = input("첫 번째 문자열을 입력하세요: ").strip()
s2 = input("두 번째 문자열을 입력하세요: ").strip()

if len(s1) == 0 or len(s2) == 0:
    print("문자열은 비어 있을 수 없습니다.")

else:
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # LCS 테이블 생성
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    print("\n[LCS 테이블]")

    print(" ", end="")
    for ch in s2:
        print(f"{ch:>3}", end="")
    print()

    for i in range(n + 1):

        if i == 0:
            print(" ", end="")
        else:
            print(s1[i - 1], end="")

        for j in range(m + 1):
            print(f"{dp[i][j]:>3}", end="")

        print()

    all_lcs = backtrack(
        dp,
        s1,
        s2,
        n,
        m
    )

    print("\nLCS 길이:", dp[n][m])

    print("\n가능한 모든 LCS")

    for idx, lcs in enumerate(
        sorted(all_lcs),
        start=1
    ):
        print(f"{idx}. {lcs}")

# %% [5~6주차] 동적계획법
arr = list(map(int, input().replace("[", "").replace("]", "").replace(",", " ").split()))

dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))

# %% [5~6주차] 분할정복 알고리즘
arr = list(map(int, input().replace("[", "").replace("]", "").replace(",", " ").split()))

def max_subarray(left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_subarray(left, mid)
    right_max = max_subarray(mid + 1, right)

    total = 0
    left_sum = -10**9
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    total = 0
    right_sum = -10**9
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    cross_max = left_sum + right_sum

    return max(left_max, right_max, cross_max)

print(max_subarray(0, len(arr) - 1))

# %% [5~6주차] 4. 집 도둑
def rob_houses(nums):
    # DP 적용을 위한 기본 상황 처리
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    # 타블레이션(Tabulation) 테이블 초기화
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # 상향식(Bottom-up) 전개
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]


# --- 함수 외부에서 입력 및 예외 처리 ---
user_input = input("각 집의 금액을 입력하세요 (예: 1 2 3 1): ").strip()

if not user_input:
    print("입력된 값이 없습니다.")
else:
    try:
        nums_list = list(map(int, user_input.split()))
        result = rob_houses(nums_list)
        print(f"최대 금액: {result}")
    except ValueError:
        print("올바른 정수 형식이 아닙니다.")

# %% [5~6주차] 5. 박람회 부스 배치
n = int(input("열의 수를 입력하세요: "))

grid = []
for i in range(3):
    grid.append(list(map(int, input(f"{i+1}열의 만족도를 입력하세요: ").split())))

masks = [1, 2, 4, 5]
# 1 = 위
# 2 = 가운데
# 4 = 아래
# 5 = 위 + 아래

dp = [[-10**18] * len(masks) for _ in range(n)]

for k in range(len(masks)):
    mask = masks[k]
    total = 0

    for r in range(3):
        if mask & (1 << r):
            total += grid[r][0]

    dp[0][k] = total

for col in range(1, n):
    for cur in range(len(masks)):
        cur_mask = masks[cur]

        cur_score = 0
        for r in range(3):
            if cur_mask & (1 << r):
                cur_score += grid[r][col]

        for prev in range(len(masks)):
            prev_mask = masks[prev]

            if cur_mask & prev_mask == 0:
                dp[col][cur] = max(dp[col][cur], dp[col - 1][prev] + cur_score)

print(max(dp[n - 1]))

# %% [5~6주차] 6. 상점 받기 게임
import re

def maximize_score(expression):

    expression = expression.replace(" ", "")

    if not expression:
        raise ValueError("수식을 입력해야 합니다.")

    pattern = r'^\d+([+-]\d+)*$'

    if not re.fullmatch(pattern, expression):
        raise ValueError(
            "잘못된 입력입니다.\n"
            "자연수와 +, - 연산자만 사용해야 하며\n"
            "예시: 1+3-8+5"
        )

    nums = list(map(int, re.findall(r'\d+', expression)))
    ops = re.findall(r'[+-]', expression)

    n = len(nums)

    max_dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]

    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]

    for length in range(1, n):

        for i in range(n - length):

            j = i + length

            max_val = float('-inf')
            min_val = float('inf')

            for k in range(i, j):

                op = ops[k]

                candidates = []

                if op == '+':
                    candidates = [
                        max_dp[i][k] + max_dp[k + 1][j],
                        max_dp[i][k] + min_dp[k + 1][j],
                        min_dp[i][k] + max_dp[k + 1][j],
                        min_dp[i][k] + min_dp[k + 1][j]
                    ]

                else:
                    candidates = [
                        max_dp[i][k] - max_dp[k + 1][j],
                        max_dp[i][k] - min_dp[k + 1][j],
                        min_dp[i][k] - max_dp[k + 1][j],
                        min_dp[i][k] - min_dp[k + 1][j]
                    ]

                max_val = max(max_val, *candidates)
                min_val = min(min_val, *candidates)

            max_dp[i][j] = max_val
            min_dp[i][j] = min_val

    return max_dp[0][n - 1]


print("=== 상점 받기 게임 ===")
print("예시 입력: 1+3-8+5")

try:
    expression = input("수식을 입력하세요: ")

    result = maximize_score(expression)

    print(f"\n얻을 수 있는 최대 점수: {result}")

except ValueError as e:
    print(f"\n입력 오류: {e}")


# ==============================================================================
# 7~8주차 | 백트래킹
# 원본 파일: (공유문서)_4_백트래킹_ipynb의_사본.ipynb
# ==============================================================================

# %% [7~8주차] 1. 미로 탈출하기 구현
n, m = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
path = []
answer = []

# 북, 남, 동, 서
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def backtrack(r, c):
    global answer

    if (r, c) == (n - 1, m - 1):
        answer = path[:]
        return True

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < m:
            if maze[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                path.append((nr, nc))

                if backtrack(nr, nc):
                    return True

                path.pop()
                visited[nr][nc] = False

    return False

visited[0][0] = True
path.append((0, 0))

if maze[0][0] == 1:
    print("탈출 불가")
elif backtrack(0, 0):
    for p in answer:
        print(*p)
else:
    print("탈출 불가")

# %% [7~8주차] 2. 지도 색칠하기 구현
graph = {
    "도봉구" : ["강북구", "노원구"],
    "강북구" : ["성북구", "노원구", "도봉구"],
    "노원구" : ["도봉구", "강북구", "성북구", "중랑구"],
    "은평구" : ["마포구", "서대문구", "종로구"],
    "종로구" : ["은평구", "서대문구", "중구", "성동구", "동대문구", "성북구"],
    "성북구" : ["종로구", "동대문구", "중랑구", "노원구", "강북구"],
    "동대문구" : ["성북구", "종로구", "성동구", "광진구", "중랑구"],
    "중랑구" : ["노원구", "성북구", "동대문구", "광진구"],
    "서대문구" : ["은평구" ,"마포구", "중구", "종로구"],
    "중구" : ["종로구", "서대문구", "용산구", "성동구"],
    "마포구" : ["은평구", "강서구", "영등포구", "용산구", "서대문구"],
    "용산구" : ["중구", "마포구", "영등포구", "동작구", "서초구", "강남구", "성동구"],
    "성동구" : ["동대문구", "종로구", "중구", "용산구", "강남구", "광진구"],
    "광진구" : ["중랑구", "동대문구", "성동구", "강남구", "송파구", "강동구"],
    "강서구" : ["양천구" ,"영등포구", "마포구"],
    "양천구" : ["강서구", "구로구", "영등포구"],
    "구로구" : ["양천구", "금천구", "관악구", "동작구", "영등포구"],
    "금천구" : ["구로구", "관악구"],
    "영등포구" : ["마포구", "강서구", "양천구", "구로구", "동작구", "용산구"],
    "동작구" : ["영등포구", "구로구", "관악구", "서초구", "용산구"],
    "강동구" : ["광진구", "송파구"],
    "송파구" : ["광진구", "강동구", "강남구"],
    "강남구" : ["송파구", "광진구", "성동구", "용산구", "서초구"],
    "서초구" : ["강남구", "용산구", "동작구", "관악구"],
    "관악구" : ["동작구", "구로구", "금천구", "서초구"]
}

# 1. 사용자로부터 사용할 색의 수를 입력받습니다.
num_colors = int(input("사용할 색의 수를 입력하세요: "))

# 2. 입력받은 수만큼 색상 리스트를 생성합니다. (예: 3 입력 시 [1, 2, 3])
colors = list(range(1, num_colors + 1))

# 차수가 큰 구부터 색칠
order = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)

assigned = {}

def can_color(gu, color):
    for near in graph[gu]:
        if near in assigned and assigned[near] == color:
            return False
    return True

def map_coloring(index):
    if index == len(order):
        return True

    gu = order[index]

    for color in colors:
        if can_color(gu, color):
            assigned[gu] = color

            if map_coloring(index + 1):
                return True

            del assigned[gu]

    return False

# 3. 결과 출력 부분도 입력받은 색의 수에 맞게 유연하게 메시지를 변경했습니다.
if map_coloring(0):
    print("\n[색칠 결과]")
    for gu in order:
        print(f"{gu} : {assigned[gu]}번 색")
else:
    print(f"\n{num_colors}가지 색으로는 모든 구를 칠할 수 없습니다.")

# %% [7~8주차] 3. 순열 생성
N = int(input())

perm = [0] * N
visited = [False] * (N + 1)

def backtrack(depth):
    if depth == N:
        print(*perm)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            perm[depth] = i
            visited[i] = True
            backtrack(depth + 1)
            visited[i] = False

backtrack(0)

# %% [7~8주차] 3. 순열 생성
N, k = map(int, input().split())

perm = [0] * k
visited = [False] * (N + 1)

def backtrack(depth):
    if depth == k:
        print(*perm)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            perm[depth] = i
            visited[i] = True
            backtrack(depth + 1)
            visited[i] = False

backtrack(0)

# %% [7~8주차] 4. 스도쿠 풀기
import ast

n = 4
box_size = 2

board = []

for _ in range(n):
    line = input().strip()

    if line.startswith("["):
        board.append(ast.literal_eval(line))
    else:
        board.append(list(map(int, line.split())))

empty = []

for r in range(n):
    for c in range(n):
        if board[r][c] == 0:
            empty.append((r, c))


def is_safe(row, col, num):
    # 같은 행에 같은 숫자가 있으면 안 됨
    for c in range(n):
        if c != col and board[row][c] == num:
            return False

    # 같은 열에 같은 숫자가 있으면 안 됨
    for r in range(n):
        if r != row and board[r][col] == num:
            return False

    # 같은 2x2 박스에 같은 숫자가 있으면 안 됨
    start_row = (row // box_size) * box_size
    start_col = (col // box_size) * box_size

    for r in range(start_row, start_row + box_size):
        for c in range(start_col, start_col + box_size):
            if (r != row or c != col) and board[r][c] == num:
                return False

    return True


def sudoku(x):
    if x == len(empty):
        return True

    row, col = empty[x]

    for num in range(1, n + 1):
        board[row][col] = num

        if is_safe(row, col, num):
            if sudoku(x + 1):
                return True

        # 백트래킹이 일어나는 시점:
        # 현재 빈칸에 num을 넣었을 때 이후 칸들을 채워도 스도쿠 조건을 만족할 수 없으므로
        # 다시 0으로 되돌리고 다음 숫자를 시도한다.
        board[row][col] = 0

    return False


if sudoku(0):
    for row in board:
        print(row)
else:
    print("해 없음")

# %% [7~8주차] 4. 스도쿠 풀기
import json
from google.colab import output
import IPython.display as display

# ==============================================================================
# 1. 탐색 과정을 기록하는 스도쿠 백트래킹 알고리즘 엔진
# ==============================================================================

def solve_sudoku_engine(board, n):
    box_size = int(n**0.5) if (int(n**0.5) ** 2 == n) else 0

    # 숫자가 채워지는 순서를 순차적으로 저장할 리스트
    # 구조: [{'r': row, 'c': col, 'val': num}, ...]
    solve_history = []

    def is_safe(row, col, num):
        # 1. 행 검사
        for x in range(n):
            if board[row][x] == num:
                return False
        # 2. 열 검사
        for x in range(n):
            if board[x][col] == num:
                return False
        # 3. 서브 박스 검사
        if box_size > 0:
            start_row = row - row % box_size
            start_col = col - col % box_size
            for i in range(box_size):
                for j in range(box_size):
                    if board[i + start_row][j + start_col] == num:
                        return False
        return True

    def backtrack():
        for row in range(n):
            for col in range(n):
                if board[row][col] == 0:
                    for num in range(1, n + 1):
                        if is_safe(row, col, num):
                            board[row][col] = num

                            # 탐색 과정 기록 (현재 좌표에 num을 채웠음을 저장)
                            solve_history.append({'r': row, 'c': col, 'val': num})

                            if backtrack():
                                return True

                            # [주석] 백트래킹이 일어나는 시점! (원상복구)
                            board[row][col] = 0

                            # 백트래킹으로 인해 지워지는 과정도 역사에 기록 (값은 0)
                            solve_history.append({'r': row, 'c': col, 'val': 0})

                    return False
        return True

    if backtrack():
        return {"status": "success", "history": solve_history}
    else:
        return {"status": "fail"}

# ==============================================================================
# 2. Colab Python <-> JS 양방향 통信 및 애니메이션 UI 정의
# ==============================================================================

def handle_solve_request(n, board_json):
    board = json.loads(board_json)
    result = solve_sudoku_engine(board, n)
    return display.JSON(result)

output.register_callback('notebook.solve_sudoku', handle_solve_request)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'Malgun Gothic', sans-serif;
            padding: 15px;
            background-color: #121212;
            color: #e0e0e0;
        }
        h2 { color: #bb86fc; margin-bottom: 5px; }
        .description { font-size: 13px; color: #a0a0a0; margin-bottom: 15px; }

        .control-panel { margin-bottom: 20px; display: flex; gap: 12px; align-items: center; }
        label { font-size: 14px; color: #e0e0e0; }

        input[type="number"] {
            width: 60px;
            padding: 6px;
            text-align: center;
            font-size: 14px;
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #444;
            border-radius: 4px;
        }

        button {
            padding: 6px 14px;
            background-color: #03dac6;
            color: #000000;
            font-weight: bold;
            border: none;
            cursor: pointer;
            font-size: 14px;
            border-radius: 4px;
            transition: opacity 0.2s;
        }
        button:hover { opacity: 0.9; }
        #btn-solve { background-color: #bb86fc; color: #000000; }

        .grid-container {
            display: inline-block;
            padding: 1px;
            background-color: #444444;
            border-radius: 4px;
        }
        .sudoku-grid {
            display: grid;
            background-color: #444444;
        }
        .cell {
            width: 48px;
            height: 48px;
            background-color: #1e1e1e;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
            user-select: none;
            box-sizing: border-box;
            outline: 1px solid #333333;
            transition: background-color 0.1s, color 0.1s;
        }
        .cell:hover { background-color: #2d2d2d; }

        /* 테마 색상 선언 */
        .cell.initial {
            color: #66cafb;
            background-color: #1a2635;
        }
        /* 현재 탐색 중인 칸 강조 효과 */
        .cell.active {
            background-color: #382c4d !important;
            color: #ffffff !important;
            transform: scale(1.05);
            z-index: 10;
        }
        .cell.solved {
            color: #ffb74d;
            background-color: #2b221a;
        }

        #message { margin-top: 15px; font-weight: bold; font-size: 16px; }
        .success-msg { color: #81c784; }
        .fail-msg { color: #e57373; }
        .info-msg { color: #ffb74d; }
    </style>
</head>
<body>

    <h2>🧩 가변 크기 스도쿠</h2>
    <div class="description">보드 크기를 정하고 칸을 채운 뒤 [스도쿠 풀기]를 누르면 백트래킹 탐색 과정이 순차적으로 시각화됩니다.</div>

    <div class="control-panel">
        <label for="size-input">보드 크기 (4~9): </label>
        <input type="number" id="size-input" value="4" min="4" max="9">
        <button onclick="generateGrid()">판 생성</button>
        <button id="btn-solve" onclick="solveSudoku()">⚡ 스도쿠 풀기</button>
    </div>

    <div class="grid-container">
        <div id="sudoku-board" class="sudoku-grid"></div>
    </div>

    <div id="message"></div>

    <script>
        let N = 4;
        let matrix = [];
        let animationInterval = null; // 애니메이션 제어용 타이머 변수

        function generateGrid() {
            // 실행 중인 애니메이션이 있다면 강제 종료
            if (animationInterval) clearInterval(animationInterval);

            const inputVal = parseInt(document.getElementById('size-input').value);
            if (isNaN(inputVal) || inputVal < 4 || inputVal > 10) {
                alert("크기는 4 이상 10 이하의 정수여야 합니다.");
                return;
            }
            N = inputVal;
            document.getElementById('message').innerHTML = "";

            const boardDiv = document.getElementById('sudoku-board');
            boardDiv.innerHTML = "";
            boardDiv.style.gridTemplateColumns = `repeat(${N}, 48px)`;

            matrix = Array.from({ length: N }, () => Array(N).fill(0));

            const boxSize = Math.floor(Math.sqrt(N));
            const isPerfectSquare = (boxSize * boxSize === N);

            for (let r = 0; r < N; r++) {
                for (let c = 0; c < N; c++) {
                    const cell = document.createElement('div');
                    cell.className = 'cell';
                    cell.id = `cell-${r}-${c}`;
                    cell.innerText = "";

                    if (isPerfectSquare) {
                        let shadowX = "0", shadowY = "0";
                        if ((r + 1) % boxSize === 0 && r < N - 1) shadowY = "2px";
                        if ((c + 1) % boxSize === 0 && c < N - 1) shadowX = "2px";
                        if (shadowX !== "0" || shadowY !== "0") {
                            cell.style.boxShadow = `inset -${shadowX} -${shadowY} 0px #bb86fc`;
                        }
                    }

                    cell.onclick = () => {
                        let currentVal = matrix[r][c];
                        let nextVal = (currentVal + 1) > N ? 0 : currentVal + 1;
                        matrix[r][c] = nextVal;

                        if (nextVal === 0) {
                            cell.innerText = "";
                            cell.classList.remove('initial');
                        } else {
                            cell.innerText = nextVal;
                            cell.classList.add('initial');
                        }
                    };
                    boardDiv.appendChild(cell);
                }
            }
        }

        async function solveSudoku() {
            if (animationInterval) clearInterval(animationInterval);

            const msgDiv = document.getElementById('message');
            msgDiv.className = "info-msg";
            msgDiv.innerText = "⏳ 백트래킹 탐색 궤적 연산 중...";

            // 기존에 연산되어 붙어있던 정답 클래스들 초기화
            for (let r = 0; r < N; r++) {
                for (let c = 0; c < N; c++) {
                    const cell = document.getElementById(`cell-${r}-${c}`);
                    if (!cell.classList.contains('initial')) {
                        cell.innerText = "";
                        cell.className = "cell";
                    }
                }
            }

            setTimeout(async () => {
                try {
                    const result = await google.colab.kernel.invokeFunction(
                        'notebook.solve_sudoku',
                        [N, JSON.stringify(matrix)],
                        {}
                    );

                    const response = result.data['application/json'];

                    if (response.status === 'success') {
                        const history = response.history;
                        msgDiv.innerText = `▶️ 탐색 애니메이션 재생 중... (총 ${history.length}단계)`;

                        let step = 0;
                        let lastActiveCell = null;

                        // 애니메이션 재생 속도 조절 (밀리초 단위, 숫자가 작을수록 빨라집니다)
                        // N 크기가 커질수록 탐색 횟수가 많아지므로 유동적으로 조절
                        const speed = N > 6 ? 15 : 40;

                        animationInterval = setInterval(() => {
                            if (step >= history.length) {
                                // 애니메이션 종료 조건
                                clearInterval(animationInterval);
                                if (lastActiveCell) lastActiveCell.classList.remove('active');
                                msgDiv.className = "success-msg";
                                msgDiv.innerText = "✅ 스도쿠 풀이 성공!";
                                return;
                            }

                            const currentRecord = history[step];
                            const cell = document.getElementById(`cell-${currentRecord.r}-${currentRecord.c}`);

                            // 이전 활성화 칸 강조 제거
                            if (lastActiveCell) lastActiveCell.classList.remove('active');

                            if (!cell.classList.contains('initial')) {
                                if (currentRecord.val === 0) {
                                    // 0으로 변하는 시점 = 백트래킹(시행착오 후 되돌아감) 발생 시점
                                    cell.innerText = "";
                                    cell.classList.remove('solved');
                                } else {
                                    // 숫자가 채워지는 시점
                                    cell.innerText = currentRecord.val;
                                    cell.classList.add('solved');
                                }
                                cell.classList.add('active');
                                lastActiveCell = cell;
                            }
                            step++;
                        }, speed);

                    } else {
                        msgDiv.className = "fail-msg";
                        msgDiv.innerText = "❌ 주어진 초기 상태로 스도쿠를 완성하는 것이 불가능합니다.";
                    }
                } catch (e) {
                    msgDiv.className = "fail-msg";
                    msgDiv.innerText = "❌ 연산 중 오류가 발생했습니다. 다시 시도해주세요.";
                }
            }, 50);
        }

        generateGrid();
    </script>
</body>
</html>
"""

display.display(display.HTML(html_code))

# %% [7~8주차] 5. 숫자 골라 최대합 만들기
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

selected = [[False] * m for _ in range(n)]
total_cells = n * m
answer = -10**18

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def can_select(r, c):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and selected[nr][nc]:
            return False
    return True


def backtrack(start, count, current_sum):
    global answer

    if count == k:
        answer = max(answer, current_sum)
        return

    # 백트래킹 조건: 남은 칸을 모두 써도 k개를 채울 수 없음
    if total_cells - start < k - count:
        return

    for idx in range(start, total_cells):
        # 남은 칸 수가 부족하면 더 볼 필요 없음
        if total_cells - idx < k - count:
            break

        r = idx // m
        c = idx % m

        if can_select(r, c):
            selected[r][c] = True

            backtrack(idx + 1, count + 1, current_sum + grid[r][c])

            # 백트래킹: 이 칸을 선택한 경우의 탐색을 끝냈으므로 선택 취소
            selected[r][c] = False


backtrack(0, 0, 0)

if answer == -10**18:
    print("선택 불가")
else:
    print(answer)

# %% [7~8주차] 5. 숫자 골라 최대합 만들기
import IPython.display as display

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'Malgun Gothic', sans-serif;
            padding: 15px;
            background-color: #121212;
            color: #e0e0e0;
            user-select: none;
        }
        h2 { color: #bb86fc; margin-bottom: 5px; }
        .description { font-size: 13px; color: #a0a0a0; margin-bottom: 15px; line-height: 1.5; }
        .description strong { color: #03dac6; }

        .control-panel { margin-bottom: 25px; display: flex; gap: 15px; align-items: center; flex-wrap: wrap; }
        .input-group { display: flex; align-items: center; gap: 6px; }
        label { font-size: 14px; color: #e0e0e0; }

        input[type="number"] {
            width: 55px;
            padding: 6px;
            text-align: center;
            font-size: 14px;
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #444;
            border-radius: 4px;
        }

        button {
            padding: 7px 15px;
            background-color: #03dac6;
            color: #000000;
            font-weight: bold;
            border: none;
            cursor: pointer;
            font-size: 14px;
            border-radius: 4px;
        }
        button:hover { opacity: 0.9; }
        #btn-solve { background-color: #bb86fc; color: #000000; }

        .grid-container {
            display: inline-block;
            padding: 2px;
            background-color: #333;
            border-radius: 6px;
            margin-bottom: 15px;
        }
        .grid-board {
            display: grid;
            gap: 2px;
            background-color: #333;
        }

        .cell {
            width: 64px;
            height: 64px;
            background-color: #1e1e1e;
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-sizing: border-box;
            border-radius: 2px;
            outline: none;
            transition: all 0.15s ease;
            border: 2px solid transparent;
        }

        /* 선택된 단 한 칸만 민트색 배경과 테두리로 강조 */
        .cell:focus {
            background-color: #1a362d !important;
            border: 2px solid #03dac6 !important;
            z-index: 5;
        }
        .cell:focus .cell-value {
            color: #03dac6;
        }

        .cell-value {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
            pointer-events: none;
        }

        /* 알고리즘 탐색 관련 스타일 */
        .cell.algo-active {
            background-color: #382c4d !important;
            transform: scale(1.05);
            z-index: 4;
        }
        .cell.algo-selected {
            background-color: #2b221a !important;
            border: 2px dashed #ffb74d;
        }
        .cell.algo-selected .cell-value { color: #ffb74d; }

        .cell.final-best {
            background-color: #3d2222 !important;
            border: 2px solid #ff5252;
        }
        .cell.final-best .cell-value { color: #ff5252; }

        #status-display {
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            min-height: 24px;
        }
        .info-text { color: #ffb74d; }
        .success-text { color: #81c784; }
        .fail-text { color: #e57373; }
    </style>
</head>
<body>

    <h2>🖼️ 격자 선택(Grid Selection) 백트래킹 시각화</h2>
    <div class="description">
        1. 행(N), 열(M), 선택할 칸수(K)를 정하고 <strong>[격자 생성]</strong>을 클릭하세요.<br>
        2. 원하는 칸을 <strong>클릭하면 강조색(민트색)</strong>으로 바뀌며 값을 입력받는 상태가 됩니다.<br>
        3. 다른 칸을 선택하면 기존 칸의 강조색은 자동으로 사라지고, 새 칸이 활성화됩니다.<br>
        4. 가중치 세팅이 끝나면 빈 곳을 눌러 포커스를 해제한 뒤 <strong>⚡ 탐색 시작</strong>을 눌러보세요!
    </div>

    <div class="control-panel">
        <div class="input-group">
            <label>행(N):</label>
            <input type="number" id="input-n" value="3" min="1" max="6">
        </div>
        <div class="input-group">
            <label>열(M):</label>
            <input type="number" id="input-m" value="4" min="1" max="6">
        </div>
        <div class="input-group">
            <label>선택 개수(K):</label>
            <input type="number" id="input-k" value="3" min="1" max="12">
        </div>
        <button onclick="buildGrid()">격자 생성</button>
        <button id="btn-solve" onclick="runJSBacktrack()">⚡ 탐색 시작</button>
    </div>

    <div class="grid-container">
        <div id="grid-board" class="grid-board"></div>
    </div>

    <div id="status-display"></div>

    <script>
        let N = 3, M = 4, K = 3;
        let gridValues = [];
        let playbackTimer = null;

        function buildGrid() {
            if (playbackTimer) clearInterval(playbackTimer);

            N = parseInt(document.getElementById('input-n').value);
            M = parseInt(document.getElementById('input-m').value);
            K = parseInt(document.getElementById('input-k').value);

            document.getElementById('status-display').innerHTML = "";
            const board = document.getElementById('grid-board');
            board.innerHTML = "";
            board.style.gridTemplateColumns = `repeat(${M}, 64px)`;

            gridValues = Array.from({length: N}, () => Array(M).fill(""));

            for (let r = 0; r < N; r++) {
                for (let c = 0; c < M; c++) {
                    const cell = document.createElement('div');
                    cell.className = 'cell';
                    cell.id = `cell-${r}-${c}`;
                    cell.tabIndex = 0;

                    const valSpan = document.createElement('span');
                    valSpan.className = 'cell-value';
                    valSpan.id = `val-${r}-${c}`;
                    valSpan.innerText = "";
                    cell.appendChild(valSpan);

                    cell.addEventListener('keydown', (e) => {
                        if ((e.key >= '0' && e.key <= '9') || e.key === 'Backspace' || e.key === '-') {
                            e.preventDefault();
                            let currentStr = gridValues[r][c].toString();

                            if (e.key === 'Backspace') {
                                currentStr = currentStr.slice(0, -1);
                            } else if (e.key === '-') {
                                if (currentStr === "") currentStr = "-";
                                else if (!currentStr.startsWith('-')) currentStr = '-' + currentStr;
                                else currentStr = currentStr.replace('-', '');
                            } else {
                                if (currentStr === "0" || currentStr === "-0") {
                                    currentStr = currentStr.startsWith('-') ? "-" + e.key : e.key;
                                } else {
                                    currentStr += e.key;
                                }
                            }
                            gridValues[r][c] = currentStr;
                            valSpan.innerText = currentStr;
                        }
                    });
                    board.appendChild(cell);
                }
            }
        }

        function runJSBacktrack() {
            if (playbackTimer) clearInterval(playbackTimer);
            const statusDiv = document.getElementById('status-display');
            statusDiv.className = "info-text";
            statusDiv.innerText = "⏳ 브라우저 자체 엔진에서 백트래킹 연산 중...";

            for (let r = 0; r < N; r++) {
                for (let c = 0; c < M; c++) {
                    document.getElementById(`cell-${r}-${c}`).classList.remove('algo-active', 'algo-selected', 'final-best');
                }
            }

            // 에러 유발하던 오타 완전 수정 완료
            let parsedGrid = [];
            for (let r = 0; r < N; r++) {
                let rowList = [];
                for (let c = 0; c < M; c++) {
                    let val = gridValues[r][c];
                    if (val === "" || val === "-") {
                        rowList.push(0);
                    } else {
                        rowList.push(parseInt(val));
                    }
                }
                parsedGrid.push(rowList);
            }

            let selected = Array.from({length: N}, () => Array(M).fill(false));
            let total_cells = N * M;
            let search_history = [];

            let directions = [[-1, 0], [1, 0], [0, 1], [0, -1]];
            let best_answer = -Infinity;
            let best_path = [];

            function can_select(r, c) {
                for (let [dr, dc] of directions) {
                    let nr = r + dr, nc = c + dc;
                    if (0 <= nr && nr < N && 0 <= nc && nc < M && selected[nr][nc]) return false;
                }
                return true;
            }

            function backtrack(start, count, current_sum) {
                if (count === K) {
                    if (current_sum > best_answer) {
                        best_answer = current_sum;
                        best_path = selected.map(row => [...row]);
                    }
                    search_history.push({type: 'success', sum: current_sum});
                    return;
                }

                if (total_cells - start < K - count) return;

                for (let idx = start; idx < total_cells; idx++) {
                    if (total_cells - idx < K - count) break;

                    let r = Math.floor(idx / M);
                    let c = idx % M;

                    if (can_select(r, c)) {
                        selected[r][c] = true;
                        search_history.push({type: 'select', r: r, 'c': c, sum: current_sum + parsedGrid[r][c]});

                        backtrack(idx + 1, count + 1, current_sum + parsedGrid[r][c]);

                        selected[r][c] = false;
                        search_history.push({type: 'unselect', r: r, 'c': c, sum: current_sum});
                    }
                }
            }

            backtrack(0, 0, 0);

            if (best_answer === -Infinity) {
                statusDiv.className = "fail-text";
                statusDiv.innerText = "❌ 조건(K개 배정 및 독립 격자)을 만족하는 조합이 존재하지 않습니다.";
                return;
            }

            let step = 0;
            let lastActiveCell = null;
            statusDiv.innerText = `▶️ DFS 탐색 재생 중... (총 ${search_history.length}단계)`;

            playbackTimer = setInterval(() => {
                if (step >= search_history.length) {
                    clearInterval(playbackTimer);
                    if (lastActiveCell) lastActiveCell.classList.remove('algo-active');

                    for (let r = 0; r < N; r++) {
                        for (let c = 0; c < M; c++) {
                            if (best_path[r][c]) {
                                document.getElementById(`cell-${r}-${c}`).classList.add('final-best');
                            }
                        }
                    }
                    statusDiv.className = "success-text";
                    statusDiv.innerText = `✅ 탐색 완료! 인접하지 않은 최대 가중치 합: ${best_answer}`;
                    return;
                }

                let record = search_history[step];
                if (lastActiveCell) lastActiveCell.classList.remove('algo-active');

                if (record.type === 'select') {
                    let cell = document.getElementById(`cell-${record.r}-${record.c}`);
                    cell.classList.add('algo-selected', 'algo-active');
                    lastActiveCell = cell;
                    statusDiv.innerText = `[탐색 중] 칸 선택 ➡️ 현재 누적 합: ${record.sum}`;
                } else if (record.type === 'unselect') {
                    let cell = document.getElementById(`cell-${record.r}-${record.c}`);
                    cell.classList.remove('algo-selected');
                    cell.classList.add('algo-active');
                    lastActiveCell = cell;
                    statusDiv.innerText = `[백트래킹] 조건 미달로 선택 취소 후 후진 ➡️ 누적 합: ${record.sum}`;
                } else if (record.type === 'success') {
                    statusDiv.innerText = `[조건 충족] K개 배치 성공! 기록된 합: ${record.sum}`;
                }
                step++;
            }, 80);
        }

        buildGrid();
    </script>
</body>
</html>
"""

display.display(display.HTML(html_code))


# ==============================================================================
# 9~10주차 | 그리디 알고리즘
# 원본 파일: 그리디_발표자료 (1) (3).ipynb
# ==============================================================================

# %% [9~10주차] 거스름돈
# [주의] 원본 노트북에서 문법적으로 불완전한 코드 셀입니다.
# 오류: SyntaxError - invalid syntax
# 원본 보존을 위해 아래 코드는 주석 처리했습니다.
# def check_multiple_relation(units): #화폐 단위 배수 확인
#     units = sorted(units, reverse=True)
#
#     for i in range(len(units) - 1):
#         if units[i] % units[i + 1] != 0:
#             return False
#
#     return True
#
#
# def greedy_change(units, paid, price, infinite=True, counts=None): #거스름돈 계산 함수
#     units = sorted(units, reverse=True)#화폐 단위 큰거부터 정렬
#
#     # 배수 관계 검사
#     if not check_multiple_relation(units):
#         print("화폐 단위가 서로 배수 관계가 아니므로 탐욕 알고리즘으로 최적해를 보장할 수 없습니다.")
#         return
#
#     # 지불 금액 검사
#     if paid < price:
#         print("지불 금액이 구매 금액보다 작습니다.")
#         return
#
#     # 거스름돈 계산
#     change = paid - price
#     remain = change
#     used = {}
#
#     print()
#     print(f"거스름돈: {change}원")
#
#     # 거스름돈이 0원인 경우
#     if change == 0:
#         print("거슬러 줄 금액이 없습니다.")
#         return
#
#     # 큰 단위 화폐부터 사용
#     for unit in units:
#         need = remain // unit
#
#         if infinite:
#             use = need
#         else:
#             use = min(need, counts.get(unit, 0)) #보유한 화폐의 수량과 필요한 화폐의 수 중 작은거 선택
#
#         used[unit] = use
#         remain -= unit * use
#
#     # 정확히 거슬러 줄 수 없는 경우
#     if remain != 0:
#         print("보유 수량이 부족하여 거스름돈을 줄 수 없습니다.")
#         print(f"부족하여 남은 금액: {remain}원")
#         return
#
#     # 결과 출력
#     total_count = 0
#     print("사용 화폐:")
#
#     for unit in units:
#         print(f"{unit}원: {used[unit]}개")
#         total_count += used[unit]
#
#     print(f"총 화폐 개수: {total_count}개")
#
#
#
# # 화폐 단위 입력
# n = int(input("사용할 화폐 종류의 개수를 입력하세요: "))
#
# units = []
#
# for i in range(n):
#     unit = int(input(f"{i + 1}번째 화폐 단위를 입력하세요: "))
#     units.append(unit)
#
# # 중복 화폐 단위 제거
# units = list(set(units))
# units = sorted(units, reverse=True)
#
# print()
# print("입력한 화폐 단위:", units)
#
# # 배수 관계 검사
# if not check_multiple_relation(units):
#     print("화폐 단위가 서로 배수 관계가 아니므로 탐욕 알고리즘으로 최적해를 보장할 수 없습니다.")
#     print("프로그램을 종료합니다.")
# else:
#     # 화폐 보유 수량 입력
#     answer = input("각 화폐를 무한히 보유하고 있나요? (Y/N): ")
#
#     if answer.upper() == "Y":
#         infinite = True
#         counts = None
#     else:
#         infinite = False
#         counts = {}
#
#         print()
#         print("각 화폐 단위별 보유 개수를 입력하세요.")
#
#         for unit in units:
#             count = int(input(f"{unit}원 보유 개수: "))1
#             counts[unit] = count
#
#     # 거래 정보 입력
#     print()
#     paid = int(input("손님이 지불한 금액을 입력하세요: "))
#     price = int(input("실제 구매 금액을 입력하세요: "))
#
#     # 거스름돈 계산 및 출력
#     greedy_change(units, paid, price, infinite, counts)

# %% [9~10주차] 도시 MST 만들고 분할 하기
class DisjointSet: #마을들이 서로 연결되어있는지 확인에 사용
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)] #각 마을 다 다른 집합

    def find(self, x): #집합 대표 찾기
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b): #a,가 속한 집합, b가 속한 집합 합치는 함수
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b: #이미 연결
            return False

        if root_a < root_b: #번호가 작은 대표를 부모로 삼도록 합침
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b

        return True

    def groups(self, n): #현재 마을들이 어떤 집합으로 나누어져 있는지 확인하는 함수
        result = {} #집합 결과 저장용

        for i in range(1, n + 1):
            root = self.find(i) #마을 i가 속한 집합 대표값 찾음

            if root not in result:
                result[root] = [] #집합 없으면 리스트 새로 생성

            result[root].append(i)#해당 리스트에 마을 i추가

        return list(result.values()) #딕셔너리 값들만 리스트로 바꾸어 반환

    def group_state(self, n): #집합 상태 보기 좋게 문자열로
        groups = self.groups(n)
        return " / ".join(str(group) for group in groups)


def city_mst_and_split(n, edges): #MST만들고 가장 비싼 간선 제거
    original_edges = edges[:]#리스트 그대로 복사
    edges = sorted(edges, key=lambda x: x[2]) #간선 비용이 적은 순서대로 정렬

    dsu = DisjointSet(n)
    mst_edges = []#MST 포함된 간선들 저장용
    total_cost = 0

    print()
    print("[1안] 모든 마을을 최소 비용으로 연결하기")
    print()

    for a, b, cost in edges:
        if dsu.union(a, b): #a,b 다른 집합이면 연결
            mst_edges.append((a, b, cost))# 간선 MST에 추가
            total_cost += cost

            print(f"추가한 간선: ({a}, {b}, {cost})")#추가한 간선, 마을들 연결 상태 출력
            print(f"집합 상태: {dsu.group_state(n)}")
            print()

            if len(mst_edges) == n - 1:#MST간선개수 확인
                break
        else:
            print(f"무시한 간선: ({a}, {b}, {cost}) - 사이클 발생")

    if len(mst_edges) != n - 1:
        print("모든 마을을 연결할 수 없습니다.")
        return

    print("MST 포함 간선 목록:")
    for edge in mst_edges:
        print(edge)

    print(f"MST 전체 비용 합: {total_cost}")
    print()

    print("[2안] 마을을 두 구역으로 나누기")
    print()

    # MST에서 가장 비용이 큰 간선을 제거
    removed_edge = max(mst_edges, key=lambda x: x[2]) #가장 비싼 간선 찾기

    split_edges = [] #비싼놈 뺀 나머지 MST간선 리스트 저장
    removed_once = False #같은 간선 중복 제거용

    for edge in mst_edges:
        if edge == removed_edge and not removed_once:
            removed_once = True #가장 비싼놈 제거
        else:
            split_edges.append(edge) #나머지 저장

    split_dsu = DisjointSet(n)#두 구역 나눈 후 연결 상태 정리 위해

    for a, b, cost in split_edges:
        split_dsu.union(a, b) #나머지 간선들 연결

    groups = split_dsu.groups(n) #어떤 구역으로 나누어졌는지 확인

    # 각 구역의 유지 비용 합 계산
    cost_by_root = {} #각 구역 유지비용 저장용

    for a, b, cost in split_edges: #각 구역 유지비용 계산
        root = split_dsu.find(a)
        cost_by_root[root] = cost_by_root.get(root, 0) + cost #기존에 저장된 비용에 더함

    print(f"MST에서 제거한 간선: {removed_edge}")
    print()

    # 원래 그래프 기준으로 두 구역 사이에 있는 길은 모두 제거 대상
    cross_edges = []

    for a, b, cost in original_edges:
        if split_dsu.find(a) != split_dsu.find(b): #a,b 대표값 다르면 서로 다른 구역--> 제거
            cross_edges.append((a, b, cost))

    print("두 구역 사이이므로 제거되는 원래 길 목록:")
    for edge in cross_edges:
        print(edge)

    print()

    total_split_cost = 0

    for idx, group in enumerate(groups, start=1): #구역 하나씩 확인
        root = split_dsu.find(group[0]) #구역 대표값 찾기
        group_cost = cost_by_root.get(root, 0) #구역 간선 비용 가져오기
        total_split_cost += group_cost

        print(f"{idx}구역 마을 목록: {group}")
        print(f"{idx}구역 유지 비용 합: {group_cost}")
        print()

    print(f"두 구역의 유지 비용 합 최솟값: {total_split_cost}")


# 입력 받기
n = int(input("마을 수 N을 입력하세요: "))
m = int(input("길의 수 M을 입력하세요: "))

edges = []

print()
print("길 정보를 입력하세요. 형식: 마을1 마을2 비용")

for i in range(m):
    a, b, cost = map(int, input(f"{i + 1}번째 길 정보: ").split())
    edges.append((a, b, cost))

city_mst_and_split(n, edges)

# %% [9~10주차] Kruskal과 Prim은 왜 정당화 되는가?
import heapq


def prim(n, edges, start=1):
    graph = [[] for _ in range(n + 1)] #n+1 크기의 인접 리스트를 만듬

    for a, b, cost in edges:
        graph[a].append((cost, b))
        graph[b].append((cost, a)) #무방향 그래프를 양방향으로 저장

    visited = [False] * (n + 1)
    heap = []

    heapq.heappush(heap, (0, start, 0)) #시작 정점을 비용 0으로 우선순위 큐에 넣는다.(비용, 현재 노드, 이전 노드)

    mst_edges = []
    total_cost = 0

    while heap and len(mst_edges) < n - 1:
        cost, now, prev = heapq.heappop(heap) #우선순위 큐에서 현재 선택 가능한 간선 중 비용이 가장 작은 간선을 꺼냄

        if visited[now]: #MST에 포함된 정점이면 다시 선택X (사이클 방지)
            continue

        visited[now] = True

        if prev != 0:
            mst_edges.append((prev, now, cost))
            total_cost += cost

            print(f"선택 간선: ({prev}, {now}, {cost})")
            print(f"현재 MST 간선 목록: {mst_edges}")
            print(f"현재 비용 합: {total_cost}")
            print()

        for next_cost, next_node in graph[now]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node, now)) #MST에 포함된 정점에서 갈 수 있는 간선들을 우선순위 큐에 추가

    if len(mst_edges) != n - 1:
        print("모든 정점을 연결할 수 없습니다.")
        return

    print("최종 MST 간선 목록:")
    for edge in mst_edges:
        print(edge)

    print(f"최종 MST 비용 합: {total_cost}")


n = 5
edges = [
    (1, 2, 1),
    (1, 3, 3),
    (2, 3, 3),
    (2, 4, 6),
    (3, 4, 4),
    (3, 5, 2),
    (4, 5, 5)
]

prim(n, edges, start=1)

# %% [9~10주차] 허프만 코딩
import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq = Counter(text)

    heap = []
    order = 0

    for char, count in freq.items():
        heapq.heappush(heap, (count, order, Node(char, count)))
        order += 1

    if len(heap) == 1:
        count, _, node = heapq.heappop(heap)
        return Node(None, count, left=node), freq

    print("[허프만 트리 구축 과정]")

    while len(heap) > 1:
        freq1, _, node1 = heapq.heappop(heap)
        freq2, _, node2 = heapq.heappop(heap)

        print(f"해 선택: 빈도 가장 작은 두 노드 선택 -> {node1.char}:{freq1}, {node2.char}:{freq2}")

        merged = Node(None, freq1 + freq2, node1, node2)

        print(f"실행 가능성 검사: 두 노드를 합쳐 빈도 {freq1 + freq2}의 새 노드 생성")
        print()

        heapq.heappush(heap, (merged.freq, order, merged))
        order += 1

    print("해 완성 검사: 남은 노드가 하나이므로 허프만 트리 완성")
    print()

    return heap[0][2], freq


def make_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        if current_code == "":
            codes[node.char] = "0"
        else:
            codes[node.char] = current_code
        return

    make_codes(node.left, current_code + "0", codes)
    make_codes(node.right, current_code + "1", codes)


def encode(text, codes):
    result = ""

    for char in text:
        result += codes[char]

    return result


def decode(encoded, root):
    result = ""
    node = root

    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            result += node.char
            node = root

    return result


def huffman_coding(text):
    if text == "":
        print("빈 문자열은 압축할 수 없습니다.")
        return

    root, freq = build_huffman_tree(text)

    codes = {}
    make_codes(root, "", codes)

    print("[문자 빈도]")
    for char, count in freq.items():
        print(f"{repr(char)}: {count}")

    print()

    print("[허프만 코드]")
    for char, code in codes.items():
        print(f"{repr(char)}: {code}")

    print()

    encoded = encode(text, codes)
    decoded = decode(encoded, root)

    original_bits = len(text) * 8
    compressed_bits = len(encoded)

    compression_ratio = compressed_bits / original_bits
    reduction_ratio = 1 - compression_ratio

    print("[압축 결과]")
    print(f"원본 문자열: {text}")
    print(f"압축된 비트열: {encoded}")
    print(f"원본 비트 수: {original_bits}")
    print(f"압축 비트 수: {compressed_bits}")
    print(f"압축 비율: {compression_ratio * 100:.2f}%")
    print(f"감소율: {reduction_ratio * 100:.2f}%")

    print()

    print("[복원 결과]")
    print(f"복원 문자열: {decoded}")

    if decoded == text:
        print("복원 성공")
    else:
        print("복원 실패")


# 입력
text = input("압축할 문자열을 입력하세요: ")
huffman_coding(text)

# %% [9~10주차] 큰 수 만들기
def Make_Big_Number(number, k):
    stack = []
    removed = 0

    print(f"입력 숫자: {number}")
    print(f"제거할 개수: {k}")
    print()

    for digit in number:
        print(f"현재 숫자: {digit}")

        while stack and stack[-1] < digit and removed < k:
            popped = stack.pop()
            removed += 1
            print(f"  {popped} 제거 -> stack = {stack}, 제거 횟수 = {removed}")

        stack.append(digit)
        print(f"  {digit} 추가 -> stack = {stack}")
        print()

    if removed < k:
        remain_remove = k - removed
        print(f"남은 제거 횟수: {remain_remove}")
        print(f"뒤에서 {remain_remove}개 제거")

        for _ in range(remain_remove):
            popped = stack.pop()
            print(f"  {popped} 제거 -> stack = {stack}")

    result = ''.join(stack)

    print(f"최종 스택: {stack}")
    print(f"결과: {result}")

    return result


# 입력 받기
number = input("숫자 문자열 number를 입력하세요: ")
k = int(input("제거할 숫자의 개수 k를 입력하세요: "))

Make_Big_Number(number, k)


# ==============================================================================
# 11~12주차 | 문자열 탐색
# 원본 파일: 문자열_탐색_발표자료 (1) (2).ipynb
# ==============================================================================

# %% [11~12주차] 코드 셀 1
def brute_force():
    text = input("본문 문자열 입력: ")
    pattern = input("찾을 패턴 입력: ")

    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i)

    if positions:
        print("패턴을 찾은 인덱스:", positions)
    else:
        print("패턴이 본문에 존재하지 않습니다.")


# 실행
brute_force()

# %% [11~12주차] 코드 셀 2
def rabin_karp(text, pattern, mod):
    n = len(text)
    m = len(pattern)

    # 예외 처리
    if m == 0 or m > n:
        print("없다")
        return

    power = pow(2, m - 1, mod)#text의 이동을 위해 power값 저장

    pattern_hash = 0
    text_hash = 0

    # 초기 해시 계산
    for i in range(m):
        pattern_hash = ((pattern_hash << 1) + ord(pattern[i])) % mod
        text_hash = ((text_hash << 1) + ord(text[i])) % mod

    #패턴 해시 출력 (필수)
    print("pattern hash:", pattern_hash)

    result = []

    for i in range(n - m + 1):

        #본문 해시 출력
        print("index", i, "hash:", text_hash)

        if pattern_hash == text_hash:#해시가 같을 시
            if text[i:i + m] == pattern:#해시 충돌 방지를 위해 문자열 한 번 더 비교
                result.append(i)

        if i < n - m:
            remove = (ord(text[i]) * power) % mod#지울 문자 지정
            text_hash = (text_hash - remove) % mod#삭제
            text_hash = ((text_hash << 1) + ord(text[i + m])) % mod#푸싱 후 새 문자 추가

    #출력 형식 수정
    if len(result) == 0:#만약 pattern을 찾지 못했다면
        print("없다")
    else:
        print("위치:", *result)


# 실행 코드
text = input("text: ").strip()
pattern = input("pattern: ").strip()
mod = int(input("mod: "))

rabin_karp(text, pattern, mod)

# %% [11~12주차] 코드 셀 3
#KMP
def build_lps(pattern):

    m = len(pattern)
    lps = [0]*m#경계 테이블

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:#패턴이 같은 정도만큼
            length += 1#Length에 저장하고
            lps[i] = length#LPS에 저장
            i += 1

        else:#일치하지 않는다면?
            if length != 0:#그 전에 0이 아니라면
                length = lps[length-1]#가능한 곳으로 점프
            else:
                lps[i] = 0#그 전도 0이면 0 저장
                i += 1

    return lps


def kmp(text, pattern):

    lps = build_lps(pattern)

    print("LPS:", "-", *lps[1:])#수업시간에 -로 0번 인덱스를 설정하라고 했으나 오류 위험이 있을 것 같아 출력 시에만 반영

    n = len(text)
    m = len(pattern)

    i = 0
    j = 0
    result = []

    while i < n:

        if text[i] == pattern[j]:#텍스트와 비교
            i += 1
            j += 1

        if j == m:#찾으면
            result.append(i-j)#결과에 추가
            j = lps[j-1]#패턴이 겹치는 경우를 대비해 찾았어도 돌아가 비교

        elif i < n and text[i] != pattern[j]:#아니면

            if j != 0:
                j = lps[j-1]#점프
            else:
                i += 1

    if len(result) == 0:
        print("없음")
    else:
        print("match count:", len(result))
        print("positions:", *result)


# 실행 코드
text = input("text: ").strip()
pattern = input("pattern: ").strip()

kmp(text, pattern)

# %% [11~12주차] 코드 셀 4
def build_skip(pattern): #건너뛰기 표 생성 함수
    m = len(pattern) # 패턴 길이
    skip = {} #딕셔너리

    # 패턴의 마지막 문자는 제외
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
# 이동 = 패턴 길이 - 현재위치 - 1
    return skip


def boyer_moore(text, pattern):
    n = len(text) #문자열 길이
    m = len(pattern) #패턴 길이

    # 예외 처리
    if m == 0: # 패턴 길이가 0 없음
        print("없다")
        return

    skip = build_skip(pattern)

    # 건너뛰기 표 출력
    print("건너뛰기 표")
    printed = set()
    for c in pattern: #하나씩 확인
        if c not in printed: #아직 출력 안했으면 (중복 문자 처리)
            print(c, ":", skip[c] if c in skip else m) # 이동값 출력 없으면 m
            printed.add(c) #출력한거 집합에 추가

    if m > n: #패턴이 본문보다 긴 경우 예외 처리
        print("없다")
        return

    result = [] # 패턴 발견 위치를 저장
    i = 0

    while i <= n - m:
        j = m - 1

        # 오른쪽 --> 왼쪽 비교
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # 패턴 발견
        if j < 0:
            result.append(i)
            i += 1  # 겹치는 패턴까지 탐색

        # 불일치
        else:
            # 항상 패턴의 마지막 문자 기준
            bad_char = text[i + m - 1]

            if bad_char in skip:
                i += skip[bad_char]
            else:
                i += m

    # 결과 출력
    if len(result) == 0:
        print("없다")
    else:
        print("위치:", *result)


# 실행 코드
text = input("text: ").strip()
pattern = input("pattern: ").strip()

boyer_moore(text, pattern)

# %% [11~12주차] 코드 셀 5
test_cases = [
    ("ABCDEFG", "CDE"),         # 위치: 2
    ("ABCABCABC", "ABC"),       # 위치: 0 3 6
    ("ABCDEFG", "HIJ"),         # 없다
    ("AAAAA", "AAA"),           # 위치: 0 1 2
    ("ABABA", "ABA"),           # 위치: 0 2
    ("BANANANA", "ANA"),        # 위치: 1 3 5
    ("ABCDAA", "A"),            # 위치: 0 4 5
    ("BBBBB", "A"),             # 없다
    ("ABCDEF", "ABCDEF"),       # 위치: 0
    ("ABCDEF", "ABCDEG"),       # 없다
    ("AB", "ABCDE"),            # 없다
    ("XYZABC", "XYZ"),          # 위치: 0
    ("ABCXYZ", "XYZ"),          # 위치: 3
    ("AAAAAAA", "A"),           # 위치: 0 1 2 3 4 5 6
    ("AAAAAAA", "AA"),          # 위치: 0 1 2 3 4 5
    ("AAAAAAA", "AAAA"),        # 위치: 0 1 2 3
    ("AbcABCabc", "ABC"),       # 위치: 3
    ("aAaAaA", "AaA"),          # 위치: 1 3
    ("A B C D", " "),           # 위치: 1 3 5
    ("HELLO WORLD", "WORLD"),   # 위치: 6
    ("123123123", "123"),       # 위치: 0 3 6
    ("a+b+a+b", "+"),           # 위치: 1 3 5
    ("abababab", "bab"),        # 위치: 1 3 5
    ("MISSISSIPPI", "ISS"),     # 위치: 1 4
    ("TTTTTT", "TTT"),          # 위치: 0 1 2 3
]

for text, pattern in test_cases:
    print(f"text = {text}, pattern = {pattern}")
    boyer_moore(text, pattern)
    print("-" * 30)

# %% [11~12주차] 코드 셀 6
#최소반복단위
def build_lps(pattern):#경계 테이블 사용

    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

    return lps


def minimum_pattern(s):

    lps = build_lps(s)

    n = len(s)
    l = lps[-1]#경계 테이블의 마지막 값

    unit = n - l

    if n % unit == 0:#최소반복단위가 있다면
        print(s[:unit])
    else:
        print(s)


# 실행
s = input().strip()
minimum_pattern(s)

# %% [11~12주차] 코드 셀 7
def longest_common_substring_length(A, B):
    # 큰 소수와 base를 이용한 롤링 해시
    BASE = 257
    MOD = 10**9 + 7

    n = len(A)
    m = len(B)

    if n == 0 or m == 0:
        return 0

    def get_prefix_hash(s):
        length = len(s)
        prefix = [0] * (length + 1)
        power = [1] * (length + 1)

        for i in range(length):
            prefix[i + 1] = (prefix[i] * BASE + ord(s[i])) % MOD
            power[i + 1] = (power[i] * BASE) % MOD

        return prefix, power

    prefixA, powerA = get_prefix_hash(A)
    prefixB, powerB = get_prefix_hash(B)

    def substring_hash(prefix, power, left, right):
        # s[left:right] 의 해시
        return (prefix[right] - prefix[left] * power[right - left]) % MOD

    def exists_common_substring(length):
        if length == 0: #공통 길이가 0인건 당연히 존재
            return True

        hash_map = {}

        # A의 길이 length인 모든 부분 문자열 해시 저장
        for i in range(n - length + 1):
            h = substring_hash(prefixA, powerA, i, i + length)
            if h not in hash_map:
                hash_map[h] = []
            hash_map[h].append(i)

        # B의 부분 문자열과 비교
        for j in range(m - length + 1):
            h = substring_hash(prefixB, powerB, j, j + length)

            if h in hash_map:
                sub_b = B[j:j + length]

                # 해시 충돌 방지를 위해 실제 문자열 비교
                for i in hash_map[h]:
                    if A[i:i + length] == sub_b:
                        return True #다 찾을 필요없이 하나만 있으면 그 길이는 존재하므로 바로 true로 반환

        return False

    left = 0
    right = min(n, m)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if exists_common_substring(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


# 입력 예시
A = input().strip()
B = input().strip()

print(longest_common_substring_length(A, B))


# ==============================================================================
# 13~14주차 | 분할 정복
# 원본 파일: 분할_정복 (4) (1) (2).ipynb
# ==============================================================================

# %% [13~14주차] 이진탐색
def binary_search_iter(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return answer


def binary_search_dc(arr, target):

    def search(left, right, answer):
        # 정복: 탐색 범위가 사라지면 지금까지 찾은 가장 왼쪽 인덱스 반환
        if left > right:
            return answer

        # 분할: 가운데 인덱스를 기준으로 탐색 범위 나누기
        mid = (left + right) // 2

        if arr[mid] == target:
            # 결합: target을 찾았으므로 answer를 갱신하고 더 왼쪽 탐색
            return search(left, mid - 1, mid)

        elif arr[mid] > target:
            # 정복: 왼쪽 구간 탐색
            return search(left, mid - 1, answer)

        else:
            # 정복: 오른쪽 구간 탐색
            return search(mid + 1, right, answer)

    return search(0, len(arr) - 1, -1)


# 입력
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# 출력
print("반복문 결과:", binary_search_iter(arr, target))
print("분할정복 결과:", binary_search_dc(arr, target))

# %% [13~14주차] 수식과 괄호 삽입
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def expression_results(expression):
    # 정복: 숫자 하나만 남으면 그 자체가 결과
    if expression.isdigit():
        return {int(expression)}

    results = set()

    for i in range(len(expression)):
        if expression[i] in '+-*':
            op = expression[i]

            # 분할: 연산자를 기준으로 왼쪽 / 오른쪽 분리
            left_expr = expression[:i]
            right_expr = expression[i + 1:]

            left_results = expression_results(left_expr)
            right_results = expression_results(right_expr)

            # 결합: 왼쪽 결과와 오른쪽 결과를 현재 연산자로 계산
            for left_value in left_results:
                for right_value in right_results:
                    results.add(calculate(left_value, right_value, op))

    return results


# 입력
expression = input()

# 출력
answer = expression_results(expression)
print(sorted(answer))

# %% [13~14주차] 학급회장 찾기
# 3-1. Brute Force 사용
def find_president_brute_force(votes):
    n = len(votes)

    if n == 0:
        return "재투표가 필요합니다."

    for candidate in votes:
        count = 0

        for vote in votes:
            if vote == candidate:
                count += 1

        if count > n // 2:
            return candidate

    return "재투표가 필요합니다."


# 3-2. Divide and Conquer 사용
def find_president_divide_conquer(votes):
    n = len(votes)

    if n == 0:
        return "재투표가 필요합니다."

    def divide_and_conquer(left, right):
        # 정복: 원소가 하나만 남으면 그 원소를 후보로 반환
        if left == right:
            return votes[left]

        # 분할: 투표 구간을 왼쪽과 오른쪽으로 나눔
        mid = (left + right) // 2
        left_candidate = divide_and_conquer(left, mid)
        right_candidate = divide_and_conquer(mid + 1, right)

        # 결합: 왼쪽 후보와 오른쪽 후보가 같으면 그대로 반환
        if left_candidate == right_candidate:
            return left_candidate

        left_count = 0
        right_count = 0

        for i in range(left, right + 1):
            if votes[i] == left_candidate:
                left_count += 1
            if votes[i] == right_candidate:
                right_count += 1

        if left_count > right_count:
            return left_candidate
        elif right_count > left_count:
            return right_candidate
        else:
            return None

    candidate = divide_and_conquer(0, n - 1)

    if candidate is not None and votes.count(candidate) > n // 2:
        return candidate
    else:
        return "재투표가 필요합니다."


# 입력
votes = list(map(int, input().split()))

# 출력
print("Brute Force:", find_president_brute_force(votes))
print("Divide and Conquer:", find_president_divide_conquer(votes))

# %% [13~14주차] 쿼드 트리
def quadtree_compress(image):
    n = len(image)

    def compress(row, col, size):
        first = image[row][col]
        same = True

        # 정복: 현재 영역이 모두 같은 값인지 확인
        for i in range(row, row + size):
            for j in range(col, col + size):
                if image[i][j] != first:
                    same = False
                    break
            if not same:
                break

        if same:
            return first

        half = size // 2

        # 분할: 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
        left_top = compress(row, col, half)
        right_top = compress(row, col + half, half)
        left_bottom = compress(row + half, col, half)
        right_bottom = compress(row + half, col + half, half)

        # 결합: 네 영역의 압축 결과를 괄호로 묶음
        return "(" + left_top + right_top + left_bottom + right_bottom + ")"

    compressed = compress(0, 0, n)
    compression_ratio = len(compressed) / (n * n) * 100

    return compressed, compression_ratio


N = int(input())
image = []

for _ in range(N):
    image.append(input().strip())

result, ratio = quadtree_compress(image)

print(result)
print(f"압축률: {ratio:.1f}%")

# %% [13~14주차] 최근접 점 쌍
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(points):
    points.sort(key=lambda p: (p[0], p[1]))

    def solve(sorted_points):
        n = len(sorted_points)

        # 정복: 점이 3개 이하이면 완전탐색
        if n <= 3:
            min_dist = float('inf')

            for i in range(n):
                for j in range(i + 1, n):
                    min_dist = min(min_dist, distance(sorted_points[i], sorted_points[j]))

            return min_dist

        # 분할: x좌표 기준으로 반으로 나눔
        mid = n // 2
        mid_x = sorted_points[mid][0]

        left_points = sorted_points[:mid]
        right_points = sorted_points[mid:]

        left_min = solve(left_points)
        right_min = solve(right_points)

        # 결합: 왼쪽 최소 거리와 오른쪽 최소 거리 중 작은 값 선택
        min_dist = min(left_min, right_min)

        # 결합: 경계선을 사이에 둔 점들 검사
        strip = []

        for point in sorted_points:
            if abs(point[0] - mid_x) < min_dist:
                strip.append(point)

        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            j = i + 1

            while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
                j += 1

        return min_dist

    return solve(points)


# 입력
n = int(input())
points = []

for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

# 출력
if n < 2:
    print("가장 가까운 두 점이 없습니다")
else:
    answer = closest_pair(points)
    print(f"{answer:.2f}")

# %% [13~14주차] 광고 가성비 챙기기
import ast


def make_viewer_count(total, logs):

    diff = [0] * (total + 1)

    for start, end in logs:

        diff[start] += 1

        diff[end] -= 1

    viewers = []

    current = 0

    for t in range(total):

        current += diff[t]

        viewers.append(current)

    return viewers


def best_ad_start(total, M, logs):

    viewers = make_viewer_count(total, logs)

    prefix_sum = [0] * (total + 1)

    for i in range(total):

        prefix_sum[i + 1] = prefix_sum[i] + viewers[i]

    def section_sum(start):

        return prefix_sum[start + M] - prefix_sum[start]

    def better(result1, result2):

        sum1, start1 = result1

        sum2, start2 = result2

        if sum1 > sum2:

            return result1

        elif sum2 > sum1:

            return result2

        else:

            if start1 < start2:

                return result1

            else:

                return result2

    def divide_conquer(left, right):

        # 정복: 광고 시작 시간이 하나만 남은 경우

        if left == right:

            return section_sum(left), left

        # 분할: 가능한 광고 시작 시간 범위를 반으로 나눔

        mid = (left + right) // 2

        # 정복: 왼쪽과 오른쪽에서 각각 최적해 탐색

        left_best = divide_conquer(left, mid)

        right_best = divide_conquer(mid + 1, right)

        # 결합: 두 결과 중 더 좋은 결과 선택

        return better(left_best, right_best)

    max_start = total - M

    best_sum, best_start = divide_conquer(0, max_start)

    return viewers, best_start, best_sum


# 입력

total = int(input("총 시간: "))

M = int(input("광고 길이: "))

logs = ast.literal_eval(input("시청 로그: "))

# 실행

viewers, start, max_value = best_ad_start(total, M, logs)

# 출력

print("초별 시청자 수:", viewers)

print("광고 시작 시각:", start)


#10/ 3/ [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)]
