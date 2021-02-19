from graphene import ObjectType, String, Int, Field, List, Schema, Float, Mutation, InputObjectType, Boolean


class Brand(ObjectType):
    id = Int()
    name = String()


class Product(ObjectType):
    id = Int()
    name = String()
    price = Float()
    stock = Int()


class Query(ObjectType):
    brands = List(Brand)
    products = List(Product)


schema = Schema(Query)

print('hello')
