from django.db import models
from datetime import date, datetime
from django.db import IntegrityError

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name'])< 2:
            errors["first_name"] = "'First Name' should be at least 4 characters"
        if len(postData['last_name'])< 2:
            errors["last_name"] = "'Last Name' should be at least 4 characters"
        if '@' not in postData['email']:
            errors["email"] = "Please, put an valid e-mail"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors["password"] = "Ambas contraseñas deben ser iguales"
        
        return errors

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        today = date.today().strftime("%Y-%m-%d")
        errors = {}
        if len(postData['title']) < 2:
            errors["name"] = "Show 'Name' should be at least 2 characters"
        if (postData['network']) == '':
            errors["network"] = "Please select a 'Network'"
        if 1 <= len(postData['desc']) < 10:
            errors["desc"] = "Show 'Description' should be at least 10 characters"
        if (postData['release_date']) > today:
        # if datetime.strptime(postData['release_date'],"%Y-%m-%d").date() > datetime.today().date():
            errors["release_date"] = "Show 'Release data' should be in the past"
        if (postData['release_date']) == '':
            errors["release_date"] = "Show 'Release data' shouldn't be empty"
        
        return errors

class Tv(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # shows
    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'
    
class Shows(models.Model):
    title = models.CharField(max_length=255, unique=True)
    release_date = models.DateField(("%Y-%m-%d"), auto_now=False, auto_now_add=False)
    network = models.ForeignKey(Tv, related_name = "shows", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=255)
    objects = ShowsManager()
    
    def __repr__(self) -> str:
        return f'[{self.id}] {self.title}, {self.release_date} from {self.network}'

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    avatar = models.URLField()
    allowed = models.BooleanField(default=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsersManager()