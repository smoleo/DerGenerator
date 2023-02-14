import eel
import random

line1=[]
line2=[]
line3=[]

    
eel.init("web")

@eel.expose
def generateNames():
    names=[]
    for i in range(15):
        names.append(str(random.choice(line1))+str(random.choice(line2))+str(random.choice(line3)))
    return names

@eel.expose
def addToWords(w1,w2,w3):
    print(w1,w2,w3)
    if(w1!=""):
        line1.append(w1)
        print("w1 changed")
    if(w2!=""):
        line2.append(w2)
        print("w2 changed")
    if(w3!=""):
        line3.append(w3)
        print("w3 changed")
        
    f = open("input.txt", "w",encoding='utf-8')
    for i in line1:
        f.write(i+",")
    f.write("\n")
    for i in line2:
        f.write(i+",")
    f.write("\n")
    for i in line3:
        f.write(i+",")
    f.write("\n")
    f.close()

         
def prepareLine(line):
    words=line.split(",")
    for i in range(len(words)):
        try:
            if(words[i][-1]!=" "):
                words[i]=words[i]+" "
        except:
            pass
    return words

with open("input.txt",encoding='utf-8') as f:
    line1 = prepareLine(u""+f.readline())
    line1.pop()
    line2 = prepareLine(u""+f.readline())
    line2.pop()
    line3 = prepareLine(u""+f.readline())
    line3.pop()

    
eel.start("index.html")
