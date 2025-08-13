import random

def room_1_riddle():
    print("\n Room 1: The Riddle Gate")
    print("Riddle: I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?")
    answer = input("Your answer: ").strip().lower()
    return answer == "echo"

def room_2_recursion():
    print("\nRoom 2: The Code Lock")
    print("You must generate the nth term of a recursive sequence: F(n) = F(n-1) + F(n-2), with F(0)=1, F(1)=1")
    try:
        n = int(input("Enter n (5–15): "))
        def fib(x):
            return 1 if x <= 1 else fib(x-1) + fib(x-2)
        print(f"F({n}) = {fib(n)}")
        return True
    except:
        return False

def room_3_memory():
    print("\nRoom 3: The Memory Vault")
    print("You’re given two variables: a = [1, 2, 3], b = a. Then b.append(4). What is a?")
    answer = input("Your answer (as a list): ").strip()
    return answer.replace(" ", "") == "[1,2,3,4]"

def room_4_bitwise():
    print("\n Room 4: The Bitwise Barrier")
    print("Decode this: What is the result of 13 ^ 7?")
    answer = input("Your answer: ").strip()
    return answer == str(13 ^ 7)

def room_5_padding():
    print("\n Final Room: The Padding Portal")
    print("You must align memory blocks. If a struct has a char (1 byte), int (4 bytes), and double (8 bytes), what’s the total size with padding?")
    print("Hint: Assume standard alignment rules.")
    answer = input("Your answer (in bytes): ").strip()
    return answer == "16"

def escape_room():
    print("Welcome to the Algorithmic Asylum")
    print("Solve each puzzle to escape. Fail one, and you're trapped forever... or until you rerun the program ")

    if not room_1_riddle():
        print("The riddle mocks your intellect. You're trapped.")
        return
    if not room_2_recursion():
        print("The code lock rejects your logic. You're trapped.")
        return
    if not room_3_memory():
        print("The memory vault scrambles your thoughts. You're trapped.")
        return
    if not room_4_bitwise():
        print("The bitwise barrier fries your circuits. You're trapped.")
        return
    if not room_5_padding():
        print("The padding portal misaligns your fate. You're trapped.")
        return

    print("\nCongratulations! You've escaped the Algorithmic Asylum with your wit intact!")

escape_room()
