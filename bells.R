library(tidyverse)

df1 <- rnorm(n = 1e6, mean = 0, sd = .1)
df2 <- rnorm(n = 1e6, mean = 0, sd = .2*.9)
df3 <- rnorm(n = 1e6, mean = 0, sd = .3*.9)
df4 <- rnorm(n = 1e6, mean = 0, sd = .4*.9)
df5 <- rnorm(n = 1e6, mean = 0, sd = .5*.9)
df6 <- rnorm(n = 1e6, mean = 0, sd = .6*.9)

df <- tibble(df1,
       df2,
       df3,
       df4,
       df5,
       df6)
df %>% 
  ggplot() +
  geom_histogram(aes(df6), bins= 5000, color = "#D7E7F3") +
  geom_histogram(aes(df5), bins= 5000, color = "#9CC3E2") + 
  geom_histogram(aes(df4), bins= 5000, color = "#62A0D0") + 
  geom_histogram(aes(df3), bins= 5000, color = "#347AB0") + 
  geom_histogram(aes(df2), bins= 5000, color = "#295F89") + 
  geom_histogram(aes(df1), bins= 5000, color = "#11293b") 

