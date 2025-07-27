#Caesar Cipher
import time

# logic flow: encrypt/decrypt | shift value | message | number sequence | shift value | letter sequence return message

#The alphabet key - after doing some reading, I know that a dictionary would be better than a list, but I have not yet learned how to use dictionaries
alphabet_key = [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6], ['g', 7], ['h', 8], ['i', 9], ['j', 10], ['k', 11], ['l', 12], ['m', 13], ['n', 14], ['o', 15], ['p', 16], ['q', 17], ['r', 18], ['s', 19], ['t', 20], ['u', 21], ['v', 22], ['w', 23], ['x', 24], ['y', 25], ['z', 26]]

#Step One: determine if we are encrypting or decrypting
plus_minus = input('How can we help: Encrypt, Decrypt, or Crack? ').strip().lower()

#Validate encrypt/decrypt input
while plus_minus not in ['encrypt', 'decrypt', 'crack']:
    plus_minus = input('Please enter "encrypt", "decrypt", or "crack": ').strip().lower()

#Step Two: get the shift value (only if not cracking)
if plus_minus != 'crack':
    shift = input('What is the Secret Shift Number? ').strip()
                  
    #Validate shift value input
    while True:
        if shift.isdigit() and int(shift) > 0 and int(shift) <= 10:
            shift = int(shift)
            break
        else:
            shift = input('Enter a whole number between 1 and 10: ').strip()

#Step Three: get the message
secret_message = input('What is the Secret Message? ').strip().lower()

#Validate the message input
secret_message_max = 200
secret_message_min = 2
while (
    not secret_message
    or len(secret_message) < secret_message_min
    or len(secret_message) > secret_message_max
    or not all(char.isalpha() or char in [' ', ',', "'", '.', '?'] for char in secret_message)
):
    print('Secret message must be between 2 and 200 characters.')
    time.sleep(1)
    print('Secret message can only contain spaces, commas, apostrophes, periods, and question marks.')
    time.sleep(1)
    secret_message = input('What is the Secret Message? ').strip().lower()

#Step Four: convert the message to a number sequence
def convert_to_number(secret_message):
    number_sequence = []
    for char in secret_message:
        if char.isalpha():
            for pair in alphabet_key:
                if char == pair[0]:
                    number_sequence.append(pair[1])
                    break
        else:
            number_sequence.append(char)
    return number_sequence

#Step Five: apply the shift value to the initial number sequence

#function to apply the encrypt shift value
def apply_encrypt_shift(initial_number_sequence, shift):
    shifted_number_sequence = []
    for number in initial_number_sequence:
        if isinstance(number, int):
            new_number = number + shift
            if new_number > 26:
                new_number -= 26
            shifted_number_sequence.append(new_number)
        else:
            shifted_number_sequence.append(number)
    return shifted_number_sequence

#function to apply the decrypt shift value
def apply_decrypt_shift(initial_number_sequence, shift):
    shifted_number_sequence = []
    for number in initial_number_sequence:
        if isinstance(number, int):
            new_number = number - shift
            if new_number < 1:
                new_number += 26
            shifted_number_sequence.append(new_number)
        else:
            shifted_number_sequence.append(number)
    return shifted_number_sequence

#Step Six: convert the shifted number sequence back to letters
def convert_to_letter(shifted_number_sequence):
    shifted_letter_sequence = []
    for number in shifted_number_sequence:
        if isinstance(number, int):
            for pair in alphabet_key:
                if number == pair[1]:
                    shifted_letter_sequence.append(pair[0])
                    break
        else:
            shifted_letter_sequence.append(number)
    return shifted_letter_sequence

#function to apply the auto-crack shift values
def auto_crack_shift(initial_number_sequence):
    cracked_messages = []
    for shift in range(1, 11):
        shifted_number_sequence = apply_decrypt_shift(initial_number_sequence, shift)
        shifted_letter_sequence = convert_to_letter(shifted_number_sequence)
        cracked_messages.append((shift, ''.join(shifted_letter_sequence)))
    return cracked_messages

# Convert message to numbers
initial_number_sequence = convert_to_number(secret_message)

#apply the shift based on the plus_minus value
if plus_minus == 'encrypt':
    shifted_number_sequence = apply_encrypt_shift(initial_number_sequence, shift)
    new_message = convert_to_letter(shifted_number_sequence)
    print('Your new message is: ' + ''.join(new_message))
    
elif plus_minus == 'decrypt':
    shifted_number_sequence = apply_decrypt_shift(initial_number_sequence, shift)
    new_message = convert_to_letter(shifted_number_sequence)
    print('Your new message is: ' + ''.join(new_message))
    
else:  # crack
    cracked_results = auto_crack_shift(initial_number_sequence)
    print("Cracked Messages:")
    for shift, message in cracked_results:
        print(f"Shift {shift}: {message}")

#Step Seven: final message
print('Thank you for using the Caesar Cipher program!')