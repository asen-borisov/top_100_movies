from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")



movies = soup.find_all(name= "h3" , class_ = "title")

titles = [movie.getText() for movie in movies]



movies_list = titles[::-1]

with open("movies.txt", mode="w") as file:
    for m in movies_list:
        file.write(f"{m}\n")


