from services import CreateMusicLink, SearchMusic 

from model.UserModel import UserModel

from repository import UserRepository


import time


from flask import Flask, request, render_template

app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():

   
    UserRepository.createUser("Ratolongo", "2002-10-02","ratinho@gmail.com","senhadoratoforte")

    time.sleep(2)

    UserRepository.getAllUsers()

    return render_template("index.html")


@app.route("/user", methods=["POST"])
def createUser():

    user = UserModel(
        request.form.get("name"),
        request.form.get("data"),
        request.form.get("email"),
        request.form.get("senha"),
    )

    print(user.name)

    request.form.get

    return render_template("index.html")

@app.route("/search", methods=["POST"])
def searchVideo():

    idVideo = SearchMusic.searchMusic(str(request.form.get("nameMusic")))
    urlVideo  = CreateMusicLink.musicLink(idVideo[0]["id"])

    return render_template('index.html', urlvideo=urlVideo)

if __name__ == "__main__":
    app.run(debug=True)


# tratar para lives o codigo do front quebra!

