from PIL import Image
import pytesseract
import VegetableList
import re


def Vegetables():
    Vegetables = VegetableList.Vegetable
    return Vegetables


def Receipt():
    TesseractPath = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ImgPath = r'C:\Users\rocze\Desktop\pythonProject\ITT\test2.png'
    Img = Image.open(ImgPath)
    pytesseract.pytesseract.tesseract_cmd = TesseractPath
    Text = pytesseract.image_to_string(Img)
    return Text.lower()


def MatchingVegetables():
    # Using created list of vegetables
    VegetablesList = Vegetables()
    # Import string taken from image
    ReceiptText = Receipt()
    # Finding matching elements and adding them into new list
    VegMatch = []
    for Vegetable in VegetablesList:
        if Vegetable in ReceiptText:
            VegMatch.append(Vegetable)
    print(VegMatch)
    print(ReceiptText)
    return VegMatch

