#ISSN 번호 검증 프로그램입니다.
#5개의 issn 코드를 받아오기
Issnlist = []#issn list
print(Issnlist)
first_num = input("ISSN 8자리를 입력하세요. (\"-\" 제외) :")#1번째 ISSN
if len(first_num) != 8: print("입력하신", first_num," 은 잘못된 번호입니다.")
    second_num = input("ISSN 8자리를 입력하세요. (\"-\" 제외) :")
if len(second_num) != 8: print("입력하신", first_num," 은 잘못된 번호입니다.")
    third_num = input("ISSN 8자리를 입력하세요. (\"-\" 제외) :")
if len(third_num) != 8: print("입력하신", first_num," 은 잘못된 번호입니다.")
    fourth_num = input("ISSN 8자리를 입력하세요. (\"-\" 제외) :")
if len(fourth_num) != 8: print("입력하신", first_num," 은 잘못된 번호입니다.")
    fifth_num = input("ISSN 8자리를 입력하세요. (\"-\" 제외) :")
if len(fifth_num) != 8: print("입력하신", first_num," 은 잘못된 번호입니다.")

#List 에 ISSN 넘버 추가하기
Issnlist.append(first_num)
Issnlist.append(second_num)
Issnlist.append(third_num)
Issnlist.append(fourth_num)
Issnlist.append(fifth_num)
#echo checking
print(Issnlist)
#역순으로 issn code를 추출하여 검증하기

i = -1 #인덱스에 -1를 집어넣어 추출하면 pop을 쓰지않고 뒤에서 엘리먼트를 가져온다.
while True: #역순 추출
    Issn_num = Issnlist[i]
    fullamount = 0 #가중치 변수 생성
    for j in range(7):
        
        amount=int(Issn_num[j])*(8-j)
        fullamount += amount
    print(fullamount)#echo checking
    a = fullamount%11
    check_num=11 - a
    if (check_num == 10 and str(Issn_num[-1]) == 'X') or (check_num == 11 and str(Issn_num[-1]) == 'O') :
        print("ISSN CODE", Issn_num,"는 검증되었습니다.")
    else:
        print("ISSN CODE", Issn_num,"는 검증되지않았습니다.")    
     
    del Issnlist[i] #검증한 Issn 제거
    if Issnlist == []:
        break
    else:
        continue
print(fullamount)    
        
    
    


 


