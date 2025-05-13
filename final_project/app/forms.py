from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    
    role = SelectField(
        'Role',
        choices=[('Usuario', 'Usuario'), ('Chef', 'Chef')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Register')

# Formulario para cambiar la contraseña del usuario
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')

# Formulario para crear o editar una receta
class RecetaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    ingredientes = TextAreaField('Ingredientes', validators=[DataRequired()])
    instrucciones = TextAreaField('Instrucciones', validators=[DataRequired()])
    tiempo_preparacion = StringField('Tiempo de preparación (min)', validators=[DataRequired()])
    porciones = StringField('Porciones', validators=[DataRequired()])
    imagen_url = StringField('URL de imagen')
    categoria = StringField('Categoría')
    submit = SubmitField('Guardar')
