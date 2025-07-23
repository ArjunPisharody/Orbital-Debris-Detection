import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future_position(debris_positions):
    """
    Very simple linear regression prediction of debris position in the future.
    """
    debris_positions = np.array(debris_positions)
    time_steps = np.arange(len(debris_positions)).reshape(-1, 1)
    
    predicted = []
    for i in range(3):  # x, y, z
        model = LinearRegression()
        model.fit(time_steps, debris_positions[:, i])
        future_steps = np.arange(len(debris_positions)).reshape(-1, 1)
        pred = model.predict(future_steps)
        predicted.append(pred)
    
    return list(zip(predicted[0], predicted[1], predicted[2]))
