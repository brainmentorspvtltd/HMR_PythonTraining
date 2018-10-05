import bs4
import urllib.request as url

web = url.urlopen('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f299869f-a183-4a64-a887-6491356429b6&pf_rd_r=PPV4Z7BZB5BH0RJDV42N&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1')

data = bs4.BeautifulSoup(web, 'lxml')

result = data.find_all('td', class_='titleColumn')
#print(result)

for name in result:
    print(name.text)
