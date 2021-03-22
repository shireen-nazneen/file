pepole=open("question3.txt","r")
pepole=pepole.read()
s=pepole.split("\n")
i=0
pepole_d=open("delhi.txt","w")
pepole_shi=open("shimla.txt","w")
pepole_o=open("other.txt","w")
while i<len(s):
    if "delhi" in  s[i]:
        pepole_d.write(s[i])
        pepole_d.write("\n")
    elif "shimla" in s[i]:
        pepole_shi.write(s[i])
        pepole_shi.write("\n")
    else:
        pepole_o.write(s[i])
        pepole_o.write("\n")
    i=i+1
pepole_d.close()
pepole_d=open("delhi.txt", "r")
a=pepole_d.readlines()
print(a)
pepole_d.close()
pepole_shi.close()
pepole_shi=open("shimla.txt","r")
b=pepole_shi.readlines()
print(b)
pepole_shi.close()
pepole_o.close()
pepole_o=open("other.txt","r")
c=pepole_o.readlines()
print(c)
pepole_o.close()
