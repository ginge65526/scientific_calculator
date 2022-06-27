import random
import string

'''func = {"int": int, "float": float}
input_float = func[g](input(format_text(prompt)))'''
# ______________________________________________________________________________________
digits = string.digits
letter_digit_list = list(string.digits + string.ascii_letters)
random.shuffle(letter_digit_list)

sample_str = "".join((random.choice(digits) for i in range(4)))

sample_str += "".join((random.choice(letter_digit_list) for i in range(6)))

alist = list(sample_str)
random.shuffle(alist)

final_str = "".join(alist)
print("Random String", final_str)
