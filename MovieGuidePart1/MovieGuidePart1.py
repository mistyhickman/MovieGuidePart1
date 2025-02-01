# ========================================
# Misty Hickman
# CIS 261
# Lab: Movie Guide Part 1
# ========================================

# Step 1: Create an empty list to store movies
movies = []

# Step 2: Create the menu display function
def show_menu():
    """Display the menu options for the user."""
    print("\nThe Movie List Program")
    print("=" * 12)
    print("COMMAND MENU")
    print("list  - List all movies")
    print("add   - Add a movie")
    print("del   - Delete a movie")
    print("exit  - Exit program")

# Step 3: Create the function to list all movies
def list_movies():
    """Display all movies in the list with numbers."""
    print("\nMovies:")
    if movies:
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie}")
    else:
        print("No movies in the list yet.")
    show_menu()



# Step 4: Create the function to add a movie
def add_movie():
    """Get movie name from user and add it to the list."""
    movie = input("Enter the movie name: ").strip()
    if movie:
       movies.append(movie)
       print(f'"{movie}" was added.')
    else:
       print("Movie name cannot be empty!")
    list_movies()



# Step 5: Create the function to delete a movie
def delete_movie():
    """Delete a movie from the list by number."""
    list_movies()
    if not movies:
        return

    try:
        movie_number = int(input("Enter the number of the movie to delete: "))
        if 1 <= movie_number <= len(movies):
            removed_movie = movies.pop(movie_number - 1)
            print(f'"{removed_movie}" was deleted.')
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Please enter a valid number.")
    list_movies()


    
# Step 6: Create the main function
def main():
    """Main program loop"""
    show_menu()
    while True:
        command = input("\nEnter command: ").strip().lower()
        if command == "list":
            list_movies()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")
            show_menu()

# Step 7: Add the program start line
if __name__ == "__main__":
        main()

