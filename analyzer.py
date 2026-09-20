import argparse
import re
from collections import Counter


def extract_ip(line):
    """Return the source IP address found in a log line, or None."""
    m = re.search(r"from (\S+)", line)
    if m is not None:
        return m.group(1)
    return None


def extract_user(line):
    """Return the username found in a log line, or None."""
    m = re.search(r"for (?:invalid user )?(\S+) from", line)
    if m is not None:
        return m.group(1)
    return None


def extract_status(line):
    """Return "Failed" or "Accepted" for a log line, or None."""
    m = re.search(r"(Failed|Accepted) (?:password|publickey) for", line)
    if m is not None:
        return m.group(1)
    return None


def main():
    parser = argparse.ArgumentParser(description="Analyse SSH login attempts in an auth.log file.")
    parser.add_argument("file", help="path to the log file")
    args = parser.parse_args()

    log_lines = []
    with open(args.file, encoding="utf-8") as f:
        for line in f:
            log_lines.append(line.strip())

    ips = []
    users = []
    statuses = []

    for line in log_lines:
        ip = extract_ip(line)
        user = extract_user(line)
        status = extract_status(line)

        if ip is None or user is None or status is None:
            continue

        ips.append(ip)
        users.append(user)
        statuses.append(status)

    statuses_count = Counter(statuses)
    ips_count = Counter(ips)
    users_count = Counter(users)

    print("\n=== SSH login report ===\n")

    print(f"{'Lines read':<20}{len(log_lines):>3}")
    print(f"{'Attempts analysed':<20}{len(ips):>3}")
    print(f"{'Failed':<20}{statuses_count['Failed']:>3}")
    print(f"{'Accepted':<20}{statuses_count['Accepted']:>3}")

    print("\nTop source IPs")
    for ip, count in ips_count.most_common():
        print(f"  {ip:<18}{count:>3}")

    print("\nTargeted users")
    for user, count in users_count.most_common():
        print(f"  {user:<18}{count:>3}")

    print()


if __name__ == "__main__":
    main()