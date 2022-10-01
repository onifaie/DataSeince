from email import header
from requests_html import HTMLSession

session= HTMLSession()

# HEADER={
#     'user-agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }

page=session.get('https://www.futurelearn.com/courses')

print(page)
all_products=page.html.find('div.Content-wrapper_1O_KH')
# print(all_products)


for product in all_products:
    # product_page=session.get(product)
    product_name=product.find('div.label-wrapper_G7pLG',first=True).text
    product_Title=product.find('div.Title-wrapper_11axP',first=True).text

    print(product_name)
    print(product_Title)
    print("==============================")
    
#     product_name=product_page.html.find('//*[@id="popular-courses-smoke-test"]/div/div[1]/a',first=True).text
#     print(product_name)
    