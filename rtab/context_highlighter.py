"""Module to enable context highlighting of rtab."""

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme


class OpenstackRegexHighlighter(RegexHighlighter):
    # base_style = "openstack."
    highlights = [
        r"(?P<positive>active|ACTIVE|:\))",
        r"(?P<negative>XXX|down|disabled)",
    ]


class JujuRegexHighlighter(RegexHighlighter):
    # base_style = "juju."
    highlights = [
        r"(?P<positive>active|idle|\bup\b)",
        r"(?P<negative>down|lost)",
    ]


class KubernetesRegexHighlighter(RegexHighlighter):
    highlights = [
        r"(?P<positive>active|idle|\bup\b)",
        r"(?P<negative>down|lost)",
    ]


class Dispatcher:
    def __init__(self, rule: str = ""):
        self.rule = rule

    # def get_theme(self) -> Theme():
    #     if self.rule:
    #         self.rule = self.rule + "."
    #     return Theme(
    #         {
    #             f"{self.rule}positive": "green",
    #             f"{self.rule}negative": "red",
    #         }
    #     )

    def get_theme(self) -> Theme():
        return Theme(
            {
                f"positive": "green",
                f"negative": "red",
            }
        )

    def get_highlighter(self):
        match self.rule:
            case "openstack":
                return OpenstackRegexHighlighter()
            case "juju":
                return JujuRegexHighlighter()
            case "kubernetes":
                return KubernetesRegexHighlighter()
            case _:
                return OpenstackRegexHighlighter()


if __name__ == "__main__":
    string = "Send cloud disabled lost XXX funds :) to money@example.org downbadxxx  xxx and   active make it ACTIVE lol but not 2023-10-10 down"
    dc = Dispatcher("openstack")
    console = Console(highlighter=dc.get_highlighter(), theme=dc.get_theme())
    console.print(string)

    dc = Dispatcher()
    console = Console(highlighter=dc.get_highlighter(), theme=dc.get_theme())
    console.print(string)
