import customtkinter as ctk
from logindata import UserInfo


def set_userinfo():
    name = username.get()
    passwd = password.get()
    user = UserInfo()
    display_user.configure(text=user.auth_creds(name, passwd))


def reset_passwd():
    reset_pass_window = ctk.CTkToplevel(root)
    reset_pass_window.focus_set()
    reset_pass_window.grab_set()
    reset_pass_window.configure(fg_color=("#BDBDBD", "#1E1E1E"))
    reset_pass_window.title("reset password")
    reset_pass_window.geometry("200x200")

    label = ctk.CTkLabel(reset_pass_window, text="Reset your password")
    label.pack()


root = ctk.CTk()
root.configure(fg_color=("#BDBDBD", "#1E1E1E"))
root.title("login")
root.geometry("250x250")
root.resizable(False, False)
frame1 = ctk.CTkFrame(root)
frame1.place(relx=0.5, rely=0.5, anchor="center")

username = ctk.CTkEntry(frame1, width=150, placeholder_text="username")
username.pack(pady=(10, 0))

password = ctk.CTkEntry(frame1, width=150, placeholder_text="password", show="*")
password.pack(pady=(10, 0))

login_btn = ctk.CTkButton(frame1, text="login", command=set_userinfo)
login_btn.pack(padx=20, pady=10)

reset_passwd = ctk.CTkButton(frame1, text="forgot password?", command=reset_passwd)
reset_passwd.pack()

display_user = ctk.CTkLabel(frame1, text="Enter your credentials")
display_user.pack(pady=(5, 10))
root.mainloop()
