**PLTR Stock Price vs. Contract Win Announcement** 
*By Lisa Cao*

*About Dataset*
- The processed Dataset can be found in 'final_output.csv'
- This dataset contains PLTR's historical stock prices PLUS their contracts win. Each row represents each trading day, and if they had been granted any government contract that day, the value of the contract would also be reflected in 'Award Amount.' 
- This dataset is the first of its kind, made possible thanks to web scraping and making API calls. It will provide great value to investors or PLTR stock researchers. 

*How the Dataset was put together* 
- This dataset is the output from merging data collected through (1) making a call to retrieve daily stock prices of PLTR (2) scraping (thanks Selenium!) the US Gov Spending website for history of contracts granted to PLTR. Finally, data was cleaned by substituting null values with 0 or default values, sorted by dates, creating 2 derived columns pertaining to delta (expressed in %) of close vs. open stock price and delta of high vs. low stock price for the sake of further data analysis by stock researchers and investors. 


*Purpose of the Dataset*
- PLTR heavily relies on government contracts, and more often than not stock price may experience larger than usual movements on days of contracts announcement. This dataset is ideally to be used by investors or stock researches who invest in PLTR and want to know the relationship between Contracts Win vs. Stock Price. 

*Requirements*
- Download the final_output.csv and start analyzing the relationship between PLTR stock price vs. Contract Win!

*Notes about the Dataset*
- Information about government contract is not complete. Due to the short-term nature of the project, I did not get to fix all technical issues, therefore we only have 31 contracts in the dataset. Given more time, I would go ahead and fix the technical issues to include the entire history of PLTR's government-granted contracts. I believe this issue is happening due to the web-page containing lazy-loaded content; however, again, I did not have enough time to figure out the solution. 
