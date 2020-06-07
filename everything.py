#all in one place
from categorizer import categorize

categorize("/content/drive/My Drive/Amazon Review Data/Office_Products_5.json.gz", prefix='office')
categorize('/content/drive/My Drive/Amazon Review Data/Books_5.json.gz', prefix = 'books')
categorize('/content/drive/My Drive/Amazon Review Data/Cell_Phones_and_Accessories_5.json.gz', prefix = 'cell_phone')
categorize('/content/drive/My Drive/Amazon Review Data/Clothing_Shoes_and_Jewelry_5.json.gz', prefix='clothing_shoe_jewellery')
categorize('/content/drive/My Drive/Amazon Review Data/Electronics_5.json.gz', prefix = 'Electronics')
categorize('/content/drive/My Drive/Amazon Review Data/Kindle_Store_5.json.gz', prefix='Kindle')
categorize('/content/drive/My Drive/Amazon Review Data/Movies_and_TV_5.json.gz', prefix = 'Movies')
categorize('/content/drive/My Drive/Amazon Review Data/Sports_and_Outdoors_5.json.gz', prefix = 'Sports')

delivery_data_paths=['drive/My Drive/CSV/office_delivery.csv','drive/My Drive/CSV/books_delivery.csv',
'drive/My Drive/CSV/cell_phone_delivery.csv','drive/My Drive/CSV/clothing_shoe_jewellery_delivery.csv',
'drive/My Drive/CSV/Electronics_delivery.csv', 'drive/My Drive/CSV/Kindle_delivery.csv',
'drive/My Drive/CSV/Movies_delivery.csv', 'drive/My Drive/CSV/Sports_delivery.csv']

from get_training_data import merge_and_split

train_data, test_data=merge_and_split(delivery_data_paths)

from vectorize_training_data import vectorize_data

vectorizer_path="/content/drive/My Drive/CSV/vectorizer.pkl"
train_features, test_features, Y_train, Y_test=vectorize_data(vectorizer_path, train_data, test_data)

from model import *
model=get_model(train_features, Y_train)
y_pred, acc=make_predictions(test_features, Y_test, model)
print(acc)