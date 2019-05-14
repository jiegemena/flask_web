from webCore.flaskapp import create_app

app = create_app()

if __name__ == '__main__':
    app.config['log'].info('start app flask ==> host={}, port={}'.format(str(app.config["HOST"]), str(app.config["PORT"])))
    app.run(host=app.config["HOST"], port=app.config["PORT"])
