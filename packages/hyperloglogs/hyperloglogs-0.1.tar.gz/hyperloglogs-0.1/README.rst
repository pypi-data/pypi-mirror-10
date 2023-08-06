Hyperloglogs
-----------------------
Allows you to take intersection of arbitrarily many hyperloglogs. 

hll = HyperLogLog(0.01) # 0.01 is % accuracy 
hll.add(1) # can add objects of any type 
hll2 = HyperLogLog(0.01)
hll3 = HyperLogLog(0.01)

hll.intersectoin([hll2, hll3]) # returns cardinality of intersection set 
NOTE THAT IN ORDER TO TAKE INTERSECTION ALL SETS MUST BE THE SAME SIZE 
or in other words, MUST HAVE THE SAME % ACCURACY 
