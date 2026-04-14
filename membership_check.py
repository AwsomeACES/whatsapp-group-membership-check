from urllib.parse import quote
import requests


DEFAULT_TIMEOUT = 15


def digits(value: str) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def check_member_via_participants(phone_digits: str, group_jid: str, base_url: str, headers: dict | None = None):
    """
    Checks whether a phone number is present in the WhatsApp group participants list.

    This function verifies group membership only.
    It does not read messages, chat history, or conversation content.
    """
    if not phone_digits or not group_jid:
        return None, None, "Missing phone/group"

    encoded_jid = quote(group_jid, safe="")
    url = f"{base_url.rstrip('/')}/api/group/{encoded_jid}/participants"

    try:
        resp = requests.get(url, headers=headers or None, timeout=DEFAULT_TIMEOUT)
        if resp.status_code >= 400:
            return None, None, f"participants endpoint returned HTTP {resp.status_code}"
        payload = resp.json()
    except Exception as exc:
        return None, None, str(exc)

    rows = []
    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        for key in ("participants", "data", "result"):
            val = payload.get(key)
            if isinstance(val, list):
                rows = val
                break

    if not isinstance(rows, list):
        return None, None, "Unexpected participants payload shape"

    target = digits(phone_digits)
    for row in rows:
        candidates = []
        if isinstance(row, str):
            candidates.append(row)
        elif isinstance(row, dict):
            for key in ("phone", "phone_number", "number", "jid", "id", "user"):
                if row.get(key):
                    candidates.append(str(row.get(key)))

        for value in candidates:
            normalized = digits(value)
            if not normalized:
                continue
            if normalized == target or normalized.endswith(target) or target.endswith(normalized):
                return True, True, None

    return True, False, None
