I try build model that can predict laptop price according to their characteristics.

I think it is interesting problem, because it is good idea to evaluate laptop according to characteristics.  

I take dataset from - https://www.kaggle.com/muhammetvarl/laptop-price.

Describe columns from this dataset:
* **Company** - *String* - Laptop Manufacturer
* **Product** - *String* - Brand and Model
* **TypeName** - *String* - Type (Notebook, Ultrabook, Gaming, etc.)
* **Inches** - *Numeric* - Screen Size
* **ScreenResolution** - *String* - Screen Resolution
* **Cpu** - *String* - Central Processing Unit (CPU)
* **Ram** - *String* - Laptop RAM
* **Memory** - *String* - Hard Disk / SSD Memory
* **GPU** - *String* - Graphics Processing Units (GPU)
* **OpSys** - *String* - Operating System
* **Weight** - *String* - Laptop Weight
* **_Price_euros_** - *Numeric* - Price (in Euro) - it is out target!


In `notebook.ipynb` - it is file with EDA, preparation dataset for training(drop duplication, cleaning outliers), 
transform categorical features to numerical. 

In this dataset is records of some `company` are rare. That's why I deleted all `company` that met less than 6 times.

Only such companies remained -- [`lenovo`, `dell`, `hp`, `asus`, `aser`, `msi`, `toshiba`, `apple`, `samsung`, `mediacom`] .

I also deleted the lines where `price_euros` is greater than 95 quintiles.

There are the tuning and evaluation accuracy  2 models: `RandomForestRegressor` and `XGBRegressor`.

For this regression I used `mean_absolute_error`. I choose `XGBRegressor`, because it has lower error.




For building Dockerfile run this command 

```
$ docker build -t midterm_image -f Dockerfile .
```

For running docker, execure this command 

```
docker run -it --rm -p 9696:9696 midterm_image
```


For checking model work we need execute `python requests_to_docker.py` with different parameters.  
