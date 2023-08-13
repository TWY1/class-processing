user_class = input("請輸入要進行處理的class：")
new_class = user_class.split(' ')

list = [new_class]
num = -1


print("-----------------------輸出分割線--------------------")

for x in range(0, len(new_class)):
    num += 1    
    out = new_class[num]
    if x != len(new_class) - 1:
        out += "."  #---$---這裡的.可更改為您想要的替換符號
    print(out, end='')
