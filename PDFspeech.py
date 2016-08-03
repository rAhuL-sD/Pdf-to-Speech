import glob
import os
import pyPdf
import pyttsx
from pyPdf import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(file("test.pdf", "rb"))

for i in range(inputpdf.numPages // 2):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i * 2))
    if i * 2 + 1 <  inputpdf.numPages:
        output.addPage(inputpdf.getPage(i * 2 + 1))
    outputStream = file("test2-page%s.pdf" % i, "wb")
    output.write(outputStream)
    outputStream.close()





engine = pyttsx.init()
engine.setProperty('rate',110)

voices = engine.getProperty('voices')

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content


print "Using voice:", repr(voices[0])
engine.setProperty('voice', voices[0].id)
engine.say("Welcome to p d f to speeech translator. Coded by navaanshu and rahul")
engine.say("your p d f will be spoken now!")
for i in range(inputpdf.numPages // 2):
             engine.say(getPDFContent("test2-page%s.pdf" % i).encode("ascii", "ignore"))
engine.runAndWait()

if quit():
    for i in range(inputpdf.numPages//2): 
        files = file("test2-page%s.pdf" % i, "wb")
    for file in files:
      os.remove(file)

