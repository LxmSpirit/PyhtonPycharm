import random
import string
import requests
import browser_cookie3


#value = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#print(value)

#print(type(value))



url = "https://www.cde.org.cn/main/xxgk/getCliniCalList"


session = requests.session()

cookies = session.get(url).cookies.get_dict()


print(cookies)


dict1 = browser_cookie3.chrome(domain_name='www.cde.org.cn')

print(dict1)
print(type(dict1))


cc=[]
s=""
for u in dict1:
    print(u.name)
    print(u.value)
    #cc.append(u)
    s = s+""+u.name+"="+u.value+"; "

#s = ("Cookie: "+s)
print(s)
cc.append(s.split(";"))
#print(cc)
print(cc)
#ss = cc[0]+";"+cc[1]
print("!!!!!!!!!")
print(cc[0])




