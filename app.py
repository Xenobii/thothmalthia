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


TRAINED_MODELS = {
    "segmentation": {
        "models": [
            {
                "name"      : "UNet VERY OLD MODEL 2016",
                "id"        : "0",
                "trained_on": "nudes",
                "score"     : 0.9,
                "date"      : "01.10.2000"
            }
        ]
    },
    "detection": {
        "models": [
            {
                "name"      : "UNet VERY OLD MODEL 2016",
                "id"        : "0",
                "trained_on": "nudes",
                "score"     : 0.9,
                "date"      : "01/10/2000"
            }
        ]
    },
    "classification": {
        "models": [
            {
                "name"      : "UNet VERY OLD MODEL 2016",
                "id"        : "0",
                "trained_on": "nudes",
                "score"     : 0.9,
                "date"      : "01"
            }
        ]
    },
}


INFERED_DATASETS = {
    "dataset1": [
        {
            "name"        : "image1",
            "input_image" : "none",
            "output_image": "none"
        },
        {
            "name"        : "image2",
            "input_image" : "none",
            "output_image": "none"
        }
    ],
    "dataset2": [
        {
            "name"       : "image1",
            "input_image": "none",
            "class"      : "bullshit"
        }
    ]
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
    if mode is None:
        mode = "segmentation"

    data = TRAINED_MODELS[mode]

    return render_template(
        "models.html",
        mode   = mode,
        models = data["models"],
        error  = "test message"
    )

@app.route('/inference')
def inference():
    id       = request.args.get("id")
    category = request.args.get("category")

    model = TRAINED_MODELS["classification"]["models"][int(id)]
    results = INFERED_DATASETS["dataset2"]
    
    return render_template(
        "inference.html",
        mode         = category,
        model        = model,
        results      = results,
        metric_label = "mIoU Score",
        error        = "test",
        success      = "Good"
    )


if __name__ == "__main__":
    app.run(debug=True)
