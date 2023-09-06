user_input = int(input())

if user_input > 1:
    print("A long time ago in a galaxy " + ("far, " * (user_input - 1)) +
        "far away...")
else:
    print("A long time ago in a galaxy far away...")
