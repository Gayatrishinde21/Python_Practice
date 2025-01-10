# list -> data stucture which can hold multiple values of multiple type
# array -> data stucture which can hold multiple values of same type

list_of_cloud = ["aws", "gcp","azure","oracle","alibaba","utho","digital ocean"]
cloud = "gcp"  #variable

print(list_of_cloud)

# add new cloud salesforce

list_of_cloud.append("salesforce")

# add new cloud IBM

list_of_cloud.append("IBM") #adds to the end of list

print(list_of_cloud)

list_of_cloud.insert(2,"Heroku") #Insert in the list

print(list_of_cloud)

print(len(list_of_cloud)) 

#list index starts from 0,1

list_of_cloud.insert(0,"Hello")

print(list_of_cloud)

#Iteration of list
for cloud in list_of_cloud:
    print(" ")
    print(cloud)

for i in range(1,10):
    print(i)

for i in range(1,10):
    print("Hello Gayatri")