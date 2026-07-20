import os
from datetime import datetime


def generate_report(total_files, duplicates):

    os.makedirs("reports", exist_ok=True)

    report_path = os.path.join("reports", "report.txt")

    with open(report_path, "w") as report:

        report.write("SMART FILE ORGANIZER REPORT\n")
        report.write("============================\n\n")

        report.write(f"Generated On: {datetime.now()}\n\n")

        report.write(f"Total Files Scanned: {total_files}\n")

        report.write(f"Duplicate Files Found: {len(duplicates)}\n\n")

        report.write("Duplicate Files:\n\n")

        for file in duplicates:
            report.write(f"{file}\n")

    print("Report Generated Successfully!")