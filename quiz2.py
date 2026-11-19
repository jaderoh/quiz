import json
import random


class Quiz:
    """퀴즈 한 문제를 나타내는 클래스"""

    def __init__(self, question, answer, choices=None):
        self.question = question
        self.answer = answer
        self.choices = choices  # 객관식이면 보기 리스트, 주관식이면 None

    def is_multiple_choice(self):
        return bool(self.choices)

    def check(self, user_answer):
        """주관식 정답 비교 (공백·대소문자 무시)"""
        return user_answer.strip().lower() == self.answer.strip().lower()

    def ask(self):
        """문제를 출제하고 맞으면 True, 틀리면 False 반환"""
        if self.is_multiple_choice():
            print(self.question)
            for i, choice in enumerate(self.choices, start=1):
                print(f"  {i}) {choice}")
            try:
                num = int(input("번호 선택: "))
            except ValueError:
                return False
            return 1 <= num <= len(self.choices) and self.choices[num - 1] == self.answer

        return self.check(input(self.question + " "))

    def to_dict(self):
        """JSON 저장용 딕셔너리로 변환"""
        data = {"question": self.question, "answer": self.answer}
        if self.choices:
            data["choices"] = self.choices
        return data

    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 Quiz 객체 생성"""
        return cls(data["question"], data["answer"], data.get("choices"))

    def __str__(self):
        tag = "[객관식] " if self.is_multiple_choice() else ""
        return f"{tag}{self.question}"


class QuizGame:
    """퀴즈 목록 관리, 저장, 진행을 담당하는 클래스"""

    def __init__(self, quiz_file="quizzes.json", score_file="highscore.json"):
        self.quiz_file = quiz_file
        self.score_file = score_file
        self.quizzes = self.load_quizzes()

    # ---------- 파일 입출력 ----------
    def load_quizzes(self):
        try:
            with open(self.quiz_file, "r", encoding="utf-8") as f:
                return [Quiz.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            return []
        except (json.JSONDecodeError, KeyError, TypeError):
            print("저장 파일이 손상되어 빈 목록으로 시작합니다.")
            return []

    def save_quizzes(self):
        with open(self.quiz_file, "w", encoding="utf-8") as f:
            json.dump([q.to_dict() for q in self.quizzes], f, ensure_ascii=False, indent=2)

    def load_high_score(self):
        try:
            with open(self.score_file, "r", encoding="utf-8") as f:
                return json.load(f)["best"]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return 0

    def save_high_score(self, best):
        with open(self.score_file, "w", encoding="utf-8") as f:
            json.dump({"best": best}, f)

    # ---------- 기능 ----------
    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz}")

    def add_quiz(self):
        question = input("문제: ").strip()
        if not question:
            print("문제를 입력해주세요.")
            return

        kind = input("유형 (1.주관식 2.객관식): ").strip()

        if kind == "2":
            choices = []
            for i in range(1, 5):
                choice = input(f"보기 {i}: ").strip()
                if not choice:
                    print("보기를 모두 입력해주세요.")
                    return
                choices.append(choice)
            try:
                num = int(input("정답 번호 (1~4): "))
            except ValueError:
                print("숫자를 입력해주세요.")
                return
            if not 1 <= num <= 4:
                print("1~4 중에서 입력해주세요.")
                return
            quiz = Quiz(question, choices[num - 1], choices)
        else:
            answer = input("정답: ").strip()
            if not answer:
                print("정답을 입력해주세요.")
                return
            quiz = Quiz(question, answer)

        self.quizzes.append(quiz)
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

    def play(self):
        if not self.quizzes:
            print("먼저 퀴즈를 등록해주세요.")
            return

        shuffled = random.sample(self.quizzes, len(self.quizzes))

        score = 0
        for quiz in shuffled:
            if quiz.ask():
                print("정답!")
                score += 1
            else:
                print("오답! 정답은", quiz.answer)

        percent = score / len(shuffled) * 100
        print(f"\n결과: {score}/{len(shuffled)} ({percent:.0f}점)")

        best = self.load_high_score()
        if percent > best:
            self.save_high_score(round(percent))
            print("🎉 신기록입니다!")
        else:
            print(f"최고 점수: {best}점")

    def run(self):
        while True:
            print("\n1.퀴즈 풀기 2.목록 3.등록 4.삭제 5.종료")
            choice = input("선택: ")
            if choice == "1":
                self.play()
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


if __name__ == "__main__":
    QuizGame().run()