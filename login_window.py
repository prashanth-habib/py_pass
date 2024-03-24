import customtkinter as ctk
from logininfo import UserInfo


def set_userinfo():
    name = username.get()
    passwd = password.get()
    user = UserInfo()
    display_user.configure(text=user.auth_creds(name, passwd))


root = ctk.CTk()
root.configure(fg_color=("#BDBDBD", "#1E1E1E"))
root.title("login")
root.geometry("250x200")
root.resizable(False, False)
frame1 = ctk.CTkFrame(root)
frame1.place(relx=0.5, rely=0.5, anchor="center")

username = ctk.CTkEntry(frame1, width=150, placeholder_text="username")
username.pack(pady=(10, 0))

password = ctk.CTkEntry(frame1, width=150, placeholder_text="password", show="*")
password.pack(pady=(10, 0))

get_username = ctk.CTkButton(frame1, text="login", command=set_userinfo)
get_username.pack(padx=20, pady=10)

display_user = ctk.CTkLabel(frame1, text="Enter your credentials")
display_user.pack(pady=(0, 10))
root.mainloop()
