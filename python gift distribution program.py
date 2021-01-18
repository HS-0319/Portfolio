gift = {1:"아이패드", 2:"맥북", 3:"애플워치", 4:"에어팟", 5:"전동킥보드"}

print("Merry Christmas!")

while True:
    if len(gift) != 0:
        a=int(input("선물 번호를 입력하세요:"))
        if a == 1:
            if 1 in gift:
                print("당신의 선물은 아이패드입니다.")
                del gift[1]
                if len(gift) == 1:
                    for key in gift.keys():
                        print("마지막 선물 선택 가능 번호는", key,"번 입니다.")
                if len(gift) == 0:
                    break
            else:
                print("이런! 이미 친구가 1번 선물을 받았어요. 다른 선물 번호를 입력하세요")

        elif a == 2:
            if 2 in gift:
                print("당신의 선물은 맥북입니다.")
                del gift[2]
                if len(gift) == 1:
                    for key in gift.keys():
                        print("마지막 선물 선택 가능 번호는", key,"번 입니다.")
                if len(gift) == 0:
                    break
            else:
                print("이런! 이미 친구가 2번 선물을 받았어요. 다른 선물 번호를 입력하세요")

        elif a == 3:
            if 3 in gift:
                print("당신의 선물은 애플워치입니다.")
                del gift[3]
                if len(gift) == 1:
                    for key in gift.keys():
                        print("마지막 선물 선택 가능 번호는", key,"번 입니다.")
                if len(gift) == 0:
                    break
            else:
                print("이런! 이미 친구가 3번 선물을 받았어요. 다른 선물 번호를 입력하세요")

        elif a == 4:
            if 4 in gift:
                print("당신의 선물은 에어팟입니다.")
                del gift[4]
                if len(gift) == 1:
                    for key in gift.keys():
                        print("마지막 선물 선택 가능 번호는", key,"번 입니다.")
                if len(gift) == 0:
                    break
            else:
                print("이런! 이미 친구가 4번 선물을 받았어요. 다른 선물 번호를 입력하세요")

        elif a == 5:
            if 5 in gift:
                print("당신의 선물은 전동킥보드입니다.")
                del gift[5]
                if len(gift) == 1:
                    for key in gift.keys():
                        print("마지막 선물 선택 가능 번호는", key,"번 입니다.")
                if len(gift) == 0:
                    break
            else:
                print("이런! 이미 친구가 5번 선물을 받았어요. 다른 선물 번호를 입력하세요")

print("선물이 이제 없네요. ㅠㅠ. 내년 크리스마스 때 만나요!")
        
