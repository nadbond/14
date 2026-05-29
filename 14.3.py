import tkinter as tk
from tkinter import messagebox


class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)

        self.flavors = [
            "Шоколад",
            "Клубника",
            "Банан",
            "Бабл-гам",
            "Ваниль"
        ]

        self.types = [
            "На палочке",
            "Мягкое мороженое",
            "В рожке"
        ]


ice_shop = IceCreamStand(
    "ОтМороженное",
    "Кафе-мороженое"
)
def update_flavors():
    list_flavors.delete(0, tk.END)

    for flavor in ice_shop.flavors:
        list_flavors.insert(tk.END, flavor)


def add_flavor():
    flavor = entry_flavor.get()

    if flavor:
        ice_shop.flavors.append(flavor)
        update_flavors()
        entry_flavor.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Ошибка",
            "Введите название вкуса"
        )


def remove_flavor():
    selected = list_flavors.curselection()

    if selected:
        index = selected[0]
        list_flavors.delete(index)
        del ice_shop.flavors[index]


def check_flavor():
    flavor = entry_flavor.get()

    if flavor in ice_shop.flavors:
        messagebox.showinfo(
            "Проверка",
            "Такой вкус есть"
        )
    else:
        messagebox.showinfo(
            "Проверка",
            "Такого вкуса нет"
        )

def update_types():
    list_types.delete(0, tk.END)

    for item in ice_shop.types:
        list_types.insert(tk.END, item)


def add_type():
    new_type = entry_type.get()

    if new_type:
        ice_shop.types.append(new_type)
        update_types()
        entry_type.delete(0, tk.END)


def remove_type():
    selected = list_types.curselection()

    if selected:
        index = selected[0]
        list_types.delete(index)
        del ice_shop.types[index]


def show_types():
    text = "\n".join(ice_shop.types)

    messagebox.showinfo(
        "Типы мороженого",
        text
    )

root = tk.Tk()
root.title("Управление кафе-мороженым")
root.geometry("850x500")

frame_left = tk.LabelFrame(
    root,
    text="Вкусы мороженого",
    padx=10,
    pady=10
)

frame_left.place(x=20, y=20, width=300, height=470)

list_flavors = tk.Listbox(
    frame_left,
    width=35,
    height=20
)

list_flavors.pack()

entry_flavor = tk.Entry(frame_left, width=30)
entry_flavor.pack(pady=10)

btn_add = tk.Button(
    frame_left,
    text="Добавить",
    command=add_flavor
)

btn_add.pack(side=tk.LEFT, padx=5)

btn_remove = tk.Button(
    frame_left,
    text="Удалить",
    command=remove_flavor
)

btn_remove.pack(side=tk.LEFT, padx=5)

btn_check = tk.Button(
    frame_left,
    text="Проверить",
    command=check_flavor
)

btn_check.pack(side=tk.LEFT, padx=5)

frame_info = tk.LabelFrame(
    root,
    text="Информация",
    padx=10,
    pady=10
)

frame_info.place(x=380, y=250, width=140, height=170)

info_text = (
    f"Название:\n"
    f"{ice_shop.name}\n\n"
    f"Кухня:\n"
    f"{ice_shop.cuisine}"
)

label_info = tk.Label(
    frame_info,
    text=info_text,
    justify="left"
)

label_info.pack()

btn_done = tk.Button(
    frame_info,
    text="Готово",
    command=root.quit
)

btn_done.pack(pady=10)


frame_right = tk.LabelFrame(
    root,
    text="Типы мороженого",
    padx=10,
    pady=10
)

frame_right.place(x=580, y=20, width=280, height=470)

list_types = tk.Listbox(
    frame_right,
    width=30,
    height=20
)

list_types.pack()

entry_type = tk.Entry(frame_right, width=25)
entry_type.pack(pady=10)

btn_add_type = tk.Button(
    frame_right,
    text="Добавить тип",
    command=add_type
)

btn_add_type.pack(side=tk.LEFT, padx=5)

btn_remove_type = tk.Button(
    frame_right,
    text="Удалить тип",
    command=remove_type
)

btn_remove_type.pack(side=tk.LEFT, padx=5)

btn_show_types = tk.Button(
    frame_right,
    text="Список",
    command=show_types
)

btn_show_types.pack(side=tk.LEFT, padx=5)

update_flavors()
update_types()

root.mainloop()