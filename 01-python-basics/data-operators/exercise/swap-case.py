# Swap case
# Let us write a program to get an English alphabet typed by
# the user. If the user types a lower-case alphabet, the
# program should convert it to upper-case and vice versa. If
# they do not type either an uppercase or lower-case
# alphabet, we display an error message

# to change case
number = 1
alpha = input("enter an English character :").strip()

if len(alpha) != 1:
    print("error: please input exactly one character")
elif alpha >= "a" and alpha <= "z":
    y = ord(alpha)
    print(chr(y - 32))
elif alpha >= "A" and alpha <= "Z":
    y = ord(alpha)
    print(chr(y + 32))
else:
    print("invalid character")
