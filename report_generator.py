
import os
from datetime import datetime


def generate_report(total_files, duplicates):
    os.makedirs("reports", exist_ok=True)

    # Create a separate report each time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(
        "reports", f"report_{timestamp}.txt"
    )

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("SMART FILE ORGANIZER REPORT\n")
        report.write("=" * 32 + "\n\n")

        report.write(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
        )
        report.write(f"Total Files Scanned: {total_files}\n")
        report.write(f"Duplicate Files Found: {len(duplicates)}\n\n")

        report.write("DUPLICATE FILES\n")
        report.write("-" * 32 + "\n")

        if duplicates:
            for file_path in duplicates:
                report.write(f"{file_path}\n")
        else:
            report.write("No duplicate files found.\n")

    return report_path
