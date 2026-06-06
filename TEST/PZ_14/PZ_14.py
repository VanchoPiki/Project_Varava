import tkinter as tk

root = tk.Tk()
root.title("Sign Up")
root.geometry("420x650")
root.configure(bg="#1e2230")

# Шапка
tk.Label(root, text="Sign Up", bg="#e09216", fg="white", font=("Arial", 14), pady=5).pack(fill="x")

# Поля ввода
tk.Label(root, text="First Name", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e1 = tk.Entry(root, width=35)
e1.insert(0, "Enter First Name...")
e1.pack(padx=40, pady=5)

tk.Label(root, text="Last Name", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e2 = tk.Entry(root, width=35)
e2.insert(0, "Enter Last Name...")
e2.pack(padx=40, pady=5)

tk.Label(root, text="Screen Name", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e3 = tk.Entry(root, width=35)
e3.insert(0, "Enter Screen Name...")
e3.pack(padx=40, pady=5)

# Дата рождения (в строчку)
tk.Label(root, text="Date of Birth", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
f_dob = tk.Frame(root, bg="#1e2230")
f_dob.pack(anchor="w", padx=40, pady=5)
em = tk.Entry(f_dob, width=10)
em.insert(0, "May")
em.pack(side="left")
ed = tk.Entry(f_dob, width=5)
ed.insert(0, "5")
ed.pack(side="left", padx=5)
ey = tk.Entry(f_dob, width=8)
ey.insert(0, "1985")
ey.pack(side="left")

# Пол
tk.Label(root, text="Gender", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
f_gen = tk.Frame(root, bg="#1e2230")
f_gen.pack(anchor="w", padx=40, pady=5)
tk.Radiobutton(f_gen, text="Male", value=1, fg="#dfd743", bg="#1e2230").pack(side="left")
tk.Radiobutton(f_gen, text="Female", value=2, fg="#dfd743", bg="#1e2230").pack(side="left", padx=10)

# Страна и контакты
tk.Label(root, text="Country", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e_c = tk.Entry(root, width=35)
e_c.insert(0, "USA")
e_c.pack(padx=40, pady=5)

tk.Label(root, text="E-mail", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e4 = tk.Entry(root, width=35)
e4.insert(0, "Enter E-mail......")
e4.pack(padx=40, pady=5)

tk.Label(root, text="Phone", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e5 = tk.Entry(root, width=35)
e5.insert(0, "Enter Phone......")
e5.pack(padx=40, pady=5)

# Пароли
tk.Label(root, text="Password", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e6 = tk.Entry(root, width=35, show="*")
e6.pack(padx=40, pady=5)

tk.Label(root, text="Confirm Password", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40)
e7 = tk.Entry(root, width=35, show="*")
e7.pack(padx=40, pady=5)

# Согласие
tk.Checkbutton(root, text="I agree to the Terms of Use", fg="#dfd743", bg="#1e2230").pack(anchor="w", padx=40, pady=10)

# Подвал с кнопками
footer = tk.Frame(root, bg="#e09216")
footer.pack(fill="x", side="bottom")

b_cancel = tk.Button(footer, text="Cancel", command=root.destroy)
b_cancel.pack(side="right", padx=10, pady=5)

b_sub = tk.Button(footer, text="submit")
b_sub.pack(side="right", pady=5)

root.mainloop()