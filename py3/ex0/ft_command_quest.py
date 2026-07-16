from sys import argv

if __name__ == "__main__":
    print("=== Command Quest ===")
    size = len(argv)
    counter = 1
    if size == 1:
        print(f"Program name: {argv[0]}")
        print("No arguments provided!")
        print(f"Total arguments: {size}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {size - 1}")
        while counter < size:
            print(f"Argument {counter}: {argv[counter]}")
            counter += 1
        print(f"Total arguments: {size}")