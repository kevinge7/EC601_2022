# EC601_2022
Hi
This is Yuxi Ge
My Google Drive link of the project is:
https://drive.google.com/drive/folders/1r62L4vqJ0VW48UESgwRNF9T9rdG3diDS?usp=sharing

I want to design software to analyze people's attitudes toward the vaccine during the pandemic. 
As a government, I want to search “Pfizer” on Twitter through Twitter API to see what people think about Pfizer(Using Google NLP API).
As a Moderna researcher, I want to search “Moderna vaccine” on Twitter through Twitter API to see what will people choose between Pfizer and Moderna. 

### Module design:

1. get input from users
2. use Google NLP API to get the keywords
3. Upload the keywords to Twitter through Twitter API
4. Get results from Twitter and then upload these tweets to Google NLP API to process the data
5. Output the result and return it to users. 

### My users could be:
Salesman
Company manager 
Researcher
Consultant

### Final Result: 

Due to some reasons, GitHub won't let me upload file sizes of more than 25 MB. I uploaded my result file to google drive(link in readme).

I am using Twitter API to get all tweets from December 2019 to March 2020 about vaccines. The size of this file is more than 100MB and I run the Twitter API code for 18 hours on my laptop. The file name is "tweets_geo_vaccine_us_nov_2020_to_mar_2021.csv" Please check it on my google drive folder. 
<img width="1633" alt="image" src="https://user-images.githubusercontent.com/112116208/195490032-1753ec48-aa4c-46b4-bc28-f066a427fd82.png">

https://drive.google.com/drive/folders/1r62L4vqJ0VW48UESgwRNF9T9rdG3diDS?usp=sharing

And then I run Google NLP to get sentiment scores about these tweets. The output file is named"score - Sheet1.csv" in the google drive folder with the same link above. 
In this file, I only output the username and the sentiment score.
<img width="304" alt="image" src="https://user-images.githubusercontent.com/112116208/195490133-d8d2a690-3c7b-4021-bf1f-dd570a8791b5.png">

In this file, I only output the username and the sentiment score.
And I think these can fully show us what do people think about vaccines. 
