********************************************************************************
*Gold as an inflation hedge
********************************************************************************

cd "C:\Users\User\Documents\Gerhard\Aberdeen HOME\Yunikarn\Youtube\Projects\Data wrangling\V5 Inflation hedge\Data"



*>>>>>>>>>>>>>>>>> Import gold prices <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
*https://backtest.curvo.eu/market-index/gold-bullion
*In EUR: 10,000 invested
*Backcasting

insheet using "Gold spot price.csv", clear

*Remove redundant columns
drop v*

*Extract year
gen st = substr(date, 1, 4)

*Convert string to numeric
destring st, gen(year)
drop st date

*Convert monthly prices to annual data
sort year
by year: egen gold=mean(goldspotprice)
by year: gen count=_n

drop goldspotprice
label var gold "Gold spot price, EUR"
label var year "Year"

*Remove duplicates
keep if count==1
drop count

*Sort and save
sort year
save "gold.dta", replace

*Line chart
line gold year


*>>>>>>>>>>>>>>>>> Import inflation rates <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
*World Bank
*Inflation rates in per cent
*Backcasting

insheet using "EU inflation World Bank.csv", clear

*Adjust rates
gen inf=eu_inflation_rate/100
label var inf "Inflation rate, Euro area"

drop eu_inflation_rate

*Sort before merging
sort year

*Merge data
merge year using "gold.dta"

drop _merge

*Save final data
save "Gold_final_data.dta", replace

*>>>>>>>>>>>>>>>>> Real return <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

use "Gold_final_data.dta", clear

*Apply inflation rate
*Create an index
gen index = 1 if year==1978
replace index = index[_n-1]*(1-inf[_n-1]) if index==.

label var index "Inflation adjustment"

*Determine real value of portfolio
gen real_gold = gold*index
label var real_gold "Portfolio value in constant prices"

*Line chart
line real_gold year







