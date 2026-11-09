class 퀴즈:
    def __init__(self, 문제, 선택지, 정답):
        self.문제 = 문제
        self.선택지 = 선택지      # 리스트: ['A', 'B', 'C', 'D']
        self.정답 = 정답          # 'A' 같은 정답
    
    def 출력(self):
        print(f"\n{self.문제}")
        for i, 선택 in enumerate(self.선택지):
            print(f"{chr(65+i)}. {선택}")  # A, B, C, D로 출력
    
    def 채점(self, 사용자_답):
        return 사용자_답 == self.정답


class 퀴즈게임:
    def __init__(self):
        self.퀴즈_목록 = []
        self.점수 = 0
    
    def 퀴즈_추가(self, 퀴즈):
        self.퀴즈_목록.append(퀴즈)
    
    def 게임_시작(self):
        print("=== 퀴즈 게임 시작 ===")
        
        for 퀴즈 in self.퀴즈_목록:
            퀴즈.출력()
            사용자_답 = input("답을 입력하세요 (A/B/C/D): ").upper()
            
            if 퀴즈.채점(사용자_답):
                print("✓ 정답입니다!")
                self.점수 += 1
            else:
                print(f"✗ 틀렸습니다. 정답은 {퀴즈.정답}입니다.")
        
        self.결과_출력()
    
    def 결과_출력(self):
        총점 = len(self.퀴즈_목록)
        print(f"\n=== 게임 종료 ===")
        print(f"점수: {self.점수}/{총점}")
        print(f"정답률: {self.점수/총점*100:.1f}%")


# 게임 실행
게임 = 퀴즈게임()

# 퀴즈 추가
게임.퀴즈_추가(퀴즈(
    "Python에서 리스트를 만드는 방법은?",
    ["list()", "[]", "{}", "()"],
    "B"
))

게임.퀴즈_추가(퀴즈(
    "클래스의 초기화 메서드 이름은?",
    ["init()", "__init__()", "start()", "create()"],
    "B"
))

게임.퀴즈_추가(퀴즈(
    "Python의 반복문은?",
    ["loop", "for", "repeat", "while"],
    "B"
))

게임.게임_시작()