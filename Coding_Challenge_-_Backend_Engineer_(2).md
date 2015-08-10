![Venmo logo](https://dl.dropboxusercontent.com/s/puvb3qyb272qo28/logoblue-233x44.png)

*Venmo values trust. Please do not share this coding challenge with anyone else.*

Imagine that your phone and wallet are trying to have a beautiful baby.
In order to make this happen, you must write a social payment app.
Implement a program that will feature users, credit cards, and payment feeds.

## Requirements:

Your executable must support two modes of execution:

  * interactively (from stdin), when run with no arguments
  * from a file of newline-delimited commands, when provided with one argument

State does not need to persist between runs.

You may implement your solution in any programming language.
If you wrote tests, include them with your submission.

In addition, please provide a README that explains:

  * how to make/run your code (a script or makefile is appreciated!)
  * your design decisions
  * the language you chose, and why you chose it

### Commands

You must support the following commands.
Any input that does not fit these specifications should print an error.

0. "user" will create a new user with a given name.
  * e.g., `user <user>`
  * User names should be alphanumeric but also allow underscores and dashes.
  * User names should be no shorter than 4 characters but no longer than 15.
  * Users start with a balance of $0.

0. "add" will create a new credit card for a given name, card number
  * e.g., `add <user> <card_number>`
  * Card numbers should be validated using Luhn-10.
  * Cards that fail Luhn-10 will display an error.
  * Cards that have already been added will display an error.
  * Users can only have one card.
    Attempting to add a second valid card will display an error.

0. "pay" will create a payment between two users.
  * e.g., `pay <actor> <target> <amount> <note>`
  * `<actor>` and `<target>` are usernames that were created in #1
  * Users cannot pay themselves.
  * Payments will always charge the actor's credit card (not decrement their balance).
  * Payments will always increase the target's balance.
  * If the actor user has no credit card, display an error.
  
0. "feed" will display a feed of the respective user's payments.
  * e.g., `feed <user>`

0. "balance" will display a user's balance
  * e.g. `balance <user>`
  
### Input Assumptions
  * All input will be space delimited.
  * Credit card numbers may vary in length, up to 19 characters.
  * Credit card numbers will always be numeric.
  * Amounts will be prefixed with "$" and will be dollars and cents

### Example Input/Output:

Extra newlines in this example are for clarity.

    $ ./mini-venmo
    > user Thomas
    > user Lisa
    > user
    ERROR: invalid arguments
    > foobar
    ERROR: command not recognized
    > user Quincy

    > add Thomas 4111111111111111
    > add Thomas 5454545454545454
    ERROR: this user already has a valid credit card
    > add Lisa 5454545454545454
    > add Quincy 1234567890123456
    ERROR: this card is invalid

    > pay Thomas Lisa $10.25 burritos
    > pay Thomas Quincy $10.00 you're awesome
    > pay Lisa Quincy $5.00 pot-luck supplies
    > pay Thomas Thomas $1.00 to myself
    ERROR: users cannot pay themselves
    > pay Quincy Thomas $2.00 a subway card
    ERROR: this user does not have a credit card

    > add Quincy 5454545454545454
    ERROR: that card has already been added by another user, reported for fraud!
    > add Quincy 5555555555554444
    > pay Quincy Thomas $14.50 a redbull vodka

    > feed Quincy
    -- Thomas paid you $10.00 for you're awesome
    -- Lisa paid you $5.00 for pot-luck supplies
    -- You paid Thomas $14.50 for a redbull vodka
    > balance Quincy
    -- $15.00
    > feed Thomas
    -- You paid Lisa $10.25 for burritos
    -- You paid Quincy $10.00 for you're awesome
    -- Quincy paid you $14.50 for a redbull vodka
    > feed Lisa
    -- Thomas paid you $10.25 for burritos
    -- You paid Quincy $5.00 for pot-luck supplies
