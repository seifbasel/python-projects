alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_amount):
    encrypted_text = ""
    for letter in plain_text:
       position = alphabet.index(letter)
       new_postion = position + shift_amount
       new_letter = alphabet[new_postion]
       encrypted_text += new_letter
    print(f"the encrybted text is {encrypted_text}")
    

def decryption(plain_text, shift_amount):
    unencrypted_text = ""
    for letter in plain_text:
       position = alphabet.index(letter)
       new_postion = position - shift_amount
       new_letter = alphabet[new_postion]
       unencrypted_text +=new_letter
    print(f"the unencrypted text text is {unencrypted_text}")
    
direction = input("Type 1 for 'encode' to encrypt, type 2 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "1":
  encryption(text,shift)
elif direction == "2":
  decryption(text,shift)
