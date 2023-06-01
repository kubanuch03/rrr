import csv

import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from main import engine, Laptop



Session = sessionmaker(bind=engine)

LINK_KIVANO = "https://www.kivano.kg/noutbuki"
HEADERS = {
    "user-agent": "ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "accept": "*/*",
}
IMAGE_MAIN_LINK = "https://www.kivano.kg"


def get_html(link, headers):
    response = requests.get(link, headers=headers)
    return response


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll("div", class_="item product_listbox oh")
    laptops = []
    for i in data:
        title = i.find("div", class_="listbox_title oh").text
        laptops.append({
            "title": title.replace("\n", ""),
            "description": i.find("div", class_="product_text pull-left").
                text.replace(title, "").strip().replace("\xa0", ""),
            "image": IMAGE_MAIN_LINK + i.find("img").get("src"),
            "price": i.find("div", class_="listbox_price text-center").text.replace("\n", ""),
        })
    return laptops


def save_file(content):
    with open("laptops.csv", "w") as file:
        laptop_writer = csv.writer(file, delimiter=',')
        titles = ["Название", "Описание", "Картинка", "Цена"]
        laptop_writer.writerow(titles)
        for i in content:
            laptop_writer.writerow([
                i.get("title"),
                i.get("description"),
                i.get("image"),
                i.get("price"),
            ])



def save_db(content):
    for i in content:
        with Session() as session:
            laptop = Laptop(title=i.get("title"),
                            description=i.get("description"),
                            image=i.get("image"),
                            price=i.get("price"))
            session.add(laptop)
            session.commit()


def get_parse():
    html_response = get_html(LINK_KIVANO, HEADERS)
    if html_response.status_code == 200:
        save_db(get_content(html_response.text))


get_parse()