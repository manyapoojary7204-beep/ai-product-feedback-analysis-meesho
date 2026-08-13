import csv

delivery_count = 0
refund_count = 0
support_count = 0
return_count = 0
payment_count = 0
cancellation_count = 0
wrong_product_count = 0
pricing_count = 0

total_reviews = 0

with open("reviews.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_reviews += 1

        pain_point = ""

        for key, value in row.items():
            if key and "pain" in key.lower():
                pain_point = value or ""
                break

        pain_point = pain_point.lower()

        if "delivery" in pain_point or "delivered" in pain_point:
            delivery_count += 1

        if "refund" in pain_point:
            refund_count += 1

        if "support" in pain_point:
            support_count += 1

        if "return" in pain_point or "pickup" in pain_point:
            return_count += 1

        if "payment" in pain_point:
            payment_count += 1

        if "cancel" in pain_point:
            cancellation_count += 1

        if "different product" in pain_point or "incomplete product" in pain_point:
            wrong_product_count += 1

        if "price" in pain_point:
            pricing_count += 1


print("Meesho Customer Feedback Analysis")
print("----------------------------------")
print("Total Reviews Analyzed:", total_reviews)
print()
print("Delivery Issues:", delivery_count)
print("Refund Issues:", refund_count)
print("Support Issues:", support_count)
print("Return/Pickup Issues:", return_count)
print("Payment Issues:", payment_count)
print("Cancellation Issues:", cancellation_count)
print("Wrong/Incomplete Product Issues:", wrong_product_count)
print("Pricing Issues:", pricing_count)