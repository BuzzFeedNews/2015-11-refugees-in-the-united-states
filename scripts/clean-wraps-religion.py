#!/usr/bin/env python
import pandas as pd
import sys

def parse_int_str(int_str):
    return int(int_str.replace(",", ""))

def main():
    _arrivals = pd.read_csv(sys.stdin, header=None, skiprows=4, names=[
        "from_date", "to_date", "origin",
        "year_str", "origin_total", 
        "religion", "arrivals", "annual_total_all"
    ])

    split_point = _arrivals[
        ~_arrivals["from_date"].str.contains("From: ")
    ].index[0]
    arrivals = _arrivals.ix[:split_point - 1].copy()

    arrivals["arrivals"] = arrivals["arrivals"].apply(parse_int_str)
    arrivals["year"] = arrivals["year_str"].apply(lambda x: int(x[-4:]))

    arrivals[[
        "year", "origin", "religion", "arrivals"
    ]].to_csv(sys.stdout, index=False, encoding="utf-8")

if __name__ == "__main__":
    main()
