from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        if username_to_check.data == 'sai':
            raise ValidationError('OOPS! User already exists')


    username = StringField(label='User Name:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='submit')
