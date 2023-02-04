#네트워크 연결
import sys
input=sys.stdin.readline

N = int(input().strip())
line_no = int(input().strip())


def compare_node(P_node, x): # 나랑 연결된 Node 찾기 --> 현재 나 x가 어디로 연결되어있는지 확인하는 부분
    if P_node[x]==x:
        return x
    P_node[x] = compare_node(P_node, P_node[x])

    return P_node[x]

def Union_node(P_node,a,b): # 둘이 비교해서 더 작은 cost를 갖는 곳으로 연결됨 --> cost에 따라서 정렬해놓았기 때문에
    a = compare_node(P_node, a)
    b = compare_node(P_node, b)
    
    if a<b:
        P_node[b] = a
    else:
        P_node[a] = b


def solve() :
    cost =0
    for i in com_list:
        c,a,b = i
        if compare_node(P_node, a) != compare_node(P_node, b):
            Union_node(P_node,a,b)
            cost +=c
    return cost



com_list = []
for i in range(line_no):
    a,b,c = map(int,(input().strip().split()))
    com_list.append([c, a, b]) # 저장 순서는 cost, com1, com2

com_list.sort()

P_node=[] # 부모노드 --> 각 컴퓨터가 어디로 연결되어 있는지 기록하기 위한 부분
for i in range(N+1):
    P_node.append(i)

print(solve())