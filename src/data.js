import integratedCodeRaw from '../알고리즘_주차별_통합코드.py?raw';

const weeklyData = [
  {
    week: '2주차',
    title: '우선순위 큐와 힙',
    concept: '우선순위 큐와 힙의 기본 동작을 이해하고 응용 문제를 분리해 정리',
    files: [],
    problems: [
      {
        id: '2-1',
        title: '응급실 환자 관리 프로그램',
        completed: true,
        contribution: '기존에 작성한 힙 구현을 응급실 상황에 적용할 수 있도록 입력·우선순위·출력 구조를 설계하고, 검토 과정을 통해 음수 우선순위 처리와 환자 번호 저장 방식을 검증함',
        percentage: 90,
        code: '',
      },
      {
        id: '2-2',
        title: '다익스트라 알고리즘 구현',
        completed: true,
        contribution: '검토',
        percentage: 15,
        code: '',
      },
      {
        id: '2-3',
        title: '라면 공장',
        completed: true,
        contribution: '검토',
        percentage: 15,
        code: '',
      },
    ],
  },
  {
    week: '3주차',
    title: '해시 테이블',
    concept: '해시 기반 자료구조를 이용해 탐색과 집계를 분리해 정리',
    files: [],
    problems: [
      {
        id: '3-1',
        title: '배운 내용 구현하기',
        completed: true,
        contribution: '자릿수 접기, 체이닝, BST+체이닝, 선형 탐사, 제곱 탐사, 이중 해싱, 재해싱 구현안을 정리하고 팀 코드에 통합·검수함. 특히 제곱 탐사 상태 갱신과 재해싱 삭제 표식 문제를 확인함',
        percentage: 80,
        code: '',
      },
      {
        id: '3-2',
        title: '급식실 출석 확인',
        completed: true,
        contribution: '요구사항 충족 여부 검토, 전체 제출본 포함 확인, 최종 실행 및 통합 검수로 교사에게 추가 해결 항목으로 인정받음',
        percentage: 60,
        code: '',
      },
      {
        id: '3-3',
        title: '두 개의 수로 특정값 만들기',
        completed: true,
        contribution: '검색 결과가 0일 때 실패로 처리되는 오류를 반례 검토로 확인하고, is not None 조건으로 수정하도록 제안해 실제 수정까지 연결함',
        percentage: 100,
        code: '',
      },
      {
        id: '3-4',
        title: '숫자 카드 개수 구하기',
        completed: true,
        contribution: '전체 코드 검수 범위에 포함하여 누락 여부, 입출력 조건, 제출본 포함 여부를 확인하고 팀 해결 결과로 인정받음',
        percentage: 40,
        code: '',
      },
    ],
  },
  {
    week: '4주차',
    title: '문자열 탐색',
    concept: '문자열 매칭과 부분 문자열 성질을 분리하여 분석',
    files: [],
    problems: [
      { id: '4-1', title: '배운 내용 구현하기', completed: true, contribution: '검토', percentage: 15, code: '' },
      { id: '4-2', title: '문자열 내 최소 반복 단위', completed: true, contribution: '검토', percentage: 15, code: '' },
      { id: '4-3', title: '최장 공통 부분 구하기', completed: true, contribution: '검토', percentage: 15, code: '' },
    ],
  },
  {
    week: '5주차',
    title: '알고리즘 설계와 성능 분석',
    concept: '시간복잡도와 탐색, 정렬, DP 응용 문제를 개별 항목으로 분리',
    files: [],
    problems: [
      { id: '5-1', title: '시간복잡도 구하기', completed: true, contribution: '검토', percentage: 15, code: '' },
      {
        id: '5-2',
        title: '합이 k인 두 수 만들기',
        completed: true,
        contribution: '해시 탐색 코드에서 0 반환값이 거짓으로 평가되는 반례를 확인하고, 목표 합을 찾는 조건을 is not None으로 고쳐야 한다는 수정안을 제시함',
        percentage: 100,
        code: '',
      },
      { id: '5-3', title: '성적 상위 k명 뽑기', completed: true, contribution: '검토', percentage: 15, code: '' },
      {
        id: '5-4',
        title: '계단 오르기',
        completed: true,
        contribution: '문제를 피보나치 구조로 해석해 f(n)=f(n-1)+f(n-2), f(1)=1, f(2)=2 점화식을 도출하고, 재귀 탐색과 반복문 최적화 풀이를 비교함. a, b 두 변수만 갱신하는 O(n) 시간·O(1) 공간 코드를 구현하고 입력값 약 35에서 실행시간 차이를 측정했으며, 황금비 일반항 기반 O(1) 계산법까지 적용해 반복문 결과와 비교하고 큰 입력에서 부동소수점 오차가 생길 수 있음을 분석함',
        percentage: 100,
        highlight: '심화 학습',
        advancedLearning: '계단을 한 번에 1칸 또는 2칸씩 오르는 경우의 수가 피보나치 구조와 같다는 점을 파악하고, 재귀 방식과 반복문 최적화 방식을 비교했다. 특히 a, b 두 변수만 갱신하는 방식으로 O(n) 시간·O(1) 공간 풀이를 구성했으며, 황금비 일반항 기반 O(1) 계산도 추가로 탐구해 큰 입력에서 부동소수점 오차가 발생할 수 있음을 확인했다.',
        code: `def climb_stairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


n = int(input())
print(climb_stairs(n))`,
      },
      { id: '5-5', title: '가장 가까운 두 수', completed: true, contribution: '검토', percentage: 15, code: '' },
      { id: '5-6', title: '섬의 개수 세기', completed: true, contribution: '검토', percentage: 15, code: '' },
    ],
  },
  {
    week: '6주차',
    title: '탐욕 알고리즘',
    concept: '그리디 선택 기준과 MST, 허프만 코딩을 문제별로 분리',
    files: [],
    problems: [
      {
        id: '6-1',
        title: '거스름돈 문제',
        completed: true,
        contribution: '발표 담당은 아니지만 팀 전체 제출 코드 검수 과정에서 정상 입력 작동 여부와 잘못된 입력 처리 방식을 확인함',
        percentage: 15,
        code: '',
      },
      {
        id: '6-2',
        title: '도시 MST 만들고, 분할하기',
        completed: true,
        contribution: '[발표 담당] Kruskal 기반 MST 구성, 가장 비용이 큰 간선 제거, 두 구역 분리 결과와 테스트 케이스를 검증해 발표자료를 준비함',
        percentage: 100,
        highlight: '심화 학습',
        advancedLearning: 'Kruskal 알고리즘은 전체 간선을 가중치가 작은 순서로 정렬한 뒤, Union-Find의 find와 union으로 사이클 여부를 판별하며 간선을 선택한다. 도시 MST 문제에서는 모든 도시를 최소 비용으로 연결한 뒤 선택된 간선 중 가장 큰 비용을 제거하여 두 구역으로 분리하는 응용 구조를 정리했다. MST의 정의, 간선 정렬, 사이클 방지, V-1개 간선 선택 종료 조건, 출력 형식까지 검토했다.',
        code: `def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    if ra < rb:
        parent[rb] = ra
    else:
        parent[ra] = rb
    return True


def split_city(n, edges):
    parent = list(range(n + 1))
    total = 0
    max_edge = 0

    for a, b, cost in sorted(edges, key=lambda x: x[2]):
        if union(parent, a, b):
            total += cost
            max_edge = max(max_edge, cost)

    return total - max_edge`,
      },
      {
        id: '6-3',
        title: 'Prim 알고리즘',
        completed: true,
        contribution: '[발표 담당] Prim의 우선순위 큐 구현, 컷 속성 정당성, Kruskal과의 비교, 시간복잡도와 발표 흐름을 체계적으로 준비함',
        percentage: 100,
        highlight: '심화 학습',
        advancedLearning: 'Prim 알고리즘은 하나의 시작 정점에서 트리를 확장하며, 현재 선택된 정점 집합과 연결되는 간선 중 가장 작은 간선을 고른다. 우선순위 큐를 사용해 최소 간선을 효율적으로 선택하고, 방문하지 않은 정점만 추가해 사이클을 막는다. 발표에서는 Prim과 Kruskal의 탐색 방식, 주요 자료구조, 사이클 처리, 적합한 그래프, O(E log V)와 O(E log E)의 복잡도 차이를 비교했다.',
        code: `import heapq


def prim(n, graph, start=1):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    total = 0
    selected = []

    while heap and len(selected) < n:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue

        visited[node] = True
        total += cost
        selected.append(node)

        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node))

    return total, selected`,
      },
      {
        id: '6-4',
        title: '허프만 코딩',
        completed: true,
        contribution: '[발표 담당] 빈도가 낮은 두 노드 선택, prefix-free 코드 생성 원리, 실행 예시 부족 문제를 검수로 확인하고 발표 설명을 보완함',
        percentage: 85,
        code: '',
      },
      {
        id: '6-5',
        title: '큰 수 만들기',
        completed: true,
        contribution: '발표 담당은 아니지만 전체 제출 코드 검수에서 스택 기반 구현의 정상 동작 여부를 확인함',
        percentage: 15,
        code: '',
      },
    ],
  },
  {
    week: '7주차',
    title: '분할 정복 알고리즘',
    concept: '이진 탐색부터 쿼드 트리와 최근접 점 쌍까지 개별 주제로 정리',
    files: [],
    problems: [
      {
        id: '7-1',
        title: '이진탐색',
        completed: true,
        contribution: '분할정복 1~6번 전체 검수의 일부로 입력값, 탐색 대상 처리, 찾은 위치와 실패 출력 형식이 문제 요구에 맞는지 확인하고 보완 방향을 정리함',
        percentage: 80,
        code: '',
      },
      {
        id: '7-2',
        title: '수식과 괄호 삽입',
        completed: true,
        contribution: '수식 분할, 연산자와 숫자 분리, 부분 문제 결과 조합, 요구 출력과 주석에서 분할·정복·결합 과정이 드러나는지 검수함',
        percentage: 80,
        code: '',
      },
      {
        id: '7-3',
        title: '학급회장 찾기',
        completed: true,
        contribution: '분할정복을 이용한 과반수 후보 탐색 코드가 후보 검출 뒤 실제 과반수인지 다시 세는 검증 과정을 포함하는지 확인함',
        percentage: 80,
        code: '',
      },
      {
        id: '7-4',
        title: '쿼드 트리',
        completed: true,
        contribution: '영역 값 일치 시 재귀 종료, 네 사분면 분할, 최초 호출 범위와 출력 형식이 요구사항에 맞는지 여러 차례 비교·검증함',
        percentage: 80,
        code: '',
      },
      {
        id: '7-5',
        title: '최근접 점 쌍',
        completed: true,
        contribution: 'x좌표 정렬, 좌우 부분 문제 해결, 중앙 strip 검사, O(n²)와 O(n log n) 비교가 코드와 주석에 드러나는지 검토하고 보완점을 정리함',
        percentage: 80,
        code: '',
      },
      {
        id: '7-6',
        title: '광고 가성비 챙기기',
        completed: true,
        contribution: '선택 구간, 계산된 가성비 또는 이익, 최종 최적값, 입력 형식과 분할정복 과정 설명이 누락되지 않도록 검토 결과를 바탕으로 보완 대상을 정리함',
        percentage: 80,
        code: '',
      },
    ],
  },
  {
    week: '8주차',
    title: '동적 계획법',
    concept: 'DP 점화식과 상태 분리를 문제 단위로 정리',
    files: [],
    problems: [
      {
        id: '8-1',
        title: '계단 오르기 구현',
        completed: true,
        contribution: '앞서 사용한 피보나치형 풀이를 동적 계획법 관점에서 다시 정리하고, dp[i]를 i번째 계단까지 올라가는 방법의 수로 정의함. dp[0]=1, dp[1]=1, dp[2]=2 초기값과 dp[i]=dp[i-1]+dp[i-2] 점화식을 적용해 전체 DP 테이블을 생성하는 표준 O(n) 풀이를 구현했으며, count_stair_ways(n)가 최종 방법 수와 DP 테이블을 함께 반환하도록 설계함. 필수 O(n) DP 풀이와 일반항 기반 O(1) 추가 탐구를 구분하고, 예외 입력·출력 형식과 시험 대비 핵심 구현 원리까지 정리함',
        percentage: 100,
        highlight: '심화 학습',
        advancedLearning: '피보나치형 계단 오르기 풀이를 동적 계획법의 관점에서 다시 정리했다. dp[i]를 i번째 계단까지 올라가는 방법의 수로 정의하고, dp[0]=1, dp[1]=1, dp[2]=2에서 시작해 dp[i]=dp[i-1]+dp[i-2]를 적용했다. 최종 답만 구하는 것이 아니라 전체 DP 테이블을 함께 반환하도록 만들어 각 단계의 값이 이전 결과로부터 어떻게 만들어지는지 확인할 수 있게 했다.',
        code: `def count_stair_ways(n):
    if n < 0:
        return 0, []

    dp = [0] * (n + 1)
    dp[0] = 1

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n], dp


n = int(input())
answer, table = count_stair_ways(n)
print(answer)
print(table)`,
      },
      {
        id: '8-2',
        title: '최장 공통 부분 수열 구현',
        completed: true,
        contribution: '제출 코드가 PDF 요구와 다르다는 점을 발견하고, DP 표에서 우선 방향을 따라 하나의 LCS를 역추적하는 방식으로 수정 방향을 정리함',
        percentage: 90,
        code: '',
      },
      { id: '8-3', title: '최대 서브 배열', completed: true, contribution: '검토', percentage: 15, code: '' },
      {
        id: '8-4',
        title: '집 도둑',
        completed: true,
        contribution: 'House Robber 유형의 dp[i]=max(dp[i-1], dp[i-2]+nums[i]) 점화식을 확인하고 인접 선택 불가 조건의 상태 전이를 검토함',
        percentage: 60,
        code: '',
      },
      {
        id: '8-5',
        title: '박람회 부스 배치',
        completed: true,
        contribution: '0-1 배낭형 배치 문제의 DP 표, 점화식, 선택 여부 비교, 역추적 방식과 탐욕법으로 최적해를 보장하지 못하는 이유를 검증함',
        percentage: 85,
        code: '',
      },
      {
        id: '8-6',
        title: '상점 받기 게임',
        completed: true,
        contribution: '격자 선택형 DP에서 열별 선택 상태를 나누고 비트마스크로 가능한 상태를 표현하는 방식을 검토함',
        percentage: 60,
        code: '',
      },
    ],
  },
  {
    week: '9주차',
    title: '백트래킹',
    concept: '탐색 가지치기와 완전탐색 문제를 개별 항목으로 정리',
    files: [],
    problems: [
      { id: '9-1', title: '미로 탈출하기 구현', completed: true, contribution: '검토', percentage: 15, code: '' },
      {
        id: '9-2',
        title: '지도 색칠하기 구현',
        completed: true,
        contribution: '서울시 25개 구 인접 딕셔너리를 구성하고, degree heuristic을 적용한 4색 정리 확장 시뮬레이터를 구현·검증·개선하여 팀 제출물에 통합함',
        percentage: 100,
        highlight: '심화 학습',
        advancedLearning: '서울시 25개 자치구를 정점, 인접 관계를 간선으로 모델링하고 네 가지 색으로 인접 구가 겹치지 않도록 칠하는 백트래킹 시뮬레이터를 구성했다. 연결 리스트를 양방향 그래프로 정규화하고, 색 시도·배정·거부·되돌리기·해 발견 과정을 단계별 로그로 남겼다. 차수가 높은 구부터 탐색하는 degree_order를 적용해 제약이 많은 구를 먼저 처리하도록 개선했으며, Streamlit과 Plotly를 이용해 지도 모드, 그래프 모드, 직접 칠하기, DFS 시뮬레이션, 상태공간트리, 자동 재생 기능까지 확장했다.',
        code: `COLORS = ["red", "blue", "green", "yellow"]


def degree_order(graph):
    return sorted(graph, key=lambda node: len(graph[node]), reverse=True)


def is_valid(graph, assignment, node, color):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True


def color_map(graph):
    order = degree_order(graph)
    assignment = {}
    steps = []

    def dfs(depth):
        if depth == len(order):
            steps.append(("solution", assignment.copy()))
            return True

        node = order[depth]
        steps.append(("enter", node, assignment.copy()))

        for color in COLORS:
            steps.append(("try", node, color, assignment.copy()))
            if is_valid(graph, assignment, node, color):
                assignment[node] = color
                steps.append(("assign", node, color, assignment.copy()))

                if dfs(depth + 1):
                    return True

                steps.append(("backtrack", node, color, assignment.copy()))
                del assignment[node]
            else:
                steps.append(("reject", node, color, assignment.copy()))

        return False

    dfs(0)
    return assignment, steps`,
      },
      { id: '9-3', title: '순열 생성', completed: true, contribution: '검토', percentage: 15, code: '' },
      {
        id: '9-4',
        title: '스도쿠 풀기',
        completed: true,
        contribution: '4×4 스도쿠 백트래킹 코드를 구현하고 행·열·2×2 박스 검사, 빈칸 목록, 실패 시 원상복구 과정을 팀 채팅에 공유하며 원리를 설명함',
        percentage: 100,
        code: '',
      },
      { id: '9-5', title: '숫자 골라 최대 합 만들기', completed: true, contribution: '검토', percentage: 15, code: '' },
    ],
  },
];


const sourceSections = integratedCodeRaw
  .split(/(?=^# %% .*$)/m)
  .filter((section) => section.startsWith('# %%'));

const getSourceCode = (...headers) => {
  return headers
    .flatMap((header) => sourceSections.filter((section) => section.startsWith('# %% ' + header)))
    .join('\n\n')
    .trim();
};

const sourceCodeById = {
  '3-1': getSourceCode('[3~4주차] 나눗셈 해싱', '[3~4주차] 자릿수 접기 해싱', '[3~4주차] 체이닝', '[3~4주차] BST + 체이닝', '[3~4주차] Tombstone', '[3~4주차] 선형 탐사', '[3~4주차] 제곱 탐사', '[3~4주차] Double Hashing', '[3~4주차] Rehashing', '[3~4주차] ReDouble', '[3~4주차] ReQuad', '[3~4주차] ReLinear'),
  '3-2': getSourceCode('[3~4주차] 급식실 출석 확인'),
  '3-3': getSourceCode('[3~4주차] 하지만 우리에겐? 해싱이 있다!'),
  '3-4': getSourceCode('[3~4주차] 3-B'),
  '4-1': getSourceCode('[11~12주차] 코드 셀 1', '[11~12주차] 코드 셀 2', '[11~12주차] 코드 셀 3', '[11~12주차] 코드 셀 4', '[11~12주차] 코드 셀 5'),
  '4-2': getSourceCode('[11~12주차] 코드 셀 6'),
  '4-3': getSourceCode('[11~12주차] 코드 셀 7'),
  '5-2': getSourceCode('[1~2주차] 합이 k인 두 수 구하기'),
  '5-3': getSourceCode('[1~2주차] 성적 상위 k명 뽑기'),
  '5-4': getSourceCode('[1~2주차] 4.계단 오르기'),
  '5-5': getSourceCode('[1~2주차] 가장 가까운 두 수'),
  '5-6': getSourceCode('[1~2주차] 섬의 개수 세기'),
  '6-1': getSourceCode('[9~10주차] 거스름돈'),
  '6-2': getSourceCode('[9~10주차] 도시 MST 만들고 분할 하기'),
  '6-3': getSourceCode('[9~10주차] Kruskal과 Prim은 왜 정당화 되는가?'),
  '6-4': getSourceCode('[9~10주차] 허프만 코딩'),
  '6-5': getSourceCode('[9~10주차] 큰 수 만들기'),
  '7-1': getSourceCode('[13~14주차] 이진탐색'),
  '7-2': getSourceCode('[13~14주차] 수식과 괄호 삽입'),
  '7-3': getSourceCode('[13~14주차] 학급회장 찾기'),
  '7-4': getSourceCode('[13~14주차] 쿼드 트리'),
  '7-5': getSourceCode('[13~14주차] 최근접 점 쌍'),
  '7-6': getSourceCode('[13~14주차] 광고 가성비 챙기기'),
  '8-1': getSourceCode('[5~6주차] 1. 계단 오르기'),
  '8-2': getSourceCode('[5~6주차] 2. 최장 공통 부분 수열 구현'),
  '8-3': getSourceCode('[5~6주차] 동적계획법'),
  '8-4': getSourceCode('[5~6주차] 4. 집 도둑'),
  '8-5': getSourceCode('[5~6주차] 5. 박람회 부스 배치'),
  '8-6': getSourceCode('[5~6주차] 6. 상점 받기 게임'),
  '9-1': getSourceCode('[7~8주차] 1. 미로 탈출하기 구현'),
  '9-2': getSourceCode('[7~8주차] 2. 지도 색칠하기 구현'),
  '9-3': getSourceCode('[7~8주차] 3. 순열 생성'),
  '9-4': getSourceCode('[7~8주차] 4. 스도쿠 풀기'),
  '9-5': getSourceCode('[7~8주차] 5. 숫자 골라 최대합 만들기'),
};

for (const week of weeklyData) {
  for (const problem of week.problems) {
    if (sourceCodeById[problem.id]) {
      problem.code = sourceCodeById[problem.id];
    }
  }
}

export const dummyData = weeklyData.flatMap((week) =>
  week.problems.map((problem) => ({
    week: week.week,
    weekTitle: week.title,
    weekConcept: week.concept,
    files: week.files,
    ...problem,
  }))
);

export const weeklySummary = weeklyData;
