from bs4 import BeautifulSoup, ResultSet
import requests
import os


"""
# Program will ask for link of target webpage, will extract contents and next it will ask for the file name to save with
# then it will save the file to the "./Unstructured_data/<selected folder>/<filename>.txt" directory with 
# given file name in .txt format
"""


class Utils:
    @staticmethod
    def askYesNo(prompt):
        posCorrectAnswers = ["y", 'yes']
        negCorrectAnswers = ["n", "no"]
        answeredCorrect = False
        userAns = str(input(prompt + " ( enter Y/N ): "))

        if posCorrectAnswers.__contains__(userAns.lower()) or negCorrectAnswers.__contains__(userAns.lower()):
            answeredCorrect = True

        while not answeredCorrect:
            print("\nPlease enter your answer as \"Y\" for yes and \"N\" for no")
            userAns = input(prompt + " ( enter Y/N ): ")
            if posCorrectAnswers.__contains__(userAns.lower()) or negCorrectAnswers.__contains__(userAns.lower()):
                answeredCorrect = True

        if posCorrectAnswers.__contains__(userAns.lower()):
            return True
        else:
            return False

    @staticmethod
    def askFolderChoiceFromDir(dirPath):
        x = next(os.walk(dirPath))
        subFoldersIter = filter(lambda dirName: not dirName.startswith("."), x[1])
        print("Select a folder number: ")

        subFolders = list(subFoldersIter)

        i = 0
        for n in subFolders:
            print(f'[{i}] {n}')
            i += 1

        return dirPath + "/" + subFolders[int(input("\nenter folder number: "))]

    @staticmethod
    def writeToTxtFile(pathToDestinationDir, fileName, listOfContent):
        if pathToDestinationDir[-1] == "/":
            pathToDestinationDir = pathToDestinationDir[0:-1]

        with open(f'{pathToDestinationDir}/' + fileName + ".txt", "w", encoding="utf-8") as fl:
            for items in listOfContent:
                fl.write(items + "\n")


class WebPageScrapper:
    def scrapPage(self, pageLink, extractFiltered):
        try:
            response = requests.get(pageLink)
            articles: ResultSet

            if response.status_code == 200:
                webPage = response.text
                soup = BeautifulSoup(webPage, "html.parser")
                articles = soup.find_all(name="p")
            else:
                raise Exception(
                    "Unexpected error !, Possible reasons:\n\tNo Internet\n\tWeb page doesn't responded\n\tWrong Url ")

            if extractFiltered:
                return self.extractContentRelatedToLucknow(articles)
            else:
                return self.extractContentUnfiltered(articles)

        except Exception as e:
            print("Error: \n", e)

    """ extractContentRelatedToLucknow():-
     Extracts content that is very related to lucknow so at least contains one of following words( to reduce unrelated data ):
     like: "Lucknow", "Uttar Pradesh", "India", "Awadh", "hindustan", "bharat"
     content contains only 10% unrelated data on average 
    """
    def extractContentRelatedToLucknow(self, articles: ResultSet):
        article_texts = []
        for article_tag in articles:
            text: str = article_tag.getText()
            if self.containsNarrowKeywords(text) or( self.containsBroadKeywords(text) and text.__len__() > 50):
                article_texts.append(text)

        return article_texts

    """ extractContentUnfiltered():-
     Extracts content all the content without any filter ( except line that is at least 40 characters long )
     extracted content contains on average 30% unrelated data like ads, disclaimers, CTO, etc
    """
    def extractContentUnfiltered(self, articles: ResultSet):
        article_texts = []
        for article_tag in articles:
            text = article_tag.getText()

            if text.__len__() > 40:
                article_texts.append(text)

        return article_texts

    def containsNarrowKeywords(self, text: str):
        narrowKeywords = ["lucknow", "uttar pradesh", "awadh", "awadhi", ]
        for keys in narrowKeywords:
            if text.lower().__contains__(keys):
                return True

        return False

    def containsBroadKeywords(self, text: str):
        broadKeywords = ["india", "bharat", "bharata"]
        for keys in broadKeywords:
            if text.lower().__contains__(keys):
                return True

        return False

# ##==================##


def main():
    print("\n\t\t=====:::: WebPage Scrapper :::======\n")
    targetWebPageLink = str(input("Enter link to the target webpage: "))

    isFilteredScrap = Utils.askYesNo(
        "Would you like to extract filtered content (i.e. with less unrelated data to India, Lucknow) ?")
    fileName = str(input("Enter file name for extracted content: "))

    print("Select the target folder, ", end="")
    folderOfExtraction = Utils.askFolderChoiceFromDir("./Unstructured_data")
    Utils.writeToTxtFile(folderOfExtraction, fileName, WebPageScrapper().scrapPage(targetWebPageLink, isFilteredScrap))
    print("Content extracted to: ", f"{folderOfExtraction}/{fileName}.txt")


main()


## After executing using inputs used in following example, content
# will be extracted to "./Unstructured_data/Tourism_Lucknow" directory's lkoTrip.txt file

"""
Example execution I/O:


		=====:::: WebPage Scrapper :::======

Enter link to the target webpage: https://theculturetrip.com/asia/india/articles/the-top-10-things-to-see-do-in-lucknow
Would you like to extract filtered content (i.e. with less unrelated data to India, Lucknow) ? ( enter Y/N ): Y
Enter file name for extracted content: lkoTrip
Select the target folder, Select a folder number: 
[0] Arts_and_Crafts
[1] Education_System_in_Lucknow
[2] Facts_About_Lucknow
[3] Food_of_lucknow
[4] Market_of_Lucknow
[5] Monuments
[6] overview_of_lucknow
[7] Tourism_Lucknow

enter folder number: 7
Content extracted to:  ./Unstructured_data/Tourism_Lucknow/lkoTrip.txt 

"""