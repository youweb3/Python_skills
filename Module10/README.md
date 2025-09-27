#  Project 1

Project: Library Inventory Management
Objective:

Create a Python script that manages a library's inventory of books using lambdas, arrays, and simple OOP concepts.

Instructions:

1. Create a Book class with attributes for title, author, and availability.

2. Use an array to store the library's collection of books.

3. Implement methods to add books, search for books by title or author, and update book availability using lambdas.

4. Create instances of the Book class and test the functionality.


This project demonstrates the following concepts:

OOP: The Book and Library classes are defined to represent books and a library, respectively.
Arrays: The books attribute in the Library class is an array (list) that stores the library's collection of books.
Lambdas:
The search_by_title and search_by_author methods use lambdas to search for books based on title and author, respectively.
The update_availability method uses a lambda to update the availability of a book with a specific title.
The script creates instances of the Book class to represent individual books and an instance of the Library class to manage the library's inventory. It demonstrates adding books to the library, searching for books by title and author using lambdas, and updating book availability. Once you have your own example you can add this to your GitHub repo.


#========================================================================

# PROJECT 2

Project: Currency Converter
Objective:

Create a Python script that converts currency using exchange rates stored in a separate module, demonstrating the concept of scope and module usage.

Instructions:

1. Create a module named exchange_rates.py to store the exchange rates.

2. Define variables for exchange rates within the module.

3. Create the main script currency_converter.py that imports the exchange_rates module.

4. Define functions in the main script to convert currency based on the exchange rates from the module.

5. Demonstrate the concept of scope by accessing variables from the module and within the functions.


This project demonstrates the following concepts:

Modules: The exchange_rates.py file serves as a module that stores the exchange rates. The currency_converter.py file imports the exchange_rates module to access the exchange rate variables.
Scope: The exchange rate variables (USD_TO_EUR, USD_TO_GBP, USD_TO_JPY) are defined within the exchange_rates module and can be accessed from the currency_converter.py script using the module name as a prefix (exchange_rates.USD_TO_EUR). This demonstrates the concept of module-level scope.
The currency_converter.py script defines functions (convert_usd_to_eur, convert_usd_to_gbp, convert_usd_to_jpy) that perform currency conversions using the exchange rates from the exchange_rates module. These functions have their own local scope, and they can access the exchange rate variables from the module.

The main() function serves as the entry point of the script. It sets the USD amount, calls the conversion functions, and prints the converted amounts in EUR, GBP, and JPY. The if __name__ == "__main__": condition ensures that the main() function is only executed when the script is run directly (not when it's imported as a module).

To run the project, make sure both exchange_rates.py and currency_converter.py are in the same directory, and then execute currency_converter.py