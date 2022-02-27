# Goofy Benchmarks

## Why?

I don't know, a friend sent me some code from r/programmerhumor and I wondered how bad it really was

## What's in here?

Nothing much, basically just a scratchpad for me to remember how to even profile code at all and to experiment with new ways of doing it


## How to run one?

`pyinstrument -r speedscope -o benchmark-file even.py` will profile `even.py` and spit out a binary file to be injested by `speedscope` which gives a nice chart in the browser.
Can instead just get a terminal output with `pyinstrument even.py`
