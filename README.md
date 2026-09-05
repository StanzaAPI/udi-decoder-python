# FDA & EU MDR Medical Device UDI Decoder — Python SDK

[![PyPI version](https://img.shields.io/pypi/v/stanzaapi-udi-decoder.svg)](https://pypi.org/project/stanzaapi-udi-decoder/)
[![Python Versions](https://img.shields.io/pypi/pyversions/stanzaapi-udi-decoder.svg)](https://pypi.org/project/stanzaapi-udi-decoder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stanza API](https://img.shields.io/badge/Powered%20by-Stanza-blue)](https://stanzaapi.com)

> Parse GS1-128, HIBCC Modulo-43, and ICCBBA ISBT 128 medical device barcodes for FDA 21 CFR 801 & EU MDR compliance.

Official, zero-dependency Python 3.8+ client library for **FDA & EU MDR Medical Device UDI Decoder**, built on the [Stanza Micro-API Network](https://stanzaapi.com). Intended for enterprise data pipelines, backend verification, and sub-5ms edge compute.

* 🌐 **Live Web Playground:** [Test your inputs online](https://stanzaapi.com/tools/udi-decoder)
* 📚 **API Documentation:** [View full schema on Stanza](https://stanzaapi.com/tools/udi-decoder)
* ⚡ **Platform Overview:** [Explore the Stanza Developer Network](https://stanzaapi.com)

---

## 📦 Installation

```bash
pip install stanzaapi-udi-decoder
```

---

## 🚀 Quickstart

```python
import os
from stanzaapi_udi_decoder import UdiDecoderClient

# Initialize client (api_key optional for local evaluation)
client = UdiDecoderClient(
    api_key=os.getenv("STANZA_API_KEY")
)

# Execute deterministic validation
response = client.parse("+H12345678901/$$3260101")

if response.get("success"):
    print("Verification Success:", response["data"])
else:
    print("Validation Error:", response.get("error"), response.get("code"))
```

---

## 📄 Example Response

```json
{
  "success": true,
  "data": {
    "valid": true,
    "issuing_agency": "HIBCC",
    "di": "H12345678901",
    "lot": "3260101"
  }
}
```

---

## ⚙️ Client Options

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `api_key` | `Optional[str]` | `os.getenv("STANZA_API_KEY")` | Your [Stanza API Key](https://stanzaapi.com). Required for production quotas. |
| `base_url` | `Optional[str]` | `"https://stanzaapi.com"` | API endpoint base URL. Custom endpoints supported for VPC enclaves. |
| `timeout` | `int` | `15` | Request timeout in seconds. |


---

## 🔗 Useful Links

* [FDA & EU MDR Medical Device UDI Decoder Interactive Sandbox](https://stanzaapi.com/tools/udi-decoder)
* [Stanza Developer Directory](https://stanzaapi.com)
* [Source Code & Issue Tracker](https://github.com/stanzaapi/udi-decoder-python)

## 📄 License

MIT © Stanza — Powered by [Stanza](https://stanzaapi.com).
