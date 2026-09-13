# auth-log-analyzer

Parses Linux `auth.log` lines and reports SSH login attempts, failures and top source IPs.

Work in progress.

## Requirements

Python 3.10+

No external dependencies.

## Usage

```
python3 analyzer.py
```

## Sample output

```
=== SSH login report ===

Total attempts     12
Failed              9
Accepted            3

Top source IPs
  203.0.113.42      5
  192.0.2.15        4
  198.51.100.7      3

Targeted users
  ahmed             4
  root              3
  admin             2
  postgres          2
  test              1
```

## How it works

Each line is parsed by anchoring on the word `from`: the source IP is the token
right after it, and the targeted username the token right before it. This handles
both `for <user> from` and `for invalid user <user> from` without depending on
fixed field positions.

Sample addresses are RFC 5737 documentation ranges.

## What it does not do yet

- Log lines are hardcoded in the script; it does not read a file
- No command-line arguments
- No filtering by date or time
- Only handles sshd password and publickey lines