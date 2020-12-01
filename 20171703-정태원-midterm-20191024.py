import turtle
print("그리고자 하는 다각형의 값을 입력하세요. (3각형 ~ 10각형만 그릴 수 있습니다.)")
n = int(input("n ="))
shape1 = ["TRIANGLE", "SQUARE"]
shape2 = ["PENTAGON", "HEXAGON", "HEPTAGON", "OCTAGON", "NONAGON","DECAGON"]
morselist = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---","-.-",".-..","--", "-.", "---", ".--.","--.-", ".-.","...","-", "..-","...-",".--","-..-","-.--","--.."]

Morse1 = ["- .-. .. .- -. --. .-.. .", "... --.- ..- .- .-. ."]
Morse2 = [".--. . -. - .- --. --- -.", ".... . -..- .- --. --- -.", ".... . .--. - .- --. --- -.", "--- -.-. - .- --. --- -.", "-. --- -. .- --. --- -.", "-.. . -.-. .- --. --- -."] 
print("1)n = ", n)
if n < 3 and n>10:
    print("본 프로그램에서는 ",n, " 각형을 그릴 수 없습니다.")
else:
    if 3<=n<=4: 
            print("받아 들인 다각형 값(", n," 에 따라 생성된 영문 메시지, 2)n = ",n,"이면 DRAW",shape1[n-3])
            print("3) 영문메시지를 Morse code로 변경한 결과 = -.. .-. .- .-- ",Morse1[n-3])
            print("6)", n,"각형 그래프를 그리기 시작합니다.")
            turtle.Screen()
            t = turtle.Pen()
            for i in range(n):
                t.forward(100)
                t.left(180-180*(n-2)/n)
            
    if 5<=n<=10:
            print("받아 들인 다각형 값(", n," 에 따라 생성된 영문 메시지, 2)n = ",n,"인 경우 DRAW",shape2[n-5])
            print("3) 영문메시지를 Morse code로 변경한 결과 = -.. .-. .- .-- ",Morse2[n-5])
            print("6)", n,"각형 그래프를 그리기 시작합니다.")
            turtle.Screen()
            t = turtle.Pen()
            for i in range(n):
                t.forward(100)
                t.left(180-180*(n-2)/n)
                

            
    
       


 
