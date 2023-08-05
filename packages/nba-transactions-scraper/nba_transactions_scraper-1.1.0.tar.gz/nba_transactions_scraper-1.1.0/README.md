
# NBA Trades and Transactions Scraper

  

This is a simple library to scrape NBA [ProSports](https://www.prosportstransactions.com/basketball/) trades and transactions data.

  

## Usage

  

  

```bash

pip install nba-transactions-scraper

```

  

  

## Methods

  

### `run(team, start, end)`

returns a Pandas dataframe of NBA transactions for a specific team from start date to end date (defaults to current date). Date format: ('yyyy-mm-dd')

  

## Example

`from nba_transactions_scraper.main import ProSports_Scraper`

`scraper = ProSports_Scraper()`

`results = scraper.run('Lakers', '2021-01-01') `

  

## Next Additions

  

- [ ] Multi-team argument

- [ ] Extracting trade $ values

- [ ] Draft Pick transactions

- [ ] Category of transactions

  

  

## Contributing

  

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

  

  

## License

  

[MIT](https://choosealicense.com/licenses/mit/)