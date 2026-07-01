from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid
from django.conf import settings


class UserManager(BaseUserManager):

  def create_user(self, email, password=None):
    if not email:
      raise ValueError('Usuários devem ter um email')

    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_superuser(self, email, password=None):
    user = self.create_user(email=email, password=password)
    user.is_admin = True
    user.save(using=self.db)
    return user


class User(AbstractBaseUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  # Vincula o modelo a um "Manager" personalizado de como os
  # usuários e superusuários são criados no banco de dados
  objects = UserManager()

  USERNAME_FIELD = 'email'

  # É o método que define como o objeto será representado em formato de texto.
  def __str__(self):
    return self.email

  # Faz parte do sistema de permissões do Django.
  # Ele serve para checar se o usuário tem uma permissão específica
  # (ex: "pode_deletar_post").

  def has_perm(self, perm, obj=None):
    return True

  # Faz parte do sistema de permissões, mas serve para o painel de administração
  # (Django Admin). Ele pergunta: "Esse usuário pode ver os modelos do app X?"
  def has_module_perms(self, app_label):
    return True

  # O Django Admin exige que um usuário seja "staff" (membro da equipe)
  # para conseguir sequer fazer login na tela do painel (/admin).
  @property
  def is_staff(self):
    return self.is_admin
