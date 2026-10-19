from flask import Flask, render_template
from urllib.parse import quote

app = Flask(__name__)

# Edit these sample products to match your real badge collection.
# Put your own product photos in static/images/ and update each image filename.
PRODUCTS = [
    {
        "id": "flower-power",
        "name": "Flower Power",
        "category": "Cute & Colourful",
        "price": 49,
        "description": "A cheerful flower badge to brighten your bag or jacket.",
        "image": "flower.svg",
        "tag": "Bestseller",
    },
    {
        "id": "smiley-days",
        "name": "Smiley Days",
        "category": "Cute & Colourful",
        "price": 39,
        "description": "A happy little smiley badge for everyday accessories.",
        "image": "smiley.svg",
        "tag": "Popular",
    },
    {
        "id": "little-star",
        "name": "Little Star",
        "category": "Minimal",
        "price": 45,
        "description": "A starry design that adds a little sparkle to your style.",
        "image": "star.svg",
        "tag": "",
    },
    {
        "id": "cherry-pop",
        "name": "Cherry Pop",
        "category": "Cute & Colourful",
        "price": 55,
        "description": "A sweet cherry design for jackets, totes and backpacks.",
        "image": "cherry.svg",
        "tag": "New",
    },
    {
        "id": "cosmic-moon",
        "name": "Cosmic Moon",
        "category": "Aesthetic",
        "price": 59,
        "description": "A dreamy moon-and-stars badge for night-sky lovers.",
        "image": "moon.svg",
        "tag": "",
    },
    {
        "id": "happy-cloud",
        "name": "Happy Cloud",
        "category": "Aesthetic",
        "price": 45,
        "description": "A soft, pastel cloud badge with a happy little face.",
        "image": "cloud.svg",
        "tag": "",
    },
]

BUSINESS_EMAIL = "abigailalvinsen@gmail.com"
WHATSAPP_NUMBER = "918971204603"  # India country code 91 + the supplied 10-digit number


@app.route("/")
def home():
    prepared_products = []
    for product in PRODUCTS:
        message = (
            f"Hi! I'd like to order this badge: {product['name']} "
            f"(₹{product['price']}). Please share availability and delivery details."
        )
        email_subject = f"Badge order enquiry - {product['name']}"
        email_body = (
            f"Hello!\n\nI'd like to order this badge:\n"
            f"Product: {product['name']}\n"
            f"Price shown: ₹{product['price']}\n"
            f"Quantity: [Please enter quantity]\n"
            f"Delivery location: [Please enter your location]\n\n"
            f"Please confirm availability, delivery charges and payment options.\n\nThank you!"
        )
        prepared_products.append({
            **product,
            "whatsapp_url": f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}",
            "email_url": (
                f"mailto:{BUSINESS_EMAIL}?subject={quote(email_subject)}"
                f"&body={quote(email_body)}"
            ),
        })
    categories = list(dict.fromkeys(product["category"] for product in PRODUCTS))
    return render_template(
        "index.html",
        products=prepared_products,
        categories=categories,
        business_email=BUSINESS_EMAIL,
        whatsapp_display="8971204603",
    )


if __name__ == "__main__":
    app.run(debug=True)
