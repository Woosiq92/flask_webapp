from flask import Flask 
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

csrf = CSRFProtect() 
db = SQLAlchemy()

# loginManager를 인스턴스화 
login_manager = LoginManager() 

# 미로그인 시 리다이렉트하는 엔드포인트 지정 
login_manager.login_view = "auth.signup"

# 로그인 후에 표시할 메세지를 아무것도 표시하지 안도록 공백으로 지정   
login_manager.login_message = ""

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
