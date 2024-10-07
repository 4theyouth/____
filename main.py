import href
import price
import price3
import sku

searchList = sku.get()

for search in searchList:
    hrefList = href.get(search)
    for hrefLink in hrefList:
        try: price3.get(hrefLink)
        except:
            try: price.get(hrefLink)
            except: pass