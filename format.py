import re

substitution = r'\g<1>\g<3>'
pattern = re.compile(
    # GirHub Flavored Markdown comment that lets darkmode images stay
    r'(?<!<!-- setup: let darkmode -->\n)'
    r'(<picture>\n(?:[ \t]+<[^>]*>[ \t]*\n)*)'
    r'([ \t]+<source[^>]*media="\(prefers-color-scheme: dark\)"[^>]*>[ \t]*\n)'
    r'((?:[ \t]+<[^>]*>[ \t]*\n)*<\/picture>)',
    flags=re.MULTILINE
)

def format(string: str) -> str:
    return pattern.sub(substitution, string)