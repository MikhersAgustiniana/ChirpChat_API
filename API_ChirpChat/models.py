from django.db import models

# Create your models here.

class foto(models.Model):
    titulo= models.CharField(max_length=100)
    url= models.CharField(max_length=100)
    create_at= models.DateTimeField(auto_now_add=True)

class usuario(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    user_name= models.CharField(max_length=100)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    id_foto= models.ForeignKey(foto, on_delete=models.CASCADE)
    is_active= models.BooleanField(default=False)
    create_at= models.DateTimeField(auto_now_add=True)

class chat(models.Model):
    user_id_1= models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='my_self_chat')
    user_id_2= models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='chat_amigo')
    create_at= models.DateTimeField(auto_now_add=True)

class mensajes(models.Model):
    contenido= models.TextField()
    id_chat= models.ForeignKey(chat, on_delete=models.CASCADE)
    leido= models.BooleanField(default=False)
    create_at= models.DateTimeField(auto_now_add=True)

class amigos(models.Model):
    my_self= models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='my_self_amigos')
    amigo= models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='amigo')
    create_at= models.DateTimeField(auto_now_add=True)

class solicitud(models.Model):
    my_self= models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='my_solicitudes')
    user= models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='solicitud_amistad')
    # aceptada= models.BooleanField(default=False)
    create_at= models.DateTimeField(auto_now_add=True)

class publicacion(models.Model):
    my_self= models.ForeignKey(usuario, on_delete=models.CASCADE)
    titulo= models.CharField(max_length=255)
    contenido= models.TextField()
    id_foto= models.ForeignKey(foto, on_delete=models.CASCADE)
    create_at= models.DateTimeField(auto_now_add=True)