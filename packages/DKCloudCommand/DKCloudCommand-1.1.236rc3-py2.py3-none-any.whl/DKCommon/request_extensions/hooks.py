import logging
import pprint

LOG = logging.getLogger(__name__)

_pp = pprint.PrettyPrinter(width=79, indent=4, depth=4)


def _truncate(text: str) -> str:
    """Truncate a string to 100 chars."""
    if len(text) > 100:
        return f"{text[:100]}...({len(text) - 100} truncated)"
    else:
        return text


def log_responses(response, *args, **kwargs):
    """A requests hook that logs errors."""
    if response.status_code >= 400:
        try:
            response_text = _truncate(response.text)
        except Exception:
            response_text = "N/A"
        LOG.error(
            "[%s] %s\nHeaders: %s\nResponse: %s",
            response.status_code,
            response.url,
            _pp.pformat(dict(response.headers)),
            response_text,
            internal=True,
            url=response.url,
            status_code=response.status_code,
        )
    return response
