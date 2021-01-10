from tkinter import *
import tkinter.font as font


height = 500  # Y
width = 1000  # X


def resize(x, y):  # resize(width, height)

    app.configure()
    app.geometry(f"{x}x{y}")
    print("Geometry changed")


def options(difficulty):
    # in difficulty get a info icon next to each one, easy = all small no ., ,medium = small but ,. , hard  = everything
    # How many minutes, types of articles???
    options_frame = Frame(app)
    options_frame.place(x=0, y=0, width=width, height=height)
    options_width = int(options_frame.place_info()["width"])
    options_height = int(options_frame.place_info()["height"])

    title = Frame(options_frame, bg="purple")
    duration = Frame(options_frame, bg="red")
    articles = Frame(options_frame, bg="green")

    title.place(x=0, y=0, width=options_width, height=0.1 * options_height)
    duration.place(x=0, y=int(title.place_info()["height"]),
                   width=0.5 * options_width, height=0.9 * options_height)
    articles.place(x=0.5 * options_width, y=int(title.place_info()["height"]),
                   width=0.5 * options_width, height=0.9 * options_height)

    title_ = Label(title, text="Options", bg="purple", font=font.Font(size=20))
    title_.place(relx=0.5, rely=0.5, anchor=CENTER)

    duration_l = Label(duration, text="Choose how many minutes you want to type", bg="red", fg="white",
                       font=font.Font(size=15))
    duration_l.place(relx=0.1, rely=0.1)

    duration_var = StringVar()  # options for time
    duration_30s = Radiobutton(duration, variable=duration_var, text="30 seconds", value=0)
    duration_1min = Radiobutton(duration, variable=duration_var, text="1 minute", value=1)
    duration_2min = Radiobutton(duration, variable=duration_var, text="2 minutes", value=2)
    duration_3min = Radiobutton(duration, variable=duration_var, text="3 minutes", value=3)
    duration_30s.place(relx=0.4, rely=0.3)
    duration_1min.place(relx=0.4, rely=0.45)
    duration_2min.place(relx=0.4, rely=0.6)
    duration_3min.place(relx=0.4, rely=0.75)


    articles_l = Label(articles, text="Choose the type of text you want to type", bg="green", fg="white",
                       font=font.Font(size=15))
    articles_l.place(relx=0.1, rely=0.1)

    article_var = StringVar()  # options for articles
    article_sci = Radiobutton(articles, variable=article_var, text="Science", value=0)
    article_pol = Radiobutton(articles, variable=article_var, text="Politics", value=1)
    article_spo = Radiobutton(articles, variable=article_var, text="Sports", value=2)
    article_lit = Radiobutton(articles, variable=article_var, text="Literature", value=3)
    article_sci.place(relx=0.4, rely=0.3)
    article_pol.place(relx=0.4, rely=0.45)
    article_spo.place(relx=0.4, rely=0.6)
    article_lit.place(relx=0.4, rely=0.75)

    final_button = Button(options_frame, font=font.Font(size=15), text="Confirm",
                          command=lambda: main_play())
    final_button.place(x=0.4 * options_width, y=0.8 * options_height,
                       width=0.2 * options_width, height=0.1 * options_height)



def main_play():
    time_ = 10

    def count(temp, label):  # timer countdown function
        if temp == 10:
            text_entry.configure(state=NORMAL)
            text_entry.delete(0, 'end')
        minutes, secs = divmod(temp, 60)
        timer_ = '{:02d}:{:02d}'.format(minutes, secs)
        label.configure(text=timer_)
        if temp == 0:
            text_entry.configure(state=DISABLED)
            return 0
        timer.after(1000, lambda: count(temp, label))
        temp -= 1

    def restart(temp):
        timer__ = Label(play_frame, bg="red", fg="white", font=font.Font(size=15))
        timer__.place(x=0.55 * play_width, y=0.38 * play_height,
                      width=0.2 * play_width, height=0.05 * play_height)
        count(temp, timer__)

    play_frame = Frame(app, bg="black")
    play_frame.place(x=0, y=0, width=width, height=height)
    play_width = int(play_frame.place_info()["width"])
    play_height = int(play_frame.place_info()["width"])

    with open("test.txt", "r", encoding="utf-8") as fl:
        test_text = fl.read()

    text_label = Label(play_frame, bg="white", fg="black", text=test_text, wraplength=450)
    text_entry = Entry(play_frame, bg="white", fg="black", font=font.Font(size=15), state=DISABLED)
    start_button = Button(play_frame, bg="red", fg="white", font=font.Font(size=15), text="START",
                          command=lambda: count(time_, timer))
    timer = Label(play_frame, bg="red", fg="white", font=font.Font(size=15))
    restart_button = Button(play_frame, bg="red", fg='white', font=font.Font(size=15), text="RESTART",
                            command=lambda: restart(time_))

    text_label.place(x=0.25 * play_width, y=0.02 * play_height,
                     width=0.5 * play_width, height=0.25 * play_height)
    text_entry.place(x=0.25 * play_width, y=0.3 * play_height,
                     width=0.5 * play_width, height=0.05 * play_height)
    start_button.place(x=0.25 * play_width, y=0.38 * play_height,
                       width=0.2 * play_width, height=0.05 * play_height)
    timer.place(x=0.55 * play_width, y=0.38 * play_height,
                width=0.2 * play_width, height=0.05 * play_height)
    restart_button.place(x=0.4 * play_width, y=0.44 * play_height,
                         width=0.2 * play_width, height=0.05 * play_height)


app = Tk()
app.configure()
app.title("Typing speed test")
app.geometry(f"{width}x{height}")

difficulty_frame = Frame(app, bg="DodgerBlue2")
# settings_frame = Frame(app, bg="DodgerBlue2")
difficulty_frame.place(x=0, y=0, width=width, height=height)

main_width = int(difficulty_frame.place_info()["width"])
main_height = int(difficulty_frame.place_info()["height"])

label_frame = Frame(difficulty_frame, bg="DodgerBlue2")
easy_frame = Frame(difficulty_frame, bg="DodgerBlue2")
medium_frame = Frame(difficulty_frame, bg="DodgerBlue2")
hard_frame = Frame(difficulty_frame, bg="DodgerBlue2")

label_frame.place(x=0, y=0, width=main_width, height=0.1 * main_height)
label_y = int(label_frame.place_info()["height"])

easy_frame.place(x=0, y=label_y, width=main_width, height=0.3 * main_height)
easy_y = int(easy_frame.place_info()["height"])

medium_frame.place(x=0, y=easy_y + label_y, width=main_width, height=0.3 * main_height)
medium_y = int(easy_frame.place_info()["height"])

hard_frame.place(x=0, y=medium_y * 2 + label_y, width=main_width, height=0.3 * main_height)

label_font = font.Font(size=20)

main_label = Label(label_frame, text="Choose difficulty", fg="white", bg="DodgerBlue2", font=label_font)
easy_button = Button(easy_frame, bg="green", fg="white", activebackground="darkgreen", activeforeground="white",
                     text="Easy", font=font.Font(size=15), command=lambda: options("easy"))
medium_button = Button(medium_frame, bg="orange", fg="white", activebackground="darkorange", activeforeground="white",
                       text="Medium", font=font.Font(size=15), command=lambda: options("medium"))
hard_button = Button(hard_frame, bg="firebrick1", fg="white", activebackground="firebrick3", activeforeground="white",
                     text="Hard", font=font.Font(size=15), command=lambda: options("hard"))

main_label.place(x=0.4 * int(label_frame.place_info()["width"]), y=0.2 * int(label_frame.place_info()["height"]),
                 width=0.2 * int(label_frame.place_info()["width"]),
                 height=0.6 * int(label_frame.place_info()["height"]))
easy_button.place(x=0.3 * int(easy_frame.place_info()["width"]), y=0.2 * int(easy_frame.place_info()["height"]),
                  width=0.4 * int(easy_frame.place_info()["width"]),
                  height=0.6 * int(easy_frame.place_info()["height"]))
medium_button.place(x=0.3 * int(medium_frame.place_info()["width"]), y=0.2 * int(medium_frame.place_info()["height"]),
                    width=0.4 * int(medium_frame.place_info()["width"]),
                    height=0.6 * int(medium_frame.place_info()["height"]))
hard_button.place(x=0.3 * int(hard_frame.place_info()["width"]), y=0.2 * int(hard_frame.place_info()["height"]),
                  width=0.4 * int(hard_frame.place_info()["width"]),
                  height=0.6 * int(hard_frame.place_info()["height"]))

if __name__ == '__main__':
    app.mainloop()
