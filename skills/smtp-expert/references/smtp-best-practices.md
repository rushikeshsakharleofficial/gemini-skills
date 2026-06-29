# SMTP Best Practices

Last reviewed: 2026-06-29

This reference is for delivery engineering, abuse prevention, and MTA troubleshooting. Prefer official mailbox-provider pages, IETF RFCs, and observed SMTP responses over forum advice. Community reports are useful signals, but do not change production mail policy from a single community post.

## Provider baseline: Gmail and Yahoo

As of the 2024 bulk-sender enforcement model used by Gmail and Yahoo, treat the following as the minimum baseline for any serious sender:

- Authenticate every sending domain. All senders need SPF or DKIM at minimum; bulk senders should use SPF, DKIM, and DMARC.
- Keep spam complaint rate below 0.3% where provider telemetry is available.
- Maintain valid forward DNS and reverse DNS. The PTR hostname should resolve back to the same sending IP.
- Use TLS for SMTP transport where supported.
- Follow RFC 5321 and RFC 5322 message formatting rules.
- For marketing or subscribed mail, support easy unsubscribe. For high-volume Gmail/Yahoo delivery, implement one-click unsubscribe headers and a visible unsubscribe link in the body.
- Do not mix transactional, OTP/security, and promotional traffic on the same reputation identity when volume is meaningful. Segment by IP pool, DKIM domain, or both.

## DMARC alignment

- DMARC passes when SPF or DKIM passes and the authenticated domain aligns with the visible `From:` domain.
- Relaxed alignment is acceptable for many provider requirements, but strict alignment (`adkim=s` and/or `aspf=s`) can be used for high-control domains after testing.
- Start new domains with `p=none` plus aggregate reporting (`rua=`), verify all legitimate senders, then move gradually to `quarantine` or `reject`.
- For direct mail to Gmail at bulk volume, the `From:` domain must align with either the SPF domain or the DKIM domain.

Operational checks:

```bash
dig +short TXT _dmarc.example.com
# Expect one valid v=DMARC1 record, not multiple conflicting records.
```

## SPF

- RFC 7208 requires SPF evaluators to limit DNS-querying mechanisms/modifiers to 10. Exceeding this returns `permerror`.
- Count `include`, `a`, `mx`, `ptr`, `exists`, and `redirect`. Prefer explicit `ip4` and `ip6` mechanisms for fixed infrastructure because they do not add DNS-querying terms.
- Avoid multiple SPF TXT records for the same domain.
- End intentionally with `~all` during rollout or `-all` after all legitimate senders are known.

Operational checks:

```bash
dig +short TXT example.com
# Verify exactly one SPF record beginning with v=spf1.
```

## DKIM

- Use DKIM for every mail stream; it survives forwarding better than SPF.
- Prefer 2048-bit RSA keys when DNS provider and MTA tooling support them. Gmail requires at least 1024-bit DKIM keys for mail to personal Gmail accounts and recommends 2048-bit keys.
- Rotate selectors with overlap: publish the new selector, sign with it, verify live traffic, then retire the old selector after caches and queues drain.
- Do not reuse one selector across unrelated customers or unrelated mail streams.

Operational checks:

```bash
dig +short TXT selector._domainkey.example.com
# Verify one TXT record with v=DKIM1 and the expected public key.
```

## IP and domain reputation

- Warm up new IPs and new DKIM domains slowly with engaged recipients first.
- Monitor provider postmaster tools, SMTP enhanced status codes, deferrals, blocklist state, bounce rate, and complaint rate.
- Avoid sudden traffic spikes after changing IP pools, DKIM domains, message templates, headers, URLs, or tracking domains.
- If Gmail returns quota/rate deferrals such as 4.7.x, reduce rate and connections first; do not keep retrying at the same rate.
- Shared IP reputation is shared. One bad client can damage all clients on the same pool.

## Reverse DNS and HELO/EHLO hygiene

- Every sending IP must have a PTR record.
- PTR hostname must have matching forward A or AAAA back to the sending IP.
- Use a stable HELO/EHLO hostname that resolves correctly and is not a generic cloud hostname.
- Keep hostname, PTR, TLS certificate naming, and monitoring labels consistent enough for operations to debug quickly.

Operational checks:

```bash
dig +short -x 192.0.2.10
dig +short A mail.example.com
dig +short AAAA mail.example.com
```

## TLS, MTA-STS, and transport security

- Disable obsolete SSLv2, SSLv3, TLS 1.0, and TLS 1.1 where supported by the MTA and OS.
- Support STARTTLS for inbound and outbound SMTP.
- MTA-STS lets a receiving domain publish that it supports TLS-secured SMTP and whether senders should refuse MX hosts without TLS and a trusted certificate.
- MTA-STS requires both DNS and HTTPS policy material: `_mta-sts.<domain>` TXT with `v=STSv1; id=...` and `https://mta-sts.<domain>/.well-known/mta-sts.txt`.
- Deploy MTA-STS in testing mode first, verify reports, then move to enforce mode.

Example policy body:

```text
version: STSv1
mode: testing
mx: mail.example.com
max_age: 86400
```

## List unsubscribe

For marketing/subscribed traffic, include both a machine-readable unsubscribe option and a visible body link. For one-click unsubscribe, include headers like:

```text
List-Unsubscribe-Post: List-Unsubscribe=One-Click
List-Unsubscribe: <https://example.com/unsubscribe/token>
```

Honor unsubscribe requests quickly. Yahoo states that unsubscribe requests should be processed within 2 days; Gmail requires one-click unsubscribe for marketing/subscribed mail from senders above 5,000 messages/day to Gmail personal accounts.

## Troubleshooting checklist

1. Capture the exact SMTP response, enhanced status code, remote MX, source IP, HELO, sender domain, DKIM selector, and queue ID.
2. Verify DNS first: MX, A/AAAA, PTR, SPF, DKIM, DMARC, MTA-STS.
3. Check whether the failure is authentication, alignment, reputation, rate limit, content, recipient validity, or transport/TLS.
4. Compare failing traffic with working traffic: IP pool, DKIM selector, From domain, template, URL domain, bounce domain, and recipient MX.
5. Reduce traffic during active deferrals; preserve queue evidence before making bulk changes.
6. Record the final fix in the SMTP learning loop so future runs can reuse the finding.

## Official references

- Gmail Help: Email sender guidelines — https://support.google.com/mail/answer/81126
- Yahoo Sender Hub: Sender Best Practices — https://senders.yahooinc.com/best-practices/
- RFC 7208: Sender Policy Framework — https://www.rfc-editor.org/rfc/rfc7208
- RFC 8461: SMTP MTA Strict Transport Security — https://www.rfc-editor.org/rfc/rfc8461
- RFC 8058: One-Click Unsubscribe — https://www.rfc-editor.org/rfc/rfc8058
- RFC 5321: Simple Mail Transfer Protocol — https://www.rfc-editor.org/rfc/rfc5321
- RFC 5322: Internet Message Format — https://www.rfc-editor.org/rfc/rfc5322
