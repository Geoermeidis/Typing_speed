import wikipedia

# docs = "https://wikipedia.readthedocs.io/en/latest/code.html#api"

sports = ["LionelMessi", "TigerWoods", "CristianoRonaldo", "Diego Maradona", "Ronaldo(Brazilian footballer)", "Pelé",
          "LebronJames", "MichaelJordan", "SerenaWilliams", "MariaSharapova", "Scottie Pippen", "JohanCruyff",
          "Zinedine Zidane", "Giannis Antetokounmpo", "RogerFederer", "Novak Djokovic", "Lewis Hamilton",
          "Michael Schumacher"]

science = []

entertainment = []

politics = []


# print(wikipedia.page(title="").content)


def fill_text(file):
    for elem in list_:
        try:
            content = wikipedia.page(title=f"{elem}").content
            with open(f"{file}", "a", encoding="utf-8") as fl:
                fl.write(content[0:content.find("==") - 1])
        except wikipedia.exceptions.PageError:
            print(elem)


print()

# fill_text("sports_.txt")
# fill_text("politics_.txt")
# fill_text("science_.txt")
# fill_text("entertainment_.txt")
