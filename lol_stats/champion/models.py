from mongoengine import Document
from mongoengine.fields import (FloatField, StringField, ObjectIdField)


# Create your models here.

class Champion(Document):
    meta = {'collection': 'champions_base_stats'}
    ID = ObjectIdField()
    health = FloatField()
    health_per_level = FloatField()
    health_regeneration = FloatField()
    health_regeneration_per_level = FloatField()
    mana = FloatField()
    mana_per_level = FloatField()
    mana_regeneration = FloatField()
    mana_regeneration_per_level = FloatField()
    attack_damage = FloatField()
    attack_damage_per_level = FloatField()
    attack_speed = FloatField()
    attack_speed_percent_per_level = FloatField()
    armor = FloatField()
    armor_per_level = FloatField()
    magic_resist = FloatField()
    magic_resist_per_level = FloatField()
    movement_speed = FloatField()
    basic_attack_range = FloatField()
    champion = StringField()
