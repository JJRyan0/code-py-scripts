# In[10]:

set_hadoop_config(credentials) 


# In[11]:

ufo = sc.textFile("swift://notebooks.keystone/2014.csv")


# In[12]:

print "Total records in the 2014.csv dataset:", ufo.count()


# In[13]:

ufoParse = ufo.map(lambda line : line.split(","))


# In[14]:

ufoParse.first()


# In[15]:

from pyspark.mllib.clustering import KMeans, KMeansModel
from numpy import array
from math import sqrt


# In[17]:

ufodataset = sc.textFile("swift://notebooks.keystone/2014.csv")
parsedData = ufo.map(lambda line: array([float(x) for x in line.split(' ')]))


# In[19]:

clusters = KMeans.train(parsedData, 2, maxIterations=10,
                        runs=10, initializationMode="random")

def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))

clusters.save(sc, "myModelPath")
sameModel = KMeansModel.load(sc, "myModelPath")


# In[ ]:
