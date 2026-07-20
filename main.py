from organizer import organize_files
from duplicate_detector import detect_duplicates
from report_generator import generate_report
import os


def count_files(folder_path):

    total = 0

    for root, dirs, files in os.walk(folder_path):
        total += len(files)

    return total


def main():

    while True:

        print("\n===================================")
        print(" SMART FILE ORGANIZER ")
        print("===================================")

        print("1. Organize Files")
        print("2. Detect Duplicate Files")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        folder_path = input("Enter folder path: ")

        if choice == "1":

            organize_files(folder_path)

        elif choice == "2":

            duplicates = detect_duplicates(folder_path)

        elif choice == "3":

            total_files = count_files(folder_path)

            duplicates = detect_duplicates(folder_path)

            generate_report(total_files, duplicates)

        elif choice == "4":

            print("Exiting Program...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()