# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = int(input("Number of class:-"))
    n = list(map(int, input("elements of array:-").strip().split()))
    # print(n)
    # tes_aray = [1,5,7]
    print(n)
    n.sort()
    print(n)
    for x in range(len(n)):
        print(n[x])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
