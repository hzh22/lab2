def Get_keyword_num():
    key_word=["auto","break","case","char","const","continue","default","do",
              "double","else","enum","extern","float","for","goto","if",
	          "int","long","register","return","short","signed","sizeof","stastic",
	          "struct","switch","typedef","union","unsigned","void","volatile","while"]
    num = 0
    store={}
    file = open("code.txt", "r", encoding='utf-8')
    while(1):
        lines=file.readlines()
        for line in lines:
            ine = line.replace(",","").replace(".","").replace("{"," ").replace("}"," ").replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
            count = line.split()
            for word in count:
                if len(word) < 2:
                    continue
                else:
                    store[word] = store.get(word, 0) + 1
        for key in list(store.keys()):
            if key not in key_word:
                del store[key]

        if not lines:
            break

        for key in store:
            if key in key_word:
                num = num + store[key]

        print("total num: ", num)
        print("switch num: ", store['switch'])
        file.close()
        return

def Get_switchcase_num(count):
    store = []
    store_1=[]
    store_2=[]
    for word in count:
        if word == "switch":
            store.append(word)
        if word == "case":
            store.append(word)
    return store
    cun =0
    sum = 0
    store_1.reverse()
    for word in store_1:
        if word == "case":
            cun = cun+1
        if word == "switch":
            if cun != "0":
                store_2.append(cun)
            cun = 0
            sum = sum + 1
    store_2.reverse()

    line_1 = " ".join(count)
    if line_1.find("else if") != -1:
        lay_1.append('1')
    elif line_1.find("if") != -1:
        lay_1.append('0')
    elif line_1.find("else") != -1:
        lay_1.append('2')
    else:
        continue