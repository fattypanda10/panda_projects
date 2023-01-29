# currency is Rupees (INR)

# slab 1
def slab1_taxable_amt(amount: float) -> float:
    slab_rate = 1
    taxable_amt = amount * (slab_rate * (1 / 100))
    return 250 if taxable_amt <= 250 else taxable_amt


# slab 2
def slab2_taxable_amt(amount: float) -> float:
    slab_rate = 0.5
    taxable_amt = 1000 + ((amount - 100000) * (slab_rate * (1 / 100)))
    return taxable_amt


# slab 3
def slab3_taxable_amt(amount: float) -> float:
    slab_rate = 0.1
    taxable_amt = 5500 + ((amount - 1000000) * (slab_rate * (1 / 100)))
    return taxable_amt


# total calculated tax
def india_tax(incoming_amt: float) -> float:
    gst_rate = 18
    taxable_value = 0
    if 0 <= incoming_amt <= 100000:
        taxable_value = slab1_taxable_amt(incoming_amt)
    elif 100000 < incoming_amt < 1000000:
        taxable_value = slab2_taxable_amt(incoming_amt)
    elif incoming_amt > 1000000:
        taxable_value = slab3_taxable_amt(incoming_amt)

    total_gst = taxable_value * (gst_rate / 100)
    return total_gst if total_gst < 60000 else 60000


if __name__ == '__main__':
    transfer_amt = 2000000  # EUR
    total_tax = india_tax(incoming_amt=transfer_amt)
