import random
text=input("write your friendes name-->")
print(text)
text_split=text.split(" ")
print(text_split)

random_person=random.randint(0,len(text_split)-1)
person=text_split[random_person]
print(f"person {person} will pay the bill")