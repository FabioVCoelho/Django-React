import graphene
import graphql_jwt

import champion.schema
import users.schema


class Query(users.schema.Query, champion.schema.Query, graphene.ObjectType):
    pass


class Mutation(champion.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
