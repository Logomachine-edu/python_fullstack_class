def reverse_string(text):
    text_reverse = text[::-1]
    text_split = text_reverse.split()
    text_split1 = text_split[::-1]

    print(" ".join(text_split1))


reverse_string("Hello World")
reverse_string("Python")
