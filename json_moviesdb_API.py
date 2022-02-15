# Working with JSON APIs in Python
# The Movie Database

from moviesdb import*
from uimoviesdb import*

while True:
    clear()
    option = printMenu()
    if option == 1:
        printResults(nowPlayingMovies())
        wait()     
    elif option == 2:
        printResults(popularMovies())
        wait()
    elif option == 3:
        phrase = input("enter movies name  ")
        printResults(searchMovies(phrase))
        wait()
    elif option == 0:
        printMenu()

         

