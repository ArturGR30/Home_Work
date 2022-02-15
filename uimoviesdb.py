# using interface for json_moviesdb_API
from os import system

def clear():
    system("cls")

def printMenu():
    print("#"*50)
    print("# 1. Show latest movies")
    print("# 2. Show popular movies")
    print("# 3. Search a movies")
    print("# 0. Exit")
    print("#"*50)
    option = int(input(">>> "))
    return option

def wait():
    input("Hit enter to continue ... ")
