from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(default_value="Hi!")


schema = Schema(query=Query)
