# Momo Stimulation Application

A simple Python command-line simulation of a mobile money (MoMo) service.

## Overview

This project is a learning/demo application that models common wallet activities such as:

- transferring money
- buying airtime
- buying internet bundles
- checking wallet balance
- topping up wallet
- allowing cash-out
- verifying a PIN and a hash code access flow

## Project structure

- `main.py` – entry point and main menu
- `config.py` – configuration values such as the default balance and PIN/hash code
- `transfer.py` – money transfer logic
- `airtimes.py` – airtime and bundle purchase logic
- `wallet.py` – wallet balance and top-up functions
- `cash_out.py` – cash-out flow
- `security.py` – PIN validation
- `validate.py` – phone number validation

## How to run

From the project folder, run:

```bash
python main.py
```

You will be prompted for the hash code defined in `config.py` before the menu is shown.

## Notes

This is a simulation, not a real banking or mobile money integration. The app stores values in memory and is intended for practice, demos, or education.


