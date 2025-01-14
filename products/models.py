from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    is_activ = models.BooleanField(default=True, verbose_name="Activo")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado em")
    class Meta:
        ordering=["name"]
        verbose_name="Marca"
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    is_activ = models.BooleanField(default=True, verbose_name="Activo")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado em")

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
    def __str__(self):
        return self.name

class product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    band = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products", verbose_name="Marca")
    category = models.ForeignKey(Category, on_delete=models.PROTECT,  related_name="products", verbose_name="Categoria")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado em")

    class Meta:
        ordering = ["title"]
        verbose_name = "Produto"

    def __str__(self):
        return self.title

