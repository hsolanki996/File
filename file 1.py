with open ("names.txt","r")as file:
    content = sorted(content)
for i in content:
    print((i.replace("\n","")).capitalize())
