/* 문제 사이트 : https://swexpertacademy.com/main/code/problem/problemDetail.do
    
    주어진 숫자부터 0까지 순서대로 찍어보세요

아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다.

N N-1 N-2 N-3 .... 0 */

a = int(input())
for i in range(a,-1,-1):
    print(i,end=' ')
