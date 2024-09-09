def add_everything_up(a, b):
    try:
        c = round(a + b, 3)
        return c
    except TypeError:
        a = str(a)
        b = str(b)
        c = a + b
        return c

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
