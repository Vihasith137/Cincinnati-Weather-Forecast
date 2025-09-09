# Spatial Weather Prediction for Cincinnati (ZIP 45202)

## Overview

This project aims to predict local weather patterns in Cincinnati’s ZIP code 45202 using historical weather and census data, spatial analysis, and ArcGIS tools. It demonstrates integrating open data with GIS and machine learning for predictive mapping.

## Data Sources

- [Census Data for 45202](https://data.census.gov/profile/45202?g=860XX00US45202)
- [Weather Records - Cincinnati](https://www.wunderground.com/history/monthly/us/oh/cincinnati)
- Optional: Land use, elevation, NDVI from [USGS EarthExplorer](https://earthexplorer.usgs.gov/) or [OpenStreetMap](https://www.openstreetmap.org/)

## Workflow

1. **Data Collection:** Gather weather, census, and optional spatial data.
2. **Data Preparation:** Clean, geocode, and integrate datasets in ArcGIS.
3. **Exploratory Analysis:** Map and analyze weather trends and spatial features.
4. **Prediction Modeling:** Build spatial prediction models (Kriging, regression, etc.).
5. **Visualization:** Produce and export predictive maps.
6. **Reporting:** Summarize methods, findings, and recommendations.

## Getting Started

1. Clone this repo.
2. Download data into `data/raw/`.
3. Follow the analysis notebook or ArcGIS Pro project workflow.

## Credits

- DEM: USGS
- Population: U.S. Census Bureau
- Weather: Weather Underground
