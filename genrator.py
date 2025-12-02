import random
import time
from faker import Faker
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

finition = ["hotmail.com", "outlook.com"]
cryptos = ['bitcoin', 'litecoin', 'bitcoin cash', 'etherum', 'etherum fork']




def run(playwright: Playwright) -> None:
    nom_fichier = 'btc_binance.txt'
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    while True:
        email_empty = 0
        with open(nom_fichier, 'a', buffering=1) as fichier:
            for i in finition:
                for crypto in cryptos:
                    fake = Faker()
                    nom = fake.name()
                    url2 = f"https://www.ecosia.org/search?method=index&q={nom.replace(' ', '+')}+{crypto}+intext:\"{i}\"+before:2019+after:2015"


                    page.goto(url2)


                    try:
                        page.get_by_role("button", name="Tout accepter").click()
                    except:
                        print()
                    r = random.randint(0,5)
                    time.sleep(r)

                    # Récupérer le HTML de la page
                    html_content = page.content()

                    # Parser le HTML avec BeautifulSoup
                    soup1 = BeautifulSoup(html_content, 'html.parser')

                    try:
                        set_emails = set()

                        # Parcourir toutes les balises contenant des classes
                        for element in soup1.find_all(class_=True):
                            # Extraire le texte de chaque élément
                            text = element.get_text()
                            # Trouver et ajouter les emails uniques dans set_emails
                            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
                            for email in emails:
                                set_emails.add(email)
                        if list(set_emails) == []:
                            email_empty = email_empty + 1
                            print("Email empty : ", email_empty)
                        else:

                            emails_list  = list(set_emails)
                            print(nom)
                            for i in emails_list:

                                print(i)
                                time.sleep(1)

                            email_empty = 0
                    except AttributeError:
                        emails = '*'
                        print("Email pas trouver")
                    for email in list(set_emails):
                        emails = str(email)+ "\n"
                        fichier.write(emails)



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


