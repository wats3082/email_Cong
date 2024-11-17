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










# PART 2: CONTRACT NOTIFICATION



To create an email alert system for when **construction contracts** become available, you need to:

1. **Identify the Source of Construction Contracts**: This could be government websites, construction industry portals, or specific contracting platforms that publish construction contract opportunities.
   
   Some common sources for construction contracts include:
   - Government procurement sites like **FedBizOpps (SAM.gov)** for U.S. government contracts.
   - Local government or state-run procurement sites.
   - Private construction bid platforms (e.g., **BidClerk**, **Construction Bidboard**).

2. **Scrape or Monitor the Contract Website**: Depending on the availability of data, you may either scrape websites or use an API (if available) to get the latest contracts.

3. **Send Email Alerts**: Once new contracts are available, an email alert will be sent to a specified email address.

4. **Schedule the Check**: The script will regularly check the website (e.g., every hour, daily) for new construction contracts.

### Requirements:
- **Requests**: To make HTTP requests.
- **BeautifulSoup**: For scraping HTML content (if needed).
- **Smtplib**: For sending email alerts.
- **Schedule**: To check for new contracts at regular intervals.



### Script Breakdown:

1. **Email Alert System**:
   - `send_email_alert`: This function sends an email with the contract details to the specified recipient using the **smtplib** library. You will need to replace the sender and receiver email addresses, as well as the sender's email password.
   
2. **Web Scraping**:
   - `scrape_construction_contracts`: This function is responsible for scraping the webpage for new construction contracts. It uses **BeautifulSoup** to parse the HTML and extract details about the contracts (e.g., title, description, link).
   - You'll need to customize the scraping logic based on the actual structure of the website you're monitoring. Use `soup.find_all()` and other `find` methods to target the correct HTML tags and classes. You can inspect the website's HTML using your browser's developer tools to determine the correct tags and attributes.

3. **Scheduling Periodic Checks**:
   - The script uses the **schedule** library to run the contract checking function periodically (in this case, every hour). You can modify this to check more or less frequently depending on your needs.

4. **Running the Script**:
   - When the script is executed, it continuously monitors the target website for new contracts, sending email alerts when new construction contracts are found.

### Customization:

1. **Website URL**:
   - Replace the `url` in `scrape_construction_contracts` with the actual URL of the website you are scraping for construction contracts.
   
2. **Scraping Logic**:
   - Modify the scraping logic based on the website’s structure. Use the browser's **Inspect** tool to find the correct HTML tags and class names for the contract title, description, and links.
   - If the website provides an API to access the contracts, you can replace the scraping code with a direct API call instead.

3. **Email Configuration**:
   - Replace the sender email, receiver email, and password with your actual email configuration. If you're using Gmail, you may need to enable "Less Secure Apps" or create an **App Password** if 2-step verification is enabled.

4. **Frequency of Checks**:
   - Modify the scheduling interval in `schedule.every(1).hour.do(scrape_construction_contracts)` to change how frequently the script checks for new contracts (e.g., every 10 minutes, daily, etc.).

### Potential Improvements:

1. **Error Handling**:
   - Add more robust error handling for network issues or changes in the website structure.
   
2. **Persistent Storage**:
   - Keep track of previously sent contracts (e.g., using a file or database) to avoid sending duplicate alerts for the same contract.

3. **Multiple Sources**:
   - You can extend the script to monitor multiple websites for construction contracts by adding more functions and handling each site's structure.

### Conclusion:

This script provides an automated solution to monitor construction contract availability from a website and send email alerts whenever a new contract is published. It can be customized to fit the needs of specific websites or procurement platforms and can be scheduled to run periodically to ensure real-time monitoring.
