import pyttsx3

while True:
    request = input("请输入文本名：")
    file = request + ".txt"
    value = eval(input("语速范围为1~200（其中不包括200，值越大语速越慢）:"))
    # 初始化
    engine = pyttsx3.init()
    # 控制语速
    rate = engine.getProperty('rate')
    # 语速范围为1~200（其中不包括200，值越大语速越慢）
    engine.setProperty('rate', rate - + value)

    # 判断文本异常，异常执行设置好的内容
    try:
        # 逐行读取file文件内容
        with open(file, "r", encoding='utf-8') as f:
            d = f.readlines()
            # 打印文件名
            print(file)
            # 去除\n
            price = [x.strip() for x in d if x.strip() != ""]
            # 去除[]
            a = ",".join(price)
            print(a)
    except FileNotFoundError:
        price = request
        print(request)
    # 阅读文本
    engine.say(price)
    engine.runAndWait()

    pd = input("是否继续：")
    if pd == "否":
        break
