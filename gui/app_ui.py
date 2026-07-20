import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox

from organizer import organize_files
from duplicate_detector import detect_duplicates
from report_generator import generate_report
from PIL import Image


# ===================== APP SETTINGS ===================== #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# ===================== MAIN WINDOW ===================== #

app = ctk.CTk()
app.configure(
    fg_color="#0B1120"
)
app.geometry("1400x850")

app.title("Smart File Organizer")

app.minsize(1200, 700)


# ===================== GLOBAL VARIABLES ===================== #

selected_folder = ""
# ===================== LOAD ICONS ===================== #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

icons_path = os.path.join(BASE_DIR, "assets", "icons")

main_logo_icon = ctk.CTkImage(
    Image.open(os.path.join(icons_path, "main_logo.png")),
    size=(90, 90)
)

total_files_icon = ctk.CTkImage(
    Image.open(os.path.join(icons_path, "total_files.png")),
    size=(40, 40)
)

duplicates_icon = ctk.CTkImage(
    Image.open(os.path.join(icons_path, "duplicates.png")),
    size=(40, 40)
)

storage_icon = ctk.CTkImage(
    Image.open(os.path.join(icons_path, "storage.png")),
    size=(40, 40)
)

categories_icon = ctk.CTkImage(
    Image.open(os.path.join(icons_path, "categories.png")),
    size=(40, 40)
)

# ===================== FUNCTIONS ===================== #

def select_folder():

    global selected_folder

    selected_folder = filedialog.askdirectory()

    if selected_folder:

        status_label.configure(
            text=f"Selected Folder:\n{selected_folder}",
            text_color="lightgreen"
        )

        total_files = 0

        total_size = 0

        categories = set()

        for root, dirs, files in os.walk(selected_folder):

            total_files += len(files)

            for file in files:

                file_path = os.path.join(root, file)

                try:

                    total_size += os.path.getsize(file_path)

                    extension = os.path.splitext(file)[1]

                    if extension:
                        categories.add(extension)

                except:
                    pass

        size_mb = round(total_size / (1024 * 1024), 2)

        files_card_label.configure(
            text=f"{total_files}"
        )

        storage_card_label.configure(
            text=f"{size_mb} MB"
        )

        categories_card_label.configure(
            text=f"{len(categories)}"
        )

    else:

        status_label.configure(
            text="No Folder Selected",
            text_color="red"
        )


def organize_action():

    if not selected_folder:

        messagebox.showwarning(
            "Warning",
            "Please Select Folder First"
        )
        return

    try:

        progressbar.set(0.2)

        app.update()

        organize_files(selected_folder)

        progressbar.set(1)

        status_label.configure(
            text="Files Organized Successfully!",
            text_color="lightgreen"
        )

        activity_box.insert(
            "end",
            "✔ Files Organized Successfully\n"
        )

    except Exception as e:

        status_label.configure(
            text=f"Error: {e}",
            text_color="red"
        )


def detect_action():

    if not selected_folder:

        messagebox.showwarning(
            "Warning",
            "Please Select Folder First"
        )
        return

    try:

        progressbar.set(0.3)

        app.update()

        duplicates = detect_duplicates(selected_folder)

        duplicate_box.delete("1.0", "end")

        duplicates_card_label.configure(
            text=f"{len(duplicates)}"
        )

        if duplicates:

            for file in duplicates:

                duplicate_box.insert(
                    "end",
                    f"📄 {file}\n\n"
                )

            status_label.configure(
                text=f"Duplicates Found: {len(duplicates)}",
                text_color="orange"
            )

        else:

            duplicate_box.insert(
                "end",
                "No Duplicate Files Found"
            )

            status_label.configure(
                text="No Duplicates Found",
                text_color="lightgreen"
            )

        progressbar.set(1)

        activity_box.insert(
            "end",
            "🔍 Duplicate Scan Completed\n"
        )

    except Exception as e:

        status_label.configure(
            text=f"Error: {e}",
            text_color="red"
        )


def generate_report_action():

    if not selected_folder:

        messagebox.showwarning(
            "Warning",
            "Please Select Folder First"
        )
        return

    try:

        total_files = 0

        for root, dirs, files in os.walk(selected_folder):
            total_files += len(files)

        duplicates = detect_duplicates(selected_folder)

        generate_report(total_files, duplicates)

        status_label.configure(
            text="Report Generated Successfully!",
            text_color="lightgreen"
        )

        activity_box.insert(
            "end",
            "📄 Report Generated Successfully\n"
        )

        progressbar.set(1)

    except Exception as e:

        status_label.configure(
            text=f"Error: {e}",
            text_color="red"
        )


def toggle_mode():

    current = ctk.get_appearance_mode()

    if current == "Dark":

        ctk.set_appearance_mode("light")

    else:

        ctk.set_appearance_mode("dark")


# ===================== HEADER ===================== #

header = ctk.CTkFrame(
    app,
    height=70,
    corner_radius=0,
    fg_color="#0F172A"
)

header.pack(
    fill="x"
)

header_title = ctk.CTkLabel(
    header,
    text="📂 Smart File Organizer",
    font=("Poppins", 30, "bold")
)

header_title.pack(
    side="left",
    padx=25,
    pady=15
)

theme_btn = ctk.CTkButton(
    header,
    text="🌙 Toggle Theme",
    width=140,
    command=toggle_mode
)

theme_btn.pack(
    side="right",
    padx=20
)


# ===================== MAIN CONTAINER ===================== #

container = ctk.CTkFrame(
    app
)

container.pack(
    fill="both",
    expand=True
)


# ===================== SIDEBAR ===================== #

sidebar = ctk.CTkFrame(
    container,
    width=260,
    corner_radius=0,
    fg_color="#111827"
)

sidebar.pack(
    side="left",
    fill="y"
)

# ===================== MAIN LOGO ===================== #

logo_label = ctk.CTkLabel(
    sidebar,
    image=main_logo_icon,
    text=""
)

logo_label.pack(
    pady=(30, 10)
)

logo_text = ctk.CTkLabel(
    sidebar,
    text="Smart Organizer",
    font=("Poppins", 24, "bold"),
    text_color="white"
)

logo_text.pack(
    pady=(0, 30)
)


# ===================== BUTTONS ===================== #

button_style = {
    "height": 52,
    "corner_radius": 15,
    "font": ("Poppins", 16, "bold"),
    "fg_color": "#2563EB",
    "hover_color": "#1D4ED8",
    "border_width": 1,
    "border_color": "#3B82F6"
}

select_btn = ctk.CTkButton(
    sidebar,
    text="📁 Select Folder",
    command=select_folder,
    **button_style
)

select_btn.pack(
    pady=10,
    padx=20,
    fill="x"
)

organize_btn = ctk.CTkButton(
    sidebar,
    text="⚡ Organize Files",
    command=organize_action,
    **button_style
)

organize_btn.pack(
    pady=10,
    padx=20,
    fill="x"
)

duplicate_btn = ctk.CTkButton(
    sidebar,
    text="🔍 Detect Duplicates",
    command=detect_action,
    **button_style
)

duplicate_btn.pack(
    pady=10,
    padx=20,
    fill="x"
)

report_btn = ctk.CTkButton(
    sidebar,
    text="📄 Generate Report",
    command=generate_report_action,
    **button_style
)

report_btn.pack(
    pady=10,
    padx=20,
    fill="x"
)

exit_btn = ctk.CTkButton(
    sidebar,
    text="❌ Exit",
    fg_color="#7F1D1D",
    hover_color="#991B1B",
    text_color="white",
    command=app.destroy,
    height=52,
    corner_radius=15,
    font=("Poppins", 16, "bold")
)

exit_btn.pack(
    pady=40,
    padx=20,
    fill="x"
)


# ===================== MAIN DASHBOARD ===================== #

main_dashboard = ctk.CTkFrame(
    container,
    fg_color="#0B1120"
)

main_dashboard.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


# ===================== DASHBOARD TITLE ===================== #

dashboard_title = ctk.CTkLabel(
    main_dashboard,
    text="Dashboard",
    font=("Segoe UI", 34, "bold")
)

dashboard_title.pack(
    anchor="w",
    pady=(10, 20)
)


# ===================== CARDS SECTION ===================== #

cards_frame = ctk.CTkFrame(
    main_dashboard,
    fg_color="transparent"
)

cards_frame.pack(
    fill="x",
    pady=10
)


def create_card(parent, title, value,icon):
    
    card = ctk.CTkFrame(
    parent,
    width=220,
    height=130,
    corner_radius=20,
    fg_color="#172036",
    border_width=1,
    border_color="#22304A"
    )

    card.pack_propagate(False)

    title_label = ctk.CTkLabel(
    card,
    text=title,
    image=icon,
    compound="left",
    font=("Poppins", 18),
    text_color="#A5B4FC"
    )

    title_label.pack(
        pady=(20, 10)
    )

    value_label = ctk.CTkLabel(
        card,
        text=value,
        font=("Segoe UI", 32, "bold"),
        text_color="white"
    )

    value_label.pack()

    return card, value_label


files_card, files_card_label = create_card(
    cards_frame,
    " Total Files",
    "0",
    total_files_icon
)

files_card.grid(
    row=0,
    column=0,
    padx=15
)

duplicates_card, duplicates_card_label = create_card(
    cards_frame,
    " Duplicate Files",
    "0",
    duplicates_icon
)

duplicates_card.grid(
    row=0,
    column=1,
    padx=15
)

storage_card, storage_card_label = create_card(
    cards_frame,
    " Storage Used",
    "0 GB",
    storage_icon
)

storage_card.grid(
    row=0,
    column=2,
    padx=15
)

categories_card, categories_card_label = create_card(
    cards_frame,
    " Categories",
    "0",
    categories_icon
)

categories_card.grid(
    row=0,
    column=3,
    padx=15
)


# ===================== STATUS LABEL ===================== #

status_label = ctk.CTkLabel(
    main_dashboard,
    text="Welcome to Smart File Organizer",
    font=("Poppins", 18, "bold"),
    text_color="#4ADE80"
)

status_label.pack(
    anchor="w",
    pady=20
)


# ===================== CONTENT SECTION ===================== #

content_frame = ctk.CTkFrame(
    main_dashboard,
    fg_color="transparent"
)

content_frame.pack(
    fill="both",
    expand=True
)


# ===================== DUPLICATE VIEWER ===================== #

duplicate_frame = ctk.CTkFrame(
    content_frame,
    corner_radius=20,
    fg_color="#111827",
    border_width=1,
    border_color="#22304A"
)

duplicate_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)

duplicate_title = ctk.CTkLabel(
    duplicate_frame,
    text="🔍 Duplicate Files",
    font=("Segoe UI", 24, "bold")
)

duplicate_title.pack(
    pady=20
)

duplicate_box = ctk.CTkTextbox(
    duplicate_frame,
    font=("Consolas", 15),
    corner_radius=15,
    fg_color="#0F172A",
    border_width=1,
    border_color="#334155",
    text_color="white"
)

duplicate_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)


# ===================== ACTIVITY PANEL ===================== #

activity_frame = ctk.CTkFrame(
    content_frame,
    width=350,
    corner_radius=20,
    fg_color="#111827",
    border_width=1,
    border_color="#22304A"
)

activity_frame.pack(
    side="right",
    fill="y"
)

activity_title = ctk.CTkLabel(
    activity_frame,
    text="📊 Recent Activity",
    font=("Segoe UI", 24, "bold")
)

activity_title.pack(
    pady=20
)

activity_box = ctk.CTkTextbox(
    activity_frame,
    width=300,
    font=("Consolas", 14),
    corner_radius=12
)

activity_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)


# ===================== PROGRESS BAR ===================== #

progressbar = ctk.CTkProgressBar(
    main_dashboard,
    height=20,
    corner_radius=20,
    progress_color="#2563EB",
    fg_color="#1E293B"
)

progressbar.pack(
    fill="x",
    pady=20
)

progressbar.set(0)


# ===================== RUN APP ===================== #

app.mainloop()