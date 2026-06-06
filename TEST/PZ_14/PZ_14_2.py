import tkinter as tk

root = tk.Tk()
root.title("Расчет массы (Вариант 7)")
root.geometry("350x200")

tk.Label(root, text="Введите массу в кг (M):", font=("Arial", 11)).pack(pady=10)

entry_mass = tk.Entry(root, font=("Arial", 11), justify="center")
entry_mass.pack(pady=5)

lbl_result = tk.Label(root, text="Количество полных тонн: -", font=("Arial", 11, "bold"), fg="white")
lbl_result.pack(pady=15)

tk.Button(
    root,
    text="Рассчитать",
    font=("Arial", 10, "bold"),
    command=lambda: lbl_result.config(
        text=f"Количество полных тонн: {int(entry_mass.get()) // 1000}"
        if entry_mass.get().isdigit()
        else "Ошибка: введите целое число!"
    )
).pack(pady=5)

root.mainloop()