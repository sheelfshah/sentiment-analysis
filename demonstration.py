from csv_categorizer import categorize_csv
from get_training_data import merge
from vectorize_training_data import vectorize_prediction_data
import statistics

path_to_scraped_reviews = "data.csv"
print("categorizing...")
categorize_csv(path_to_scraped_reviews, prefix="demo")
print("categorized")

delivery_data_paths = ["demo_delivery.csv"]
fake_data_paths = ["demo_fake.csv"]
price_data_paths = ["demo_price.csv"]
faulty_data_paths = ["demo_faulty.csv"]

delivery_data = merge(delivery_data_paths)
fake_data = merge(fake_data_paths)
price_data = merge(price_data_paths)
faulty_data = merge(faulty_data_paths)

vectorizer_path = ""
delivery_features, delivery_results = vectorize_prediction_data(
    vectorizer_path, delivery_data)
fake_features, fake_results = vectorize_prediction_data(
    fake_path, fake_data)
price_features, price_results = vectorize_prediction_data(
    vectorizer_path, price_data)
faulty_features, faulty_results = vectorize_prediction_data(
    vectorizer_path, faulty_data)

model_path = ""
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

delivery_predictions, delivery_accuracy = make_predictions(
    delivery_features, delivery_results, model)
fake_predictions, fake_accuracy = make_predictions(
    fake_features, fake_results, model)
price_predictions, price_accuracy = make_predictions(
    price_features, price_results, model)
faulty_predictions, faulty_accuracy = make_predictions(
    faulty_features, faulty_results, model)

print(delivery_accuracy, statistics.mean(delivery_predictions))
