# Image To Text Converterter (ITTC)
ITTC is **Python** application which uses **Tesseract** library to recongnize text from image. The library was used to get this text in printed form so application output becomes copyable. Simple script from this library
is located in `extract.py`   
Application comes with Graphic User Interface without console use. To make GUI look simple, I decided to use Python library **Dear PyGui**. 

**Application Logo**     
![First](https://i.imgur.com/ni6wMUV.png)
## Installation 
As I mentioned before, the application uses two Python libraries which are not included originally. To make this work we have to install them manually to our python.     

We will start with [Tesseract installation](https://tesseract-ocr.github.io/tessdoc/Installation.html). After we finished we install the **Python Wrapper Pytesseract** using pip in python with      

`pip install pytesseract`        

The first library is now fully working, now we can move on to the [Dear PyGui](https://pypi.org/project/dearpygui/#files). I want to mention the [Documentation of the library](https://dearpygui.readthedocs.io/en/latest/index.html) 
for anyone who is interested in how this GUI works. We install the library similarly with pip in python:       

`pip install dearpygui`    

When we are done we can clone the github folder and make link to `dist\ITTC v1.2.exe` on our desktop.     

**Main menu**            
![Second](https://i.imgur.com/waCCGD4.png)      


For image load we have to use Dear PyGui explorer. We find our image destionation and confirm choose.     

**Folder explorer**       
![Second](https://i.imgur.com/t2uIRhQ.png)      


## Software versioning
**v1.0** Working script for one image load. Added buttons for script control.      
**v1.1** Responsible design was made. Script is now able to accept multiple images in a row.    
**v1.2** Script works as fully standalone application.   


## An example of input and copyable output         
![First](https://i.imgur.com/T8kT5Rq.png)

