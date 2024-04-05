from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from modules.modals import User_mgmt

class Signup(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=4)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6)])
    signup = SubmitField('Iniciar Sesión')

    def validate_username(self,username):
        user = User_mgmt.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one')

    def validate_email(self,email):
        user = User_mgmt.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Account with this email ID already exists')

class Login(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember =  BooleanField('Remember me')
    login = SubmitField('Login')

class createTweet(FlaskForm):
    tweet = TextAreaField('¿Que piensas?',validators=[DataRequired(),Length(max=500)])
    tweet_img = FileField('Inclir Imagen',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Publicar')

class FormQuestion(FlaskForm):
    edad = StringField('Edad', validators=[DataRequired()])
    genero = StringField('Género', validators=[DataRequired()])
    ubicacion = StringField('Ubicación (país/ciudad)', validators=[DataRequired()])
    estado_civil = StringField('Estado Civil', validators=[DataRequired()])
    discapacidad = StringField('¿Tienes alguna discapacidad o condición de salud relevante?', validators=[DataRequired()])

    intereses = StringField('¿Cuáles son tus intereses principales? (separados por coma)', validators=[DataRequired()])
    habilidades = StringField('¿En qué materias o actividades destacas? (separadas por coma)', validators=[DataRequired()])
    tiempo_libre = TextAreaField('¿Qué tipo de actividades te gusta realizar en tu tiempo libre?', validators=[DataRequired()])

    expectativas = TextAreaField('¿Qué esperas de una carrera universitaria?', validators=[DataRequired()])
    experiencia = TextAreaField('¿Tienes alguna experiencia laboral relacionada con algún campo específico?', validators=[DataRequired()])
    proyectos = TextAreaField('¿Has participado en proyectos extracurriculares o actividades relacionadas con alguna área de estudio?', validators=[DataRequired()])

    nivel_educativo = StringField('¿Cuál es tu nivel educativo actual?', validators=[DataRequired()])
    titulo = TextAreaField('¿Tienes algún título universitario o técnico? Si es así, ¿en qué área?', validators=[DataRequired()])
    curso = TextAreaField('¿Tienes algún curso, certificación o experiencia de aprendizaje relevante?', validators=[DataRequired()])

    entorno_aprendizaje = StringField('¿Qué tipo de entorno de aprendizaje prefieres?', validators=[DataRequired()])
    equilibrio = TextAreaField('¿Qué importancia le das al equilibrio entre vida personal y académica?', validators=[DataRequired()])
    enfoque = TextAreaField('¿Prefieres un enfoque teórico o práctico en tus estudios?', validators=[DataRequired()])
    tamaño_institucion = TextAreaField('¿Tienes alguna preferencia sobre el tamaño de la institución educativa?', validators=[DataRequired()])

    meta_profesional = TextAreaField('¿Tienes alguna meta profesional específica o un plan de carrera definido?', validators=[DataRequired()])
    interes_areas = TextAreaField('¿Tienes interés en áreas emergentes o tecnológicas?', validators=[DataRequired()])
    posgrado = TextAreaField('¿Tienes algún plan de continuar tus estudios a nivel de posgrado?', validators=[DataRequired()])

    submit = SubmitField('Enviar')

class UpdateProfile(FlaskForm):
    username = StringField('Usuario',validators=[Length(min=4)])
    email = StringField('Email',validators=[Email()])
    bio = StringField('Dinos un poco sobre ti',validators=[Length(max=100)])
    profile = FileField('Actualiza tu foto de perfil',validators=[FileAllowed(['jpg','png'])])
    profile_bg = FileField('Actualiza tu imagen de fondo',validators=[FileAllowed(['jpg','png'])])
    bday = DateField('Añade tu nacimiento')
    save = SubmitField('Guardar')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User_mgmt.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Usuario ya ocupado elige otro porfavor')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User_mgmt.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Correo electronico en uso elge otro porfavor')