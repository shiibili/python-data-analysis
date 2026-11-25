"""import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(50,30,1000)
plt.hist(data,bins=30)
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()"""
"""import numpy as np"""
"""import matplotlib.pyplot as plt 
data=[40,45,47,48,50,51,52,53,55,59]
mean=np.mean(data)
print(mean)
sd=np.std(data)
print(sd)
r=np.random.normal(mean,sd,100)
plt.hist(data,bins=100)
plt.show()"""
"""import numpy as np
import matplotlib.pyplot as plt
n=np.random.normal(500,50,1000)
plt.hist(n,bins=10)
plt.show()"""
"""import numpy as np
import matplotlib.pyplot as plt
data=[40,45,48,49,50,51,52,55,60]
mean=np.mean(data)
median=np.median(data)
plt.hist(data,bins=5)
plt.show()"""
"""import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(50,10,1000)
plt.hist(data,bins=30)
plt.show()"""
"""import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(100,20,500)
plt.hist(data,bins=5)
plt.show()"""
"""mean=50000
sd=5000
v=60000
z=(v-mean)/sd
print(z)
"""
"""mean=100
sd=15
sd1=("68%",mean-sd,mean+sd)
sd2=("95%",mean-(2*sd),mean+(2*sd))
sd3=("99.7%",mean-(3*sd),mean+(3*sd))
print(sd1)
print(sd2)
print(sd3)"""
"""a=0
b=20
un=1/(b-a)
print(un)
ab=10-5
pdf=un*ab
print(pdf)"""
"""a=10
b=30
u=1/(b-a)
p=u*(20-15)
print(p*100)"""
"""a=0
b=20
c=5
d=15
app=(d-c)/(b-a)
print(app)"""
"""a=10
b=50
c=20
d=30
A=(d-c)/(b-a)
print(A)"""
"""import numpy as np
data=np.random.normal(100,500,1000)
print(data[:10])
a=(300-200)/(500-100)
print(a)"""
"""a=1/5
b=1/a
print(a,b)"""
"""r=1/10
rr=1/r
print(rr)"""
"""import numpy as np
l=1/10
lam=l
print(lam)
x=5
p=1-np.exp(-lam*x)
print(p)"""
"""import numpy as np
lam=1/8
print(lam)
a=1/lam
print(a)"""
"""import numpy as np
lam=0.2
x=5
p=1-np.exp(-lam*x)
print(p)"""
"""import numpy as np
l=0.1
t=10
p=1-np.exp(-l*t)
print(p)"""
"""import numpy as np
l=0.2
t=5
p=np.exp(-l*t)
print(p)"""
"""import numpy as np
lab=0.2
s=3
t=4
right=np.exp(-lab*(s+t))/np.exp(-lab*s)
print(right)
left=np.exp(-lab*t)
print(left)"""
"""import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(0,1,1000)
plt.hist(data,bins=10)
plt.show()"""
"""x=800
m=500
sd=100
z=(x-m)/sd
print(z)
m=40000
sd=5000
sd1=(m-sd,m+sd,"68%")
sd2=(m-(2*sd),m+(2*sd),"95%")
sd3=(m-(3*sd),m+(3*sd),"99.7%")
print(sd1,sd2,sd3)"""
"""a=2
b=10
u=1/(b-a)
print(u)
A=2
B=10
C=8
D=10
p=(D-C)/(B-A)
print(p)"""
"""a=2
b=12
pdf=1/(b-a)
c=5
d=8
dc=d-c
p=pdf*dc
print(p*100)
ap=(d-c)/(b-a)
print(ap*100)"""
"""import numpy as np
lam=5
print("lambda",lam)
avr=(1/5)
print("average time",avr)
time=10/60
p=1-np.exp(-lam*time)
print(p*100)
"""
"""lab=3
time=10/60
p=np.exp(-lab*time)
print(p)"""
"""import numpy as np
data=[400, 500, 600, 450, 550]
sample=np.mean(data)
population=sample
print("mean sample",sample)
print("mean population",population)
"""
"""import numpy as np
data=[10, 20, 30, 40, 50, 60]
sample=np.mean(data)
population=sample
print(sample,"=sample mean")
print(population,"=poplation mean and actual value")"""
"""import numpy as np
truemean=80
data=[75,85,78,82,80]
est=np.mean(data)
print(truemean,est)
if est==truemean:
    print("unbaised")
else:
    print("biased")"""
"""import numpy as np
true=100
data= [95, 105, 98, 102]
avg=np.mean(data)
print(true,avg)
if avg==true:
    print("unbased")
else:
    print("biased")"""
"""import numpy as np
true=100
data = [110, 115, 105, 120]
avg=np.mean(data)
print(true,avg)
if avg==true:
    print("unbised")
else:
    print("baised")"""

"""import numpy as np
true=100
samples=[[80,100],[90,100,95,105],[98,100,99,101,102],[99,100,100,101,99,100,100,101,99,100]]
for sample in samples:
    estimate=np.mean(sample)
    print(len(sample),estimate)"""
"""import numpy as np
true=1000
sampledata={
    10:700,
    50:850,
    100:950,
    500:980,
    1000:995
}
for i,j in sampledata.items():
    print(i,j)"""
"""import numpy as np
true=100
EstimatorA=[80, 120, 90, 110]
EstimatorB=[95, 105, 98, 102]
A=np.var(EstimatorA)
B=np.var(EstimatorB)
print(A,B)
if A<B:
    print("A efficent")
else:
    print("Beffient")"""
"""import numpy as np
true=50
A = [45, 55, 48, 52]
B = [40, 60, 45, 55]
a=np.var(A)
b=np.var(B)
print(a,b)
if a<b:
    print(a,"is efficent")
else:
    print(b,"is efficient")"""
"""import numpy as np
data = [20, 25, 30, 35, 40]
mean=np.mean(data)
vari=np.var(data,ddof=1)
pv=np.var(data)
print(mean,vari,pv)"""
"""import numpy as np
data = [10, 20, 30, 40, 50, 60]
s=np.std(data,ddof=1)
n=len(data)
se=s/np.sqrt(n)
print(s,n,se)"""
"""import numpy as np
spending = [420, 450, 480, 500, 520, 550, 580, 600]
sm=np.mean(spending)
sd=np.std(spending,ddof=1)
size=len(spending)
print(size)
sde=sd/np.sqrt(size)
print(sm,sd,sde)"""
"""import numpy as np
true=100
estimates = [95, 105, 98, 102]
m=np.mean(estimates)
print(m,true)
if m==true:
    print("ubaised")
else:
    print("biased")"""
"""import numpy as np
true=500
data={
    10:55,
    100:52,
    1000:50,
    5000:50
}
for i,j in data.items():
    print(i,j)"""
"""import numpy as np
A=[90, 110, 95, 105]
B=[98, 102, 99, 101]
a=np.var(A)
b=np.var(B)
print(a,b)
if a<b:
    print(a,"efficent")
else:
    print("efficent",b)"""
"""You take a sample of 64 students:

Sample mean = 73
Population standard deviation = 12
Significance level = 0.05"""
"""import numpy as np
from scipy.stats import norm
sm=73
psd=12
psm=70
n=64
a=0.05
z=(sm-psm)/(psd/ np.sqrt(n))
print(z)
pvalue= 2 * (1 - norm.cdf(abs(z)))
print(pvalue)
if pvalue<a:
    print("reject H0")
else:
    print("fail to reject h1")
    A company claims that the average production time is 50 minutes.

You collect a sample of 100 products:

Sample mean = 52 minutes
Population standard deviation = 10 minutes
Significance level = 0.05"""
"""import numpy as np
from scipy.stats import norm
pm=50
psd=10
sm=52
n=100
a=0.5
z=(sm-pm)/(psd/ np.sqrt(n))
print(z)
pvalue=2*(1 - norm.cdf(abs(z)))
print(pvalue)
if pvalue<a:
    print("reject h0")
else:
    print("fail ti reject")"""
"""pvalue = 0.03
a= 0.05
if pvalue<a:
    print("reject")
else:
    print("fail to reject")"""
"""Company claims average delivery time = 40 minutes.

Population SD = 8
Sample mean = 42
n = 64
a = 0.05"""
"""import numpy as np
from scipy.stats import norm
pm=40
psd=8
sm=42
n=64
a=0.05
z=(sm-pm)/(psd/np.sqrt(n))
print(z)
pvalue=2*(1-norm.cdf(abs(z)))
print(z,pvalue)
if pvalue<a:
    print("reject")
else:
    print("fail to reject")"""
"""import scipy.stats as ttest_1samp
data = [72, 68, 75, 71, 69, 74, 73, 70]
result=ttest_1samp(data,70)
print(result.statistic)
print(result.pvalue)"""
"""from scipy.stats import ttest_1samp
data = [9, 11, 10, 12, 8, 9, 11, 10]
r=ttest_1samp(data,10)
print(r.statistic)
print(r.pvalue)
if r.pvalue<0.05:
    print("reject")
else:
    print("fail to reject")"""
"""from scipy.stats import ttest_ind
A=[10, 12, 11, 13, 10]
B=[15, 16, 14, 17, 15]
stats,pvalue=ttest_ind(A,B)
print(stats,pvalue)
if pvalue<0.03:
    print("reject h0")
else:
    print("fail to reject")"""
"""import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(100,20,500)
plt.hist(data,bins=5)
plt.show()"""
"""import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 50
sd = 10

x = np.linspace(mean - 4*sd, mean + 4*sd, 1000)
y = norm.pdf(x, mean, sd)

plt.plot(x, y)
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.title("Normal Distribution")
plt.show()"""
"""import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 20

x = np.linspace(a, b, 100)
y = 1 / (b - a)

plt.plot(x, [y] * len(x))
plt.xlabel("Values")
plt.ylabel("Probability Density")
plt.title("Uniform Distribution")
plt.show()"""
import numpy as np
true=50
data=[48,52,49,51,50]
a=np.mean(data)
print(a,true)
if a==true:
    print("unbiaseness")
else:
    print("biaseness")
    



































