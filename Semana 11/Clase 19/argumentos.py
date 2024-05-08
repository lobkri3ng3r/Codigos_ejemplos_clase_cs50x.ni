from sys import argv, exit

if len(argv) != 2:
    print(len(argv))
    print("Demasiados argumentos")
    exit(1)

print(argv[1])
exit(0)

# nombre = "Michael"

# for i in nombre:
#     print(i)