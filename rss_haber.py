import feedparser

url="http://cnnturk.com/feed/rss/news"

haberler=feedparser.parse(url)

i=0
for haber in haberler.entries:
    i +=1
    print(i,haber.title)
    print(haber.link)
  #  print(haber.summary)
    print("\n")
    
    
