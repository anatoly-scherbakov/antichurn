# antichurn

[![Build Status](https://travis-ci.com/iolanta.tech/antichurn.svg?branch=master)](https://travis-ci.com/iolanta.tech/antichurn)
[![Coverage](https://coveralls.io/repos/github/iolanta.tech/antichurn/badge.svg?branch=master)](https://coveralls.io/github/iolanta.tech/antichurn?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/antichurn.svg)](https://pypi.org/project/antichurn/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Help to make hard decisions with multiple choices


## Motivation

Suppose you have a decision to make that involves multiple variables, and each of those variables can have one of multiple choices.

- Write down your options for each in a YAML file, just as in [choices.yaml](choices.yaml).
- Generate all possible combinations of your choices like this:

```bash
cat choices.yaml | python run.py > choices.csv 
```

- Import your CSV file into Airtable (or another spreadsheet editor, but let's focus on Airtable now)
- Change the type of all the columns to Single Select
- Add two more columns: **Status** and (optionally) **Note**.
- Then, engage your thought process. Exclude the combinations that, due to various reasons, are unacceptable, - and whatever is left is indubitably the solution.

Or a few solutions, which you probably need more research on to choose.

I will work to further automate and streamline this process.

## Literature

- I've read a book on logical and mathematical puzzles in my childhood, the name of which I do not recall, but it had quite a few puzzles like this
- There is a Theory for solving innovation problems which might have tools like this one 

And I've left a note on Notion about this, but it's in Russian and will only be public if I make it looking nice enough: [Salvation from the combinatoric explosion](https://www.notion.so/2c7c252780ab4e8ca8d21bee1fbb8304). I am adding the link for my own reference only. 

## License

[MIT](https://github.com/iolanta.tech/antichurn/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [084fb1b54d4fab37583ca85faf5c52abb3356499](https://github.com/wemake-services/wemake-python-package/tree/084fb1b54d4fab37583ca85faf5c52abb3356499). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/084fb1b54d4fab37583ca85faf5c52abb3356499...master) since then.
