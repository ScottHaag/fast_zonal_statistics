# fast_zonal_statistics

1) Unzip the file data/data.zip file

2) Make sure docker has enough main memory or the kernel will die using the rasterstats library Set it at at least 14 gb

3) docker-compose -f Fast_Zonal_Statistics.yml up --build

4) docker exec -it fzs bash
    a) jupyter lab --ip=0.0.0.0 --allow-root
    b) Connect with http://127.0.0.1:8888/?token=yourtokenhere
    c) Open and run FastZonalStastics.ipynb