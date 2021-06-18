The given file can be run after initializing airflow to the directory, running web server and airflow scheduler

airflow db init
airflow webserver --port 8080
airflow scheduler

the above approach worked just fine with linux but i was having issues running it on my windows system (some 'temios' error) so i took the docker approach

docker-compose up --build   //make sure you are in the main directory

The json_builder.py handles the creation and storage of jsondata, the neo4j_query.py writes the json data to the database and the main_dag.py handles the scheduling/running at specified intervals.

The neo4j Desktop used was an older version since the latest one seems to have removed plugin support (especially APOC which i used).
Also at times neo4j might need the json file in its import directory to work despite specifying absolute path.


