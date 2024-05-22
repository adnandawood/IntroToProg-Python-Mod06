import json  # Importing the JSON module for handling JSON data

class FileProcessor:
    """
    A class to handle file processing operations.
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Read data from a JSON file and load it into a list.

        Parameters:
            file_name (str): The name of the file to read from.
            student_data (list): The list to store the loaded data.
        """
        try:
            with open(file_name, "r") as file:  # Open the file in read mode
                student_data.extend(json.load(file))  # Load JSON data from file into the list
        except Exception as e:  # Handle exceptions
            IO.output_error_messages("Error reading file:", e)  # Call output_error_messages method to display error

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Write data from a list to a JSON file.

        Parameters:
            file_name (str): The name of the file to write to.
            student_data (list): The list containing data to write.
        """
        try:
            with open(file_name, "w") as file:  # Open the file in write mode
                json.dump(student_data, file)  # Write list data to JSON file
        except Exception as e:  # Handle exceptions
            IO.output_error_messages("Error writing to file:", e)  # Call output_error_messages method to display error


class IO:
    """
    A class to handle input/output operations.
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Output error messages along with the exception details.

        Parameters:
            message (str): The error message to display.
            error (Exception): The exception object.
        """
        print(message)  # Print the error message
        if error:
            print("Error details:", error)  # Print error details if available

    @staticmethod
    def output_menu(menu: str):
        """
        Output the menu to the console.

        Parameters:
            menu (str): The menu string to display.
        """
        print(menu)  # Print the menu

    @staticmethod
    def input_menu_choice():
        """
        Prompt the user to input a menu choice.

        Returns:
            str: The user's menu choice.
        """
        return input("What would you like to do: ")  # Prompt user for menu choice and return input

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Output the student data to the console.

        Parameters:
            student_data (list): The list containing student data.
        """
        print("-" * 50)  # Print separator line
        for student in student_data:  # Iterate through student data
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')  # Print student details
        print("-" * 50)  # Print separator line

    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompt the user to input student data and add it to the list.

        Parameters:
            student_data (list): The list to store the student data.
        """
        try:
            student_first_name = input("Enter the student's first name: ")  # Prompt user for first name
            if not student_first_name.isalpha():  # Check if input contains only alphabets
                raise ValueError("The first name should only contain alphabets.")  # Raise error if input is invalid
            student_last_name = input("Enter the student's last name: ")  # Prompt user for last name
            if not student_last_name.isalpha():  # Check if input contains only alphabets
                raise ValueError("The last name should only contain alphabets.")  # Raise error if input is invalid
            course_name = input("Please enter the name of the course: ")  # Prompt user for course name
            student_data.append({  # Add student data to list
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            })
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")  # Print registration confirmation
        except ValueError as e:  # Handle value errors
            IO.output_error_messages("Value Error:", e)  # Call output_error_messages method to display error
        except Exception as e:  # Handle other exceptions
            IO.output_error_messages("Error:", e)  # Call output_error_messages method to display error


# Defining data constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Defining data constants
FILE_NAME: str = "Enrollments.json"

# Defining data variables and constants
student_data: list = []

# Reading data from file
FileProcessor.read_data_from_file(FILE_NAME, student_data)  # Call read_data_from_file method to load data from file

while True:
    IO.output_menu(MENU)  # Display the menu
    menu_choice = IO.input_menu_choice()  # Get user's menu choice

    if menu_choice == "1":  # If user chooses option 1
        IO.input_student_data(student_data)  # Call input_student_data method to input student data

    elif menu_choice == "2":  # If user chooses option 2
        IO.output_student_courses(student_data)  # Call output_student_courses method to display student data

    elif menu_choice == "3":  # If user chooses option 3
        FileProcessor.write_data_to_file(FILE_NAME, student_data)  # Call write_data_to_file method to save data to file
        IO.output_student_courses(student_data)  # Call output_student_courses method to display student data

    elif menu_choice == "4":  # If user chooses option 4
        break  # Exit the loop

    else:  # If user enters invalid option
        print("Please only choose option 1, 2, 3, or 4")  # Display error message

print("Program Ended")  # Display program end message