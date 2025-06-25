def navigate_forest():
    """
    Simulates navigating a forest by choosing left or right.
    The loop continues until 'left' is chosen.
    """
    print("You find yourself at a fork in the forest path.")
    while True:
        user_input = input("Enter your direction (left or right): ").strip().lower()

        if user_input == "right":
            print("You venture deeper into the woods. There is no clear path here, just more trees.")
        elif user_input == "left":
            print("You have successfully exited the forest! Congratulations!")
            break
        else:
            print("Invalid direction. Please choose 'left' or 'right'.")

if __name__ == "__main__":
    navigate_forest()

