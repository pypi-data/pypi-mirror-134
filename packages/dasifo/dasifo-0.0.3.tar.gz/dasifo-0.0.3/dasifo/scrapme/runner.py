import requests
from bs4 import BeautifulSoup

global URL
URL = "https://www.cora.fr/"


def set_url(url):
    """ define our default website url. """
    URL = url

def __request_html_page_and_parse(link):
    try:
        page = requests.get(link)
        return BeautifulSoup(page.content, "html.parser")
    except:
        print("HTML page not reachable! it could be not found or due to bad Network ... !")

def faire_mes_courses():
    """
        we want to list all products categories on this website.
        all produits are grouped by category for example: Animaux, Bébé, .....
        returns: array of categories that we will request for!
    """
    soup = __request_html_page_and_parse(URL)
    arr = []
    # find the navigation header of products
    lis = soup.nav.find_all("li", class_="c-list__item c-header-menu__nav-list-item")
    for li in lis:
        arr.append(li.find().attrs['href'])
    return arr


def sub_categories(of=None):
    """
    :param of: a string to be added to our url link then request html page
    :return: an array of subcategories that filters the products
    """
    if not isinstance(of, str):
        return []
    arr = []
    soup = __request_html_page_and_parse(URL+ of)
    lis = soup.nav.find_all("li", class_="c-list__item c-header-menu-layer__category")
    for li in lis:
        arr.append(li.find().attrs['href'])
    return arr

def get_products(link, only_priced=True):
    """
    :param link: url to be requested with HTTP (GET method)
    :param only_priced: True, False, None
        if True, we will only extract the products with a price.
        if False, extract the products which haven't a price.
        else, we return all the list of products.
    :return: a list of dicts, each dict represents a product described by : name, price, image
    """
    products = []
    soup = __request_html_page_and_parse(link)

    # we search for all products in the html page by looking to all li elements with class attribute
    by_class = "c-list__item c-product-list-container-products__item c-product-list-container-products__item--grid"
    li_products = soup.find_all("li",
                             class_=by_class)

    # we iterate all products found in our html page
    for pr in li_products:
        new_product = {}
        name = pr.find('a', class_="c-link-to c-product-list-item--grid__title c-link-to--hover-primary-light")
        new_product['name'] = name.get_text().replace("\n", ' ').strip()
        new_product['image'] = pr.find('img').attrs['src']
        try:  # is there any price in this product? if not, it ll throw an error
            price = pr.find('p', class_="c-price__amount")
            new_product['price'] = float(price.findChild().get_text().replace("\n", ' ').strip().replace(',', '.'))
        except:
            if only_priced == False:
                products.append(new_product)

        if only_priced != False and 'price' in new_product.keys():
            products.append(new_product)
    return products

def list_of_products(link="https://www.cora.fr/faire_mes_courses/animaux/chats/hygienesoin_et_accessoires_chat-c-176673", max_pages=None, only_priced=True):
    """
    we will ieterate all paginated pages that lists our products.
    :param link: url to be requested with HTTP (GET method)
    :param max_pages: limit the number of html pages to look at
    :param only_priced: True, False, None
        if True, we will only extract the products with a price.
        if False, extract the products which haven't a price.
        else, we return all the list of products.
    :return: a list of dicts, each dict represents a product described by : name, price, image
    """
    all_products = []
    i = 1
    if not isinstance(max_pages, int):
        # just trying to limit the number of html pages to look at
        max_pages = i
    while i!=0 and i <= max_pages: # ?? we can add a param to satisfy the limit number of paginations
        products = get_products(link+"?pageindex="+str(i), only_priced=only_priced)
        i += 1
        if any(products):
            all_products += products
        else:
            i == 0 # to exit the while loop because there are no products anymore
    return all_products

if __name__ == '__main__':
    print(list_of_products(max_pages=3))