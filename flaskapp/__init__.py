from flask import Flask
import os

import db
import auth
import blog

app = Flask(__name__, instance_relative_config=True, )
app.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join
                        (app.instance_path, "flaskapp.sqlite"), )
db.init_app(app)
# Register blueprint views
app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)
# Use blog index as main view for user
app.add_url_rule("/", endpoint="index")


@app.route("/")
def sign_in():
    return "Oops Something went wrong".title()


if __name__ == "__main__":
    app.run(debug=True)
