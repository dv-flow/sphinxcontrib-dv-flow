
from docutils.parsers.rst import Directive
from docutils import nodes
from .__version__ import VERSION
from dv_flow.mgr import TaskGraphBuilder
from typing import ClassVar

class TaskDirective(Directive):
    optional_arguments = 1
    has_content = True

    def run(self):
        result = []

        targetnode = nodes.target()
        anchorid = nodes.make_id('ABC')
        targetnode['ids'].append(anchorid)
        targetnode['names'].append(anchorid)
        targetnode.line = self.lineno

        result.append(targetnode)

        section_node = nodes.section()
        textnodes, title_messages = self.state.inline_text("DEF", self.lineno)
        titlenode = nodes.title("GHI", "", *textnodes)

        section_node['names'].append("MySection")
        section_node += titlenode
        section_node += title_messages
        section_node += nodes.paragraph(text="This is open text")
        self.state.document.note_implicit_target(section_node, section_node)

        result.append(section_node)


        return result
    pass

def setup(app):
    app.add_directive('dv-flow.task', TaskDirective)
    return {
        'parallel_read_safe': True,
        'version': VERSION
    }