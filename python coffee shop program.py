price=[]

print("<메뉴>")
print("1.아메리카노 3000원")
print("2.카페라떼 3500원")
print("3.카페모카 3800원")
print("4.종료")

while True:
    a = int(input("번호 선택: "))
    if a==1:
        b = int(input("몇 잔? "))
        c = 3000 * b
        price.append(c)
    elif a==2:
        d = int(input("몇 잔? "))
        e = 3500 * d
        price.append(e)
    elif a==3:
        f = int(input("몇 잔? "))
        g = 3800 * f
        price.append(g)
    elif a==4:
        if sum(price) >= 20000:
            discount_price = sum(price) * 0.1
            final_price = sum(price) * 0.9
            print("총액: ",sum(price))
            print("할인액: ",discount_price)
            print("결제액: ",final_price)
            break
        else:
            print("총액: ",sum(price))
            print("할인액: 0")
            print("결제액: ",sum(price))
            break
        
