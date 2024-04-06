from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.goodreads.com/book/show/52867387-beach-read'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

title = []
authors = []
avg_ratings = []
rating_counts = []
review_counts = []
year = []

try:
    book_title = soup.find("h1", class_="Text__title1").text
    author = soup.find('span', class_ ='ContributorLink__name').text
    avg_rating = soup.find('div', class_='RatingStatistics__rating').text
    num_ratings = soup.find('span', attrs={'data-testid': 'ratingsCount'}).text.split()[0]
    num_reviews = soup.find('span', attrs={'data-testid': 'reviewsCount'}).text.split()[0]
    published_year = soup.find('p', attrs={'data-testid': 'publicationInfo'}).text.split()[-1]

    title.append(book_title)
    authors.append(author)
    avg_ratings.append(avg_rating)
    rating_counts.append(num_ratings)
    review_counts.append(num_reviews)
    year.append(published_year)

except AttributeError:
    print("Data was not found")




good_reads = pd.DataFrame({
    "Title": title,
    # "URL": url_list,
    "Authors": authors,
    "Avg Ratings": avg_ratings,
    "Number of Ratings": rating_counts,
    "Number of Reviews": review_counts,
    "Published_year": year
})

good_reads.to_csv('goodreads.csv')
