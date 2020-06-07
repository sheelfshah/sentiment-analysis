#uses path to tfidvectorizer to vectorize data
#assumes vectorizer has been pickled and data is pandas dataframe

import pickle

def vectorize_data(vectorizer_path, train_data, test_data):
	vectorizer_file=open(vectorizer_path, 'rb')
	vectorizer=pickle.load(vectorizer_file)
	vectorizer_file.close()

	train_features = vectorizer.transform(train_data['reviewText'])
	test_features = vectorizer.transform(test_data['reviewText'])
	Y_train = train_data.Sentiment.values.astype('float')
	Y_test = test_data.Sentiment.values.astype('float')
	return train_features, test_features, Y_train, Y_test