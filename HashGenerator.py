from colorama import Fore, init
import hashlib
import pyfiglet
import os

init(autoreset=True)

def print_header():
    print(Fore.LIGHTYELLOW_EX + ' ' + '#' * 100)
    print(Fore.LIGHTYELLOW_EX + pyfiglet.figlet_format(f' HASH GENERATOR', font='ansi_shadow'))
    print(Fore.LIGHTYELLOW_EX + ' ' + '#' * 100)

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def md5(use_string):
    if use_string:
        use_string = input(Fore.LIGHTGREEN_EX + "Input : ")
        hash_value = hashlib.md5(use_string.encode()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
        return
    file = input(Fore.LIGHTGREEN_EX + "Location: ")
    try:
        with open(file, 'rb') as f:
            hash_value = hashlib.md5(f.read()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except FileNotFoundError:
        print("Error: File Not Found!")
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except Exception as error:
        print(f"Error: {error}")
        input(Fore.LIGHTMAGENTA_EX + 'OK')

def sha256(use_string):
    if use_string:
        use_string = input(Fore.LIGHTGREEN_EX + "Input : ")
        hash_value = hashlib.sha256(use_string.encode()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
        return
    file = input(Fore.LIGHTGREEN_EX + "Location : ")
    try:
        with open(file, 'rb') as f:
            hash_value = hashlib.sha256(f.read()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except FileNotFoundError:
        print("Error: File Not Found!")
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except Exception as error:
        print(f"Error: {error}")
        input(Fore.LIGHTMAGENTA_EX + 'OK')

def sha1(use_string):
    if use_string:
        use_string = input(Fore.LIGHTGREEN_EX + "Input : ")
        hash_value = hashlib.sha1(use_string.encode()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
        return
    file = input(Fore.LIGHTGREEN_EX + "Location : ")
    try:
        with open(file, 'rb') as f:
            hash_value = hashlib.sha1(f.read()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except FileNotFoundError:
        print("Error: File Not Found!")
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except Exception as error:
        print(f"Error: {error}")
        input(Fore.LIGHTMAGENTA_EX + 'OK')

def sha224(use_string):
    if use_string:
        use_string = input(Fore.LIGHTGREEN_EX + "Input : ")
        hash_value = hashlib.sha224(use_string.encode()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
        return
    file = input(Fore.LIGHTGREEN_EX + "Location : ")
    try:
        with open(file, 'rb') as f:
            hash_value = hashlib.sha224(f.read()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except FileNotFoundError:
        print("Error: File Not Found!")
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except Exception as error:
        print(f"Error: {error}")
        input(Fore.LIGHTMAGENTA_EX + 'OK')

def sha384(use_string):
    if use_string:
        use_string = input(Fore.LIGHTGREEN_EX + "Input : ")
        hash_value = hashlib.sha384(use_string.encode()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
        return
    file = input(Fore.LIGHTGREEN_EX + "Location : ")
    try:
        with open(file, 'rb') as f:
            hash_value = hashlib.sha384(f.read()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except FileNotFoundError:
        print("Error: File Not Found!")
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except Exception as error:
        print(f"Error: {error}")
        input(Fore.LIGHTMAGENTA_EX + 'OK')

def sha512(use_string):
    if use_string:
        use_string = input(Fore.LIGHTGREEN_EX + "Input : ")
        hash_value = hashlib.sha512(use_string.encode()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
        return
    file = input(Fore.LIGHTGREEN_EX + "Location : ")
    try:
        with open(file, 'rb') as f:
            hash_value = hashlib.sha512(f.read()).hexdigest()
        print(hash_value)
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except FileNotFoundError:
        print("Error: File Not Found!")
        input(Fore.LIGHTMAGENTA_EX + 'OK')
    except Exception as error:
        print(f"Error: {error}")
        input(Fore.LIGHTMAGENTA_EX + 'OK')

options = {"1" : md5,
           "2" : sha256,
           "3" : sha1,
           "4" : sha224,
           "5" : sha384,
           "6": sha512}
while True:
    clear_screen()
    print_header()
    print(Fore.LIGHTCYAN_EX + """
    1 : File
    2 : String
    q : Quit
    """)
    mode = input(Fore.LIGHTGREEN_EX + '>>> ')
    if mode == 'q' : break
    elif mode == '1' : use_string = False
    elif mode == '2' : use_string = True
    clear_screen()
    print_header()
    print(Fore.LIGHTCYAN_EX + """
    1 : md5
    2 : sha256
    3 : sha1
    4 : sha224
    5 : sha384
    6 : sha512
    q : Quit
    """)
    command = input(Fore.LIGHTGREEN_EX + '>>> ')
    if command == 'q' : break
    func = options.get(command)
    clear_screen()
    print_header()
    if func: func(use_string)