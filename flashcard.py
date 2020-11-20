# -*- coding: utf-8 -*-
inputFile = str(input("input file : "))
outputFile = str(input("output file : "))

import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import urllib.request

def getTraduction(url):
    urllib.request.urlretrieve(url, "webpage.html")
    #A chercher dans : <p class="googleTranslate_section_text" lang="fr"><span class="ng-star-inserted">ville</span>
    fichier = open("webpage.html","r")
    fichier.close()


def getImagesFromURL(url):
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        imgURL = img.attrs.get("src")
        if not imgURL:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        imgURL = urljoin(url, imgURL)
        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = imgURL.index("?")
            imgURL = imgURL[:pos]
        except ValueError:
            pass
        urls.append(imgURL)
    return urls

word = list()
picture = list()

print("Starting compilation ...")
file = open(inputFile,"r")
content = file.readlines()
file.close()
file = open(outputFile,"w")
file.write("<table><thead><tr><th colspan=\"2\">The daily vocabulary</th></tr></thead><tbody>")
for line in content:
    res = getImagesFromURL("https://fr.glosbe.com/ru/fr/" + line)[3]
    file.write("<tr>")
    file.write("<td>"+line+"</td>")
    word.append(line)
    picture.append(res)
    file.write("<td><img src=\"" + res + "\"></td>")
    file.write("</tr>")
file.write("</tbody></table>")
file.close()
print("Compilation ended !")

rep = str(input("Create an ANKI csv ? (y): "))
if rep == "y":
    file = open("ANKI.csv","w")
    for i in range(len(word)):
        file.write(word[i].replace("\n", "") + ";<img src=\"" + picture[i] + "\">\n")
    file.close()
    print("ANKI file created as ANKI.csv !")
