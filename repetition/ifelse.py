#if else
is_male = True
is_tall = False

if is_tall and is_male:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a man but not tall")
elif not(is_male) and is_tall:
    print("you are tall but not a man")
else:
    print("you are neither male or tall")