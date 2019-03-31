from demoWeb import create_app


if __name__ == '__main__':
    app = create_app(debug=True)
    app.config['log'].info('start app flask ==> host={}, port={}'.format(str(app.config["HOST"]), str(app.config["PORT"])))
    app.run(host=app.config["HOST"], port=app.config["PORT"])
