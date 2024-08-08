import customtkinter
import pass_check

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("750x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Secure password check", font=('Roboto', 20))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter your password", show="*")
entry1.pack(pady=12, padx=10)

def check_password():
    password = entry1.get()
    result = pass_check.pwned_api_check(password)
    # Display the result or handle it as needed
    if result:
        message = (
            f"This password has been seen {result} times before.\n\n"
            "It's highly recommended to choose a more secure password.\n\n"
            "Tips for a secure password:\n"
            "- Use at least 8 characters.\n"
            "- Include a mix of letters, numbers, and special characters.\n"
            "- Avoid common words or easily guessable information.\n"
            "- Use unique passwords for different accounts."
        )

        displayBox.delete("1.0", "end")
        displayBox.insert("1.0", message)

    else:
        message = (
            "This password has not been seen in any data breaches.\n\n"
            "However, this doesn't guarantee absolute security.\n\n"
            "Ensure your password is strong by following these tips:\n\n"
            "- Use at least 8 characters.\n"
            "- Include a mix of letters, numbers, and special characters.\n"
            "- Avoid common words or easily guessable information.\n"
            "- Use unique passwords for different accounts."
        )
        displayBox.delete("1.0", "end")
        displayBox.insert("1.0", message)

button = customtkinter.CTkButton(master=frame, text="Check", command=check_password)
button.pack(pady=12, padx=10)

displayBox = customtkinter.CTkTextbox(master=frame, height=200, width=400)
displayBox.pack(pady=12, padx=10)

if __name__ == '__main__':
    root.mainloop()