from django.db import models


# table CategoryModel
# Column category_name
# Column2 created_at

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductModel(models.Model):
    product_name = models.CharField(max_length=80)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)
    descriptions = models.TextField()
    image = models.FileField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    # pip install pillow
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class CartModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    user_product_quantity = models.IntegerField(default=0)
    user_add_date = models.DateTimeField(auto_now_add=True, null=True)
#
#    def get_deal_total(self):
#        price = self.product.deal_price
#        quantity = self.quantity
#        total = price * quantity
#        return total

#@property
#def get_cart_deal_total(self):
#    orderitem = self.orderitem_set.all()
#    total = sum(item.get_deal_total for item in orderitem)
#    return total

    #
    def __str__(self):
        return f"{self.user_product})"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class FavoritesModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    user_product_quantity = models.IntegerField(default=0)
    user_add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user_product})"

    class Meta:
        verbose_name = "Favorites"
        verbose_name_plural = "Favorites"