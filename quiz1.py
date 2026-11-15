import json
import os

# 퀴즈 데이터 저장 파일
QUIZ_FILE = "quizzes.json"
SCORE_FILE = "scores.json"

class QuizProgram:
    def __init__(self):
        self.quizzes = self.load_quizzes()
        self.scores = self.load_scores()
    
    def load_quizzes(self):
        """저장된 퀴즈 데이터 불러오기"""
        if os.path.exists(QUIZ_FILE):
            try:
                with open(QUIZ_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_quizzes(self):
        """퀴즈 데이터 저장"""
        with open(QUIZ_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.quizzes, f, ensure_ascii=False, indent=2)
    
    def load_scores(self):
        """저장된 점수 데이터 불러오기"""
        if os.path.exists(SCORE_FILE):
            try:
                with open(SCORE_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {"total": 0, "correct": 0, "wrong": 0}
        return {"total": 0, "correct": 0, "wrong": 0}
    
    def save_scores(self):
        """점수 데이터 저장"""
        with open(SCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=2)
    
    def add_quiz(self):
        """새로운 퀴즈 추가"""
        print("\n=== 퀴즈 추가 ===")
        question = input("문제를 입력하세요: ").strip()
        
        if not question:
            print("❌ 문제를 입력해야 합니다.")
            return
        
        options = []
        print("선택지를 입력하세요 (4개, 빈 줄로 종료):")
        for i in range(4):
            option = input(f"선택지 {i+1}: ").strip()
            if not option:
                print("❌ 4개의 선택지를 모두 입력해야 합니다.")
                return
            options.append(option)
        
        while True:
            try:
                answer = int(input("정답 번호 (1-4): "))
                if 1 <= answer <= 4:
                    break
                print("❌ 1~4 사이의 숫자를 입력하세요.")
            except ValueError:
                print("❌ 숫자를 입력하세요.")
        
        quiz = {
            "id": len(self.quizzes) + 1,
            "question": question,
            "options": options,
            "answer": answer
        }
        
        self.quizzes.append(quiz)
        self.save_quizzes()
        print(f"✅ 퀴즈가 추가되었습니다! (ID: {quiz['id']})")
    
    def show_quizzes(self):
        """저장된 퀴즈 목록 확인"""
        print("\n=== 퀴즈 목록 ===")
        
        if not self.quizzes:
            print("저장된 퀴즈가 없습니다.")
            return
        
        for quiz in self.quizzes:
            print(f"\n[ID: {quiz['id']}] {quiz['question']}")
            for i, option in enumerate(quiz['options'], 1):
                print(f"  {i}. {option}")
            print(f"  정답: {quiz['answer']}")
    
    def solve_quiz(self):
        """퀴즈 풀기"""
        print("\n=== 퀴즈 풀기 ===")
        
        if not self.quizzes:
            print("풀 수 있는 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return
        
        print(f"총 {len(self.quizzes)}개의 퀴즈가 있습니다.\n")
        
        correct_count = 0
        
        for quiz in self.quizzes:
            print(f"[문제 {quiz['id']}] {quiz['question']}")
            for i, option in enumerate(quiz['options'], 1):
                print(f"  {i}. {option}")
            
            while True:
                try:
                    user_answer = int(input("답을 선택하세요 (1-4): "))
                    if 1 <= user_answer <= 4:
                        break
                    print("❌ 1~4 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("❌ 숫자를 입력하세요.")
            
            if user_answer == quiz['answer']:
                print("✅ 정답입니다!\n")
                correct_count += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {quiz['answer']}번입니다.\n")
        
        # 점수 기록
        total = len(self.quizzes)
        wrong_count = total - correct_count
        
        self.scores["total"] += total
        self.scores["correct"] += correct_count
        self.scores["wrong"] += wrong_count
        self.save_scores()
        
        print("=" * 40)
        print(f"결과: {correct_count}/{total} 정답")
        print(f"정답률: {(correct_count/total*100):.1f}%")
        print("=" * 40)
    
    def show_scores(self):
        """점수 확인"""
        print("\n=== 점수 확인 ===")
        
        total = self.scores["total"]
        correct = self.scores["correct"]
        wrong = self.scores["wrong"]
        
        if total == 0:
            print("아직 풀어본 퀴즈가 없습니다.")
            return
        
        accuracy = (correct / total * 100) if total > 0 else 0
        
        print(f"총 문제 수: {total}개")
        print(f"정답: {correct}개")
        print(f"오답: {wrong}개")
        print(f"정답률: {accuracy:.1f}%")
    
    def show_menu(self):
        """메인 메뉴 표시"""
        print("\n" + "=" * 40)
        print("       🎯 퀴즈 프로그램 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 확인")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)
    
    def run(self):
        """프로그램 실행"""
        while True:
            self.show_menu()
            choice = input("선택 (1-5): ").strip()
            
            if choice == "1":
                self.solve_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_scores()
            elif choice == "5":
                print("\n👋 프로그램을 종료합니다.")
                break
            else:
                print("❌ 1~5 사이의 숫자를 입력하세요.")


if __name__ == "__main__":
    program = QuizProgram()
    program.run()
