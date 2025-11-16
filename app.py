from flask import Flask, render_template, request

app = Flask(__name__)


MODE_INFO = {
    "segmentation": {
        "models": [
            {
                "name": "UNet VERY OLD MODEL 2016",
                "id": "0",
            }
        ],
        "collections": [
            {
                "name" : "nudes",
                "num_samples": 5000
            }
        ]
    },
    "detection": {
        "models": [
            {
                "name": "UNet VERY OLD MODEL 2016",
                "id": "0",
            }
        ],
        "collections": [
            {
                "name" : "nudes",
                "num_samples": 5000
            }
        ]
    },
    "classification": {
        "models": [
            {
                "name": "UNet VERY OLD MODEL 2016",
                "id": "0",
            }
        ],
        "collections": [
            {
                "name" : "nudes",
                "num_samples": 5000
            }
        ]
    },
}


@app.route("/")
def index():
    return render_template("index.html", is_homepage=True)


@app.route('/train_model')
def train_model():
    mode = request.args.get("category")
    
    if mode is None:
        mode = "segmentation"

    advanced_config = {
        "learning_rate": {
            "range" : "discrete",
            "values": [0.00001, 0.0001, 0.001, 0.01, 0.1],
            "lower" : 0.00001,
            "upper" : 0.1
        },
        "batch_size": {
            "range" : "discrete",
            "values": [1, 2, 4, 8, 16, 32, 64],
            "lower" : 1,
            "upper" : 64
        },
        "epochs": {
            "range": "continuous",
            "min"  : 1,
            "max"  : 100,
            "step" : 1,
            "lower": 1,
            "upper": 100
        },
    }

    data = MODE_INFO[mode]
    
    return render_template(
        "train_model.html",
        mode            = mode,
        models          = data["models"],
        collection_list = data["collections"],
        advanced_config = advanced_config,
    )


@app.route('/collections')
def collections():
    return render_template("collections.html")


@app.route('/models')
def models():
    mode = request.args.get("category")
    MODE_INFO = {
        "segmentation": {
            "models": [
                ("UNetlite", "Dataset1", "90%", "01/10/2000"),
                ("FNetlite", "Eataset1", "80%", "01/10/2000"),
            ]
        },
        "detection": {
            "models": [
                ("UNetlite", "Dataset1", "20%", "01/10/2000"),
            ]
        },
        "classification": {
            "models": [
                ("UNetlite", "Dataset1", "90%", "01/10/2000"),
            ]
        },
    }
    if mode is None:
        mode = "segmentation"

    data = MODE_INFO[mode]

    return render_template(
        "models.html",
        mode       = mode,
        model_list = data["models"],
        error      = "test message"
    )

@app.route('/inference')
def inference():
    name = request.args.get("name")
    attributes = {
        "name"      : name,
        "Trained on": "ZLU-Leaper",
        "mIoU"      : 72.3
    }
    results = [
        {
            "name" : name,
            "image": "undefined",
            "mask" : "undefined"
        }
    ]
    print(results)
    return render_template(
        "inference.html",
        attributes = attributes,
        results    = results,
        error      = "test",
        success    = "Good"
    )


if __name__ == "__main__":
    app.run(debug=True)
