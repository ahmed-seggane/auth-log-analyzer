# auth-log-analyzer

Parses Linux `auth.log` lines and reports SSH login attempts, failures and top source IPs.

Work in progress.

## Requirements

Python 3.10+

No external dependencies.

## Usage

```
python3 analyzer.py sample_auth.log
python3 analyzer.py --help
```

The log file path is a required argument, so the tool can be pointed at any
file without editing the code.

## Sample output

```
=== SSH login report ===

Lines read           15
Attempts analysed    12
Failed                9
Accepted              3

Top source IPs
  203.0.113.42        5
  192.0.2.15          4
  198.51.100.7        3

Targeted users
  ahmed               4
  root                3
  admin               2
  postgres            2
  test                1
```

## How it works

Each line is matched against regular expressions that describe the shape of an
SSH authentication event. A line that does not match is skipped, which is why
the report shows both the number of lines read and the number of attempts
actually analysed — a real `auth.log` also contains `sudo`, `cron` and other
entries that are not login attempts.

Three patterns are used: one for the source IP, one for the targeted username
(handling both `for <user> from` and `for invalid user <user> from`), and one
for the outcome.

Sample addresses are RFC 5737 documentation ranges.

## What it does not do yet

- Only handles sshd password and publickey authentication lines
- Ignores other SSH events, such as connections closed during authentication
- No filtering by date or time
- Plain text output only — no JSON or CSV