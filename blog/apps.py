from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

class PersonalConfg(AppConfig):
    default_auto_field = 'Models.personal'
    name = 'personal'