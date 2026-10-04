def dashboard():
    """Prints  
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """
    # your code here
    print("========================================")
    print("📚  YOUR LIBRARY")
    print("========================================")



def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour. 
    This number should be rounded to 1 decimal place"""
    # your code here
    return round(pages / 40, 1)


def add_book(library):
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    # your code here
    title_input = input("Book title: ")
    author_input = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)
    title = title_input.strip().title()
    author = author_input.strip().title()
    book = {
        "title": title,
        "author": author,
        "pages": pages,
        "hours": hours
    }
    library.append(book)
    # use an f-string to print "'{title}' by {author} -- approx. {hours} to read"
    print(f"""Book added: 
    
    '{title}' by {author} -- approx. {hours} hours to read""")

def view_books(library):
    if not library:
        print(f"Your library is empty. Add a book first!")
    else:
        for books in range(len((library))):
            print(f"{books + 1}.  '{library[books].get("title")}' - {library[books].get("author")} ({library[books].get("pages")} - approx. {library[books].get("hours")} hours to read)")
        
def show_menu():
    print(f"""
    What would you like to do?

    1) View books
    2) Add a book

    q) Quit
    
    """)

    user_input = input("> ")
    return user_input.strip().lower()


def main():
    library = []
    dashboard()

    while True:
        menu_input = show_menu()
        match menu_input:
            case "1":
                view_books(library)
            case "2":
                add_book(library)
            case "q" | "quit" | "exit":
                print(f"Goodbye!")
                break
            case _:
                print(f"Sorry, that option isn't available.")



if __name__ == "__main__":
    main()