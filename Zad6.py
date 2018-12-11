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
    statisticFromFilesCsv = {}

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

            index = "Numer placówki"
            self.makeStatistic(index)



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
                content=csv.DictReader(csvfile, delimiter=',')
                contentList = {}
                for line in content:
                    # contentList.append(line)
                    contentList=line


                self.contentCsv.append(contentList)
                print("Plik %s został wczytany"%fileCsv)

    def makeStatistic(self,index):
        for csv in self.contentCsv:             #dopuki sa czytane pliki csv
            for row in csv:


                # while self.statisticFromFilesCsv[row[index]]:
                #     print("wartosc juz istnieje")
                # else:
                #     self.statisticFromFilesCsv.append(row)
                #     print("wartosc dodana do licznika")
                # self.contentCsv.keys();
                print(row[index])












apl = Application()