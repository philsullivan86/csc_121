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


def add_book():
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    # your code here
    title = input("Title?")
    author = input("Author?")
    pages = int(input("Pages?"))
    hours = estimate_reading_time(pages)
    # use an f-string to print "'{title}' by {author} -- approx. {hours} to read"
    print(f"'{title}' by {author} -- approx. {hours} to read")



def main():
    dashboard()
    add_book()


if __name__ == "__main__":
    main()