#DATA ANALYSIS FOR ALL HOUSING DATA GATHERED IN CALIFORNIA CRAIGSLIST
library(tidyverse)
library(viridis)
library(ggmap)

setwd("/Users/irahorecka/Desktop/Harddrive_Desktop/Python/CL_Mining/py3.7/Data/2019-09-15")

dat <-  read.csv("2019-09-15_all_craigslist_housing_eby_California.csv", sep = ',', header=T, stringsAsFactors = F)
dat <- dat %>%
  filter(Post.has.Geotag != 'None',
         Area!='None')

for(i in 1:length(dat$CL.State)){
  x <- str_extract_all(dat$Post.has.Geotag[i],"\\(?[0-9,.]+\\)?")[[1]][1]
  dat$long[i] <- substr(x,2,nchar(x)-1)
  y <- str_extract_all(dat$Post.has.Geotag[i],"\\(?[0-9,.]+\\)?")[[1]][2]
  dat$lat[i] <- substr(y,0,nchar(y)-1)
  dat$Price[i] <- gsub(",", "", substr(dat$Price[i],2,20), fixed = TRUE)
  dat$Area[i] <- substr(dat$Area[i],1,nchar(dat$Area[i])-3)
}
dat <- dat[-106,]
dat$long <- as.numeric(dat$long)
dat$lat <- -(as.numeric(dat$lat))+.033
dat$Price <- as.numeric(dat$Price)
dat <- dat %>%
  filter(Price > quantile(Price,.25)-1.5*(IQR(Price)),
         Price < quantile(Price,.75)+1.5*(IQR(Price)))
dat$Price_Area <- dat$Price/as.numeric(dat$Area)
dat <- dat %>%
  filter(Price_Area > quantile(Price_Area,.25)-1.5*(IQR(Price_Area)),
         Price_Area < quantile(Price_Area,.75)+1.5*(IQR(Price_Area)))

states <- map_data('state')
counties <- map_data('county')
ca_df <- subset(states, region == "california")
ca_county <- subset(counties, region == "california")
#dat$long <-  as.numeric(substr((str_extract_all(dat$Post.has.Geotag,"\\(?[0-9,.]+\\)?"))[[1]][1],2,nchar(dat$Post.has.Geotag)-2))
#ca_county <- merge(ca_county, county_cl[, c("subregion", "Median")], by="subregion")

# dat <- dat %>%
#   filter(Bedrooms == 2)
ca_base <- ggplot(ca_df, aes(x = long, y = lat, group = group)) +
  coord_fixed(1.3) +
  geom_polygon(color = 'black',fill='grey30')
ca_base + theme_nothing() +
  geom_polygon(data = ca_county, fill = NA, color = "black") +
  geom_polygon(color = "black", fill = NA) +
  coord_fixed(xlim = c(-120, -124),  ylim = c(36, 39.8), ratio = 1.3) +
  geom_point(data=dat, aes(y=long,x=lat, color=(Price_Area)), inherit.aes = F, size = 2, alpha = .3) +
  scale_color_viridis(option = 'B') 

hist(dat$Price_Area)
qqnorm(dat$Price_Area)
