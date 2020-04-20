# Betere Buienradar

# Data

5 minuten forecast tot 2 uur vooruit. 
Aanname: Buitenradar en buienalarm gebruiken dit ook. 
filetype: H5
URL: https://data.knmi.nl/datasets/radar_forecast/1.0?q=radar+forecast

10 minuten weerdata incl. neerslag voor 53 weerstations. 
filetype: NC
URL: ftp://data.knmi.nl/download/Actuele10mindataKNMIstations/1/noversion/

5m neerslag data op basis van wolkreflecties en gevallen regen. 
filetype: H5
URL: ftp://data.knmi.nl/download/nl_rdr_data_rtcor_5m/1.0/noversion

# Log 20-04

- Doel was forecast raster data inladen in mapbox
- H5 omgezet naar TIF -> upload to mapbox failed
- H5 raster omzetten naar GEOjson (https://gist.github.com/psaia/06ebe6da964f0e39a530) -> gebruik gemaakt van gdal_polygonize ogr2ogr geo2topo
- Gelukt om raster om te zetten naar shape en die te visualiseren met geopandas en matplotlib
- TODO: layer met NL kaartje eronder plotten. 

Conclusie: Waarschijnlijk willen we dit GEO pad niet bewandelen en moeten we een nieuwe use case zoeken. 

# Betere Buienradar Scoping Call
Timo, Mark, Simon, Job

# 2020-04-16

Doel: Betere buienradar web app bouwen die beter voorspelt dan buienradar. 
- Locatie: Nederland
- Data: ftp://data.knmi.nl/download/Actuele10mindataKNMIstations/1/noversion/2020/04/16/ 

Technisch doel: Een datagedreven cloudoplossing neerzetten en overengineeren. 
- Open source focus
- IaaS v.s. PaaS?
- Cloud agnostic?
- Technology stack kiezen
- Logging
- Failover and disaster recovery
- DevOps: infra, model logic, app logic

MinimumViableProduct: 
- 1 databron ontsluiten
- PoC: KNMI plaatje nabouwen
- Data pijplijn
- Web app: static page serves KNMI plaatje
- Simpel forecasting model 

SuperViableProduct:
- Advanced modelling + validation
- MLops pipeline: train, register, deploy as API
- Advanced web app features

### Tech Stack

## Azure

Platform: cloud-specific PaaS components
Azure DevOps: IaC, Data pipeline, web app deployments
MS SQL DB
Data Factory: from API -> prep (Python/Databricks) -> SQL DB 
Functions: from API -> prep -> SQL DB
App Services for Docker: flask/streamlit app with plotly plot

## Open source

Gitlab:  CI/CD
Platform: Kubernetes, cloud managed services
Data pipeline: Airflow K8s, Metaflow, Luigi
PostGres: K8s, managed
Web app docker: K8s docker, Heroku
MLops: Cortex, Kubeflow, polyaxon, MLflow