---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, tests-from-specs]
description: Should invoke tests-from-specs and apply its method
---

We have Xray test cases for checkout and some automated tests. I've pasted both below. How can an agent help close the gap? Start by telling me exactly where we stand.

XRAY EXPORT (checkout)
CHK-101 | Guest can complete checkout with a valid card | Expected: order confirmation shown
CHK-102 | Expired card is rejected | Expected: error "Card expired", no order created
CHK-103 | Promo code SAVE10 reduces subtotal by 10% | Expected: discount line shown
CHK-104 | Cart total recalculates when quantity changes | Expected: updated total
CHK-105 | Free shipping applies above $50 | Expected: shipping $0
CHK-106 | Address validation rejects missing postcode | Expected: inline error
CHK-107 | Order confirmation email is sent | Expected: email within 1 minute
CHK-108 | Checkout should feel fast | Expected: good experience

AUTOMATED TESTS (tests/checkout.spec.ts)
test('CHK-101 guest checkout happy path', ...)
test('CHK-102 expired card rejected', ...)
test.skip('CHK-105 free shipping over 50', ...)   // flaky, skipped since March
test('promo code applies discount', ...)           // no ID; asserts SAVE10 gives 10% off
test('CHK-106 missing postcode shows error', ...)
