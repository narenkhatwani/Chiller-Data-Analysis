import matplotlib.pyplot as plt
import numpy as np

data=np.array([
[2005,7804],        
[2006,8010],        
[2007,8746],        
[2008,8903],        
[2009,10741],        
[2010,10923],        
[2011,10483]])

x,y=data.T
plt.ylabel("Incidents of Birdstrike")
plt.xlabel("Year")
plt.scatter(x,y)


data1=np.array([
[2005,7673.7857143],        
[2006,8240.1428572],        
[2007,8806.5000001],        
[2008,9372.857143],        
[2009,9939.2142859],        
[2010,10505.5714288],        
[2011,11071.9286717]])

x,y=data1.T
plt.ylabel("Incidents of Birdstrike")
plt.xlabel("Year")
plt.scatter(x,y)
plt.plot(x,y)
