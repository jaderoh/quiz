import random
import json

with open('state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

#print(data)

#퀴즈프로그램 만들기 시작하기
print("="*50)
print("나만의 퀴즈 게임")
print("="*50)
print("1. 퀴즈 풀기")
print("="*50)
choose = int(input("선택 : "))
if choose == 1 :
    print("퀴즈를 시작합니다! (총 5문제)")
    print("-"*30)
    print("[문제1]")
    print("질문")
    print("""
        1. 4개
        2. 5개
        3. 6개
        4. 7개
    """)
    answer = int(input("정답입력 : "))
    if answer == 3 :
        print("정답입니다!")
    else :
        print("틀렸습니다!")
    print("-"*30)
