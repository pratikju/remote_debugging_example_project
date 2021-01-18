from remote_debugging import create_app

app = create_app()

if __name__ == "__main__":
    from os import getenv

    app.run(host=getenv("HOST"), port=5000, debug=True)
