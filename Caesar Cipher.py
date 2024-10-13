caesar_art = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
'''

print(caesar_art)
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

direction = input("Type 'encode' to encode and 'decode' to decode:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift:\n"))

def caesar(original_text, shift_amount,encode_or_decode):
    alpha_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alpha:
            alpha_text += letter
        else:
            shifted_position = alpha.index(letter) + shift_amount
            shifted_position %= len(alpha)
            alpha_text += alpha[shifted_position]
        print(f"Here is the encoded result: {alpha_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encode and 'decode' to decode:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to do it again. Otherwise, type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")

#for encryption
'''def encrypt(original_text, shift_amount):
    cip_text = ""

    for letter in original_text:
        shifted_position = alpha.index(letter) + shift_amount
        shifted_position %= len(alpha)
        cip_text += alpha[shifted_position]
    print(f"Here is the encoded result: {cip_text}")

encrypt(original_text= text, shift_amount=shift)'''

#for decrpytion
'''def decrypt(original_text, shift_amount):
    alpha_text = ""

    for letter in original_text:
        shifted_position = alpha.index(letter) - shift_amount
        shifted_position %= len(alpha)
        alpha_text += alpha[shifted_position]
    print(f"Here is the encoded result: {alpha_text}")

decrypt(original_text= text, shift_amount=shift)'''



