from pathlib import Path 

basefir = Path(__file__).parent.parent 

#BaseConfig 클래스 작성하기 

class BaseConfig: 
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"


class LocalConfig(BaseConfig): 
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
        SQLALCHEMY_TRACK_MODIFICATIONS = False 
        SQLALCHEMY_ECHO = True

class TestingConfig(BaseConfig): 
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
        SQLALCHEMY_TRACK_MODIFICATIONS = False 
        WTF_CSRF_ENABLED = False

config = {
       "testing" : TestingConfig, 
       "local" : LocalConfig, 
}
