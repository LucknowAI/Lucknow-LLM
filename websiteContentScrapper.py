from bs4 import BeautifulSoup
# import lxml
import requests

# replace string with your target website's link
websiteToScrap = "https://www.clubmahindra.com/blog/stories/10-must-visit-architectural-marvels-in-lucknow"

## Some websites to test scrapping
# "https://www.voguebusiness.com/beauty/why-indias-beauty-market-is-turning-heads")
# "https://www.britannica.com/place/Lucknow")

response = requests.get(websiteToScrap)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
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

articleExtracts = extractContentRelatedToLucknow()

print("Enter file name for extracted data (eg: myFile): ")
extractFileName = str(input())

with open( "./Unstructured_Data/"+extractFileName+".txt", "w", encoding= "utf-8") as fl:
    for items in articleExtracts:
        fl.write( items + "\n" )

# for items in articleExtracts:
#     print(items)