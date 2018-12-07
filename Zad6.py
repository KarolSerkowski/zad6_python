import tkinter as tk
from tkinter import filedialog as fd
import os
import glob
import csv


from tkinter import messagebox as msb


class Application:

    directory = ""
    listCsvFiles = []
    contentCsv = []

    def __init__(self):
        self.window = tk.Tk()
        self.window.bind("<Button-1>", self.click_ppm_lpm_controller)
        self.window.bind("<Button-3>", self.click_ppm_lpm_controller)
        textInfo =  "Witaj, \n kliknij w to okno aby wybrać katalog z plikami csv\n "
        self.displayInfo(textInfo)

        self.window.mainloop()

    def displayInfo(self, textInfo):
        text = tk.StringVar()
        label = tk.Label(self.window, textvariable=text, padx=100, pady=20)
        label.pack()
        text.set(textInfo)

    def click_ppm_lpm_controller (self, event):

        if msb.askokcancel("Wybór folderu z plikami CSV", "Wybierz folder w ktorym znajduje sie pliki CSV"):
            self.openDirectoryWithCsvFiles()
            self.createListPathesCsvFilesInDirectory()
            self.openCsvFile()

            for row in self.contentCsv:
                # print (row['Kwota transakcji'])
                # print(row)
                for x in row:
                    print(x)
            index = "Numer placówki"
            self.makeStatistic(self.contentCsv, index)



    def openDirectoryWithCsvFiles(self):

        self.directory = fd.askdirectory()  # wskazanie ścieżki do folderu docelowego
        if self.directory:
            msb.showinfo("Info", "Wybrano folder {folder}, pliki CSV które się w nim znajdują zostaną przetworzone.".format(folder=self.directory))
            self.directory=self.walidacjaSciezki(self.directory)
            print("katalog {katalog} został załadowany".format(katalog=self.directory))

    def walidacjaSciezki(self,path):
        newPath = path.replace('\n', '')
        newPath = newPath.replace("/[/]+", "/")
        newPath = newPath.replace("\[\]+", "\\")
        if (newPath[len(newPath)-1]!="\\" or newPath[len(newPath)-1]!="/"):
            newPath = newPath+"/"
        return newPath

    def createListPathesCsvFilesInDirectory(self):
        for file in glob.glob(self.directory+"*.csv"):
            self.listCsvFiles.append(file)
            print("Scieżki plików zostały zaimportowane (%s)"%file)

    def openCsvFile(self):
        for fileCsv in self.listCsvFiles:
            with open(fileCsv, 'r') as csvfile:
                content=csv.reader(csvfile, delimiter=',')
                contentList = []
                for line in content:
                    contentList.append(line)

                self.contentCsv.append(contentList)
                print("Plik %s został wczytany"%fileCsv)

    def makeStatistic(contentList, index):
        for row in contentList:
            indexNumerPlacowki = row[index]
            updateStatistic = contentList[indexNumerPlacowki]
            if (updateStatistic):
                print(contentList[indexNumerPlacowki])
                # for prezydent in (updateStatistic):
                #     updateStatistic['%s' % prezydent] += int(row['%s' % prezydent])
                    # print(prezydent)
                    # print(updateStatistic['%s' %prezydent])
        # return statisticTemplate





apl = Application()