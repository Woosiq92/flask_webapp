from flask import Blueprint, render_template
from apps.crud.forms import UserForm
from flask import Blueprint, render_template, redirect, url_for
from apps.app import db 
from apps.crud.models import User 

# blueprint 객체 생성
crud = Blueprint(
    "crud", 
    __name__, 
    template_folder = "templates", 
    static_folder = "static", 
)

@crud.route("/")
def index(): 
    return render_template("crud/index.html")

@crud.route("/sql")
def sql(): 
    # 모든 데이터 가져오기 
    db.session.query(User).all() 
    return "콘솔 로그를 확인해 주세요"

@crud.route("/users/new", methods = ["GET", "POST"])
def create_user(): 
    form = UserForm() 

    if form.validate_on_submit(): 
        user = User (
            username = form.username.data, 
            email = form.email.data, 
            password = form.password.data, 
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form = form )

@crud.route("/users")
def users(): 
    #사용자 일람 취득 
    users = User.query.all()
    return render_template("crud/index.html", users = users)

@crud.route("/users/<user_id>", methods = ["GET", "POST"])
def edit_user(user_id): 
    form = UserForm()
	
    #User 모델을 이용하여 사용자를 취득한다. 
    user = User.query.filter_by(id=user_id).first() 

    #form으로 부터 제출된 경우는 사용자를 갱신하여 사용자 조회 화면으로 리다이렉트한다. 
    if form.validate_on_submit(): 
        user.username = form.username.data 
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit() 
        return redirect(url_for("crud.users"))
    
    return render_template("crud/edit.html", user = user, form = form)


@crud.route("/users/<user_id>/delete", methods = ["POST"])
def delete_user(user_id): 
    user = User.query.filter_by(id = user_id).first() 
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
