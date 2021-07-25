studentDB = {}

while True:
    print("================\n1)추가 2)삭제 3)수정\n4)조회 5)종료\n================")
    selected = int(input("원하시는 기능을 선택하세요: "))
    print("================")

    if selected==1:
        a = input('이름을 입력하세요:')
        b = input('나이를 입력하세요:')
        c = input('학번을 입력하세요:')
        d = input('학과명을 입력하세요:')
        studentDB[a] = [b, c, d]

    elif selected==2:
        a = input('이름을 입력하세요:')
        del studentDB[a]

    elif selected==3:
        a = input('이름을 입력하세요:')
        del studentDB[a]
        b = input('나이를 입력하세요:')
        c = input('학번을 입력하세요:')
        d = input('학과명을 입력하세요:')
        studentDB[a]=[b, c, d]

    elif selected == 4:
        a = input('이름을 입력하세요:')
        if a in studentDB:
            print(studentDB[a])
        else:
            print("그런 값은 없습니다.")


    elif selected == 5:
        break;

    else:
        print("1~5중에 하나를 입력하세요.")
