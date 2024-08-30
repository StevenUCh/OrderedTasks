# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Length, Email, EqualTo

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Login')


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    task_id = HiddenField()  # Campo oculto para el ID de la tarea
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    due_date = DateTimeField('Due Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Submit')

