class Bird():
    sound = {"앵무새" : "안녕하세요?",
            "참새" : "짹짹",
            "비둘기" : "9999",
            "닭" : "교촌교촌",
            "러버덕" : "QUACK",
            "펭귄" : "꾸르륵"
            }

    def __init__(self, birdtype: str):  #초기화
        self.birdtype = birdtype
    
    def birdfly(self) -> None:
        print(f"{self.birdtype}가 날고 있습니다.")

    def birdsing(self) -> None:
        s = Bird.sound.get(self.birdtype, "짹짹")  # 모르는 새면 기본 소리
        print(f"{s}")

while True:
    try:
        user_input = input("새의 종류와 행동(울기, 날기)을 입력하세요: ")
        birdtype, action = [s.strip() for s in user_input.split(",", 1)]
        b = Bird(birdtype)

        if birdtype not in Bird.sound:    # 유효성 검사
            print("다시 작성해 주세요.")
        else: 
            if action == "날기":
                b.birdfly()
            elif action == "울기":
                b.birdsing()
            else:
                print("지원하지 않는 행동입니다: 울기/날기 중 선택")
                
    except ValueError:
        print("오류가 발생했습니다. 다시 작성해 주세요!")
        print(f"새 종류: {Bird.sound.keys()}")
    
    finally:
        check_cont = input("계속 하시겠습니까? Y/N ").strip().lower()
        if check_cont == "n":
            break