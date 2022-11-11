# Project Group 

Number of members: 5

Student numbers: Zhenlin Xu(5721679), Luyang Cao(5685915), Yuchen Qi(5695392), Xinghao Lou(5698715), Yimin Xu(5696925)

# Research Objective

*Requires data modeling and quantitative research in Transport, Infrastructure & Logistics*
- Investigate the distribution and hotspot of the origin and destination of the travel by taxi in New York City.

- Detect the hotspot of the origin and destination of travel by taxi in New York City:
the locations of all the origins and destinations of taxi trips in New York City in January, 2014.
K-Means to cluster the center hotspots of ODs.
Elbow algorithm to select a proper k value.
Cluster using different combinations of the features.
Visualize the hotspots of ODs.

- Analyze the characteristics of the data from different perspectives, such as:
The number of trips for different passenger counts per day by hour
The total amount of fares for different passenger counts per day by hour
Average trip distance per day by hour for weekdays and weekends
Average travel speed in weekdays and weekends by hour
Tip behavior of taxi passengers varying with time and other attributes
etc.

# Contribution Statement

*Be specific. Some of the tasks can be coding (expect everyone to do this), background research, conceptualization, visualization, data analysis, and data modeling*

**Zhenlin Xu (5721679)**: Split the dataset; Analyze and visualize the main problem of taxi trips’ OD spatial distributions in New York City. 

**Luyang Cao (5685915)**: Analyze the average trip distance per day by hour for weekdays and weekends.

**Yuchen Qi (5695392)**: Visualize sample tip amount distribution with various pickup locations and analyze tip behavior of taxi passengers as well as its possible changes with time and other attributes.

**Xinghao Lou (5698715)**: Analyze the characteristics of  average travel speed in weekdays and weekends by hour.        

**Yimin Xu (5696925)**: Analyze the number of trips for different passenger counts per day by hour and the total amount of fares for different passenger counts per day by hour.

# Data Used
The data used in this group project were collected and provided to the NYC Taxi and Limousine Commission (TLC). Raw data is available at TLC Trip Record Data - TLC (nyc.gov).

# Data Pipeline

1. Background research:
Collect and read taxi travel-related literature about the study of the Origin-Destination pair.

2. Data collecting: 
Download taxi travel data collected from 2014 provided by TLC Trip Record Data - TLC (nyc.gov). 
Read dataset instructions about the explanation of each column.


3. Data splitting and cleaning: 
The total size of the dataset for the whole year 2014 is around 27G. We decided to split the data and only use one week of data for the research.
Preprocessing steps including datetime parsing, and choosing specific columns are done while reading the csv file.
We clean the data with NaN value.
We filter the data that have abnormal values.

4. Origin and destination clustering: using the clustering algorithms from Scikit-learn to calculate cluster centers of taxi travel origins and destinations.
The k-means algorithm from Scikit-learn is used.
An elbow algorithm is implemented to choose the best hyperparameter for k.
A collection of hyperparameters are selected to fine-tune the results.

5. Statistical explanatory: using Pandas to calculate several traffic parameters and Matplotlib to visualize the results.
To be done after the mid-term check
Matplotlib and Seaborn to visualize 2D plots.

6. Origin and destination visualization: using Plotly to visualize the spatial-temporal evolution of the New York City taxi travel origin and destination hotspots.
To be done after the mid-term check
Geopandas to visualize the geo-scatter plots.

7. Visualization of the different characteristics of the data set by Matplotlib and Plotly express.
The characteristics mentioned in the objectives are visualized. 
