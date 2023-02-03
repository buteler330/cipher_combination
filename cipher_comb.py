import sys,random

def en_or_decrypt():
    answer=input("encrypt[1] or decrypt[2]? (answer 1 or 2):  ")
    if answer!="1" and answer!="2":
        print("wrong argument!")
    return answer
def check_type(sentence):
    sentence=sentence.replace(" ","")
    if sentence.isalpha():
        return True
    else:
        return False
# ==============bacon
def bacon():
    def encrypt():
        print("[!] plaintext can only contain letter and space. not number or other punctuation")
        plaintext=''
        plaintext=input("plaintext: ")
        check_result=check_type(plaintext)
        if check_result!=True:
            print("wrong plaintext content")
            return 0
        plaintext_test=plaintext.replace(" ","")
        plaintext=plaintext.lower()
        # key_map=[]-----
        key_map={}
        key_source=["a","b"]
        # **因为不希望密码本里有重复部分，然后2^5=32,26个元素，很难没有，所以打算封装成函数，调用，if验证
        def gen_key_map():
                str=''
                for j in range(5):
                    index=random.randint(0,1)
                    str+=key_source[index]
                # print(str)
                return str
        # 生成随机密码本
        i=0
        while i<26:
            str=gen_key_map()
            if str in key_map.values():
                continue
            else:
                key_map[alpha[i]]=str
                # key_map.append(str)------
                i+=1
        print(key_map)
        # 转换plaintext
        trans_plain=''
        for h in range(len(plaintext)):
            if plaintext[h]==" ":
                # 防止明文最后带有空格,如果h是最后一位的小标，就结束，或者下一个还是空格的话也结束
                try:
                    if h==len(plaintext)-1:
                        break
                    elif plaintext[h+1]==" ":
                        break
                except:
                    break
                trans_plain+=" "
            else:   
                # position=alpha.index(plaintext[h])
                # trans_plain+=key_map[position]
                trans_plain+=key_map.get(plaintext[h])
                # trans_plain+=key_map[plaintext[h]]
        print(f"[trans_plain===>]{trans_plain}")
        # 生成随机cover文本
        covertext=''
        for ind in range(5*len(plaintext_test)):
            covertext+=alpha[random.randint(0,25)]
        print(f'[covertext===>]  {covertext}')
        # 生成密文
        cou=0
        covertext_count=0
        cipher=''
        while cou<len(trans_plain):
            if trans_plain[cou]==" ":
                cipher+=" "
                cou+=1
                if trans_plain[cou]=="b":
                    cipher+=covertext[covertext_count].upper()
                    cou+=1
                    covertext_count+=1
                else:
                    cipher+=covertext[covertext_count].lower()
                    cou+=1
                    covertext_count+=1
                continue
            else:
                if trans_plain[cou]=="b":
                    cipher+=covertext[covertext_count].upper()
                    cou+=1
                    covertext_count+=1
                else:
                    cipher+=covertext[covertext_count].lower()
                    cou+=1
                    covertext_count+=1
        print(f"[key map===>] {key_map}")
        print(f'[cipher===>] {cipher}')
    # --------decrypt-------:
    def decrypt():
        key_map=input("key_map: ")
        try:
            key_map=eval(key_map)
            key_map=dict(key_map)
        except:
            print("wrong key_map format")
            return 0
        cipher=input("cipher: ")
        check_result=check_type(cipher)
        if check_result!=True:
            print("wrong cipher content")
            return 0
        trans_ab=''
        plaintext=""
        cipher_i=0
        # 转换成ab形式
        while cipher_i <len(cipher):
            if cipher[cipher_i]==" ":
                trans_ab+=" "
                cipher_i+=1
            else:
                if cipher[cipher_i]<"a":
                    trans_ab+="b"
                else:
                    trans_ab+="a"
                cipher_i+=1
        print(f"[trans_cipher===>] {trans_ab}")
        # 转换成明文
        count_5=0
        #将字典中的values单分出来变成列表，因为字典中键唯一，值不唯一，所以不好索引
        key_value=list(key_map.values())
        while count_5<len(trans_ab):
            str=''
            if trans_ab[count_5]==" ":
                plaintext+=" "
                count_5+=1
                continue
            for i in range(5):
                str+=trans_ab[count_5+i]
            count_5+=5
            ind=key_value.index(str)
            plaintext+=alpha[ind]
        print(f"[plaintext===>]  {plaintext}")
    answer=en_or_decrypt()
    if answer=="1":
        res=encrypt()
        return res
    elif answer=="2":
        res=decrypt()
        return res
    else:
        continue_flag=input("retry? y/n:  ")
        if continue_flag=="y":
            bacon()
        else:
            sys.exit()
# =============virginia
def virginia():
    def encrypt():
        plaintext=input("plaintext:  ")
        key=input("key:  ")
        check_result=check_type(plaintext+key)
        if check_result!=True:
            print("wrong plaintext or key content")
            return 0
        plaintext=plaintext.lower()
        key=key.lower()
        num_key=[]
        # key转换为下标
        for char in key:
            num_key.append(alpha.index(char))
        # 转换
        cipher=""
        count=0
        key_count=0
        # 一般来说是按照长的那个在外层，但是这里可能密钥会比原文短，所以应该原文在外，但是如果原文在外，内层就不能用for,不然会导致空格时，密钥元素无法被顺移
        while count<len(plaintext):
            if plaintext[count]==" ":
                cipher+=" "
                count+=1
            else:
                cipher+=alpha[((alpha.index(plaintext[count]))+num_key[key_count%len(key)])%26]
                count+=1
                key_count+=1
        print(f"[原文:]{plaintext}")
        print(f"[密文:]{cipher}")
        print(f"[密钥:]{key}")
    def decrypt():
        cipher=input("cipher: ")
        key=input("key: ")
        check_result=check_type(cipher+key)
        if check_result!=True:
            print("wrong cipher or key content")
            return 0
        num_key=[]
        plaintext=""
        for j in key:
            num_key.append(alpha.index(j))
        # 解码
        cipher_count=0
        key_count=0
        while cipher_count<len(cipher):
            if cipher[cipher_count]==" ":
                plaintext+=" "
                cipher_count+=1
            else:
                plaintext+=alpha[((alpha.index(cipher[cipher_count]))-(num_key[key_count%len(key)])+26)%26]
                cipher_count+=1
                key_count+=1
        print(f"[plaintext===>]: {plaintext}")
    answer=en_or_decrypt()
    if answer=="1":
        res=encrypt()
        return res
    elif answer=="2":
        res=decrypt()
        return res
    else:
        continue_flag=input("retry? y/n:  ")
        if continue_flag=="y":
            virginia()
        else:
            sys.exit()
#===============caesar_cipher
def caesar():
    def encrypt():
        plaintext=input("plaintext:  ")
        key=input("key(number):  ")
        if key.isdigit()==True:  
            check_result=check_type(plaintext)
        else:
            print("wrong key")
            return 0
        key=int(key)
        if check_result!=True:
            print("wrong plaintext content")
            return 0
        cipher=''
        length=len(plaintext)
        count=0
        while count<length:
            if plaintext[count]==" ":
                cipher+=" "
                count+=1
            else:
                cipher+=alpha[(alpha.index(plaintext[count])+key)%26]
                count+=1
        print(f"[cipher===>]:{cipher}")
    def decrypt():
        cipher=input("cipher: ")
        try:
            key=eval(input('key: '))
            key=int(key)
        except:
            print("wrong key format")
            return 0
        check_result=check_type(cipher)
        if check_result!=True:
            print("wrong cipher content")
            return 0
        plaintext=""
        for word in cipher:
            if word==" ":
                plaintext+=" "
            else:
                plaintext+=alpha[(alpha.index(word))-key]
        print(f"[plaintext===>]: {plaintext}")
    answer=en_or_decrypt()
    if answer=="1":
        res=encrypt()
        return res
    elif answer=="2":
        res=decrypt()
        return res
    else:
        continue_flag=input("retry? y/n:  ")
        if continue_flag=="y":
            caesar()
        else:
            sys.exit()
# =================fence
def fence():
    def encrypt():
        plaintext=input("plaintext: ")
        if check_type(plaintext)!=True:
            print("wrong type")
            return 0
        plaintext_=plaintext.replace(" ","")
        row_list=[]
        for i in range(2,len(plaintext_)):
            if len(plaintext_)%i==0:
                row_list.append(i)
            else:
                continue
        fences=input(f"choice:{row_list} fences:  ")
        try:
            fences=int(fences)
        except:
            print("wrong type of fences")
            return 0
        trans="" 
        count=0
        while count<fences:
            for ind in range(count,len(plaintext_),fences):
                trans+=plaintext_[ind]  
            count+=1
            if count==fences:
                break
            else:
                trans+="\n"
        cipher=trans.replace("\n","")
        print(f"[trans_part===>]:\n{trans}")
        print(f"[cipher===>]: {cipher}")
    def decrypt():
        cipher=input("cipher: ")
        if check_type(cipher)==False:
            print("wrong type")
            return 0
        try:
            fences=eval(input("fences: "))
        except:
            print("wrong fences type")
            return 0
        cipher_lengeth=len(cipher)
        col_count=int(cipher_lengeth/fences)
        count=0
        str=""
        while count<col_count:
            str+=cipher[count:cipher_lengeth+1:col_count]
            count+=1
        print(f'[plaintext===>]: {str}')
    answer=en_or_decrypt()
    if answer=="1":
        res=encrypt()
        return res
    elif answer=="2":
        res=decrypt()
        return res
    else:
        continue_flag=input("retry? y/n:  ")
        if continue_flag=="y":
            fence()
        else:
            sys.exit()
# -----------------------------------------------------
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if __name__=='__main__':
    while True:
        method=input(f"virginia( v )\t\tbacon( b )\ncasear( c )\t\tfence( f )\n[answer v or b or c or f]:")
        # method=eval(method)
        if method=="v":
            inter_flag=virginia()
            if inter_flag==0:
                flag=input("use or not? y/n:  ")
                if flag=="y":
                    virginia()
                else:
                    sys.exit()
        elif method=="b":
            inter_flag=bacon()
            if inter_flag==0:
                flag=input("use or not? y/n:  ")
                if flag=="y":
                    bacon()
                else:
                    sys.exit()
        elif method=="c":
            inter_flag=caesar()
            if inter_flag==0:
                flag=input("use or not? y/n:  ")
                if flag=="y":
                    caesar()
                else:
                    sys.exit()
        elif method=="f":
            inter_flag=fence()
            if inter_flag==0:
                flag=input("use or not? y/n:  ")
                if flag=="y":
                    fence()
                else:
                    sys.exit()
        else:
            print("wrong")
            use_flag=input("use or not? y/n:  ")
            if use_flag=="y":
                continue
            else:
                break
        print("-----------------------------------------------------")
        again=input("continue? y/n  ")
        if again=="y":
            continue
        else:
            break












