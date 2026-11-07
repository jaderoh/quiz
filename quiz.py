import random
import json

with open('state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
#print(data)

print("="*50)
print("나만의 퀴즈 게임")
print("="*50)
print("1. 퀴즈 풀기")
print("5. 종료하려면 q를 입력하세요")
print("="*50)
choose = int(input("선택 : "))
answer = "a"
while choose == 1 and answer!= "q" :
    print("퀴즈를 시작합니다! (총 5문제)")
    print("-"*30)
    q = random.randrange(0,3)
    print("[문제1]")
    print(data["quizzes"][q]["question"])
    for i in range(4):
        print(str(i+1)+".", data["quizzes"][q]["choices"][i])
    answer = int(input("정답입력 : "))
    if answer == data["quizzes"][q]["answer"] :
        print("정답입니다!")
    elif answer in range(5):
        print("틀렸습니다!")
    else :
        print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
    print("-"*30)
