from flask import Flask 
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect() 
db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ", 
        SQLALCHEMY_DATABASE_URI = 
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}", 
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        # sql 을 콘솔 로그에 출력 
        SQLALCHEMY_ECHO = True ,
         WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f",
    )

    # SQLALCHEMY 와 앱 연계 
    db.init_app(app)

    csrf.init_app(app)

    Migrate(app, db)

    login_manager.init_app(app)

    from apps.crud import views as crud_views 
    
    app.register_blueprint(crud_views.crud, url_prefix = "/crud")

    return app
