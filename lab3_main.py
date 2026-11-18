import tkinter as tk
from PIL import Image, ImageTk
from music import start_music, stop_music
import random

SIZE = 600
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'


def create_pixel_rain(parent, color, count=30):
    canvas = tk.Canvas(
        parent,
        bg="#202030",
        highlightthickness=0,
        bd=0
    )

    canvas.place(x=0, y=0, relwidth=1, relheight=1)

    pixels = []

    def start_animation():
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        for i in range(count):
            size = random.randint(3, 5)
            x = random.randint(0, width)
            y = random.randint(-height, 0)
            speed = random.randint(3, 5)

            pixel = canvas.create_rectangle(x, y, x + size, y + size,
                                            fill=color, outline="")

            pixels.append([pixel, speed, size])

        animate()

    def animate():
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        for pixel, speed, size in pixels:
            canvas.move(pixel, 0, speed)

            coords = canvas.coords(pixel)

            if coords[1] > height:
                x = random.randint(0, width - size)
                y = 0

                canvas.coords(pixel, x, y, x + size, y + size)

        canvas.after(35, animate)

    canvas.after(200, start_animation)
    return canvas


def generate_key():
    blocks = []

    for i in range(3):
        letters = random.choices(ALPHABET, k=3)
        numbers = random.choices(NUMBERS, k=2)
        generated_key = letters + numbers
        random.shuffle(generated_key)

        generated_key = ''.join(generated_key)

        blocks.append(generated_key)

    key = '-'.join(blocks)
    return key


def render_frames(parent):
    header = tk.Frame(parent, bg="#202030")
    footer = tk.Frame(parent, bg="#202030")
    body = tk.Frame(parent, bg="#FFFFFF")

    header.pack(side='top', fill=tk.X)
    footer.pack(side=tk.BOTTOM, fill='x')
    body.pack(side='top', fill='both', expand=True)

    render_header(header)
    entry_key = render_body(body)
    render_footer(footer, entry_key)


def render_header(parent):
    create_pixel_rain(parent, "#00BFFF")
    lbl_title = tk.Label(parent, text="Генератор ключа",
                         font=("", 24, "bold"), fg="#D8F5F5", bg="#202030")
    lbl_title.pack(pady=15, side='left', padx=10)


def render_body(parent):
    image = Image.open("шахматы.jpg")
    image = image.resize((750, 450))
    bg_image = ImageTk.PhotoImage(image)

    lbl_background = tk.Label(parent, image=bg_image)
    lbl_background.image = bg_image
    lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_info = tk.Label(parent, text="Твой ключ:",
                        font=("", 14, "bold"), fg="white", bg="#202030")

    lbl_info.place(relx=0.5, rely=0.4, anchor="center")

    entry_key = tk.Entry(parent, font=("", 18), justify="center",
                         width=22)

    entry_key.place(relx=0.5, rely=0.55, anchor="center")

    return entry_key


def generate_key_button(entry_key):
    key = generate_key()

    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)


def render_footer(parent, entry_key):
    create_pixel_rain(parent, "#00FF7F")
    btn_generate = tk.Button(parent, text="Сгенерировать", font=("", 14),
                             bg="#4CAF50", fg="white",
                             command=lambda: generate_key_button(entry_key))

    btn_generate.pack(pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("БЕСПЛАТНЫЕ КЛЮЧИ")
    root.geometry(f"{SIZE}x{SIZE}")
    root.minsize(SIZE, SIZE)
    body = render_frames(root)
    start_music()

    def close_window():
        stop_music()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close_window)

    root.mainloop()
