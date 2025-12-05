import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import pyfiglet


ascii_banner = pyfiglet.figlet_format('Name2Mail', font="slant")
print("\n", "-"*100, "\n")
print(ascii_banner)
print("Un tools fait pour générer des mails, en fonction des informations fournies par Vous! "
      "\nVous récupérer toutes les informations dans info.txt."
      "\nCréer par théorick")
print("\n", "-"*100, "\n")

def run(playwright: Playwright) -> None:
    emails_list = ["hotmail.com", "outlook.com", "gmail.com", 'yahoo.com', 'protonmail.com']

    nom = str(input('Nom a rechercher : '))
    prenom = str(input('Prenom a rechercher :'))
    info_spmt = str(input('Information a rechercher : '))
    nom_fichier = 'info.txt'
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url2 = f"https://www.ecosia.org/search?method=index&q=test"
    page.goto(url2)

    try:
        page.get_by_role("button", name="Tout accepter").click()
    except:
        print()
    while True:
        email_empty = 0
        with open(nom_fichier, 'a', buffering=1) as fichier:
            for email in emails_list:
                url2 = f"https://www.ecosia.org/search?method=index&q={prenom}+{nom}+{info_spmt.replace(" ", "+")}+intext:\"{email}\""
                page.goto(url2)


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
                        time.sleep(2)
                    else:

                        emails_list  = list(set_emails)

                        for i in emails_list:

                            print(i)
                            time.sleep(1)

                        email_empty = 0
                except AttributeError:
                    emails = '*'
                    print("Email pas trouver")
                for email in list(set_emails):
                    emails = str(email)+ "\n"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


