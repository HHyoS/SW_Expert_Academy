문제 사이트 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD#none

개발 환경 : pycham


문제 설명 :

    아래는 비상연락망을 나타낸 그림이다.


![SW문제해결+기본 +10일차+-+Contact_그림1](https://user-images.githubusercontent.com/57944215/179356321-e2be8fe6-c2e1-4a6e-9dda-c1560e631658.png)

 
    각 원은 개개인을 의미하며, 원 안의 숫자는 그사람의 번호를 나타내고 빨간원은 연락을 시작하는 당번을 의미한다.

    화살표는 연락이 가능한 방향을 의미한다.

    위의 예시에서는 7번과 1번은 서로 연락이 가능하다,

    하지만 2번과 7번의 경우 2번은 7번에게 연락할 수 있지만 7번은 2번에게 연락할 수 없다.

    비상연락망이 가동되면 아래 그림과 같이 연락을 시작하는 당번인 2번은 연락 가능한 7번과 15번에 동시에 연락을 취한다 (다자 간 통화를 사용한다고 가정).

![SW문제해결+기본 +10일차+-+Contact_그림2](https://user-images.githubusercontent.com/57944215/179356350-ab217335-4bd1-4f38-8c5f-dcbdc5a5fa66.png)


    그 다음 아래와 같이 7번은 1번에게, 15번은 4번에게 연락을 취한다 (이 과정은 동시에 일어난다고 가정한다).
 
![SW문제해결+기본 +10일차+-+Contact_그림3](https://user-images.githubusercontent.com/57944215/179356347-3f7e3d85-d561-4627-b07c-62ad53068b60.png)


    그 다음 아래와 같이 1번은 8번과 17번에게 동시에 연락하며, 이와 동시에 4번은 10번에게 연락한다.

    7번과 2번의 경우는 이미 연락을 받은 상태이기 때문에 다시 연락하지 않는다.
 
![SW문제해결+기본 +10일차+-+Contact_그림4](https://user-images.githubusercontent.com/57944215/179356359-026c1931-c7b2-485e-a31c-c974e144f7b5.png)


    위의 모습이 연락이 끝난 마지막 모습이 되며, 마지막에 동시에 연락 받은 사람은 8번, 10번, 17번의 세 명이다.

    이 중에서 가장 숫자가 큰 사람은 17번이므로 17을 반환하면 된다.

    ※ 3, 6, 11, 22번은 시간이 지나도 연락을 받지 못한다.
 
[제약 사항]

    연락 인원은 최대 100명이며, 부여될 수 있는 번호는 1이상, 100이하이다.

    단, 예시에서 5번이 존재하지 않듯이 중간 중간에 비어있는 번호가 있을 수 있다.

    한 명의 사람이 다수의 사람에게 연락이 가능한 경우 항상 다자 간 통화를 통해 동시에 전달한다.

    연락이 퍼지는 속도는 항상 일정하다 (전화를 받은 사람이 다음사람에게 전화를 거는 속도는 동일).

    비상연락망 정보는 사전에 공유되며 한 번 연락을 받은 사람에게 다시 연락을 하는 일은 없다.

    예시에서의 3, 6, 11, 22번과 같이 연락을 받을 수 없는 사람도 존재할 수 있다.
 
[입력]

    입력의 첫 번째 줄에는 입력 받는 데이터의 길이와 시작점이 주어진다.

    그 다음 줄에 입력받는 데이터는 {from, to, from, to, …} 의 순서로 해석되며 예시의 경우는 
    
    {2, 7, 11, 6, 6, 2, 2, 15, 15, 4, 4, 2, 4, 10, 7, 1, 1, 7, 1, 8, 1, 17, 3, 22}와 같다.

    그런데 순서에는 상관이 없으므로 다음과 같이 주어진 인풋도 동일한 비상연락망을 나타낸다 
    
    (같은 비상연락망을 표현하는 다양한 인풋이 존재 가능하다).

    {1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 4, 2}

    다음과 같이 동일한 {from, to}쌍이 여러 번 반복되는 경우도 있으며, 한 번 기록된 경우와 여러 번 기록된 경우의 차이는 없다.

    {1, 17, 1, 17, 1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 11, 6, 4, 2}
 
[출력]

    #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

입력

    24 2
    1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
    300 42
    42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42 34 16 40 59 5 31 78 7 74 87 22 46 25 73 71 30 78 74 98 13 87 91 62 37 56 68 56 75 32 53 51 51 42 25 67 31 8 92 8 38 58 88 54 84 46 10 10 59 22 89 23 47 7 31 14 69 1 92 63 56 11 60 25 38 49 84 96 42 3 51 92 37 75 21 97 22 49 100 69 85 82 35 54 100 19 39 1 89 28 68 29 94 49 84 8 22 11 18 14 15 10 17 36 52 1 50 20 57 99 4 25 9 45 10 90 3 96 86 94 44 24 88 15 4 49 1 59 19 81 97 99 82 90 99 10 58 73 23 39 93 39 80 91 58 59 92 16 89 57 12 3 35 73 56 29 47 63 87 76 34 70 43 45 17 82 99 23 52 22 100 58 77 93 90 76 13 1 11 4 70 62 89 2 90 56 24 3 86 83 86 89 27 18 58 33 33 70 55 22 90

출력

    #1 17
    #2 96
  
풀이 알고리즘

    처음 연락을 시작 한 이후, 각 단계마다 퍼져나가면서 연락하지 않은 사람 들 중 연락이 가능한 사람들에게 연락하며 마지막 단계에서 연락받은 사람 중 번호가
    
    가장 큰 번호를 찾는 문제였습니다.
    
    처음 시작한 이후, 계속해서 퍼져나가며 더이상 불가능할떄까지 반복하는 탐색은 BFS탐색이라고 생각하였고, BFS탐색의 동작이 이 문제에서 원하는 방식과 동일하다고
    
    생각하였습니다.
    
    제가 생각한 알고리즘은 다음과 같습니다
    
    1. 현재 queue에 담긴 번호의 수(현재 단계에서 탐색할 번호들의 숫자) 만큼 반복하며 담긴 숫자와 연결된 사람 중 연결되지 않은 사람에게 연락
    
    2. (1)을 하는 과정에서 가장 큰 수룰 찾아 저장
    
    3. (2)단계 종료 후 연락할 사람이 없다면 (1)로 돌아가지 않고 (2)에서 저장한 가장 큰 수 출력
    
    4. (3)단계에서 queue가 안비어졌다면, (1)로 돌아가서 다시 반복 실시
    
구 현

    from collections import deque


    for a in range(1,11) :
        N,node = map(int,input().split())

        grp = [[] for _ in range(101)]
        temp = list(map(int, input().split()))
        for b in range(0,N,2):
            grp[temp[b]].append(temp[b+1])

        queue = deque()
        check = [0 for _ in range(101)]
        queue.append(node)
        check[node] = 1
        answer = 0

        while len(queue) != 0 :
            ans = -1
            size = len(queue)
            for _ in range(size) :
                num = queue.popleft()
                for b in grp[num] :
                    if check[b] == 0 :
                        queue.append(b)
                        check[b] = 1
                        if  b > ans :
                            ans = b
                if ans != -1 :
                    answer = ans

        print('#'+str(a)+' '+ str(answer))






    
