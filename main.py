from bltypes import QuoteAttempt, QuoteResult


def main():
    example_qa = QuoteAttempt(
        id="id_01",
        forename="John",
        surname="Smith",
        email="john.smith@test.com",
        is_premium=False,
        payment_frequency="monthly",
    )
    quote_result = submit_quote(example_qa)
    print(quote_result)


def submit_quote(quote_attempt: QuoteAttempt) -> QuoteResult:
    quote_attempt_id = quote_attempt.id
    quote_result = QuoteResult(
        id="id_02",
        quote_attempt_id=quote_attempt_id,
        successful_quote=True,
        total_premium="14.02",
        quote_expiry_date="2022-09-05",
        messages=None,
    )
    return quote_result


if __name__ == "__main__":
    main()
