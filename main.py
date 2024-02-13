print("Hello world")

with open("initial.txt", "w") as file:
    file.write("To be, or not to be, that is the question, "
               "Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, "
               "Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; "
               "No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, "
               "'tis a consummation Devoutly to be wish'd. To die, to sleep.")

with open("initial.txt", "r") as file:
    text_from_file = file.read()

print(text_from_file)
print(len(text_from_file.split()))
words = re.findall(r"\w{7,}", text_from_file)

with open("final.txt", "w") as file:
    file.write(" ".join(words))


with open('initial.txt', "r") as file:
    text = file.read()

restricted_word = "die"
print(text)
print(text.count(restricted_word))
text = text.replace(restricted_word.lower(), "*" * len(restricted_word))
print(text)

