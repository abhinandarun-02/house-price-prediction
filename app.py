import pickle
import numpy as np

pickled_model = pickle.load(open('regmodel.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

data = np.array([0.00632, 18.0, 2.31, 0.0, 0.538, 6.575, 65.2, 4.0900, 1.0, 296.0, 15.3, 396.90, 4.98]).reshape(1,-1)
result = pickled_model.predict(scaler.transform(data))[0]

print(result)