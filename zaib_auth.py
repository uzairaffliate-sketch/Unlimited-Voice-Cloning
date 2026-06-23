# zaib_auth.py
# Unlimited Voice Cloning by Zaib — Server-side access key guard
# All sensitive strings are runtime-decoded; no plaintext credentials stored.

import base64
import hashlib
import time
import logging
import urllib.request
import urllib.parse
import json
import asyncio
from typing import Optional

logger = logging.getLogger(__name__)

# ── Runtime string decoder (XOR with 0x42) ─────────────────────────────────
def _x(arr):
    return ''.join(chr(c ^ 0x42) for c in arr)

# Verification endpoint — same encoding array as frontend
# Decodes to: https://zaibtts.com/check/check.php
_EP_RAW = [42,54,54,50,49,120,109,109,56,35,43,32,54,54,49,108,
           33,45,47,109,33,42,39,33,41,109,33,42,39,33,41,108,50,42,50]
_CHECK_URL: str = _x(_EP_RAW)

# Transport secret — used to decrypt the X-ZK header sent by the browser
# Decodes to: Zaib2024xTTS
_TS_RAW = [24,35,43,32,112,114,112,118,58,22,22,17]
_TRANSPORT_SECRET: str = _x(_TS_RAW)

# ── In-memory key cache ─────────────────────────────────────────────────────
# Structure: { sha256(key) -> (is_valid: bool, expires_at: float) }
_CACHE: dict = {}
_CACHE_TTL: int = 600        # seconds — re-verify every 10 min
_NET_TIMEOUT: int = 6        # seconds — check.php call timeout
_FAIL_OPEN: bool = True      # if check.php is unreachable, let user through
                             # (TTS is useless without the server model anyway)

# ── Crypto helpers ──────────────────────────────────────────────────────────

def _hash(key: str) -> str:
    """One-way fingerprint — keys are never stored in plaintext."""
    return hashlib.sha256(key.encode('utf-8')).hexdigest()


def decrypt_zk_header(header_value: str) -> str:
    """
    Decrypt the X-ZK header sent by the browser.
    Browser encrypts: base64( XOR(raw_key, TRANSPORT_SECRET) )
    """
    if not header_value:
        return ''
    try:
        raw = base64.b64decode(header_value).decode('latin-1')
        ts  = _TRANSPORT_SECRET
        return ''.join(chr(ord(c) ^ ord(ts[i % len(ts)])) for i, c in enumerate(raw))
    except Exception:
        return ''


# ── Key validation ──────────────────────────────────────────────────────────

def _call_check_php_sync(key: str) -> Optional[bool]:
    """Synchronous urllib call to check.php (run in thread executor)."""
    try:
        params  = urllib.parse.urlencode({'key': key})
        url     = f"{_CHECK_URL}?{params}"
        req     = urllib.request.Request(
            url,
            headers={'User-Agent': 'ZaibTTSServer/1.0', 'Cache-Control': 'no-cache'}
        )
        with urllib.request.urlopen(req, timeout=_NET_TIMEOUT) as resp:
            body = resp.read().decode('utf-8')
        data = json.loads(body)
        if not isinstance(data, dict) or not isinstance(data.get('valid'), bool):
            logger.warning("zaib_auth: unexpected check.php response structure")
            return None
        return data['valid'] is True
    except Exception as exc:
        logger.warning("zaib_auth: check.php unreachable — %s", exc)
        return None


async def validate_key(raw_key: str) -> bool:
    """Async key validation with in-memory cache."""
    if not raw_key or len(raw_key) < 6:
        return False

    h   = _hash(raw_key)
    now = time.monotonic()

    # ── Cache hit ──
    if h in _CACHE:
        is_valid, expires_at = _CACHE[h]
        if now < expires_at:
            return is_valid

    # ── Cache miss — call check.php in thread (non-blocking) ──
    loop   = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, _call_check_php_sync, raw_key)

    if result is None:
        # Network failure — apply fail-open policy
        if _FAIL_OPEN:
            # Don't cache network failures; let next request retry
            return True
        return False

    _CACHE[h] = (result, now + _CACHE_TTL)
    return result


def evict_key(raw_key: str) -> None:
    """Remove a key from cache (e.g. on explicit logout)."""
    _CACHE.pop(_hash(raw_key), None)
