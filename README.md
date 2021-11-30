# Scrapy

## How to Build
1. move to the directory of this repository
2. docker-compose build

## How to Run Scrapy
1. docker-compose up -d
2. docker exec -it scrapy_app_1 sh
3. cd /src/project/project
4. scrapy crawl yobimasuMeta -o yobimasu_meta.csv<br>
By customizing above command, you can choose which Spiders to use and which files to output.

## Time
kokochie_meta:15m
parasapo_meta:4h