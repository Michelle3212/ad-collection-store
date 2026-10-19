# Little Badge Studio — Python Flask storefront

A beginner-friendly badge shop website. Customers can browse sample badge designs and contact the seller directly through WhatsApp or email with the chosen product pre-filled in the message.

## Requirements
- Python 3.10 or newer
- Visual Studio Code
- VS Code Python extension

## Run on Windows (VS Code terminal)

1. Extract the ZIP file.
2. In VS Code, choose **File → Open Folder** and open the `badge_store_app` folder.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

5. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run this in the same terminal, then activate again:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

6. Install Flask:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the website:

   ```powershell
   python app.py
   ```

8. Open the local address shown in the terminal, usually **http://127.0.0.1:5000**.

Keep the terminal running while testing the website. Press `Ctrl + C` to stop it.

## Add your real products

Open `app.py` and edit the `PRODUCTS` list. Each product has:
- `name`: badge name
- `category`: `Cute & Colourful`, `Aesthetic`, or `Minimal` (or your own category)
- `price`: price in rupees
- `description`: short product description
- `image`: image filename inside `static/images/`
- `tag`: optional label such as `New` or `Bestseller`

To use your own photo, copy it into `static/images/`, then change that product's `image` value to the filename, e.g. `"my-badge.jpg"`. Use your own product photos for accurate listings.

## Contact settings

The contact details are near the top of `app.py`:
- Email: `abigailalvinsen@gmail.com`
- WhatsApp number is formatted with India's country code `91` plus the supplied number `8971204603`, for a WhatsApp link.

If WhatsApp does not open, check that the phone number is registered with WhatsApp.

## Important
- The six products and prices are examples. Replace them with your real products and prices before publishing.
- This starter app does not accept online payments or store orders in a database. Customers send you an order enquiry through WhatsApp/email, and you confirm availability, delivery and payment with them.
- `debug=True` is suitable for local testing only. Use a production deployment setup before making the site public.


## Brand logo and adding your own products

- The storefront brand is **A & D Collection** and uses `static/images/ad-collection-logo.png`. Replace that file with your updated logo image (keep the same filename) to change the logo.
- Open `app.py` and find the `PRODUCTS = [` list near the top. Each dictionary is one product card. Copy an existing dictionary to add another product, then change its `id`, `name`, `category`, `price`, `description`, `image`, and `tag`. Use a unique lowercase `id` with hyphens. Use a numeric price without the rupee symbol, for example `129`.
- Save each product photo in `static/images/`, then set its filename in the product's `image` field. Example: `image: "my-badge.jpg"`. Supported common formats include JPG, PNG, and WebP.
- The category filter buttons are generated from the categories in `PRODUCTS`, so you can add your own category names.
- Save your files and restart Flask with `Ctrl+C`, then run `python app.py` (or use ` .\.venv\Scripts\python.exe app.py` from the folder containing `app.py`). Refresh the browser.
- This starter website sends enquiries through WhatsApp/email; it does not take online payments or store orders.
