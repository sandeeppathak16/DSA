import re


def has_abba(s):
    for i in range(len(s) - 3):
        a, b, c, d = s[i:i + 4]

        if a == d and b == c and a != b:
            return True

    return False


def get_abas(s):
    abas = []

    for i in range(len(s) - 2):
        a, b, c = s[i:i + 3]

        if a == c and a != b:
            abas.append(a + b + c)

    return abas


def supports_tls(ip):
    outside = re.split(r'\[.*?\]', ip)
    inside = re.findall(r'\[(.*?)\]', ip)

    if any(has_abba(part) for part in inside):
        return False

    return any(has_abba(part) for part in outside)


def supports_ssl(ip):
    outside = re.split(r'\[.*?\]', ip)
    inside = re.findall(r'\[(.*?)\]', ip)

    abas = []

    for part in outside:
        abas.extend(get_abas(part))

    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]

        if any(bab in part for part in inside):
            return True

    return False


def solve(filename="7.txt", part=1):
    with open(filename) as f:
        ips = [line.strip() for line in f]

    if part == 1:
        return sum(supports_tls(ip) for ip in ips)

    return sum(supports_ssl(ip) for ip in ips)