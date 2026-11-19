import json

FILENAME = "quizzes.json"


def load_quizzes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("저장 파일이 손상되어 빈 목록으로 시작합니다.")
        return []


def save_quizzes():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)


quizzes = load_quizzes()


def list_quizzes():
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return
    for i, quiz in enumerate(quizzes, start=1):
        print(f"{i}. {quiz['question']}")


def add_quiz():
    question = input("문제: ").strip()
    answer = input("정답: ").strip()
    if not question or not answer:
        print("문제와 정답을 모두 입력해주세요.")
        return
    quizzes.append({"question": question, "answer": answer})
    save_quizzes()
    print("등록되었습니다.")


def delete_quiz():
    list_quizzes()
    if not quizzes:
        return
    try:
        num = int(input("삭제할 번호: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    if 1 <= num <= len(quizzes):
        quizzes.pop(num - 1)
        save_quizzes()
        print("삭제되었습니다.")
    else:
        print("없는 번호입니다.")


def is_correct(user_answer, answer):
    return user_answer.strip().lower() == answer.strip().lower()


def play_quiz():
    if not quizzes:
        print("먼저 퀴즈를 등록해주세요.")
        return
    score = 0
    for quiz in quizzes:
        user_answer = input(quiz["question"] + " ")
        if is_correct(user_answer, quiz["answer"]):
            print("정답!")
            score += 1
        else:
            print("오답! 정답은", quiz["answer"])
    percent = score / len(quizzes) * 100
    print(f"\n결과: {score}/{len(quizzes)} ({percent:.0f}점)")


def main():
    while True:
        print("\n1.퀴즈 풀기 2.목록 3.등록 4.삭제 5.종료")
        choice = input("선택: ")
        if choice == "1":
            play_quiz()
        elif choice == "2":
            list_quizzes()
        elif choice == "3":
            add_quiz()
        elif choice == "4":
            delete_quiz()
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("1~5 중에서 선택해주세요.")


main()

