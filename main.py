from flask import Flask, redirect, render_template
from flask_login import LoginManager, login_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, StringField
from wtforms.validators import DataRequired

import db_session
from users import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


class LoginForm(FlaskForm):
    nickname = StringField('Никнейм', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Пароль заново', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('register.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/functional')
def functional():
    pass


@app.route('/landing')
def landing():
    pass


@app.route('/profile')
def profile():
    pass


def main():
    app.run()


if __name__ == '__main__':
    main()
