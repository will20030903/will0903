old = int(input("請輸入年齡:"))

if old < 20:
    print("嗨！小朋友")
    import sys
    sys.exit(0)

if old >= 50:
    print("不尚賢，使民不爭；不貴難得之貨，使民不為盜；不見可欲，使心不亂。")
    print("是以聖人之治，虛其心，實其腹，弱其志，強其骨。常使民無知無欲。")
    print("使夫知者不敢為也。為無為，則無不治。")
    print("看不懂正常因為你太老了")
    import sys
    sys.exit(0)

if old < 50 and old >= 20:
    print("嗨！年輕人")
gender = int(input("請輸入性別: 男性---打1 女性---打2 "))
single = int(input("請輸入感情狀態:(單身---打1 or 非單身---打2 "))
if gender == 1 and single == 1:
    print("單身狗")
    import sys
    sys.exit(0)
elif gender == 1 and single == 2:
    print("有前途")
    import sys
    sys.exit(0)
elif gender == 2 and single == 1:
    print("沒人愛的可憐仔")
    import sys
    sys.exit(0)
elif gender == 2 and single == 2:
    print("嗨! 大嬸")
    import sys
    sys.exit(0)

