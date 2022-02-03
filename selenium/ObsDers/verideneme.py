from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import xlsxwriter
import xlrd
imgLink = []
name = []
class Veri:
     def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser  = webdriver.Chrome(ChromeDriverManager().install())
    
    
     def open(self):
      
        self.browser.get('https://www.kitapyurdu.com/index.php?route=product/category&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC&limit=100')
        time.sleep(3)
        for a in range(99):
         b = a +1
         imgLink.append(self.browser.find_element_by_xpath( f"/html/body/div[4]/div/div[3]/div/div[2]/div[{b}]/div[3]/div/a/img").get_attribute("src"))
         name.append(self.browser.find_element_by_xpath(f"/html/body/div[4]/div/div[3]/div/div[2]/div[{b}]/div[4]/a/span").text)
        else:
         print("Bitti")

     def Yaz(self):
        planWorkbook = xlsxwriter.Workbook("KategoriKitap.xlsx")
        planSheet = planWorkbook.add_worksheet("Kitap")
        planSheet.write("A1","İmgLink")
        planSheet.write("B1","Name")
        for a in range(99):
           planSheet.write(f"A{a+3}",imgLink[a])
           planSheet.write(f"B{a+3}",name[a])
        else:
         print("Bitti")
           
        planWorkbook.close()
     
     def imgindir(self):
        dosya = "books.xlsx"
        inputWorkBook = xlrd.open_workbook(dosya)
        inputWorksheet = inputWorkBook.sheet_by_index(0)
        imgName = []
        link = []
        for a in range(2,inputWorksheet.nrows):
           imgName.append(inputWorksheet.cell_value(a,0))
           link.append(inputWorksheet.cell_value(a,10))
        else:
           print("Bitti")
        print(imgName)
        print(link)




      




veri = Veri()
veri.imgindir()


