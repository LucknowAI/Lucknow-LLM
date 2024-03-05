from bs4 import BeautifulSoup
import requests

###
# Program will ask for link of target webpage, will extract content and then it will ask for the file name to svae with
# then it will save the file to the "./Unstructured_data/<filename>.txt" directory with given file name and .txt format
###

print("Paste website link: ", end= "")
websiteToScrap = str(input())

response = requests.get(websiteToScrap)
webPage = response.text
soup = BeautifulSoup(webPage, "html.parser")
articles = soup.find_all(name="p")

# extracts content that is very related to lucknow so at least contains one of following words( to reduce unrelated data ):
# "Lucknow", "Uttar Pradesh", "India", "Awadh", "hindustan", "bharat"
# content contains only 10% unrelated data on average
def extractContentRelatedToLucknow():
    article_texts = []
    for article_tag in articles:
        text = article_tag.getText()

        if (
                text.__contains__("Lucknow") or text.__contains__("Uttar Pradesh")
                or text.__contains__("lucknow") or text.__contains__("uttar pradesh") or text.__contains__("Awadh")
                or text.__contains__("awadh") or (text.__contains__("India") and text.__len__() > 50)
                or (text.__contains__("Bharat") and text.__len__() > 50) or (text.__contains__("Bharata") and text.__len__() > 50)
                or (text.__contains__("bharat") and text.__len__() > 50) or (text.__contains__("bharata") and text.__len__() > 50)
        ) and text.__len__() > 30:
            article_texts.append(text)

    return article_texts


# extracts content all the content without any filter ( except line that is at least 40 characters long )
# extracted content contains on average 30% unrelated data like ads, disclaimers, CTO, etc
def extractContentUnfiltered():
    article_texts = []
    for article_tag in articles:
        text = article_tag.getText()

        if text.__len__() > 40:
            article_texts.append(text)

    return article_texts


## Select any one method of extraction ( just uncomment req. one and comment other one )
#
# articleExtracts = extractContentUnfiltered()
articleExtracts = extractContentRelatedToLucknow() ## Recommended For better content

print("Enter file name for extracted data (eg: myFile): ", end="")
extractFileName = str(input())

with open( "./Unstructured_Data/"+extractFileName+".txt", "w", encoding= "utf-8") as fl:
    for items in articleExtracts:
        fl.write( items + "\n" )
