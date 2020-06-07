#takes review data and categorizes it into review classes based on keywords

import csv
import gzip
import re
import json
import pandas as pd
from text_cleaner import clean

delivery_keywords = ['late', 'delay', 'wait', 'days', 'shipment','shipping', 'deliver', 'early', 'cancel']
fake_keywords = ['fake', 'counterfeit', 'knockoff', 'phony', 'fraud', 'bogus', 'sham', 'not real', 'not genuine', 'forged', 'scam', 'hoax']
price_keywords = ['expensive', 'price', 'cost', 'exorbitant', 'cheap', 'budget', 'money', 'poor', 'rich', 'rate', 'discount', 'deal', 'bargain']
faulty_keywords = ['damage', 'broken', 'defect', 'busted', 'smashed', 'not work', 'no seal', 'not in work', 'out of order', 'thirdgrade', 'third grade', 'substandard', 'sub standard' , 'faulty', 'malfunction', 'nonfunction', 'non function', 'flaw', 'tear', 'torn']

def categorize(filepath, prefix="data"):
  try:
    f=gzip.open(filepath)
  except:
    print("Invalid filepath")
    return
  df = pd.DataFrame(columns = ["rating", "reviewerID", "productID", "reviewText"])
  df.to_csv(prefix+'_delivery.csv', index=False)
  df.to_csv(prefix+'_fake.csv', index=False)
  df.to_csv(prefix+'_price.csv', index=False)
  df.to_csv(prefix+'_faulty.csv', index=False)
  csv_delivery=open(prefix+'_delivery.csv', 'a+', newline='')
  csv_fake=open(prefix+'_fake.csv', 'a+', newline='')
  csv_price=open(prefix+'_price.csv', 'a+', newline='')
  csv_faulty=open(prefix+'_faulty.csv', 'a+', newline='')
  writer_delivery = csv.writer(csv_delivery)
  writer_fake = csv.writer(csv_fake)
  writer_price = csv.writer(csv_price)
  writer_faulty = csv.writer(csv_faulty)
  for jsonRow in f:
    try:
      dictRow = (json.loads(jsonRow.strip()))
      reviewText=dictRow["reviewText"][-400:] #only last 400 chars, no cleaning though
      reviewText = clean(reviewText)  #cleaned 400 chars
      rating=dictRow["overall"]
      if rating>4.5:
         continue
      reviewerID=dictRow["reviewerID"]
      productID=dictRow["asin"]
    except:
      #print("Row ignored")   # missing data, or failed json load
      continue
    for key in delivery_keywords:
      if re.search(key, reviewText):
        writer_delivery.writerow([rating, reviewerID, productID, reviewText])
        break
    for key in fake_keywords:
      if re.search(key, reviewText):
        writer_fake.writerow([rating, reviewerID, productID, reviewText])
        break
    for key in price_keywords:
      if re.search(key, reviewText):
        writer_price.writerow([rating, reviewerID, productID, reviewText])
        break
    for key in faulty_keywords:
      if re.search(key, reviewText):
        writer_faulty.writerow([rating, reviewerID, productID, reviewText])
        break
    #print("Row successfully processed")
  print("File has been processed")
  f.close()
  return