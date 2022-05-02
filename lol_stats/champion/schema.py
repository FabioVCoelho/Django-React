import graphene
from graphene_mongo import MongoengineObjectType
from graphql import GraphQLError
from mongoengine.queryset.visitor import Q

from users.schema import UserType
from .models import Champion


class ChampionSchema:
    user = graphene.Field(UserType)
    id = graphene.String()
    health = graphene.Float()
    health_per_level = graphene.Float()
    health_regeneration = graphene.Float()
    health_regeneration_per_level = graphene.Float()
    mana = graphene.Float()
    mana_per_level = graphene.Float()
    mana_regeneration = graphene.Float()
    mana_regeneration_per_level = graphene.Float()
    attack_damage = graphene.Float()
    attack_damage_per_level = graphene.Float()
    attack_speed = graphene.Float()
    attack_speed_percent_per_level = graphene.Float()
    armor = graphene.Float()
    armor_per_level = graphene.Float()
    magic_resist = graphene.Float()
    magic_resist_per_level = graphene.Float()
    movement_speed = graphene.Float()
    basic_attack_range = graphene.Float()
    champion = graphene.String()

    class Arguments:
        health = graphene.Float()
        health_per_level = graphene.Float()
        health_regeneration = graphene.Float()
        health_regeneration_per_level = graphene.Float()
        mana = graphene.Float()
        mana_per_level = graphene.Float()
        mana_regeneration = graphene.Float()
        mana_regeneration_per_level = graphene.Float()
        attack_damage = graphene.Float()
        attack_damage_per_level = graphene.Float()
        attack_speed = graphene.Float()
        attack_speed_percent_per_level = graphene.Float()
        armor = graphene.Float()
        armor_per_level = graphene.Float()
        magic_resist = graphene.Float()
        magic_resist_per_level = graphene.Float()
        movement_speed = graphene.Float()
        basic_attack_range = graphene.Float()
        champion = graphene.String()


class ChampionType(MongoengineObjectType):
    class Meta:
        model = Champion


class Query(graphene.ObjectType):
    champions = graphene.List(ChampionType, search=graphene.String(), first=graphene.Int(), skip=graphene.Int())

    def resolve_champions(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Champion.objects.all()
        if search:
            filter_search = Q(champion__icontains=search)
            qs = qs.filter(filter_search)
        if skip:
            qs = qs[skip:]
        if first and not skip:
            qs = qs[:first]
        if first and skip:
            qs = qs[skip:first + skip]
        return qs


class CreateChampion(graphene.Mutation, ChampionSchema):

    def mutate(self, info, health, health_per_level, health_regeneration, health_regeneration_per_level, mana, mana_per_level, mana_regeneration,
               mana_regeneration_per_level, attack_damage, attack_damage_per_level, attack_speed, attack_speed_percent_per_level, armor,
               armor_per_level, magic_resist, magic_resist_per_level, movement_speed, basic_attack_range, champion):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("You must be logged to create a champion")

        champion = Champion(health=health, health_per_level=health_per_level, health_regeneration=health_regeneration,
                            health_regeneration_per_level=health_regeneration_per_level, mana=mana, mana_per_level=mana_per_level,
                            mana_regeneration=mana_regeneration,
                            mana_regeneration_per_level=mana_regeneration_per_level, attack_damage=attack_damage,
                            attack_damage_per_level=attack_damage_per_level, attack_speed=attack_speed,
                            attack_speed_percent_per_level=attack_speed_percent_per_level, armor=armor,
                            armor_per_level=armor_per_level, magic_resist=magic_resist, magic_resist_per_level=magic_resist_per_level,
                            movement_speed=movement_speed, basic_attack_range=basic_attack_range, champion=champion)
        champion.save()

        return CreateChampion(
            id=champion.id,
            champion=champion.champion,
            health=health, health_per_level=health_per_level, health_regeneration=health_regeneration,
            health_regeneration_per_level=health_regeneration_per_level, mana=mana, mana_per_level=mana_per_level,
            mana_regeneration=mana_regeneration,
            mana_regeneration_per_level=mana_regeneration_per_level, attack_damage=attack_damage,
            attack_damage_per_level=attack_damage_per_level, attack_speed=attack_speed,
            attack_speed_percent_per_level=attack_speed_percent_per_level, armor=armor,
            armor_per_level=armor_per_level, magic_resist=magic_resist, magic_resist_per_level=magic_resist_per_level,
            movement_speed=movement_speed, basic_attack_range=basic_attack_range
        )


class UpdateChampion(graphene.Mutation, ChampionSchema):
    class Arguments:
        champion = graphene.String(required=True)
        health = graphene.Float(required=False)
        health_per_level = graphene.Float(required=False)
        health_regeneration = graphene.Float(required=False)
        health_regeneration_per_level = graphene.Float(required=False)
        mana = graphene.Float(required=False)
        mana_per_level = graphene.Float(required=False)
        mana_regeneration = graphene.Float(required=False)
        mana_regeneration_per_level = graphene.Float(required=False)
        attack_damage = graphene.Float(required=False)
        attack_damage_per_level = graphene.Float(required=False)
        attack_speed = graphene.Float(required=False)
        attack_speed_percent_per_level = graphene.Float(required=False)
        armor = graphene.Float(required=False)
        armor_per_level = graphene.Float(required=False)
        magic_resist = graphene.Float(required=False)
        magic_resist_per_level = graphene.Float(required=False)
        movement_speed = graphene.Float(required=False)
        basic_attack_range = graphene.Float(required=False)

    def mutate(self, info, champion, health=None, health_per_level=None, health_regeneration=None, health_regeneration_per_level=None, mana=None,
               mana_per_level=None, mana_regeneration=None,
               mana_regeneration_per_level=None, attack_damage=None, attack_damage_per_level=None, attack_speed=None,
               attack_speed_percent_per_level=None, armor=None,
               armor_per_level=None, magic_resist=None, magic_resist_per_level=None, movement_speed=None, basic_attack_range=None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("You must be logged to update a champion")

        champion = Champion.objects.filter(champion=champion).first()
        if not champion:
            raise Exception("Champion not found")

        if health:
            champion.health = health
        if mana:
            champion.mana = mana
        if health_per_level:
            champion.health_per_level = health_per_level
        if health_regeneration:
            champion.health_regeneration = health_regeneration
        if health_regeneration_per_level:
            champion.health_regeneration_per_level = health_regeneration_per_level
        if mana_per_level:
            champion.mana_per_level = mana_per_level
        if mana_regeneration:
            champion.mana_regeneration = mana_regeneration
        if mana_regeneration_per_level:
            champion.mana_regeneration_per_level = mana_regeneration_per_level
        if attack_damage:
            champion.attack_damage = attack_damage
        if attack_damage_per_level:
            champion.attack_damage_per_level = attack_damage_per_level
        if attack_speed:
            champion.attack_speed = attack_speed
        if attack_speed_percent_per_level:
            champion.attack_speed_percent_per_level = attack_speed_percent_per_level
        if armor:
            champion.armor = armor
        if armor_per_level:
            champion.armor_per_level = armor_per_level
        if magic_resist:
            champion.magic_resist = magic_resist
        if magic_resist_per_level:
            champion.magic_resist_per_level = magic_resist_per_level
        if movement_speed:
            champion.movement_speed = movement_speed
        if basic_attack_range:
            champion.basic_attack_range = basic_attack_range

        champion.save()

        return UpdateChampion(
            champion=champion.champion,
            id=champion.id,
            health=health, health_per_level=health_per_level, health_regeneration=health_regeneration,
            health_regeneration_per_level=health_regeneration_per_level, mana=mana, mana_per_level=mana_per_level,
            mana_regeneration=mana_regeneration,
            mana_regeneration_per_level=mana_regeneration_per_level, attack_damage=attack_damage,
            attack_damage_per_level=attack_damage_per_level, attack_speed=attack_speed,
            attack_speed_percent_per_level=attack_speed_percent_per_level, armor=armor,
            armor_per_level=armor_per_level, magic_resist=magic_resist, magic_resist_per_level=magic_resist_per_level,
            movement_speed=movement_speed, basic_attack_range=basic_attack_range
        )


class DeleteChampion(graphene.Mutation):
    champion = graphene.String()
    message = graphene.String()

    class Arguments:
        champion = graphene.String()

    def mutate(self, info, champion):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("You must be logged to delete a champion")

        champion = Champion.objects.filter(champion=champion)
        if not champion:
            raise Exception("Champion not found")

        champion.delete()
        return DeleteChampion(message="Sucess")


class Mutation(graphene.ObjectType):
    create_champion = CreateChampion.Field()
    update_champion = UpdateChampion.Field()
    delete_champion_by_name = DeleteChampion.Field()
