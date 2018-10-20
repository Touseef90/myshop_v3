import pandas as pd
import os
from django.conf import settings
from .models import Category, Product

class Recommend(object):

    def suggest_products_for(self, product_id):
        id = int(product_id)
        PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
        file = os.path.join(PROJECT_PATH, 'predict1.csv')
        prediction=pd.read_csv(file)
        recoList=prediction[prediction.item1==id]\
                    [["item2","score"]]\
                    .sort_values("score", ascending=[0])
        if recoList.empty:
            return False
        else:
            p_id = list(int(x) for x in recoList["item2"])
            products = Product.objects.filter(id__in=p_id)
            return products
