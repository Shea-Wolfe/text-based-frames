from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=140)

class Item(models.Model):
    name = models.CharField(max_length=140)
    view = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    room = models.ForeignKey(Room)

class Exit(models.Model):
    name = models.CharField(max_length=140)
    exit = models.ForeignKey(Room, related_name='exit')
    entrance = models.ForeignKey(Room, related_name='entrance')


