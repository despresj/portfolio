# 1. Random Interval Timer
# I found myself wanting a timer that would select a 
# random time between three and eight minutes at random. 
# When I was unable to find one, I wrote a function for it.

random_interval_timer <- function(rounds = 10, 
                                  rest_minutes = 30, 
                                  min_time_minutes = 2.5, 
                                  max_time_minutes = 7.5){
  
  min_time <- (min_time * 60) - 30
  max_time <- (max_time * 60) - 30
  # convert minutes to seconds and subtract 30 to account for 30 second notice
  for(i in 1:rounds){
    if(i == 1){
      system(paste(
        "say Random Interval Between", round(min_time / 60 ,0), "and", 
        round(max_time / 60 ,0), "Minutes, Begin round", i))
    }  else{
      system(paste("say begin round", i))
    }
    
    beepr::beep(1)  
    time <- runif(1, min_time , max_time)
    # runif generates a number at random between min_time and max_time
    print(paste(round(time/60, 2), "minutes"))
    Sys.sleep(time)
    
    system("say Thirty Seconds Remaining")
    Sys.sleep(30)
    beepr::beep(1)  
    
    system(paste("say", round(time/60, 1), "Minute Round Complete:", 
                 round(rest, 0), "Seconds to Rest"))
    Sys.sleep(rest)
    beepr::beep(1)  
  }
}

random_interval_timer(rounds = 2, rest = 2, min_time = 2, max_time = 3)
