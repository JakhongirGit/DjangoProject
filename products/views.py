from django.shortcuts import render, redirect
from products.handler import bot
from products.models import ProductModel, CategoryModel, CartModel, FavoritesModel


def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context=context)

def not_fount_page(request):
    return render(request, 'notfound.html')

def search(request):
    # Пользотватель отправляет Iphone12
    if request.method == 'POST':
        # {'search_product': Iphone12 }
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(product_name__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('notfound')

# Страница определенного продукта
def product_page(request, id):
    product = ProductModel.objects.get(id=id)
    context = {'product': product}
    return render(request, 'single_product.html', context=context)


def about_page(request):
    return render(request, 'about.html')

def add_product_to_cart(requst, id):
    if requst.method == 'POST':
        checker = ProductModel.objects.get(id=id)
        if checker.count >= int(requst.POST.get('pr_count')):
            CartModel.objects.create(user_id=requst.user.id, user_product=checker,
                                    user_product_quantity=int(requst.POST.get('pr_count')))
            print('SUCCESS')
            return redirect('/user_cart')

        else:
            print('ERROR')
            return redirect('/')

def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Новый заказ ока!'

        for i in cart:
            main_text += f'\n Товар: {i.user_product}' \
                         f'\n Кол-во: {i.user_product_quantity}\n' \
                         f'\n ID пользователя: {i.user_id}\n' \
                         f'\n Цена: {i.user_product.price}\n'
            bot.send_message(-1002220820793, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, 'cart.html', context={'cart': cart})

#фаворит
def add_product_to_favorites(requst, id):
    if requst.method == 'POST':
        FavoritesModel.objects.create(user_id=requst.user.id,
                                    user_product_quantity=int(requst.POST.get('pr_count')))
        return redirect('/user_favorites')

    else:
            print('ERROR')
            return redirect('/')

def user_favorites(request): #Убрать?
    favorites = FavoritesModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Новый заказ ока!'

        for i in favorites:
            main_text += f'\n Товар: {i.user_product}' \
                         f'\n Кол-во: {i.user_product_quantity}\n' \
                         f'\n ID пользователя: {i.user_id}\n' \
                         f'\n Цена: {i.user_product.price}\n'
            bot.send_message(-1002220820793, main_text)
            favorites.delete()
            return redirect('/')
    else:
        return render(request, 'cart.html', context={'cart': cart})
