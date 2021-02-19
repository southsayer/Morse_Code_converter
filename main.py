morse_code = {
    "a": ".-",
    "b": "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': ".---",
    'k': "-.-",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    's': "...",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    'x': "-..-",
    'y': "-.--",
    'z': "--..",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '0': "-----",
    '/': "-..-.",
    '.': "._._._",
    ',': "--..--",
    '?': "..--..",
    "'": ".----.",
    '"': ".-..-.",
    '!': "-.-.--",
    '(': "-.--.",
    ')': "-.--.-",
    ':': "---...",
    ';': "_._._.",
    '=': "_..._",
    '+': ".-.-.",
    '-': "_...._",
    '_': "..__._",
}
list = []
sentence = input("Welcome To Morse Code Converter\n"
                 "Translate a Message\n"
                 "Enter your message below 👇\n").lower()
for letter in sentence:
    for code in morse_code:
        if letter == code:
            encoded_sentence = morse_code[code]
            list.append(encoded_sentence)
encoder = " ".join(list)
print(f"your Morse code is given below 👇 \n"
      f"{encoder}")
