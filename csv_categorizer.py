import pandas as pd
import csv
import re
from text_cleaner import clean

delivery_keywords = ['late', 'delay', 'wait', 'days',
                     'shipment', 'shipping', 'deliver', 'early']
fake_keywords = ['fake', 'counterfeit', 'knockoff', 'phony', 'fraud',
                 'bogus', 'sham', 'not real', 'not genuine', 'forged', 'scam', 'hoax']
price_keywords = ['expensive', 'price', 'cost', 'exorbitant', 'cheap',
                  'budget', 'money', 'poor', 'rich', 'rate', 'discount', 'deal', 'bargain']
faulty_keywords = ['damage', 'broken', 'defect', 'busted', 'smashed', 'not work', 'no seal', 'not in work', 'out of order', 'thirdgrade',
                   'third grade', 'substandard', 'sub standard', 'faulty', 'malfunction', 'nonfunction', 'non function', 'flaw', 'tear', 'torn']
sound_keywords = ['sound', 'quality', 'loud', 'clear', 'clarity', 'bass']
fake_keywords = sound_keywords


def categorize_csv(filepath, prefix="data"):
    try:
        f = pd.read_csv(filepath, encoding="ISO-8859-1")
    except:
        print("Invalid filepath")
        return
    df = pd.DataFrame(
        columns=["rating", "reviewer", "product", "reviewText"])
    df.to_csv(prefix + '_delivery.csv', index=False)
    df.to_csv(prefix + '_fake.csv', index=False)
    df.to_csv(prefix + '_price.csv', index=False)
    df.to_csv(prefix + '_faulty.csv', index=False)
    csv_delivery = open(prefix + '_delivery.csv', 'a+', newline='')
    csv_fake = open(prefix + '_fake.csv', 'a+', newline='')
    csv_price = open(prefix + '_price.csv', 'a+', newline='')
    csv_faulty = open(prefix + '_faulty.csv', 'a+', newline='')
    writer_delivery = csv.writer(csv_delivery)
    writer_fake = csv.writer(csv_fake)
    writer_price = csv.writer(csv_price)
    writer_faulty = csv.writer(csv_faulty)
    for i in range(f.shape[0]):
        try:
            dictRow = f.iloc[i, :]
            # only last 400 chars, no cleaning though
            reviewText = dictRow["content"][-400:] + " " + dictRow["title"]
            reviewText = clean(reviewText)  # cleaned 400 chars
            rating = int(dictRow["rating"])
            if rating > 4:
                continue
            reviewerID = dictRow["author"]
            productID = dictRow["product"]
        except:
            # print("Row ignored")   # missing data, or failed json load
            continue
        for key in delivery_keywords:
            if re.search(key, reviewText):
                writer_delivery.writerow(
                    [rating, reviewerID, productID, reviewText])
                break
        for key in fake_keywords:
            if re.search(key, reviewText):
                writer_fake.writerow(
                    [rating, reviewerID, productID, reviewText])
                break
        for key in price_keywords:
            if re.search(key, reviewText):
                writer_price.writerow(
                    [rating, reviewerID, productID, reviewText])
                break
        for key in faulty_keywords:
            if re.search(key, reviewText):
                writer_faulty.writerow(
                    [rating, reviewerID, productID, reviewText])
                break
        #print("Row successfully processed")
    print("File has been processed")
    return
