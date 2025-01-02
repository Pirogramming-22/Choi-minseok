import random

def brGame():
    num=0
    playerFlag=0
    player = 'computer'
    inputNum=0
    while num!=31:
        if player == 'computer':
            inputNum = random.randint(1,3)
        else:
            while True:
                inputNum = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
                if type(inputNum) != int:
                    print('정수를 입력하세요')
                    continue
                if inputNum != 1 and inputNum != 2 and inputNum != 3:
                    print('1, 2, 3 중 하나를 입력하세요')
                    continue
                break
        while inputNum>0:
            num+=1
            print(f"{player} : {num}")
            inputNum-=1
            if num==31:
                break
        
        playerFlag+=1
        if playerFlag%2==0:
            player='computer'
        else:
            player='player'
        if num==31:
            print(f'{player} win!')
            break



