![logoPurwadhika](https://www.purwadhika.com/static/media/logo.b4fc6414.png)

# TAHARAUTO - YOUR USED CAR PREDICTOR
### Background
The rise of used car enthusiasts makes the price of used cars more varied. Seeing this phenomenon I took the initiative to help novice fans to find out the estimated price of the cars.
### About
TAHARAUTO is a system created to predict the price of used cars. This prediction system is based on a dataset in Kaggle. The data was taken from a car sales portal in America, edmunds.com. More than 7000 cars with various manufacturers such as BMW, FORD, Toyota, Audi along with each different type.

This project divides each car variety from each manufacturer based on 3 main classes. This aims to make it easier for new players to know what car they want to know based on similar types of cars or some famous brands.

The results of this prediction are the price of a car based on the manufacturer, class type, vehicle model, vehicle transmission, driven wheels, horsepower, and year.

### Exploratory Data

The data that I used was obtained from Kaggle (https://www.kaggle.com/CooperUnion/cardataset). After cleaning the data and solving missing values problems, I tried to explore more about this data. Some discoveries are.

![CarYearDistribution](https://raw.githubusercontent.com/mutaharrikihsan12/Data-Science-Projects/master/Taharauto%20-%20Car%20Price%20Prediction/static/images/plotlib_car_year.png)
![CarDistribution](https://github.com/mutaharrikihsan12/Data-Science-Projects/blob/master/Taharauto%20-%20Car%20Price%20Prediction/static/images/plotlib_car_distribution.png)
![CarPopular](https://github.com/mutaharrikihsan12/Data-Science-Projects/blob/master/Taharauto%20-%20Car%20Price%20Prediction/static/images/plotlib_car_popular.png)

### Car Estimation
User Input some car parameters to predictor. In this case the sample that I used is this sample. 
 BMW           
 Class - 1
 Coupe
 Manual
 2WD - Rear
 335 Horsepower
 2011

Real Price is 46136

![inputuser](https://github.com/mutaharrikihsan12/Data-Science-Projects/blob/master/Taharauto%20-%20Car%20Price%20Prediction/static/images/INPUT_DEMO.PNG)
![resultuser](https://github.com/mutaharrikihsan12/Data-Science-Projects/blob/master/Taharauto%20-%20Car%20Price%20Prediction/static/images/RESULT_DEMO.PNG)

This tool gave 46679 as the result. The prediction algorithm is using RandomForestRegression with r2 score 93.7% and MAE percentage from target value is 7%
