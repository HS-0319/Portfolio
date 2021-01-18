now = int(input('현재 층: '))
hope = int(input('가는 층 입력: '))

def goUp(now, hope):
     for floor in range(now, hope+1):
          print('현재 층은', floor, '입니다.')
     print(hope,'층에 도착하였습니다. 안녕히 가세요.')

def goDown(now, hope):
     for floor in range(now, hope-1, -1):
          print('현재 층은', floor,'입니다.')
     print(hope,'층에 도착하였습니다. 안녕히 가세요.')
     
if (now == hope) or (now < 1) or (5 < hope):
     print('다른 층(1~5)을 눌러주세요.')
else:
     if now < hope:
          goUp(now, hope)
     else:
          goDown(now, hope)
