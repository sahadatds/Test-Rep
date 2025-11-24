def generate_random_number():
    x = id(0)
    x = id(x)
    x = str(x)[2]
    return x

print(generate_random_number())