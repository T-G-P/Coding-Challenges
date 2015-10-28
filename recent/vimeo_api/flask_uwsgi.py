from vimeo_api import create_app

"""
This script provides the necessary application instance for uwsgi
"""
app = create_app()

if __name__ == "__main__":
    app.run()
