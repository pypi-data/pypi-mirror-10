Introduction
============

The purpose of this package is to provide an extra verification step for Plone
when self-registration is enabled.

When you install this product, before a user can register with the Plone site, they
first must verify they have a valid email address.

This is meant to be a proof-of-concept solution. There are no tests and I haven't
spent a lot of time on it.

Yes, I know very sophisticated spam bots can also automate the email verification
process. To address that, the next step for this package would be to check the email
address against database/API with a known list of bad emails/domains(if there is such a thing).