********************************************************************************
*World Inequality Database
********************************************************************************

cd "C:\Users\User\Documents\Gerhard\Aberdeen HOME\Yunikarn\Youtube\Playlists\Data wrangling\V8 World Inequality Data"

use WID.dta, clear

*Declare time dimension
tsset year

*Plot all time series
twoway (line france year) (line uk year, lpattern(".")) ///
(line china year) (line germany year, lpattern(" --")) ///
(line russia year, lpattern("_"))

*Linear interpolation
ipolate france year, gen(france_p)

*Exactly the same outcome
twoway (line france year) (line france_p year)


