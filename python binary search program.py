a=[]
flag=0

b=int(input("입력할 수 개수:"))

for i in range(0,b,1):
    num=int(input("입력할 수를 입력하세요:"))
    a.append(num)

key=int(input("찾고자 하는 수를 입력하세요: "))

low=0
high=b-1

for i in range(0,b,1):
    if low<=high:
        mid=int((low+high)/2)

        if key==a[mid]:
            print("index 위치: ",mid)
            flag=1
            break
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1

    else:
        print("-1")
