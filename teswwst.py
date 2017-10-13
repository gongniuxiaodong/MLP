import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# orders=[]
# order_products_train=[]
# order_products_prior=[]
# orders=pd.read_csv(open('e:/Downloads/orders.csv'))
# order_products_train=pd.read_csv(open('e:/Downloads/order_products__train.csv'))
# order_products_prior=pd.read_csv(open('e:/Downloads/order_products__prior.csv'))
#
# orders_prior = orders[orders['eval_set']=='prior']
# # orders_test = orders[orders['eval_set']=='prior']
#
# orders_prior_products = pd.merge(order_products_prior,orders_prior,on='order_id',how='right')
# # test_prior_orders = pd.merge(order_products_prior,orders_test,on='order_id',how='right')
#
# orders_train = orders[orders['eval_set']=='train']
# # test_order_ids = orders[orders['eval_set']=='test']
#
# orders_train_products = pd.merge(order_products_train,orders_train,on='order_id',how='right')
# # test_data = pd.merge(test_order_ids,test_prior_orders,on='user_id',how='lef
# train_data=orders_prior_products.append(orders_train_products)
# label=train_data['reordered']
# print(orders)