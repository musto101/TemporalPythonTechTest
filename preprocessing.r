library(lubridate)
library(caret)

dat <- read.csv('data/one_day.csv')
dat$created_at <- as.character(format(as_datetime(dat$created_at),
                                    format = "%H:%M"))
dat$timestamp <- as.character(format(as_datetime(dat$timestamp),
                                     format = "%H:%M"))
dat$updated_at <- as.character(format(as_datetime(dat$updated_at),
                                      format = "%H:%M"))

dat$created_from <- NULL # Its only got one value

dat$project_id <- as.character(dat$project_id)

write.csv(dat, 'data/one_day_pp.csv')
