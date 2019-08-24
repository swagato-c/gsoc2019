# GSOC 2019
This is the github repo for my [Google Summer of Code 2019](https://summerofcode.withgoogle.com/projects/#5067547718713344) project under [Red Hen Lab](http://www.redhenlab.org/).

## Feature Recognition in Works of Art
![log](media/logo.png)
- [Project Description](#project-description)
- [Goals](#goals)
- [Tools and Libraries](#tools/libraries)
- [About Me](#about-me)
- [Reference](#reference)


## Project Description
Mentors: [Peter Bell](https://uni-erlangen.academia.edu/PeterBell), [Leonardo Impett](http://www.biblhertz.it/en/institute/staff/staffdatabase/staff-details/ma-leonardo-impett/).

The goal of the project is to build an iconographic feature recognizer. The current methodology as suggested by Leo will be to perform Image Captioning based on [Iconclass](http://iconclass.org) codes. The current testing dataset is provided by [Rijksbureau voor Kunsthistorische Documentatie (RKD)](http://rkd.nl) based on paintings from Biblical scenes of the New Testament. The development and training will be done on Jupyter Notebooks and then the inference will be done using Python scripts on the backend and a web frontend; all of which is available [here](https://github.com/swagato-c/icon-caption).

## Goals
*Weeks 1 - 4*
- [x] Study the problem well
- [x] Implement GradCAM, GradCAM++
- [x] Scrap the RKD site for the images
- [x] Perform Data Cleaning  

*Weeks 5 - 8*
- [x] Start training the CNN based on Iconclass codes 
- [x] Train Stage-1 via Transfer Learning
- [x] Train Stage-2 via Transfer Learning
- [x] Train Stage-3 via Transfer Learning

*Weeks 9 - 11*
- [x] Write the Server and the CAM scripts
- [x] Write HTML + CSS + JS frontend 
- [x] Write Dockerfile and containerize 
- [x] Deploy container in the cloud

## Tools/Libraries
- [Unsync](https://pypi.org/project/unsync/)
- [Aiohttp](https://pypi.org/project/aiohttp/)
- [Aiofiles](https://pypi.org/project/aiofiles/)
- [PyTorch](https://pytorch.org/)
- [fastai](https://github.com/fastai/fastai/)
- [Scikit-Image](https://scikit-image.org/)
- [Imagehash](https://github.com/JohannesBuchner/imagehash)

## About Me
- **Name**: Swagato Chatterjee
- **Email**: swagato.31dec@gmail.com
- **Github**: https://github.com/swagato-c
- **Website**: https://swagtao-c.github.io/

This README will be updated weekly so stay tuned!
