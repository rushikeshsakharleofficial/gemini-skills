# SMTP Best Practices

## DMARC Alignment
- **Identifier Alignment**: Ensure that the domain in the `From:` header matches the domain used in SPF and/or DKIM.
- **Strict vs. Relaxed**: Use `adkim=s` or `aspf=s` for strict alignment, requiring an exact domain match. Relaxed alignment allows subdomains.

## IP Reputation
- **Warm-up**: Gradually increase sending volume from new IPs to establish trust with mailbox providers.
- **Monitoring**: Regularly check blacklists (e.g., Spamhaus, Barracuda) and feedback loops (FBLs).
- **PTR Records**: Ensure valid Reverse DNS (rDNS) is configured for all sending IPs.

## TLS Ciphers for MTAs
- **Encryption**: Prefer STARTTLS for opportunistic encryption.
- **Cipher Suites**: Use modern, secure ciphers. Avoid SSLv2, SSLv3, and TLS 1.0/1.1.
- **MTA-STS**: Implement MTA Strict Transport Security to enforce TLS encryption for incoming mail.

## SPF (Sender Policy Framework)
- **Lookups**: Keep the number of DNS lookups under the limit of 10.
- **Mechanisms**: Use `ip4`, `ip6`, and `include` appropriately. End with `~all` (SoftFail) or `-all` (Fail).

## DKIM (DomainKeys Identified Mail)
- **Key Length**: Use at least 2048-bit RSA keys.
- **Rotation**: Regularly rotate DKIM selectors to mitigate the impact of compromised keys.
