import requests
import time
import json

def get_all_books_from_open_library(query):
    url = "https://openlibrary.org/search.json"
    books = []
    offset = 0
    limit = 100

    while True:
        params = {
            'q': query,
            'limit': limit,
            'offset': offset
        }
        response = requests.get(url, params=params)
        data = response.json()

        if 'docs' not in data or not data['docs']:
            break  # Exit if no more results are found

        books.extend(data['docs'])

        offset += limit


    return books

query = "database"
start_time = time.time()
books = get_all_books_from_open_library(query)
end_time = time.time()
execution_time = end_time - start_time
print(f"Querying {query} in {execution_time} seconds")
output_file = 'books_data.json'

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

print(f"All book data saved to {output_file}")