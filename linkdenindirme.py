import xlsxwriter
import xlrd
import requests # to get image from the web
import shutil 

inputWorkBook = xlrd.open_workbook(r"C:\Users\senak\Desktop\cocuk_kitaplari11 (1).xlsx")
inputWorksheet = inputWorkBook.sheet_by_index(0)
imgName = []
link = []
for a in range(1,inputWorksheet.nrows):
   imgName.append(inputWorksheet.cell_value(a,6))
   link.append(inputWorksheet.cell_value(a,16))
else:
   print("Bitti")
print(imgName)
print(link)

for a in range(len(imgName)-1):
   # Open the url image, set stream to True, this will return the stream content.
   if (link[a]==""):
      continue
   r = requests.get(link[a], stream = True)

   # Check if the image was retrieved successfully
   if r.status_code == 200:
      # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
      r.raw.decode_content = True
      
      # Open a local file with wb ( write binary ) permission.
      with open(imgName[a]+".jpg",'wb') as f:
         shutil.copyfileobj(r.raw, f)
         
      print('Image sucessfully Downloaded: ',imgName[a]+".jpg")
   else:
      print('Image Couldn\'t be retreived')
