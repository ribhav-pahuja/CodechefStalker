from bs4 import BeautifulSoup
import requests
username = input("Enter the username you want to query: ")
url = "https://www.codechef.com/users/" + username
r = requests.get(url)
soup = BeautifulSoup(r.content,"html5lib")
rating_div = soup.findAll("div",attrs={"class":"rating-number"})
try:
    rating = rating_div[0]
    print(rating.text)
except IndexError :
    print("Please Enter a valid username.")
