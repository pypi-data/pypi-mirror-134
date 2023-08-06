import os

# Used if we can't determine the Unicode version supported via environment variables.
_FALLBACK_UNICODE_VERSION = "9.0.0"

# ucs-detect was used to determine which version of Unicode a terminal supports.
# TODO: Windows Terminal?
_TERMINAL_SUPPORT = {
    "iTerm.app": {
        "unknown": "12.1.0",
        "3.4.15": "12.1.0",
    },
    "Apple_Terminal": {
        "unknown": "13.0.0",
        "443": "13.0.0",
    },
    "vscode": {
        "unknown": "12.1.0",
        "1.63.2": "12.1.0",
    },
    "alacritty": {
        "unknown": "13.0.0",
    },
    "JetBrains-JediTerm": {
        "unknown": "13.0.0",
    },
}


def _detect_unicode_version() -> str:
    """
    Returns the Unicode version supported by the current terminal program and version.
    Terminal program and version are detected using environment variables:

     - ``UNICODE_VERSION`` env var is "standard", supported by wcwidth package,
     - ``TERM_PROGRAM`` env var is exported by Apple Terminal, iTerm2, VSCODE.
     - ``TERMINAL_EMULATOR`` env var is exported by jediterm (JetBrains IDE terminals),
     - ``TERM_PROGRAM_VERSION`` is exported by all terminals which export TERM_PROGRAM (see above)

    Returns: Unicode version string supported by the terminal software.
    """
    unicode_env_var = os.getenv("UNICODE_VERSION")
    if unicode_env_var:
        return unicode_env_var

    term_program = os.getenv("TERM_PROGRAM", os.getenv("TERMINAL_EMULATOR"))
    # Alacritty doesn't export an env var specifically for identifying itself,
    # but we can check for the log env var instead to detect it.
    if not term_program and os.getenv("ALACRITTY_LOG"):
        term_program = "alacritty"

    if not term_program:
        return _FALLBACK_UNICODE_VERSION

    term_version = os.getenv("TERM_PROGRAM_VERSION", "unknown")
    program_version_map = _TERMINAL_SUPPORT.get(term_program, {})
    supported_unicode_version = program_version_map.get(
        term_version, _FALLBACK_UNICODE_VERSION
    )
    return supported_unicode_version
