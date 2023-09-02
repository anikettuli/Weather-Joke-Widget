try:
    # Try to import asyncio and Jokes class from jokeapi module
    import asyncio
    from jokeapi import Jokes
except ImportError:
    # If ImportError occurs, it means the jokeapi module is not installed
    # Import the os module for running shell commands
    import os

    # Use os.system to run 'pip install jokeapi' to install the module
    os.system("pip install jokeapi")

    # After installation, import the Jokes class from jokeapi module
    from jokeapi import Jokes


# Define an asynchronous function to print a joke
async def print_joke():
    # Create an instance of the Jokes class
    j = await Jokes()  # Initialise the class

    # Retrieve a random joke
    joke = await j.get_joke()

    # Check the type of the joke and print it accordingly
    if joke["type"] == "single":
        # If it's a single-line joke, print just the joke
        print(joke["joke"])
    else:
        # If it's a two-part joke, print the setup and delivery separately
        print(joke["setup"])
        print(joke["delivery"])


# Define a main function
def main():
    # Run the print_joke function within the asyncio event loop
    asyncio.run(print_joke())


# Entry point of the script
if __name__ == "__main__":
    # Call the main function when the script is executed directly
    main()
