s_url_length = 7
s_url_dict={}
f_url_dict={}
co=0
def Converter(s):
    dic={}
    for j in range(len(s)):
        dic[j]=s[j]
    return dic

base62=Converter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
def genShortURL(fullURL):
    if (fullURL in f_url_dict):
        print("ShortURL already Exists"+f_url_dict[fullURL])
        return
    global co
    s=""
    k=co
    co+=1
    if (k==0):
        s="0000000"
        if (s not in s_url_dict):
            s_url_dict[s]=fullURL
            f_url_dict[fullURL]=s
            print("short url for "+fullURL+" is https://ca.ke/"+s)
            return
    while(k!=0):
        s=base62[k%62]+s
        k=k//62
    l=len(s)
    if (l<s_url_length):
        for i in range(s_url_length-l):
            s="0"+s
    if (s not in s_url_dict):
        s_url_dict[s]=fullURL
        f_url_dict[fullURL]=s
    print("short url for "+fullURL+" is https://ca.ke/"+s)

while (True):
    print("Enter \n\t1) generate ShortURL\n\t2)redirect ShortURL")
    userInput=int(input())
    if (userInput==""):
        fullURL=input("Enter an URL to shorten it : ")
        genShortURL(fullURL)
    elif (userInput==2):
        shortURL=input("Enter a short url: ")
        if short_url_dict.get(shortURL,None) is not None:
            print("redirecting to "+short_url_dict[shortURL])
        else:
            print("Doesn't exist")
    else:
        print("Invalid Input")