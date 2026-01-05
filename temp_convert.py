#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 01,04, 2026
# This program uses a for loop calculate the factors of the number


def fahrenheit():
    try:
        # Ask the user for a temperature in Celsius (as a decimal)
        celsius = float(input("Enter temperature in Celsius: "))

        # Convert Celsius to Fahrenheit
        fahrenheit_temp = (9 / 5) * celsius + 32

        # Display the converted temperature
        print(f"{celsius}°C is equal to {fahrenheit_temp:.2f}°F")

    except ValueError:
        # Runs if the user enters something that is NOT a number
        print("Invalid input. Please enter a number next time.")


def main():
    # Main only calls the function
    fahrenheit()


# Start of the program
if __name__ == "__main__":
    main()
