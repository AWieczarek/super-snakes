from urllib.request import Request, urlopen
import re

print("Witaj w programie do pobierania artykułów ze strony TestHub.pl")

n = int(input("Podaj liczbe podstron do pobrania(max 207): "))

if n<207 and n>0:
    f = open("artykuly.txt", "w", encoding='utf-8')
    print("Pobieram...")
    for subsite in range(n):
        path = "https://testhub.pl/page/"+str(subsite+1)+"/"
        req = Request(path, headers={'User-Agent': 'Mozilla/5.0'})

        html = urlopen(req).read().decode('utf-8')
        articles = re.findall(r'<a href="([A-za-z0-9\-/.,:\?\=\&]+)" class="post-title">',html)
        titles = re.findall(r'<h2>([\s\S]*?)</h2>',html)

        for x, title in zip(articles,titles):
            path2 = Request(x , headers={'User-Agent': 'Mozilla/5.0'})
            html2 = urlopen(path2).read().decode('utf-8')
            descriptions = re.findall(r'<p>(.*?)</p>',html2)
            subtitles = re.findall(r'<h2>(.*?)</h2>',html2)
            title = re.sub('&nbsp;', ' ', title)
            f.write(title+'\n\n')

            for subtitle in subtitles:
                subtitle = re.sub('&nbsp;', ' ', subtitle)
                f.write(subtitle+'\n\n')

            for description in descriptions:
                description = re.sub('&nbsp;', ' ', description)
                temp = re.compile('<.*?>')
                description = re.sub(temp, '', description)
                description
                f.write(description+'\n\n')
            
            f.write('\n\n')
    print("Pobralem!")
    f.close()
    print("Artykuły zostały zapisane w pliku artykuly.txt w biezacym katalogu")
else:
    print("Bledna liczba podstron")
