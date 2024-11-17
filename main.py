

import requests
import pandas as pd
import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Set up the email details for alerts
def send_email_alert(transaction_details):
    """Send an email alert when a transaction exceeds $250,000."""
    sender_email = "your_email@gmail.com"  # Replace with your email
    receiver_email = "recipient_email@example.com"  # Replace with recipient's email
    password = "your_email_password"  # Replace with your email password
    
    subject = "Stock Trade Alert: Member of Congress Transaction Over $250,000"
    body = f"A member of Congress has made a transaction over $250,000.\n\nDetails:\n{transaction_details}"

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email using SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Fetch stock price from Yahoo Finance
def get_stock_price(symbol):
    """Fetch current stock price using yfinance."""
    stock = yf.Ticker(symbol)
    current_price = stock.history(period="1d")['Close'].iloc[0]
    return current_price

# Function to process the disclosure data
def process_disclosures():
    """Fetch and process the stock disclosures."""
    # Example URL for House Financial Disclosures CSV (this could be an API or direct link)
    disclosure_url = "https://www.example.com/house_stock_disclosures.csv"  # Replace with actual source
    try:
        # Fetch the disclosure data
        df = pd.read_csv(disclosure_url)

        # Filter out transactions greater than $250,000
        df['Transaction Value'] = df['Amount'] * df['Shares']  # Assumed columns, adjust based on real data
        df_filtered = df[df['Transaction Value'] > 250000]
        
        for index, row in df_filtered.iterrows():
            # Get stock price
            stock_symbol = row['Ticker']  # Assumed column, adjust based on actual data
            stock_price = get_stock_price(stock_symbol)
            market_value = stock_price * row['Shares']  # Calculate market value of the stock

            # Alert if the transaction exceeds $250,000
            if market_value > 250000:
                transaction_details = f"Member: {row['Member Name']}\n" \
                                      f"Transaction: {row['Transaction Type']} {row['Shares']} shares of {stock_symbol}\n" \
                                      f"Transaction Value: ${market_value:.2f}\n" \
                                      f"Stock Price: ${stock_price:.2f}"
                send_email_alert(transaction_details)

    except Exception as e:
        print(f"Error processing disclosures: {e}")

# Function to schedule periodic checks
def schedule_alerts():
    """Schedule the disclosure check to run periodically."""
    schedule.every(1).hour.do(process_disclosures)  # Check every hour for new disclosures

    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait 1 minute before checking again

# Main function
def main():
    print("Starting Congress Stock Trading Alert System...")
    schedule_alerts()

# Run the script
if __name__ == "__main__":
    main()

