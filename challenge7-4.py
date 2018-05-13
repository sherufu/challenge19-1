answers = [10, 25, 50]

while True:
    answer = input("> ")
    if answer == "q":
        break
    try:
        answer = float(answer)
        if answer in answers:
            print("正解")
        else:
            print("不正解")
    except:
        print("数字を入力するか、qで終了します")
