from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    # coerce=int is to convert the input to integer
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
#     This allows you to indicate whether the quantity has to be added to any existing quantity in the cart for this product
