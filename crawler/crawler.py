import requests
import time
import os
import concurrent.futures

# Define the base URL
base_url = "https://taaghche.com/book/"

# Define the range of IDs
start_id = 210000
end_id = 400000

# Directory to save the HTML files
output_dir = 'book_pages'
os.makedirs(output_dir, exist_ok=True)


# Function to download and save the page content
def save_page(book_id, thread_exceptions):
    url = f"{base_url}{book_id}/"
    try:
        response = requests.get(url)

        if response.status_code == 404:
            print(book_id," : 404")
            # thread_exceptions.append(book_id)
            return

        with open(os.path.join(output_dir, f"{book_id}.html"), 'w', encoding='utf-8') as f:
            print(f'Saving book with id: {book_id}')
            f.write(response.text)
    except Exception as e:
        print(e)
        thread_exceptions.append(book_id)


# Function to process a range of IDs
def process_range(start, end, thread_exceptions, modulus=4):
    for book_id in range(start, end + 1, modulus):
        print("Processing ", book_id)
        save_page(book_id, thread_exceptions)
        # Add a small delay to avoid overwhelming the server
        time.sleep(0.1)


# Create a thread pool with 4 threads
num_threads = 6
exceptions_list = [[] for _ in range(num_threads)]

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for i in range(num_threads):
        thread_start_id = start_id + i

        futures.append(executor.submit(process_range, thread_start_id, end_id, exceptions_list[i], num_threads))

    # Wait for all threads to complete
    concurrent.futures.wait(futures)

# Merge all exception lists into one
exceptions = [ex for sublist in exceptions_list for ex in sublist]

# Save the list of exceptions to a file
with open('exceptions.txt', 'w') as f:
    for ex in exceptions:
        f.write(f"{ex}\n")
