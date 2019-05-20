# OCR-with-Selenium

## Description
OCR using free online OCR service. 

使用免费在线文字识别服务的文字识别。

## Prerequisite
### Python Modules
- selenium  
  For simulating web browser actions
- PIL  
  For getting image from clipboard
- pyperclip  
  For copying OCR result into clipboard
### Drivers
- chromedriver  
  For simulating Chrome  
  Downloads are available here: http://chromedriver.chromium.org/home
  
## How to use
```
python ocr.py
```
This command will running OCR through webpage in the background and copy the OCR result directly into your clipboard.

### Recommended Usage
- Write a .bat (or .sh with Linux) with previous command.
- Using ```Win + R```, and then ```snippingtool``` for Windows screen snipping tool. (Or other prefered screen snipping tools)
- Run the .bat (or .sh) with double clicks and just wait for the OCR result!

## Arguments
- CHINESE_MODE  
  This will convert some of the English punctuations into Chinese punctuations. By default, it's set True.
