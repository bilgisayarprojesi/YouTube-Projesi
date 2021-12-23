from pytube import YouTube

url = input("Video Bağlantısını Giriniz:")
yt = YouTube(url)

if yt.length > 120:
    question = input("Videoyu İndirmek İstiyor Musunuz? (Evet/Hayır): ")
    if question == "Evet":
        print("Video İndiriliyor...")
    else:
        print("Video İndirilmeye İzin Verilmedi Veya Yanlış Komut Yazıldı")

video1 = yt.streams.filter(progressive=True).get_by_itag(22)
video1.download()

print("***************************************************************")
print("Video İndirildi")
print("Video Başlığı:", yt.title)
print("Thumbnail Resmi:", yt.thumbnail_url)
print("Video Sahibi:", yt.author)
print("Video Rating:", yt.rating)
print("Video Uzunluğu:", yt.length)
print("İzlenme Sayısı:", yt.views)
print("***************************************************************")
print("Video Açıklaması:", yt.description)
print("***************************************************************")
