import random
import string

length = 16

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)
