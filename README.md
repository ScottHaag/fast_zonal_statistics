# fast_zonal_statistics

## Step 1 Unzip the file data/data.zip file

## Make sure docker has enough main memory or the kernel will die using the rasterstats library
## Set it at at least 14 gb

1) docker-compose -f Fast_Zonal_Statistics.yml up --build

## To Run Jupyter Notebook
1) docker exec -it fzs bash

    - jupyter lab --ip=0.0.0.0 --allow-root

    - Connect with http://127.0.0.1:8888/?token=yourtokenhere

    - Open and run FastZonalStastics.ipynb

## To start the notebook in a windows machine
## 1_ open command prompt
## 2_ Navigate to the correct directory
## 3_ Type 'jupyter notebook' into the command prompt
## 4_ Open the FastZonalStastics.ipynb file
