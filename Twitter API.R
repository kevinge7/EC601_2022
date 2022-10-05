install.packages("ROAuth")
library(ROAuth)
requestURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "https://api.twitter.com/oauth/access_token"
authURL <- "https://api.twitter.com/oauth/authorize"
consumerKey <- "gj66YYGOqTsmPKfTnvrVVGg0p"
consumerSecret <- "ZX1eiXNJisErOK8EW9l14VQK8RNM1TmX8SY5DwVrIOdrjDO8U4"
my_oauth <- OAuthFactory$new(consumerKey=consumerKey, consumerSecret=consumerSecret,
                             requestURL=requestURL, accessURL=accessURL, authURL=authURL)

my_oauth$handshake(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl"))

setwd("~/Dropbox/credentials/twitter")

save(my_oauth, file="my_oauth")

toInstall <- c("ggplot2", "scales", "R2WinBUGS", "devtools", "yaml", "httr", "RJSONIO")
install.packages(toInstall, repos = "http://cran.r-project.org")
library(devtools)
install_github("pablobarbera/twitter_ideology/pkg/tweetscores")

library(tweetscores)

setwd("~/")

data <- read.csv("march_result.csv")

#install.packages("dplyr") #- install this package if its not on the R instance already
library(dplyr)

user_name_tweet_count <- data %>% group_by(user_screen_name) %>% count()
usernames <- user_name_tweet_count %>% filter(n >= 5) %>% dplyr::select(user_screen_name)


user_scores<- data.frame(matrix(vector(), 0, 2,
                                dimnames=list(c(), c("screen_name", "ideology_score"))),
                         stringsAsFactors=F)

for(user in usernames$user_screen_name){
  skip_to_next <- FALSE
  tryCatch({
    friends <- getFriends(screen_name=user, oauth=my_oauth)
    results <- estimateIdeology2(user, friends)
  }, error=function(e){skip_to_next <<- TRUE})
  if(skip_to_next) { next }
  print("results computed successfully.")
  user_scores[nrow(user_scores) + 1,] = list(screen_name = user,
                                             ideology_score = results)
}

write.csv(user_scores, file = "march_user_scores.csv")
write.csv(friends, file = "march_friends_result.csv")
write.csv(user_names, file= "march_user_name.csv")
