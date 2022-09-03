from dataclasses import dataclass
from typing import List, Literal, Optional


PaymentFrequency = Literal["monthly", "annual"]


@dataclass
class QuoteAttempt:
    id: str
    forename: str
    surname: str
    email: str
    is_premium: bool
    payment_frequency: PaymentFrequency


@dataclass
class QuoteResult:
    id: str
    quote_attempt_id: str
    successful_quote: bool
    total_premium: str
    quote_expiry_date: str
    messages: Optional[List[str]]


@dataclass
class PurchaseAttempt:
    id: str
    quote_result_id: str
    payment_method: str
    payment_details_token: str

@dataclass
class PurchaseResult:
    id: str
    purchase_attempt_id: str
    successful_purchase: bool
    messages: Optional[List[str]]
