# Introduction to Data Science: Final Project

## Proposal:


Groundwater is something we often don't think a lot about. However, groundwater supplies almost half of all drinking water around the globe. It also plays a large part in global food production, taking up almost half of the water used in agriculture. The quality of that groundwater can play a big role in the overall quality of life a person experiences. Living in an area without clean groundwater means a person is either being exposed to harmful contamiants daily, or they are required to import clean water from elsewhere, taking an economic toll on an area. 


I previously worked on a project that was concerned about the effect sea level rise had on the groundwater along the coast of  San Diego and Ventura California. We wanted to see if there was a dectectable effect of sea level rise on groundwater levels and quality by looking at observed monitoring well data. There was a lot of data avaliable over all however, the data was not consistent enough to be reliable in creating a trend analysis. One of the main challenges we faced was that a large portion of the water quality sample data did not have a corresponding groundwater level measurement. Because they sample data was not consistent, we needed to use a groundwater level measurement to normalize the sample data. As water levels change, the quality of the water changes, so we needed to normalize the data to make it easier to compare the data overtime.  

In this project I wanted to see if it was possible to predict the groundwater level based on the date a sample was take, the date a sample was taken, the observed local precipitation and temperatures. I also wanted to see if there was a relationship between the groundwater level and the quality of the water.

Monitoring well sample data will be taken from [GeoTracker](https://geotracker.waterboards.ca.gov/data_download_by_county) and combined with a maximum contaminant level (MCL) dataset to determing the magnitude at which a sample at a specific location is above its limit. This will be used to determine an estimate for water quality at a given point. These points will then be correlated to a disadvantaged communities (DACs) database to determine if a well with worse groundwater quality is more likely to fall in a DAC or not.

Some possible data visualizations would be a scatter plot of water quality and socioeconomic status, A trend analysis for wells within DACs to determine if the quality is changing overtime.
