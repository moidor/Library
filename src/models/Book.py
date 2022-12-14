class Book:
    def __init__(self, title, year, summary):
        self.title = title,
        self.year = year,
        self.summary = summary

    def introduce_book(self, title, year):
        print(f"{title.upper()} has been published in {year}.")

    def summarize(self, title, year, summary):
        # Retravailler la longueur et l'affichage du résumé
        print(f"Summary of {title.upper()}, {year}: \n"
              f"{summary}")

    def list_books_by_year(self, title, year):
        return f"Books published in {year}: \n{title}."

    # def list_books_by_year(self, title, year, author_firstname, author_lastname):
    #     print(f"Books published in {year} : \n"
    #           f"{title} - by {author_firstname} {author_lastname}.")
