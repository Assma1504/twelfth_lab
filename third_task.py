#I'll try to create file by my self and write there all words
from pathlib import Path

myFileEnRu = Path("en-ru.txt")
myFileRuEn = Path("ru-en.txt")

if Path(myFileEnRu).exists():
    myFileEnRu.write_text("cat - кошка \ndog - собака\nhome - дом\nto do - делать\nto make - изготавливать\nmouse - мышь, манипулятор мышь", encoding="utf-8")
else:
    myFileEnRu.touch()
    myFileEnRu.write_text("cat - кошка \ndog - собака\nhome - дом\nto do - делать\nmouse - мышь\nto make – изготавливать", encoding="utf-8")

with open(myFileEnRu, encoding="utf-8") as file:
    lines = file.readlines()

newDictionary = {}
for line in lines:
    splitedLine = line.strip().split("-")
    newDictionary[splitedLine[1]] = splitedLine[0]

sortedDictionary = {key : newDictionary[key] for key in sorted(newDictionary)}
for key in sortedDictionary:
    print(f"{key} - {sortedDictionary[key]}")

with open(myFileRuEn, "w", encoding="utf-8") as file:
    for key in sortedDictionary:
        file.write(f"{key} - {sortedDictionary[key]} \n")


