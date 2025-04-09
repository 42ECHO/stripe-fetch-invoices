import os
import stripe
import requests
from datetime import datetime


# === CONFIGURATION ===
STRIPE_API_KEY = ""  # <- Replace with your Stripe secret API key
INVOICES_DIR = "invoices"
DATE_FROM = "2025-03-01" # <- Set the date from which to download invoices
DATE_TO = "2025-04-01" # <- Set the date to which to download invoices

# === INITIALIZE STRIPE ===
stripe.api_key = STRIPE_API_KEY

# === CREATE FOLDER IF IT DOESN'T EXIST ===
os.makedirs(INVOICES_DIR, exist_ok=True)

# === CONVERT DATE TO UNIX TIMESTAMP ===
def to_unix_timestamp(date_str):
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp())

created_filter = {
    "gte": to_unix_timestamp(DATE_FROM),
    "lte": to_unix_timestamp(DATE_TO)
}

# === DOWNLOAD ALL INVOICES ===
invoices = stripe.Invoice.list(limit=100, created=created_filter)

for invoice in invoices.auto_paging_iter():
    if invoice["status"] != "paid":
        continue
    invoice_id = invoice["number"]
    pdf_url = invoice["invoice_pdf"]
    
    if not pdf_url:
        print(f"Invoice {invoice_id} does not have a PDF file.")
        continue

    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        file_path = os.path.join(INVOICES_DIR, f"Invoice-{invoice_id}.pdf")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Saved {file_path}")
    else:
        print(f"Failed to download PDF for invoice {invoice_id}")

print("Done!")

