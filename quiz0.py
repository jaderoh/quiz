import random
import json

with open('state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
#print(data)

ok = [False]*3

def quizshow(num):
    print("퀴즈를 시작합니다! (총 5문제)")
    print("-"*30)
    print("[문제"+str(num+1)+"]")
    print(data["quizzes"][num]["question"])
    for i in range(4):
        print(str(i+1)+".", data["quizzes"][num]["choices"][i])
    answer = int(input("정답입력 : "))
    if answer == data["quizzes"][num]["answer"] :
        print("정답입니다!")
        ok[num] = True
        q = random.randrange(0,3)
        quizshow(q)
    elif answer in range(5):
        print("틀렸습니다!")
        quizshow(num)
    else :
        print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
        quizshow(num)
    print("-"*30)

print("="*50)
print("나만의 퀴즈 게임")
print("="*50)
print("1. 퀴즈 풀기")
print("5. 종료하려면 q를 입력하세요")
print("="*50)
choose = int(input("선택 : "))
answer = "a"
while choose == 1 and answer!= "q" :
    q = random.randrange(0,3)
    quizshow(q)
    
print("퀴즈를 종료합니다")
print(ok)

