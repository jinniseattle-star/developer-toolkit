import random
import string
import pyperclip

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)


pyperclip.copy(password)
print("Copied to clipboard!")
