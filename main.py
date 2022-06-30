import pyttsx3 #install the package/module (pip instll pyttsx3)
import PyPDF2 #pip install PyPDF2 [run both of these commands in the terminal]
book=open('Understanding_Software_Architecture.pdf','rb') 
                                                        #give the name of the pdf file and keep it in the directory where you main.py is
pdf_reader=PyPDF2.PdfFileReader(book) 
                                     #use PyPDF2.PdfFileReader() to select the book varible
total_page=pdf_reader.numPages # .numPages method is used from 
                               #PyPdf2   to which returns the total number of pages
speaker=pyttsx3.init() 
                        #here we initilize the python text to speech module
startpage=10 #initializing the page from where we can start to listen to
for i in range(startpage,total_page): #iterating everytime whenever a page ends
    page=pdf_reader.getPage(i)
                                 #selecting a single page from pdf and iterating everytime with (i)
    text=page.extract_text()   #extracting the text of the page
    speaker.say(text)           #spaker will say the extrancted text only
    speaker.runAndWait()         
                          #spakers keeps on saying until the text is finished  
