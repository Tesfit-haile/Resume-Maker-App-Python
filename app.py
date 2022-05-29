from flask import Flask
from CV_PROJECT import app, models, routes, db


@app.shell_context_processor
def shell_context():
    return {
        'models': models,
        'app': app,
        'db': db,
        'routes': routes
    }


if __name__ == '__main__':
    app.run(debug=True, port=4890)
