import requests

key = "e8142ce551f1c0e693af16e960a6bdfc"
lang = "en-US"

#phrase = input("enter some keywords ")

def nowPlayingMovies():
    now_playing_address = f"https://api.themoviedb.org/3/movie/now_playing?api_key={key}&language={lang}"
    response = requests.get(now_playing_address)
    return response

def popularMovies():
    popular_address = f"https://api.themoviedb.org/3/movie/popular?api_key={key}&language={lang}"
    response = requests.get(popular_address)
    return response

def searchMovies(phrase):
    search_address = f"https://api.themoviedb.org/3/search/movie?api_key={key}&language={lang}&query={phrase}&page=1&include_adult=false"
    response = requests.get(search_address)
    return response



def printResults(response):
    data = response.json()
    for movie in data["results"]:
        print("#"*60)
        print(f'{movie["title"]} / {movie["release_date"]} ({movie["vote_average"]})')
        print(f'{movie["overview"]}')
        print("#"*60)