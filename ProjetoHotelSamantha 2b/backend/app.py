from flask import Flask
app = Flask(_name_)

@app.route("/")
def home():
   return"Bom dia galera 2b!"

   app.run()