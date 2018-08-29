# python_hbase
This code create a 'table' in hbase with file configuration.

## Getting Started
### Prerequisites
* Python 2.7+
* starbase
* Hbase

### Installing
Debian
```
sudo apt-get install python python-pip
pip install starbase
```
CentOS
```
sudo yum install python python-pip
pip install starbase
```

And you need a cluster or a single node with HBase in my case i use the sandbox of hortonworks:
https://br.hortonworks.com/products/sandbox/

And a file in my case i use u.data file, you cand find this file into this dataset 
http://files.grouplens.org/datasets/movielens/ml-100k.zip

You need to change this line of code for your HBase IP:
```c = Connection("192.168.56.13","8000")```
And this line of code for you file
```ratingFile = open("/tmp/ml-100k/u.data","r")```
