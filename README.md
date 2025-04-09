# Stripe Invoice Downloader

A simple Python script to automatically download paid invoices from Stripe within a specified date range.

## Features

- Downloads paid invoices from Stripe as PDF files
- Configurable date range for invoice selection
- Automatically creates an invoices directory
- Skips invoices without PDF files
- Provides progress feedback during download

## Prerequisites

- Python 3.x
- Stripe account with API access
- Required Python packages:
  - stripe
  - requests

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
cd invoices-fetch
```

2. Install required packages:
```bash
pip install stripe requests
```

## Configuration

Open `download.py` and configure the following variables:

```python
STRIPE_API_KEY = ""  # Your Stripe secret API key
DATE_FROM = "2025-03-01"  # Start date for invoice search
DATE_TO = "2025-04-01"    # End date for invoice search
```

## Usage

1. Set your Stripe API key and desired date range in the configuration section
2. Run the script:
```bash
python download.py
```

The script will:
- Create an `invoices` directory if it doesn't exist
- Download all paid invoices within the specified date range
- Save them as PDF files in the format `Invoice-{invoice_number}.pdf`
- Print progress information to the console

## Output

Invoices will be saved in the `invoices` directory with filenames in the format:
```
Invoice-{invoice_number}.pdf
```

## Error Handling

The script will:
- Skip invoices that don't have PDF files
- Print error messages for failed downloads
- Continue processing remaining invoices if one fails

## Security Note

Never commit your Stripe API key to version control. Consider using environment variables or a configuration file for sensitive data.


## Authors

- [@octocodeio](https://www.github.com/octocodeio)

