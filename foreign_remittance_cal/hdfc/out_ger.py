def german_fees(transfer_amt: float) -> float:
    # currency is Euro (EUR)
    paperless_order_percent = 1.5
    swift_fees = 1.55
    third_party_fees = 25

    if (paperless := (transfer_amt * (paperless_order_percent / 100))) > 10:
        return paperless + swift_fees + third_party_fees
    return 10 + swift_fees + third_party_fees


if __name__ == '__main__':
    outgoing_amount = 1
    total_txn_fees = german_fees(transfer_amt=outgoing_amount)
