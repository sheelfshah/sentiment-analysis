#takes categorized data as a list of filepaths
#merges it into a single dataframe and splits it to return training and testing data
#after appending a sentiment column at the end
#sentiment is 1 for ratings greater than 3 and 0 otherwise

import pandas as pd

def merge_and_split(filepaths=[], frac=0.75):
	df = pd.DataFrame(columns = ["rating", "reviewerID", "productID", "reviewText"])
	for filepath in filepaths:
		try:
			df_=pd.read_csv(filepath)
		except:
			print("invalid filepath")
			continue
		df=pd.concat([df, df_], axis=0)
	df['Sentiment'] = df.apply(lambda x: 1 if x['rating']>3 else 0, axis=1)
	train_text = df.sample(frac=0.75, random_state=0)
	test_text = df.drop(train_text.index)
	return train_text, test_text