# spotifymoods
 
A simple ML model to classify Spotify tracks using audio features.

## Installation
```shell
pip install spotifymoods
```

## Usage
### Train the model
```python
import pandas as pd
from spotifymoods import train

# create a Pandas DataFrame from the file 'training_data.csv'
train_data = pd.read_csv('training_data.csv')

# save the trained model to the files 'trained_model.pkl' & 'scaled.pkl'
train(data=train_data, trained_output='trained.pkl', scaled_output='scaled.pkl')
```


### Predict moods
```python
import pandas as pd
from spotifymoods import predict

# create a Pandas DataFrame from the file 'test_data.csv'
test_data = pd.read_csv('test_data.csv')

# use the trained model from the files 'trained.pkl' & 'scaled.pkl', and return the results as DataFrame
result = predict(data=test_data, trained_path='trained.pkl', scaled_path='scaled.pkl')

# output the results to a .csv file
result.to_csv('result.csv', index=False)
```

### CSV data examples
``training_data.csv``
```text
energy,liveness,tempo,speechiness,acousticness,instrumentalness,danceability,duration_ms,loudness,valence,id,mood
0.549,0.22,130.749,0.0698,0.000798,0.00485,0.357,244573,-7.843,0.531,3kdMzXOcrDIdSWLdONHNK5,Energetic
0.975,0.16,129.022,0.0618,5.13e-05,0.713,0.594,205760,-3.21,0.899,3rFEKOClXOdNFO6fQGuQ9j,Energetic
```

``test_data.csv``
```text
energy,liveness,tempo,speechiness,acousticness,instrumentalness,danceability,duration_ms,loudness,valence,id
0.549,0.22,130.749,0.0698,0.000798,0.00485,0.357,244573,-7.843,0.531,3kdMzXOcrDIdSWLdONHNK5
0.975,0.16,129.022,0.0618,5.13e-05,0.713,0.594,205760,-3.21,0.899,3rFEKOClXOdNFO6fQGuQ9j
```