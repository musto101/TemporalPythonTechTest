library(lubridate)
library(caret)

## logistic regression
dat <- read.csv('data/one_day.csv')
dat$created_at <- as.numeric(as_datetime(dat$created_at))
dat$timestamp <- as.numeric(as_datetime(dat$timestamp))
dat$updated_at <- as.numeric(as_datetime(dat$updated_at))

dat$created_from <- NULL # Its only got one value

dat$project_id <- as.character(dat$project_id)

write.csv(dat, 'data/one_day_pp.csv')
