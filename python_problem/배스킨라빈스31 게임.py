num=0
inputNum = 0
while True:
    inputNum = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
    if type(inputNum) != int:
        print('정수를 입력하세요')
        continue
    if inputNum != 1 and inputNum != 2 and inputNum != 3:
        print('1, 2, 3 중 하나를 입력하세요')
        continue
    break