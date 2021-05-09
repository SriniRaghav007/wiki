import wikipedia
query=input('Enter your search questions\n')
wiki(query)
lat=float(input('Enter Latitude\n')) 
lon=float(input('Enter Longitude\n'))
wikigeo(lat,lon)
def wiki(query):
    l=wikipedia.search(query, results=10, suggestion=False)
    print(l)
    print(wikipedia.summary(l[0], sentences=0, chars=0, auto_suggest=False, redirect=True))
def wikigeo(lat,lon):
    l1=wikipedia.geosearch(lat, lon,title=None, results=10, radius=1000) 
    print(l1)
    print(wikipedia.summary(l1[0], sentences=0, chars=0, auto_suggest=False, redirect=True))
