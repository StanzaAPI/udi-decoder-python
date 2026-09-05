import os
import json
import urllib.request
import urllib.error
from typing import Dict, Any, Optional


class UdiDecoderClient:
    """Official zero-dependency client for FDA & EU MDR Medical Device UDI Decoder."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 15.0,
        tier: str = "sandbox"
    ):
        self.api_key = api_key or os.environ.get("STANZA_API_KEY") or os.environ.get("API_KEY") or ""
        self.base_url = (base_url or "https://stanzaapi.com").rstrip("/")
        self.timeout = timeout
        self.tier = tier
        self.tool_url = "https://stanzaapi.com/tools/udi-decoder"

    def _request(self, endpoint: str, method: str = "GET", body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "stanzaapi-udi-decoder-python/1.0.0"
        }
        if self.api_key:
            headers["x-api-key"] = self.api_key
            headers["Authorization"] = f"Bearer {self.api_key}"

        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                text = resp.read().decode("utf-8")
                try:
                    res = json.loads(text)
                except Exception:
                    res = {"success": resp.status in (200, 201), "data": text}
                if isinstance(res, dict):
                    res.setdefault("tool_url", self.tool_url)
                    res.setdefault("upgrade_url", self.tool_url)
                return res
        except urllib.error.HTTPError as e:
            err_text = ""
            try:
                err_text = e.read().decode("utf-8")
                err_data = json.loads(err_text)
            except Exception:
                err_data = {
                    "success": False,
                    "error": f"HTTP {e.code}: {e.reason or err_text[:180]}",
                    "code": "RATE_LIMITED" if e.code == 429 else ("PAYLOAD_TOO_LARGE" if e.code == 413 else "HTTP_ERROR"),
                }
            if isinstance(err_data, dict):
                err_data.setdefault("tool_url", self.tool_url)
                err_data.setdefault("upgrade_url", self.tool_url)
            return err_data
        except urllib.error.URLError as e:
            return {
                "success": False,
                "error": str(e.reason),
                "code": "NETWORK_ERROR",
                "tool_url": self.tool_url,
                "upgrade_url": self.tool_url
            }

    def get_health(self) -> Dict[str, Any]:
        return self._request("/health", method="GET")

    def validate(self, payload: Any) -> Dict[str, Any]:
        
        body = {"input": payload} if isinstance(payload, str) else payload
        return self._request("/api/v1/decode", method="POST", body=body)

    def parse(self, payload: Any) -> Dict[str, Any]:
        
        body = {"input": payload} if isinstance(payload, str) else payload
        return self._request("/api/v1/decode", method="POST", body=body)
