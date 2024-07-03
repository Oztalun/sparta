import random



restart = 'y'
best = -1
check = ['n', "N", "아니요", "아니", "y", "Y", "네"]  # 다시 할지 안할지 물어볼때 양식 맞는지 비교용
while restart not in check[0:4]:
    if best!=-1:
        print(f'최고기록은 {best}번 입니다.')
    computer = random.randint(1, 100)
    time = 0
    answer = 0
    while answer!=computer:
        error = True
        while error:
            try:
                answer = int(input("숫자를 입력해 주세요 : "))
                if answer <= 0 or answer > 100:
                    print('유효 범위 밖입니다. \n1~100까지의 숫자만 입력 해 주십시오.')
                else:
                    error = False
            except ValueError:
                print("문자를 입력하지 말아주세요.")
                error = True
        if answer>computer:
            print('down')
        elif answer<computer:
            print("up")
        time+=1
        # print(answer,computer)
    print(f'정답입니다\n{time}번 시도하셨습니다')
    if best>time or best==-1:
        best=time
    restart = input('다시 하시겠습니까? (y/n) : ')
    while restart not in check:
        print('양식에 맞게 입력 해 주세요')
        restart = input('다시 하시겠습니까? (y/n) : ')