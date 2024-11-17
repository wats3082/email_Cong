Creating a Python script to alert users when members of the U.S. Congress buy or sell over $250,000 in stock requires access to public financial disclosures, which members of Congress are legally required to submit. These disclosures are typically available through the **Stock Act** (Stop Trading on Congressional Knowledge Act), and they are usually released in the form of data files by government websites such as the **U.S. House of Representatives** or **Senate**.

While there is no direct API from the government for monitoring these transactions in real-time, you can use publicly available resources like:
- **US House of Representatives Financial Disclosure API** (or other available data formats like `.csv` files).
- **Web scraping** for public data (if an API is not available).
- A **stock price API** to calculate the current market value.

For the purpose of this script, I will assume you have access to these disclosures in CSV or JSON format. You can extend this script to alert you when a transaction exceeds $250,000 in value.

### Required Libraries:
1. **Requests**: To interact with APIs (if available).
2. **Pandas**: To manipulate and analyze data (CSV/JSON).
3. **yfinance**: To fetch stock prices for transactions.
4. **SMTPLib**: To send email alerts (you can use this to notify users).
5. **Schedule**: To run the script periodically for checking new data.

### Steps for the Script:
1. **Fetch the Financial Disclosure Data** (CSV, API, or web scraping).
2. **Calculate the Market Value of Transactions** based on stock price (use `yfinance`).
3. **Check if the transaction exceeds $250,000**.
4. **Alert the user via Email or other methods**.



### Script Breakdown:

1. **Fetching Data**: 
   - `process_disclosures` is the function that processes the financial disclosure data. It assumes that the disclosures are in a CSV format that contains the stock ticker symbol, number of shares, and transaction amount. You'll need to modify this to match the real data source you're working with.
   
2. **Stock Price Calculation**:
   - The script uses `yfinance` to fetch the current stock price for the given ticker symbol. The stock price is then used to calculate the market value of the transaction. If the market value is greater than $250,000, an alert is triggered.

3. **Sending Alerts**:
   - When a transaction exceeds $250,000, the script triggers the `send_email_alert` function to send an email with the transaction details. You can modify this to use other alert mechanisms (like Slack or SMS) if desired.
   
4. **Scheduled Execution**:
   - The script uses `schedule` to run the `process_disclosures` function periodically. In this example, it checks every hour for new disclosures. You can adjust this frequency as needed.
   
5. **Running the Script**:
   - When you run the script, it will continuously monitor for new stock transactions and send email alerts when the conditions are met.

### Customization:

1. **Disclosure Source**:
   - Replace the URL `https://www.example.com/house_stock_disclosures.csv` with the actual URL where you can download or access the financial disclosure data.
   
2. **Email Setup**:
   - Replace the `sender_email`, `receiver_email`, and email credentials in the `send_email_alert` function with your actual email details. You might need to set up an app password for Gmail if you are using it for sending emails.
   
3. **Transaction Data Format**:
   - Modify the logic in `process_disclosures` to match the actual format of the disclosure data you're working with (e.g., column names for transaction amounts, stock tickers, etc.).

4. **Alert Methods**:
   - If you want alerts via other methods (e.g., SMS, Slack), you can replace the email logic with integrations for those services (e.g., using Twilio for SMS or Slack's API).

### Limitations:
- **Data Source**: The script assumes you can access the required disclosures in CSV or API format. You may need to scrape websites or use other APIs if the data is not readily available.
- **API Rate Limits**: Be aware of potential rate limits when using APIs like `yfinance` or other services. Consider using caching to avoid excessive calls.

This script provides a basic framework for monitoring congressional stock trades and alerting users when a significant transaction occurs.
