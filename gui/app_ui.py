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
is_light_mode = False

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


def refresh_dashboard_stats():
    """Refresh file count, storage, and file-type statistics."""
    if not selected_folder or not os.path.isdir(selected_folder):
        return

    total_files = 0
    total_size = 0
    file_types = set()

    for root, dirs, files in os.walk(selected_folder):
        dirs[:] = [
            folder for folder in dirs
            if folder not in {"reports", "logs"}
        ]

        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                total_files += 1
                total_size += os.path.getsize(file_path)

                extension = os.path.splitext(filename)[1].lower()
                if extension:
                    file_types.add(extension)
            except OSError:
                continue

    files_card_label.configure(text=str(total_files))
    storage_card_label.configure(
        text=f"{total_size / (1024 * 1024):.2f} MB"
    )
    categories_card_label.configure(text=str(len(file_types)))


def select_folder():
    global selected_folder

    folder = filedialog.askdirectory(title="Select a folder to organize")

    if not folder:
        status_label.configure(
            text="No Folder Selected",
            text_color="orange"
        )
        return

    selected_folder = folder
    status_label.configure(
        text=f"Selected: {selected_folder}",
        text_color="lightgreen"
    )

    refresh_dashboard_stats()

    activity_box.insert("end", "📁 Folder selected\n")
    activity_box.see("end")




def organize_action():
    if not selected_folder:
        messagebox.showwarning(
            "Folder Required",
            "Please select a folder first."
        )
        return

    try:
        progressbar.set(0.2)
        app.update_idletasks()

        organize_files(selected_folder)

        refresh_dashboard_stats()
        progressbar.set(1)

        status_label.configure(
            text="Files organized successfully!",
            text_color="lightgreen"
        )
        activity_box.insert("end", "✔ File organization completed\n")
        activity_box.see("end")

    except Exception as e:
        status_label.configure(text="Organization failed", text_color="red")
        messagebox.showerror("Organization Error", str(e))

    finally:
        progressbar.set(0)



def generate_report_action():
    if not selected_folder:
        messagebox.showwarning(
            "Folder Required",
            "Please select a folder first."
        )
        return

    try:
        progressbar.set(0.3)
        app.update_idletasks()

        total_files = 0

        for root, dirs, files in os.walk(selected_folder):
            dirs[:] = [
                folder for folder in dirs
                if folder not in {"reports", "logs"}
            ]
            total_files += len(files)

        duplicates = detect_duplicates(selected_folder)
        report_path = generate_report(total_files, duplicates)

        status_label.configure(
            text="Report generated successfully!",
            text_color="lightgreen"
        )

        activity_box.insert(
            "end",
            f"📄 Report saved: {report_path}\n"
        )
        activity_box.see("end")

        messagebox.showinfo(
            "Report Generated",
            f"Your report was saved to:\n{os.path.abspath(report_path)}"
        )

    except Exception as e:
        status_label.configure(text="Report generation failed", text_color="red")
        messagebox.showerror("Report Error", str(e))

    finally:
        progressbar.set(0)




def toggle_mode():
    global is_light_mode

    is_light_mode = not is_light_mode

    if is_light_mode:
        ctk.set_appearance_mode("light")

        app.configure(fg_color="#F3F6FC")
        container.configure(fg_color="#F3F6FC")
        header.configure(fg_color="#FFFFFF")
        sidebar.configure(fg_color="#E8EEF8")
        main_dashboard.configure(fg_color="#F3F6FC")

        header_title.configure(text_color="#172554")
        logo_text.configure(text_color="#172554")
        dashboard_title.configure(text_color="#172554")
        status_label.configure(text_color="#15803D")

        for card in (
            files_card,
            duplicates_card,
            storage_card,
            categories_card
        ):
            card.configure(
                fg_color="#FFFFFF",
                border_color="#DCE4F0"
            )

        duplicate_frame.configure(
            fg_color="#FFFFFF",
            border_color="#DCE4F0"
        )
        activity_frame.configure(
            fg_color="#FFFFFF",
            border_color="#DCE4F0"
        )
        for label in (
           files_card_label,
           duplicates_card_label,
           storage_card_label,
           categories_card_label
        ):
           label.configure(text_color="#172554")

        for label in card_title_labels:
            label.configure(text_color="#334155")

        duplicate_title.configure(text_color="#172554")
        activity_title.configure(text_color="#172554")

        duplicate_box.configure(
            fg_color="#F8FAFC",
            text_color="#1E293B",
            border_color="#DCE4F0"
        )
        activity_box.configure(
            fg_color="#F8FAFC",
            text_color="#1E293B"
        )

        theme_btn.configure(
            text="☀️ Light Mode",
            fg_color="#DBEAFE",
            hover_color="#BFDBFE",
            text_color="#1D4ED8"
        )

    else:
        ctk.set_appearance_mode("dark")

        app.configure(fg_color="#0B1120")
        container.configure(fg_color="#0B1120")
        header.configure(fg_color="#0F172A")
        sidebar.configure(fg_color="#111827")
        main_dashboard.configure(fg_color="#0B1120")

        header_title.configure(text_color="#FFFFFF")
        logo_text.configure(text_color="#FFFFFF")
        dashboard_title.configure(text_color="#FFFFFF")
        status_label.configure(text_color="#4ADE80")

        for card in (
            files_card,
            duplicates_card,
            storage_card,
            categories_card
        ):
            card.configure(
                fg_color="#172036",
                border_color="#22304A"
            )

        duplicate_frame.configure(
            fg_color="#111827",
            border_color="#22304A"
        )
        activity_frame.configure(
            fg_color="#111827",
            border_color="#22304A"
        )
        for label in (
           files_card_label,
           duplicates_card_label,
           storage_card_label,
           categories_card_label
        ):
            label.configure(text_color="#F8FAFC")

        for label in card_title_labels:
            label.configure(text_color="#CBD5E1")
        duplicate_title.configure(text_color="#FFFFFF")
        activity_title.configure(text_color="#FFFFFF")

        duplicate_box.configure(
            fg_color="#0F172A",
            text_color="#FFFFFF",
            border_color="#334155"
        )
        activity_box.configure(
            fg_color="#111827",
            text_color="#FFFFFF"
        )

        theme_btn.configure(
            text="🌙 Dark Mode",
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            text_color="#FFFFFF"
        )

        for label in (
          files_card_label,
          duplicates_card_label,
          storage_card_label,
          categories_card_label
        ):
          label.configure(text_color="#FFFFFF")





def detect_action():
    if not selected_folder:
        messagebox.showwarning(
            "Folder Required",
            "Please select a folder first."
        )
        return

    try:
        progressbar.set(0.3)
        app.update_idletasks()

        duplicates = detect_duplicates(selected_folder)

        duplicate_box.delete("1.0", "end")
        duplicates_card_label.configure(text=str(len(duplicates)))

        if duplicates:
            for file_path in duplicates:
                duplicate_box.insert("end", f"📄 {file_path}\n\n")
            status_label.configure(
                text=f"Duplicates found: {len(duplicates)}",
                text_color="orange"
            )
        else:
            duplicate_box.insert("end", "No duplicate files found.")
            status_label.configure(
                text="No duplicates found",
                text_color="lightgreen"
            )

        activity_box.insert("end", "Duplicate scan completed\n")

    except Exception as e:
        messagebox.showerror("Duplicate Scan Error", str(e))

    finally:
        progressbar.set(0)


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
card_title_labels = []

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
    corner_radius=16,
    fg_color="#172036",
    border_width=1,
    border_color="#2D3B55"
    )

    card.pack_propagate(False)

    title_label = ctk.CTkLabel(
        card,
        text=title,
        image=icon,
        compound="left",
        font=("Segoe UI", 15, "bold"),
        text_color="#CBD5E1"
    )

    card_title_labels.append(title_label)

    title_label.pack(
        pady=(20, 10)
    )

    value_label = ctk.CTkLabel(
        card,
        text=value,
        font=("Segoe UI", 30, "bold"),
        text_color="#F8FAFC"
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
    font=("Consolas", 13),
    corner_radius=12,
    fg_color="#0F172A",
    text_color="#E2E8F0",
    border_width=1,
    border_color="#334155"
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