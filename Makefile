default:

.PHONY: data \
		data/WRAPS-arrivals-by-destination-2005-2015-clean.csv \
		data/WRAPS-arrivals-by-religion-2005-2015-clean.csv 

data: data/WRAPS-arrivals-by-destination-2005-2015-clean.csv data/WRAPS-arrivals-by-religion-2005-2015-clean.csv 

data/WRAPS-arrivals-by-destination-2005-2015-clean.csv:
	python scripts/clean-wraps-destination.py < data/WRAPS-arrivals-by-destination-2005-2015.csv > $@

data/WRAPS-arrivals-by-religion-2005-2015-clean.csv:
	python scripts/clean-wraps-religion.py < data/WRAPS-arrivals-by-religion-2005-2015.csv > $@
