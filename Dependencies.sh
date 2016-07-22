#!/bin/bash

sudo apt-get install libpng-dev libjpeg-dev libtiff-dev zlib1g-dev 
sudo apt-get install gcc g++ 
sudo apt-get install autoconf automake libtool checkinstall

cd ~
wget http://www.leptonica.org/source/leptonica-1.69.tar.gz
tar -zxvf leptonica-1.69.tar.gz
cd leptonica-1.69
./configure
make
sudo checkinstall
sudo ldconfig

cd ~ 
wget https://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.02.02.tar.gz
tar -zxvf tesseract-ocr-3.02.02.tar.gz
cd tesseract-ocr
./autogen.sh
./configure
make 
sudo make install
sudo ldconfig


wget https://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.02.eng.tar.gz 
tar -zxvf tesseract-ocr-3.02.eng.tar.gz 
sudo mv ./tesseract-ocr/tessdata/* /usr/local/share/tessdata/ 


wget https://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.02.hin.tar.gz 
tar -zxvf tesseract-ocr-3.02.hin.tar.gz 
sudo mv ./tesseract-ocr/tessdata/* /usr/local/share/tessdata/ 

