answer = input("好きな食べ物は？\n")

with open("challenge9-2.txt", "w", encoding="utf-8") as f:
    f.write(answer)
