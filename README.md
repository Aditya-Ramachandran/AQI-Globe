# AQI Globe
<br>


[![Made with Plotly](https://img.shields.io/badge/Made%20with-Plotly-1f425f.svg)](https://plotly.com/)  [![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-1f425f.svg)](https://www.streamlit.io/) <br>
<br>
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aqi-globe.streamlit.app/)




![AQI Globe Landing](/Images/AQI%20Globe%20Landing.jpg)

## About 

AQI Globe is a Streamlit app that shows the Air Quality Index (AQI) values of different cities around the world in a nice visual way. The AQI is a measure of how polluted the air is, and it is based on different pollutants such as particulate matter (PM2.5), nitrogen dioxide (NO2), and ozone (O3).

Users can interact with the app by selecting a country and city from the dropdown menu, or by using the search bar to find a specific city. The app also allows users to sort the cities by different criteria such as AQI value, pollutant concentration, and city name.

The app uses data from two datasets obtained from Kaggle, which were merged to provide a comprehensive view of AQI values across various countries and cities. The data is presented using Plotly, a Python library for creating interactive data visualizations.

The application provides a simple and intuitive way for users to explore AQI values and gain insights into air pollution levels worldwide.

## Features
* Interactive map showing the location of each city
* Dropdown menu to select a city/ country
* Overall country stats
* Visualize air pollution trends and statistical data of the most polluted cities in a country using line plots

## Intallation and usage
* Clone this repository <br>
`https://github.com/Aditya-Ramachandran/AQI-Globe.git`
* Change the working directory to the cloned repository by running <br>
`cd AQI-Globe`
* Install the required dependencies by running<br>
`pip install -r requirements.txt`
* To use the app, run the following command in your terminal<br>
`streamlit run app.py`
* The app will open in your default browser and you can start exploring the AQI values for different cities

## Contributing
Thank you for considering contributing to this project! If you would like to contribute, please make sure to read the [contribution guidelines](CONTRIBUTING.md) before making a pull request.


## License
This project is licensed under the MIT License - see the LICENSE file for details.
