from flask import Flask, render_template, request, redirect, url_for
import json


# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby


app = Flask(__name__)

messages = {}
json_file = "data/recepty.json"


def save_data():
    with open (json_file, "w", encoding="UTF-8") as f:
        json.dump(messages, f, indent = 4)


@app.route("/")
def vitej():
    return render_template("vitej.html")



@app.route("/form")
def form():
    login = request.args.get("login")
    zprava = request.args.get("text")
    if login and zprava:
        zprava[login] = zprava
        print(messages)
        save_data()

    if zprava == "nvm":
        print("autor byl příliš líný na napsání receptu")
    return render_template("form.html")



print(messages)




@app.route("/form")
def form():
    login = request.args.get("login")
    zprava = request.args.get("text")
    if login and zprava:
        zprava[login] = zprava
        print(messages)
        save_data()

    if zprava == "nvm":
        print("autor byl příliš líný na napsání receptu")
    return render_template("form.html")




# request.args.get("???")
# request.form.get("???")
# print("???")
# cursor.execute("???")


if __name__ == "__main__":
    app.run(debug=True)


# KOMENTÁŘ PRO ÚKOL 7: Kod na konci spusti aplikaci pres debug. Je to standardni ukonceni kodu, aby se funkce spustili.