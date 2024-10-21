import tkinter as tk
from tkinter import messagebox
import datetime


class Post:
    def __init__(self, author, text):
        self.author = author
        self.time = datetime.datetime.now()
        self.likes = 0
        self.text = text
        self.comments = []

    def like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)


# Функция для отображения поста в интерфейсе
def display_post(post):
    post_time = post.time.strftime("%Y-%m-%d %H:%M:%S")
    post_text.set(f"Автор: {post.author}\n"
                  f"Время публикации: {post_time}\n"
                  f"Лайков: {post.likes}\n"
                  f"Текст сообщения: {post.text}")

    comments_listbox.delete(0, tk.END)
    for comment in post.comments:
        comments_listbox.insert(tk.END, comment)


# Функция для обработки лайков
def like_post():
    post.like()
    display_post(post)


# Функция для добавления комментария
def add_comment():
    comment = comment_entry.get()
    if comment.strip():
        post.add_comment(comment)
        comment_entry.delete(0, tk.END)
        display_post(post)
    else:
        messagebox.showwarning("Ошибка", "Комментарий не может быть пустым!")


# Функция для открытия окна публикации после входа
def open_post_window():
    login_window.destroy()

    global root
    root = tk.Tk()
    root.title("Публикация в сети")

    global post
    post = Post(author="ЪЪЪ", text="Это мой первый пост!")

    global post_text
    post_text = tk.StringVar()

    post_label = tk.Label(root, textvariable=post_text, justify=tk.LEFT, anchor="w")
    post_label.pack(padx=10, pady=10, fill=tk.BOTH)

    like_button = tk.Button(root, text="Лайк", command=like_post)
    like_button.pack(padx=10, pady=5)

    comment_label = tk.Label(root, text="Добавить комментарий:")
    comment_label.pack(padx=10, pady=5)

    global comment_entry
    comment_entry = tk.Entry(root)
    comment_entry.pack(padx=10, pady=5, fill=tk.X)

    add_comment_button = tk.Button(root, text="Добавить", command=add_comment)
    add_comment_button.pack(padx=10, pady=5)

    global comments_listbox
    comments_listbox = tk.Listbox(root, height=5)
    comments_listbox.pack(padx=10, pady=10, fill=tk.BOTH)

    display_post(post)

    root.mainloop()


# Функция для проверки логина и пароля
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        open_post_window()
    else:
        messagebox.showerror("Ошибка входа", "Неправильный логин или пароль!")


login_window = tk.Tk()
login_window.title("Вход в систему")

tk.Label(login_window, text="Логин:").pack(padx=10, pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(padx=10, pady=5)

tk.Label(login_window, text="Пароль:").pack(padx=10, pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(padx=10, pady=5)

login_button = tk.Button(login_window, text="Войти", command=login)
login_button.pack(pady=10)

login_window.mainloop()
