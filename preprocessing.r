library(lubridate)
library(caret)

dat <- read.csv('data/one_day.csv')
dat$created_at <- as.character(format(as_datetime(dat$created_at),
                                    format = "%H:%M:%S"))
dat$timestamp <- as.character(format(as_datetime(dat$timestamp),
                                     format = "%H:%M:%S"))
dat$updated_at <- as.character(format(as_datetime(dat$updated_at),
                                      format = "%H:%M:%S"))

dat$created_from <- NULL # Its only got one value

dat$project_id <- as.character(dat$project_id)

write.csv(dat, 'data/one_day_pp.csv')
