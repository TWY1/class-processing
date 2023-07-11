user_class = input("請輸入要進行處理的class：")
new_class = user_class.split(' ')

list = [new_class]
num = -1


print("-----------------------輸出分割線--------------------")

for x in range(0, len(new_class)):
    num += 1    
    out = new_class[num]
    if x != len(new_class) - 1:  #當x 不是等於len(b) 記得減掉 - 1 的時候就執行這些下面.這個程式但是如果當x 等於 len(b) - 1 的時候那這樣判斷條件就不達成所以就不會繼續執行 因為這個判斷條件是要不成立的情況下才會執行
        out += "."  #---$---這裡的.可更改為您想要的替換符號
    print(out, end='')