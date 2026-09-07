<div align="center">
  <img src="./banner.svg" alt="adcs-audit" width="800">
</div>

# adcs-audit

> Review AD Certificate Services templates for known misconfiguration classes

Part of a red-team tooling collection for **authorised** security testing.

## Install

```bash
git clone https://github.com/amooryx/adcs-audit.git
cd adcs-audit
```

## Usage

```bash
python adcs_audit.py <target>
```

| Flag | Description |
|---|---|
| `-o, --output` | Write results to a file |
| `-v, --verbose` | Verbose output |
| `-y, --yes` | Skip the authorisation prompt |

## Disclaimer

> **Authorised security testing only.** Use this against systems you own or have
> explicit written permission to test. The tool prompts for authorisation before
> acting and is provided for professional engagements, labs, and research.

## Author

**Omar Khalid** — [omareldemery.com](https://omareldemery.com) | [@amooryx](https://github.com/amooryx)

Certifications: OSCP+ · OSCP · CRTP · eWPTX · eCPPT · eCDFP · eCIR · eJPT
