import json

FILENAME = "quizzes.json"


class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def is_correct(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()


class QuizGame:
    def __init__(self):
        self.quizzes = self.load_quizzes()

    def load_quizzes(self):
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Quiz(d["question"], d["answer"]) for d in data]
        except FileNotFoundError:
            return []
        except (json.JSONDecodeError, KeyError, TypeError):
            print("저장 파일이 손상되어 빈 목록으로 시작합니다.")
            return []

    def save_quizzes(self):
        data = [{"question": q.question, "answer": q.answer} for q in self.quizzes]
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

    def add_quiz(self):
        question = input("문제: ").strip()
        answer = input("정답: ").strip()
        if not question or not answer:
            print("문제와 정답을 모두 입력해주세요.")
            return
        self.quizzes.append(Quiz(question, answer))
        self.save_quizzes()
        print("등록되었습니다.")

    def delete_quiz(self):
        self.list_quizzes()
        if not self.quizzes:
            return
        try:
            num = int(input("삭제할 번호: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            return
        if 1 <= num <= len(self.quizzes):
            self.quizzes.pop(num - 1)
            self.save_quizzes()
            print("삭제되었습니다.")
        else:
            print("없는 번호입니다.")

    def play_quiz(self):
        if not self.quizzes:
            print("먼저 퀴즈를 등록해주세요.")
            return
        score = 0
        for quiz in self.quizzes:
            user_answer = input(quiz.question + " ")
            if quiz.is_correct(user_answer):
                print("정답!")
                score += 1
            else:
                print("오답! 정답은", quiz.answer)
        percent = score / len(self.quizzes) * 100
        print(f"\n결과: {score}/{len(self.quizzes)} ({percent:.0f}점)")

    def run(self):
        while True:
            print("\n1.퀴즈 풀기 2.목록 3.등록 4.삭제 5.종료")
            choice = input("선택: ")
            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.list_quizzes()
            elif choice == "3":
                self.add_quiz()
            elif choice == "4":
                self.delete_quiz()
            elif choice == "5":
                print("종료합니다.")
                break
            else:
                print("1~5 중에서 선택해주세요.")


QuizGame().run()