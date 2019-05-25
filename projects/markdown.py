"""
Markdown to HTML Converter - Converts Markdown formatted text into HTML files. Implement basic
tags like p, strong, em etc. Optional: Implement all tags from Markdown Syntax Docs.
"""
from abc import ABCMeta, abstractmethod
import re


class Utils:
    """Utilities"""

    @classmethod
    def get_blocks_file(cls, text):
        """
        :param text:
        :return:
        """
        def blocks():
            """blocks"""
            block = []
            for line in open(text).readlines():
                if line.strip():
                    block.append(line)
                elif block:
                    yield ''.join(block).strip()
                    block = []

        return list(blocks())

    @classmethod
    def get_blocks_string(cls, text):
        """
        :param text:
        :return:
        """
        def blocks():
            """blocks"""
            block = []
            for line in text.split("\n"):
                if line.strip():
                    block.append(line)
                elif block:
                    yield ''.join(block)
                    block = []

        return list(blocks())

    @classmethod
    def output(cls, content):
        """
        :param content:
        """
        with open('~/output.html', 'w') as file:
            file.write(content)
        assert file.closed


class Handler:
    """handler class"""
    def callback(self, prefix, name, *args):
        """
        :param prefix: find method
        :param name:
        :param args: call back method pass with args
        :return: if we fail just return None
        """
        method = getattr(self, prefix + name, None)
        try:
            return method(*args)
        except TypeError:
            return None

    def start(self, name):
        """
        start simply calls the method start_name
        where name is the param passed
        """
        return self.callback('start_', name)

    def end(self, name):
        """
        end simply calls the method end_name
        where name is the param passed
        """
        return self.callback('end_', name)

    def sub(self, name):
        """
        substitution rules
        """

        def substitution(match):
            """
            :param match:
            :return:
            """
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result

        return substitution


class HTMLRenderer(Handler):
    """html document rules"""

    @staticmethod
    def start_document():
        """
        :return: basic start of HTML document
        """
        return '<html><head><title></title></head><body>'

    @staticmethod
    def end_document():
        """
        :return:
        """
        return '</body></html>'

    @staticmethod
    def start_paragraph():
        """
        :return: paragraph rules
        """
        return '<p>'

    @staticmethod
    def end_paragraph():
        """
        :return:
        """
        return '</p>'

    @staticmethod
    def start_heading():
        """
        :return: heading rules
        """
        return '<h1>'

    @staticmethod
    def end_heading():
        """
        :return:
        """
        return '</h1>'

    @staticmethod
    def sub_strong(match):
        """
        :param match:
        :return: substitutions
        """
        return '<strong>{0}</strong>'.format(match.group(1))

    @staticmethod
    def sub_break():
        """
        :return: Break rules
        """
        return '<br />'

    @staticmethod
    def data(block):
        """
        :param block:
        :return:
        """
        return block


# noinspection PyCompatibility
class Rule(metaclass=ABCMeta):
    """
    A rule has a condition and an action and a type.
    If the condition is met, the action will be applied.
    Each rule should have a type to explain its intention, no type means there
    is no rule to accomplish
    """

    def __init__(self):
        self._type = None

    def action(self, block, handler):
        """
        feed handler instructions > start > data > end for block modifications
        if there is no type return False - there is no rule.
        :return: String - block with rule applied or Boolean - NA
            Action should be the same for all rules
        """
        if self._type:
            return ''.join(
                [handler.start(self._type), handler.data(block), handler.end(self._type)])
        return False

    @abstractmethod
    def condition(self, block):
        """
        :return: Boolean Check to see if block meets condition of the rule
        """
        return False

    def type(self):
        """
        :return: String representation of the rule type
        """
        return self._type


class HeadingRule(Rule):
    """
        HeadingRule condition: A block is a Heading if:
                 it is one line (does not contain \n)
                 lte 70 characters
    """
    _type = "heading"

    def condition(self, block):
        """
        :param block:
        :return:
        """
        return ("\n" not in block) and (len(block) <= 70)


class ParagraphRule(Rule):
    """
        ParagraphRule is going to be the end rule as it's
        the default rule if no others are followed up - for HTML
    """
    _type = "paragraph"

    def condition(self, block):
        """
        :param block:
        :return:
        """
        return True


class Parser:
    """
    class docs
    """

    def __init__(self, handler):
        """
        Constructor
        :param handler: which renderer to use
        rules and filters handles layout while filters
        handle detection of strings such as emphasis/mail
        """
        self._handler = handler
        self._rules = []
        self._filters = []

    @property
    def handler(self):
        """
        :return:
        """
        return self._handler

    @property
    def rules(self):
        """
        :return:
        """
        return self._rules

    def add_rule(self, *args):
        """
        Remember the order in which rules are added is important
        """
        for rule in args:
            self._rules.append(rule)

    @property
    def filters(self):
        """
        :return:
        """
        return self._filters

    def add_filter(self, pattern, name):
        """
        appends a filter function to filters
        :param pattern: pattern to find
        :param name:    name of the pattern
        """

        def apply_filter(block, handler):
            """
            :param block: the block of text we are working with
            :param handler: renderer
            """
            return re.sub(pattern, handler.sub(name), block)

        self._filters.append(apply_filter)

    def parse(self, content):
        """
        :return: a string representation of the resultant from parsing content through
        self.handler
        """

        def parse_help():
            """
            apply starting document rule
            """
            yield self.handler.start("document")
            for block in Utils.get_blocks_file(content):
                # apply filters
                for filter_meth in self.filters:
                    block = filter_meth(block, self.handler)
                # apply rules
                for rule in self._rules:
                    if rule.condition(block):  # check to see if condition applies

                        action = rule.action(block, self._handler)
                        # yield action if one exists
                        if action:
                            yield action
                        break
            # apply end document rule
            yield self.handler.end("document")

        return "".join([var_x for var_x in parse_help() if isinstance(var_x, str)])


if __name__ == "__main__":
    Y = HTMLRenderer()
    X = Parser(Y)
    F = input("Enter file location: ")
    X.add_rule(HeadingRule(), ParagraphRule())
    X.add_filter(r"\*(.+|.?)\*", 'strong')
    X.add_filter(r"*  \n", 'break', )
    T = X.parse(F)
    Utils.output(T)
