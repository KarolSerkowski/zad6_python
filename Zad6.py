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
    dictStatisticOfAllCsvFiles = {}
    displayStatistics = ""

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
            self.contentCsv=self.openAndConvertValueInCsvFile()
            self.displaySum()
            # self.makeStatistic(self.contentCsv)



    def openDirectoryWithCsvFiles(self):

        self.directory = fd.askdirectory()  # wskazanie ścieżki do folderu docelowego
        if self.directory:
            msb.showinfo("Info", "Wybrano folder {folder}, pliki CSV które się w nim znajdują zostaną przetworzone a posumowanie zostanie wyświetlone w głównym oknie.".format(folder=self.directory))
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

    def openAndConvertValueInCsvFile(self):
        for fileCsv in self.listCsvFiles:
            with open(fileCsv, 'r') as csvfile:
                content=csv.DictReader(csvfile, delimiter=',')
                for row in content:


                    print("%s"%row['Numer placówki'])

                    self.dictStatistics(row['Numer placówki'], row['Kwota transakcji'])


            print("Plik %s został wczytany"%fileCsv)



    def dictStatistics(self, placowka, kwota):
        if placowka in self.dictStatisticOfAllCsvFiles:
            self.dictStatisticOfAllCsvFiles[placowka]+=int(kwota)
        else:
            self.dictStatisticOfAllCsvFiles[placowka]=int(kwota)
        print("Przetworzona suma:")
        print(self.dictStatisticOfAllCsvFiles[placowka])
         
    def displaySum(self):
        nr_placowki = 0
        for placowka in self.dictStatisticOfAllCsvFiles:
            nr_placowki +=1
            suma_transakcji = self.dictStatisticOfAllCsvFiles['%s'%nr_placowki]
            self.displayStatistics += "Suma transakcji w placówce nr {placowka}: {suma}\n ".format(placowka=nr_placowki, suma=suma_transakcji)
            print (self.dictStatisticOfAllCsvFiles['%s'%nr_placowki])
        self.displayInfo(self.displayStatistics)



apl = Application()