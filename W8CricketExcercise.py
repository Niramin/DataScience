import numpy as np



"""
one)Find mean,median,IQR for Sachin,Rahul,India
two)Histogram of Sachin's scores with 10 bins
three)Mean of Sachin's scores grouped by 25 matches
four)Find the mean of Sachins scores where he scored a century
five)Mean of Sachin's scores when Rahul scores less than 10
six)Mean of Sachin's score based on which quartile India's score falls in
seven)For every match find who scored more runs
eight)How many more runs does Sachins score on average after having scored x runs
nine)How many matches Sachin took to score 1000 runs then next 1000 runs..
"""

def one(file):
    k=["Sachin","Rahul","India"]
    for i in range(0,3):
        j=file[:,i]
        #print(j)
        #mean
        mn=np.mean(j)
        print("-------------------------------------")
        print("The mean of "+k[i],"'s scores is","%.2f"%mn)
        #median
        md=np.median(j)
        print("The median of "+k[i],"'s scores is","%.2f"%md,"\n\n")
        #IQR
        #k= np.asarray(k, dtype = np.float64)
        iqr=np.percentile(j,75)-np.percentile(j,25)
        print("The IQR of "+k[i],"'s scores is",iqr)

def two(file):
    s=file[:,0]
    print(np.histogram(s,bins=10))

def three(file):
    s=file[:,0]
    k=np.hsplit(s,9)
    x=1
    for i in k:
        print("mean",x,":",np.mean(i))
        x+=1

def four(file):
    s=file[:,0]
    s=[x for x in s if x>=100]
    print(np.mean(s))

def five(file):
    sr=file[:,0:2]
    sr=[x[0] for x in sr if x[1]<10]
    #print(sr)
    print("%.2f"%np.mean(sr))

def six(file):
    k=file[:,[0,2]]
    nper=np.percentile(k[:,1],[25,50,75])
    #print(np.digitize(k[:,1],bins=nper))
    kn=np.vstack((k[:,0],np.digitize(k[:,1],bins=nper)))
    kn=np.transpose(kn)
    knn=kn[kn[:,1].argsort()]
    print("Mean 1 :%.2f"%np.mean([x[0] for x in knn if x[1]==0]))
    print("Mean 2 :%.2f"%np.mean([x[0] for x in knn if x[1]<=1]))
    print("Mean 3 :%.2f"%np.mean([x[0] for x in knn if x[1]<=2]))
    print("Mean 4 :%.2f"%np.mean([x[0] for x in knn if x[1]<=3]))
    #print(knn)

def seven(file):
    sr=file[:,0:2]
    sr=file[:,0]-file[:,1]
    for i in range(len(sr)):
        if sr[i]>0:
            print("Match",i+1,": Sachin scored more")
        elif sr[i]==0:
            print("Match",i+1,": Both scored equal runs")
        else:
            print("Match",i+1,": Rahul scored more")

def eight(file):
    s=file[:,0]
    s=np.sort(s)
    #print(s)
    for i in set(s):
        print("On average Sachin will score %.0f"%(np.mean([x for x in s if x>=i])-i),"more if he scores",int(i),"runs")

def nine(file):
    s=file[:,0]
    s=np.cumsum(s)
    print(np.histogram(s,bins=np.arange(0,10000,1000)))
    #print(np.sum(asl))


def main():
    f1=np.genfromtxt(r'C:\Users\cric_data-200320-181217.tsv',skip_header=1,usecols=[1,2,3])
    #one(f1)
    #two(f1)
    #three(f1)
    #four(f1)
    #five(f1)
    #six(f1)
    #seven(f1)
    #eight(f1)
    nine(f1)

if __name__=="__main__":
    main()


