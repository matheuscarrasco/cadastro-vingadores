from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_word():
    return render_template("home.html")
# from model.interface import Interface


# def main():
#     Interface()

# if __name__ == '__main__':
#     main()
