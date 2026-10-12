
import os

from organizer import organize_files
from duplicate_detector import detect_duplicates
from report_generator import generate_report


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

        choice = input("Enter your choice: ").strip()

        # Exit before asking for a folder path
        if choice == "4":
            print("Exiting Program...")
            break

        if choice not in {"1", "2", "3"}:
            print("Invalid Choice. Please enter 1, 2, 3, or 4.")
            continue

        folder_path = input("Enter folder path: ").strip().strip('"')

        if not os.path.isdir(folder_path):
            print("Error: Folder does not exist. Please try again.")
            continue

        if choice == "1":
            organize_files(folder_path)

        elif choice == "2":
            duplicates = detect_duplicates(folder_path)

        elif choice == "3":
            total_files = count_files(folder_path)
            duplicates = detect_duplicates(folder_path)
            report_path = generate_report(total_files, duplicates)
            print(f"Report Generated Successfully! Saved to: {report_path}")


if __name__ == "__main__":
    main()
