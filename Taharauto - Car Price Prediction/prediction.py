import pickle
from pandas import DataFrame,get_dummies
model = pickle.load(open('finalized_model.sav' , 'rb'))
real_columns = pickle.load(open('real_colomn.sav' , 'rb'))
dummy_columns = pickle.load(open('x_dummies_colomn.sav' , 'rb'))

# new_data = {'Make': 'BMW', 'Model': 'Class -1', 'Year': '2015', 'Engine Fuel Type': 'Premium', 'Engine HP': 250, 'Engine Cylinders': 11, 'Transmission Type': 'AUTOMATIC', 'Driven_Wheels': 
# '4WD', 'Number of Doors': 2, 'Vehicle Size': 'Large', 'Vehicle Style': 'SUV', 'highway MPG': 25, 'city mpg': 31}

def prediction(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=dummy_columns, fill_value=0)
    # print(dummy_columns)
    hasil = model.predict(df)
    return(hasil)

# print(prediction(new_data))