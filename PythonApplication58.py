studentDB = {} # studentDB라는 빈 딕셔너리 생성

while True: # while문으로 무한 반복
    print("================\n1)추가 2)삭제 3)수정\n4)조회 5)종료\n================")
    selected = int(input("원하시는 기능을 선택하세요: "))
    print("================") # 안내문 출력하기

    if selected==1: # 만약, selected가 1이라면
        a = input('이름을 입력하세요:') # 사용자로부터 이름 입력받기
        b = input('나이를 입력하세요:') # 사용자로부터 나이 입력받기
        c = input('학번을 입력하세요:') # 사용자로부터 학번 입력받기
        d = input('학과명을 입력하세요:') # 사용자로부터 학과명 입력받기
        studentDB[a] = [b, c, d] # a를 키 값으로 하고 리스트 [b, c, d]를 밸류 값으로 하는 요소를 딕셔너리 studentDB에 추가하기

    elif selected==2: # 만약, selected가 1이 아니고 2라면
        a = input('이름을 입력하세요:') # 사용자로부터 이름 입력받기
        del studentDB[a] # a를 키 값으로 하는 요소를 딕셔너리 studentDB에서 삭제하기

    elif selected==3: # 만약, selected가 1이 아니고 2도 아니고 3이라면
        a = input('이름을 입력하세요:') # 사용자로부터 이름 입력받기
        del studentDB[a] # a를 키 값으로 하는 요소를 딕셔너리 studentDB에서 삭제하기
        b = input('나이를 입력하세요:') # 사용자로부터 나이 입력받기
        c = input('학번을 입력하세요:') # 사용자로부터 학번 입력받기
        d = input('학과명을 입력하세요:') # 사용자로부터 학과명 입력받기
        studentDB[a]=[b, c, d] # a를 키 값으로 하고 리스트 [b, c, d]를 밸류 값으로 하는 요소를 딕셔너리 studentDB에 추가하기

    elif selected == 4: # 만약, selected가 1이 아니고 2도 아니고 3도 아니고 4라면
        a = input('이름을 입력하세요:') # 사용자로부터 이름 입력받기
        if a in studentDB: # 만약, a를 키 값으로 하는 요소가 딕셔너리 studentDB 안에 있다면
            print(studentDB[a]) # a를 키 값으로 하는 밸류 값들을 출력하기
        else: # 만약, a를 키 값으로 하는 요소가 딕셔너리 studentDB 안에 없다면
            print("그런 값은 없습니다.") # 출력하기


    elif selected == 5: # 만약, selected가 1이 아니고 2도 아니고 3도 아니고 4도 아니고 5라면
        break; # 반복문 빠져 나가기

    else: # 만약, selected가 1이 아니고 2도 아니고 3도 아니고 4도 아니고 5도 아니라면
        print("1~5중에 하나를 입력하세요.") # 출력하기
