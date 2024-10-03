import href
import price
import sku

searchList = sku.get()

for search in searchList:
    hrefList = href.get(search)
    for hrefLink in hrefList:
        try: price.get(hrefLink)
        except: pass