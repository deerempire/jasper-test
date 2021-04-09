from dotenv import load_dotenv
load_dotenv()  # load environment variables (secret, client id, ...)

# order is important! import after loading env:
from website import create_app
from website.config import DevelopmentConfig
app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
