import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Define URL
URL = "https://books.toscrape.com/"

# Step 2: Send request to website
page = requests.get(URL)

# Step 3: Parse HTML content
soup = BeautifulSoup(page.content, "html.parser")

# Step 4: Find all book elements
books = soup.find_all("article", class_="product_pod")

print("\n***Book List***")

# Step 5: Extract book information
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    print("Title:", title)
    print("Price:", price)
    print("Availability:", availability)
    print()

print("***END***")

# -----------------------------------------------------

print("\n***Available Book Element***")

# Step 6: Filter books that are in stock
available_books = []

for book in books:
    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    if "In stock" in availability:
        available_books.append(book)

# Step 7: Count number of available books
print("Number of elements:", len(available_books))

# Step 8: Display filtered books
for book in available_books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    print(title)
    print(price)
    print()

print("***END***")

#Save data into CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability"])

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        writer.writerow([title, price, availability])
