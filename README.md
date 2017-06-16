# Code Institute - Stream 3 Project -  [Link](https://breatheworld.herokuapp.com/)

## Breathe The World - eCommerce Site

An online shop to buy cans of air from different parts of the World, inspired in the concept of Souvenir and Marcell Duchamp's contemporary art.

## Technologies used :

<img src="https://camo.githubusercontent.com/904ade21b6fb63dec17555495bb36f749ba52023/68747470733a2f2f73332d75732d776573742d322e616d617a6f6e6177732e636f6d2f706c7567696e7365727665722f646f635265736f75726365732f737461636b2e737667" width="350px">

### Along with:

- [Python](https://www.python.org)
- [Django](https://www.djangoproject.com)
- [Bootstrap](http://getbootstrap.com)
- [jQuery](http://jquery.com)
- [SQLite](https://www.sqlite.org)
- [Stripe](https://www.stripe.com)

`all specifications & versions can be found on requirements.txt`


## Deployment

Deployed from Github to Heroku. (https://www.heroku.com)
Media and Static files hosted on Amazon Storage Servives (https://aws.amazon.com)
DataBase Heroku Postgres :: Database


## Testing
Before deployment tested accounts privacy, password recovery (gives the "email" to Python terminal), models and views for example


```
def remove_from_cart(request, id):
    cartItem = CartItem.objects.get(user=request.user, id=id)
    cartItem.quantity -= 1 

    if cartItem.quantity > 0:      ** --> prevents item below 0 which could lead to negative cart **
        cartItem.save()
    else:
        cartItem.delete()

    return redirect(reverse('cart'))
```

Once deployed I did test links and responsive design in diferent devices.
Tested stripe pay method


