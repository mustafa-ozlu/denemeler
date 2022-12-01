from pytube import YouTube

while True:
    print("\n     Çıkmak için --> Q 'ya basın   ")
    link=input("     Youtube URL'sini girin : ")
    
    if link.upper()=="Q" :
        break;
    
    else:
        yt=YouTube(link)
        
        print("Kanal Sahibi\t:",yt.author)
        print("Video Başlığı\t:",yt.title)
        print("İzlenme Sayısı\t:",yt.views)
        print("Paylaşım Tarihi\t:",yt.publish_date)
        
        yd=yt.streams.get_highest_resolution()
        
        yd.download('./video')
    