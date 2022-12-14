import json
import os
import traceback
from src.streams.Database_text_streams.Authors_stream import authors_stream
from src.streams.Database_text_streams.Books_stream import books_stream
from src.streams.Database_text_streams.Customers_stream import customers_stream
from src.streams.Database_text_streams.Sellers_stream import sellers_stream

# Vérification de l'existence du fichier JSON
my_json_file = "C:\\Users\\Cham\\PycharmProjects\\Library\\src\\streams\\Database_JSON_streams\\data_json_import.json"
file_exists = os.path.exists(my_json_file)
print(f"Does the file exist ? {file_exists}")

# Ouverture du fichier en UTF-8
try:
    with open(my_json_file, mode="r", encoding="utf-8") as infile:
        # Décodage et chargement du fichier JSON en Python
        parsed_file = json.load(infile)
except FileNotFoundError as file_error:
    print(f"Error_numero: {file_error.errno} - {file_error}")
    traceback.print_exc()

# Itération sur le tableau d'objets "authors" dans le fichier JSON
for attribute in parsed_file["authors"]:
    # print(f"JSON: {attribute}")
    lastname, firstname, year_of_birth, city, country, literature_language = \
        attribute["lastname"], attribute["firstname"], attribute["year_of_birth"], \
        attribute["city"], attribute["country"], attribute["literature_language"]
    # Ajout de l'auteur itéré en base de données
    authors_stream(lastname, firstname, year_of_birth, city, country, literature_language)

# Itération sur le tableau d'objets "books" dans le fichier JSON
for attribute in parsed_file["books"]:
    print(f"JSON: {attribute}")
    title, year, summary, author_firstname, author_lastname = \
        attribute["title"], attribute["year"], attribute["summary"], \
        attribute["author_firstname"], attribute["author_lastname"]
    # Ajout du livre itéré en base de données
    books_stream(title, year, summary, author_firstname, author_lastname)

# Itération sur le tableau d'objets "customers" dans le fichier JSON
for attribute in parsed_file["customers"]:
    print(f"JSON: {attribute}")
    lastname, firstname, year_of_birth, address, zip_code, city, country, language = \
        attribute["lastname"], attribute["firstname"], attribute["year_of_birth"], \
        attribute["address"], attribute["zip_code"], attribute["city"], \
        attribute["country"], attribute["language"]
    # Ajout du livre itéré en base de données
    customers_stream(lastname, firstname, year_of_birth, address, zip_code, city, country, language)

# Itération sur le tableau d'objets "customers" dans le fichier JSON
for attribute in parsed_file["sellers"]:
    print(f"JSON: {attribute}")
    name, city, country = \
        attribute["name"], attribute["city"], attribute["country"]
    # Ajout du livre itéré en base de données
    sellers_stream(name, city, country)
