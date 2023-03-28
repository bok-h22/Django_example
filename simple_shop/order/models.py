from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="상품")
    order_qty = models.IntegerField(verbose_name="수량")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="주문일자")

    def __str__(self):
        return f"{self.user} / {self.product}"

    class Meta:
        db_table="tb_order"
        verbose_name = "주문"
        verbose_name_plural = "주문"