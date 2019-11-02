import sys, os, requests, urllib2
from bs4 import BeautifulSoup

menu_actions  = {}
def main_menu():
    os.system('clear')
    print "Autor: Pawel Wrzosek"
    print "Grupa: 17I2"
    print "Nr albumu: 632"
    print " "
    print " "
    print "-------------------------------------------------------------"
    print "Wcisnij [1] aby wygenerowac Piramide"
    print "Wcisnij [2] aby sprawdzic status wybranej strony www"
    print "Wcisnij [3] aby wypisac view-source strony www"
    print "Wcisnij [4] aby wyszukac zawartosc tekstowa tagow HTML dowolnej strony"
    print "Wcisnij [5] aby wypisac adresy odnoscnikow"
    print 'Wcisnij [0] aby zakonczyc program'
    print "-------------------------------------------------------------"
    choice = raw_input(" Szymon mowi: ")
    exec_menu(choice)
    return
#Wykonanie menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Twoj wybor jest niepoprawny\n"
            menu_actions['main_menu']()
    return
# Menu 1 Piramida
def menu1():
    print "Piramida\n"
    def trojkat():
        rows = input("Wpisz liczbe wierszy: ")
        for i in range (rows):
            print ' '*(rows-i-1) + '*'*(2*i+1)
    trojkat()
    print "[9] Cofnij"
    print "[0] Zakoncz"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
# Menu 2 Status www
def menu2():
    print "Status strony www\n"
    print "Podaj nazwe strony (sama domene, bez http:// albo www.)"
    strona = raw_input()
    try:
        r = requests.head("http://" + strona)
        print strona + " " + "ma status: "
        print (r.status_code)
        print " "
        print " "
        print " "
    except requests.ConnectionError:
        print("Strona nieaktywna")
        print " "
        print " "
        print " "
    print "[9] Cofnij"
    print "[0] Zakoncz"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
def menu3(): #Menu 3 zrodlo strony
    print "view-source www\n"
    print "Podaj nazwe strony (sama domene, bez http:// albo www.)"
    html = raw_input()
    url = 'http://'+html
    response = urllib2.urlopen(url)
    webContent = response.read()
    print(webContent)

    print "[9] Cofnij"
    print "[0] Zakoncz"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
def menu4():#Menu 4 zawartosc tagu HTML
    print "Podaj nazwe strony (sama domene, bez http:// albo www.)"
    www = raw_input()
    url = "http://" + www
    content = urllib2.urlopen(url).read()
    zawartosc = BeautifulSoup(content)
    print "Podaj tag html do odszukania, np = (a h2 title) itp.:"
    tag = raw_input()
    print " "
    print " "
    print " "
    print "---Wyniki---"
    print " "
    print " "
    print " "
    suma = 0
    for el in zawartosc.find_all(tag):
        suma = suma + 1
        print el.getText()
    print " "
    print " "
    print " "
    print "------------"
    print " "
    print " "
    print "-------------------------Podsumowanie-------------------------"

    print "Suma linkow to: ", suma
    print "--------------------------------------------------------------"
    print " "
    print "[9] Cofnij"
    print "[0] Zakoncz"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
def menu5():#Menu 5 Linki strony www
    print "Podaj nazwe strony (sama domene, bez http:// albo www.)"
    adres = raw_input()
    adreswww = "http://" + adres
    url = urllib2.urlopen(adreswww).read()
    soup = BeautifulSoup(url)
    print " "
    print " "
    print " "
    print "---Wyniki---"
    print " "
    print " "
    print " "
    with open('linki.html', 'a') as f:
        f.write("<ul>")
    suma = 0
    for line in soup.find_all('a'):
        suma = suma + 1
        print(line.get('href'))
        text = line.get('href')
        with open('linki.html', 'a') as f:
            f.write("<li>" + text + "<li/>")
    with open('linki.html', 'a') as f:
        f.write("</ul>")
    print " "
    print " "
    print " "
    print "------------"
    print " "
    print " "
    print " "
    print "-------------------------Podsumowanie-------------------------"
    print "Zapisano do linki.html"
    print "Suma linkow zapisanych to: ", suma
    print "--------------------------------------------------------------"
    print " "
    print " "
    print " "
    print "[9] Cofnij"
    print "[0] Zakoncz"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
#Powrot do menu
def back():
    menu_actions['main_menu']()
#Zamkniecie programu
def exit():
    sys.exit()
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '9': back,
    '0': exit,
}
if __name__ == "__main__":
    main_menu()
