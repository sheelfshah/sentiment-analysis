#creates and trains model

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

def get_model(train_features, Y_train, first_layer_size=120, second_layer_size=20, epochs=10, batch_size=256):
	model = Sequential()
	model.add(Dense(first_layer_size, input_dim=train_features.shape[1], activation='relu'))
	model.add(Dropout(0.3))
	model.add(Dense(second_layer_size, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	model.fit(train_features, Y_train, epochs=epochs, batch_size=batch_size)
	return model

def make_predictions(test_features, Y_test, model):
	y_pred = model.predict(test_features)
	num_correct=0
	tot=0
	for i in range(len(y_pred)):
		if np.round(y_pred[i])==Ytest[i]:
	    	num_correct+=1
	    tot+=1
	return y_pred, num_correct/tot	#accuracy 