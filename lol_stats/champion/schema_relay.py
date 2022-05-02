import django_filters
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from champion.models import Champion


# To use the relay schema with django_filter, the model must be a relational model (django.db.Model) and not a Document, to use with mongo
# it must be with another package (django_monogoengine_filter)
class ChampionFilter(django_filters.FilterSet):
    class Meta:
        model = Champion
        fields = ['champion']


class ChampionNode(DjangoObjectType):
    class Meta:
        model = Champion
        interfaces = (graphene.relay.Node,)


class RelayQuery(graphene.ObjectType):
    relay_champion = graphene.relay.Node.Field(ChampionNode)
    relay_champions = DjangoFilterConnectionField(ChampionNode, filterset_class=ChampionFilter)


class RelayCreateChampion(graphene.relay.ClientIDMutation):
    champion = graphene.Field(ChampionNode)

    class Input:
        health = graphene.Float()
        # ... others attributes

    def mutate_and_get_payload(self, info, **input):
        user = info.content.user

        champion = Champion(heatlh=input.get("health"), posted_by=user)
        champion.save()

        return RelayCreateChampion(champion=champion)


class RelayMutation(graphene.AbstractType):
    relay_create_champion = RelayCreateChampion.Field()
