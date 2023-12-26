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
        match rule:
            case "openstack":
                highlighter_object = OpenstackRegexHighlighter()
            case "juju":
                highlighter_object = JujuRegexHighlighter()
            case "kubernetes":
                highlighter_object = KubernetesRegexHighlighter()
            case _:
                highlighter_object = None
        if highlighter_object:
            return Console(highlighter=highlighter_object, theme=self.get_theme())
        return Console()


# if __name__ == "__main__":
#     string = "Send cloud disabled lost XXX funds :) to money@example.org "
#     string += "downbadxxx  xxx and   active make it ACTIVE lol but not 2023-10-10 down"

#     dc = Dispatcher()
#     console = dc.get_console("openstack")
#     console.print(string)

#     console = dc.get_console()
#     console.print(string)
