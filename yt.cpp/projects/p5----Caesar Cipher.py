#e(x)=(x+n)mod26--->encription
#d(x)=(x-n)mod26--->description

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encript_fun(text_line,key):
    chifer_text=""
    for i in text_line:
        position=alphabet.index(i)
        new_position=(position+key)%26
        chifer_text+=alphabet[new_position]
    print(f"the encript message is ------->{chifer_text}")

def decript_fun(chifer_text,key):
    plane_line=""
    for i in chifer_text:
        position=alphabet.index(i)
        new_position=(position-key)%26
        plane_line+=alphabet[new_position]
    print(f"the decript message is --------->{plane_line}")    

exit=False
while not exit:
   user=input("enter the encript ot the decript-------->")
   text=input("ente the message-------->")
   key=int(input("entr the shift key---------->"))

   if user=="encript":
      encript_fun(text_line=text,key=key)
   elif user=="decript":
      decript_fun(chifer_text=text,key=key)
   else:
      print("invild option")
   v=input("say me that you want to countinue yes or no------->")
   if v=="no":
      exit=True


