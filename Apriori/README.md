# Apriori Algorithm in  Python
## Introduction 
 This is old mmining algorithm in Mining Association Rules 
 
 And I implement this Algorithm from this paper
 	
> *R. Agrawal and R. Srikant. “Fast Algorithms for Mining Association Rules.”  Proc. 1994 Int’l Conf. Very Large Data Bases (VLDB ’94), pp. 487-499, Sept. 1994 .io*

 There are two property in Frequent Itemset Mining
 	
> Property1: *if an itemset is infrequent, all it supersets must be infrequent and they need not be examined futher.*

> Property2: *if an itemset is frequent, all its subsets must be frequent and they need not be examined further.*

### Prune Stage

 Apriori Algorithm use *Property1* to *"Prune"* infrequent superset

 This part cat see in **Apriori_prune** function in Apriori.py

### Join Stage

 Apriori Algorithm use **Apriori_gen** to create k+1 candidate 

 Combines two frequent k-itemset(now k=3),which have same k-1 prefix to generate new (k+1)-itemsets 

 Example:
 
 	k=3 Ck=(a,b,c),(a,b,e) 

	Have same k-1 prefix (a,b) 

	Can combine generate (k+1)-itemset(k=4)  

	Ck+1=(a,b,c,e)

## Usege 
	python Apriori.py

