"""Module to enable context highlighting of rtab."""

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme


class OpenstackRegexHighlighter(RegexHighlighter):  # pylint: disable=too-few-public-methods
    """Highlight rules specific to openstack."""

    highlights = [
        r"(?P<positive>active|ACTIVE|:\))",
        r"(?P<negative>XXX|down|disabled)",
    ]


class JujuRegexHighlighter(RegexHighlighter):  # pylint: disable=too-few-public-methods
    """Highlight rules specific to juju."""

    highlights = [
        r"(?P<positive>active|idle|\bup\b)",
        r"(?P<negative>down|lost)",
    ]


class KubernetesRegexHighlighter(RegexHighlighter):  # pylint: disable=too-few-public-methods
    """Highlight rules specific to kubernetes."""

    highlights = [
        r"(?P<positive>active|idle|\bup\b)",
        r"(?P<negative>down|lost)",
    ]


class Dispatcher:
    """Class to get a rich console object based on highlight mode requested."""

    @staticmethod
    def get_theme() -> Theme:
        """Generate a rich theme object without prefix."""
        return Theme(
            {
                "positive": "green",
                "negative": "red",
            }
        )

    def get_console(self, rule: str = "") -> Console:
        """Generate a rich console object with highlight rules.

        :param rule: string to match a specific highlighting rule
        """
        theme = self.get_theme()
        match rule:
            case "openstack":
                return Console(highlighter=OpenstackRegexHighlighter(), theme=theme)
            case "juju":
                return Console(highlighter=JujuRegexHighlighter(), theme=theme)
            case "kubernetes":
                return Console(highlighter=KubernetesRegexHighlighter(), theme=theme)
            case _:
                return Console()
