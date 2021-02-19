# graphql-example

Simple example of creating a graphql schema on top of a simple REST service

## Example of calling the endpoints

```
Main page:
http://localhost:5000/

All brands:
http://localhost:5000/brands

All products:
http://localhost:5000/products

Product id of '5':
http://localhost:5000/products/5

Full details:
http://localhost:5000/products/5/details
```

GraphQL

```

{
  products {
    id
    name
    price
    stock
    parent {
      id
      name
    }
  }
}
```

```
{
  brands {
    id
    name
  }
}
```

```
{
  brand(id: 1) {
    id
    name
    products {
      name
      price
      stock
    }
  }
}
```

Add mutation:

```
mutation {
  addBrand(name: "BALENCIAGA") {
    ok
    brand {
      id
      name
    }
  }
}
```

Add mutation with products:

```
mutation {
  addBrand(name: "BALENCIAGA", products: [{name: "Shirt YOYO", price: 99, stock: 6}]) {
    ok
    brand {
      id
      name
    }
  }
}
```

query products:

```
query {
  brands {
    id
    name
    products {
      id
      name
      price
      brand {
        id
      }
      stock
    }
  }
}
```
