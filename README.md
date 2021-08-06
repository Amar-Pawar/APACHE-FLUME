# APACHE-FLUME

## First we have to get key for access from given site
 https://www.alphavantage.co/

### Then we will get data from STOCK API DOCUMENTATION

### After this step we will write a python code to fetch the data from API

### After this we have to create .conf file for this application and we have to add all the properties for source , sink etc.

### In source command we have to give command to run our python file so that it will take output from that to store o HDFS
agent1.sources.tail.command = python3 /home/ubuntu/Documents/hadoop_practice/real_time_data.py

### Then we have to run the command for flume to store this data into HDFS
$ bin/flume-ng agent --conf ./conf/ -f conf/stock.conf -n agent1 -Dflume.root.logger=DEBUG
