from cmdline_parser import args_parser
from exchange_rate import calculate_exchange_rate
from in_ind import india_tax
from out_ger import german_fees


def main(euros_to_transfer: float) -> dict:
    # german bank fees
    fees_german = german_fees(transfer_amt=euros_to_transfer)

    # currency conversion (EUR -> INR)
    currencies_info = {
        "base_curr": "EUR",
        "curr_req": ["INR"]
    }

    # exchange rate
    euros_to_inr_rate = calculate_exchange_rate(currencies=currencies_info)

    # exchanged amount
    amt_in_inr = euros_to_transfer * euros_to_inr_rate[currencies_info["curr_req"][0]]

    # indian tax
    tax_india = india_tax(incoming_amt=amt_in_inr)

    # inr received after indian tax deduction
    inr_received = amt_in_inr - tax_india

    # summary of transaction
    print(f"""
        Transfer Amount: {euros_to_transfer} EUR
        German Bank Fees: {fees_german} EUR
        Exchange Rate: 1 EUR = {euros_to_inr_rate[currencies_info["curr_req"][0]]} INR
        Amount in INR: {amt_in_inr}
        India GST Tax: {tax_india} INR
        Amount Received in India: {inr_received} INR
        """)

    return {
        "transfer_amount_euro": euros_to_transfer,
        "german_bank_fees": fees_german,
        "exchange_rate": euros_to_inr_rate[currencies_info["curr_req"][0]],
        "amount_in_inr": amt_in_inr,
        "india_gst_tax": tax_india,
        "received_amount_in_india": inr_received
    }


if __name__ == '__main__':
    args = args_parser()
    transaction_info = main(euros_to_transfer=args.amount_euros[0])
    # transaction_info = main(euros_to_transfer=1)
