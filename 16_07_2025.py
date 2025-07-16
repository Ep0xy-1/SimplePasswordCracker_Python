import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import hashlib
import time
import threading
import platform
import os

# Hash methods
HASH_METHODS = {
    'MD5': hashlib.md5,
    'SHA1': hashlib.sha1,
    'SHA256': hashlib.sha256
}

# Load passwords from file or fallback
def load_passwords():
    try:
        with open("passwords.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ['password', '123456', 'letmein', 'qwerty', 'admin', 'monkey', 'dragon']

def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 300)
    else:
        os.system('play -nq -t alsa synth 0.3 sine 1000 2>/dev/null')  # Linux/macOS

def log(message):
    log_box.config(state='normal')
    log_box.insert(tk.END, f"{message}\n")
    log_box.see(tk.END)
    log_box.config(state='disabled')

def start_cracking():
    hash_value = hash_entry.get().strip()
    method = hash_method.get()
    pw_length = password_length.get()

    if not hash_value or not method or pw_length < 5 or pw_length > 12:
        messagebox.showerror("Input Error", "Please enter valid inputs.")
        return

    time_limit = 30 + ((pw_length - 5) * 20)
    passwords = load_passwords()

    result_label.config(text="Cracking...")
    timer_label.config(text=f"Timer: {time_limit}s")

    log_box.config(state='normal')
    log_box.delete('1.0', tk.END)
    log_box.config(state='disabled')

    def countdown(seconds):
        while seconds > 0:
            timer_label.config(text=f"Timer: {seconds}s")
            time.sleep(1)
            seconds -= 1

    def run_crack():
        threading.Thread(target=countdown, args=(time_limit,)).start()

        method_func = HASH_METHODS[method]
        start_time = time.time()

        for word in passwords:
            hashed_word = method_func(word.encode()).hexdigest()
            log(f"Trying: {word} -> {hashed_word}")
            if hashed_word == hash_value:
                elapsed = time.time() - start_time
                result_label.config(text=f"✅ Found: {word} in {round(elapsed, 2)}s")
                log(f"Password cracked: {word}")
                play_sound()
                return
            if time.time() - start_time > time_limit:
                break

        result_label.config(text=f"❌ Failed in {round(time.time() - start_time, 2)}s")
        log("Password not found or time limit reached.")

    threading.Thread(target=run_crack).start()

def hash_input_password():
    raw = password_entry.get().strip()
    method = hash_method.get()
    if not raw or method not in HASH_METHODS:
        messagebox.showerror("Input Error", "Enter a valid password and select hash method.")
        return
    hashed = HASH_METHODS[method](raw.encode()).hexdigest()
    hash_entry.delete(0, tk.END)
    hash_entry.insert(0, hashed)
    messagebox.showinfo("Success", "Password hashed and inserted above.")
    log(f"Generated hash: {hashed}")

def fun_feature():
    log("🎉 Fun Feature Activated: 'You're leveling up in cybersecurity!'")
    messagebox.showinfo("🎉 Surprise!", "You're leveling up in cybersecurity!")

# ------------------------ UI SETUP ------------------------ #
root = tk.Tk()
root.title("Advanced Password Cracker")
root.geometry("640x640")
root.resizable(False, False)

# Dark Mode Theme
bg_color = "#1e1e1e"
fg_color = "#d4d4d4"
root.configure(bg=bg_color)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Consolas", 11))
style.configure("TButton", background=bg_color, foreground=fg_color, font=("Consolas", 10), padding=6)
style.configure("TEntry", fieldbackground="#2d2d2d", foreground=fg_color)
style.configure("TCombobox", fieldbackground="#2d2d2d", background="#2d2d2d", foreground=fg_color)

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Hashed Password:").pack(pady=(10, 2))
hash_entry = ttk.Entry(main_frame, width=60)
hash_entry.pack()

ttk.Label(main_frame, text="Hash Method:").pack(pady=(10, 2))
hash_method = ttk.Combobox(main_frame, values=list(HASH_METHODS.keys()), state='readonly')
hash_method.set("SHA256")
hash_method.pack()

ttk.Label(main_frame, text="Password Length (5–12):").pack(pady=(10, 2))
password_length = tk.IntVar(value=8)
length_spinbox = ttk.Spinbox(main_frame, from_=5, to=12, textvariable=password_length, width=5)
length_spinbox.pack()

ttk.Button(main_frame, text="Start Cracking", command=start_cracking).pack(pady=15)

result_label = ttk.Label(main_frame, text="Result will appear here.")
result_label.pack(pady=5)

timer_label = ttk.Label(main_frame, text="Timer: --")
timer_label.pack(pady=(0, 15))

# Hashing helper
ttk.Label(main_frame, text="Password to Hash (for testing):").pack(pady=(10, 2))
password_entry = ttk.Entry(main_frame, width=40)
password_entry.pack()
ttk.Button(main_frame, text="Generate Hash", command=hash_input_password).pack(pady=10)

# Log display
ttk.Label(main_frame, text="🧾 Cracking Log:").pack(pady=(10, 5))
log_box = scrolledtext.ScrolledText(main_frame, height=10, width=75, bg="#2d2d2d", fg=fg_color, font=("Consolas", 10))
log_box.config(state='disabled')
log_box.pack()

ttk.Button(main_frame, text="🎮 Fun Feature", command=fun_feature).pack(pady=15)

root.mainloop()
