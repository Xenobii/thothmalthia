from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/train_model', methods=['GET'])
def train_model():
    mode = request.args.get("category")
    MODE_INFO = {
        "segmentation": {
            "models": [
                ("UNetlite", "2D Images"),
                ("UNet", "2D Images")
            ]
        },
        "detection": {
            "models": [
                ("UNetlite", "2D Images"),
                ("UNet", "2D Images")
            ]
        },
        "classification": {
            "models": [
                ("UNetlite", "2D Images"),
                ("UNet", "2D Images")
            ]
        },
    }
    if mode is None:
        mode = "segmentation"
        
    data = MODE_INFO[mode]
    
    return render_template(
        "train_model.html",
        mode            = mode,
        model_list      = data["models"],
        collection_list = []
    )


@app.route('/collections')
def collections():
    return render_template("collections.html")


@app.route('/models')
def models():
    return render_template("models.html")


if __name__ == "__main__":
    app.run(debug=True)
