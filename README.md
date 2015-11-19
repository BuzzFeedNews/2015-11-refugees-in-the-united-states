# U.S. Refugee Data and Analysis

This repository contains data and analysis supporting the BuzzFeed News article, "[Where U.S. Refugees Come From — And Go — In Charts](http://www.buzzfeed.com/jsvine/where-us-refugees-come-from-and-go-in-charts)," published on November 19, 2015.

## Data

The refugee data come from the [Department of State's Refugee Processing Center](https://www.wrapsnet.org/)'s [data portal](http://www.wrapsnet.org/Reports/InteractiveReporting/tabid/393/Default.aspx). Specifically, it comes from the "Arrivals by Destination and Nationality" and "Arrivals by Nationality and Religion" reports, and was generated on November 18, 2015. The raw and cleaned files can be found in this repository's [`data` directory](data/).

To calculate per-capita arrivals by state, the analysis uses the [Census Bureau's 2014 population estimates](http://www.census.gov/popest/data/state/asrh/2014/index.html).

## Analysis and Charts

The code behind the analysis and charts was written in Python, and [can be found here](notebooks/us-refugee-analysis.ipynb).

To re-run the analysis yourself, you'll need to install the Python requirements listed in [`requirements.txt`](requirements.txt).

## Questions / Feedback?

Email the author, Jeremy Singer-Vine, at jeremy.singer-vine@buzzfeed.com.
