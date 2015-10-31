from __future__ import print_function

from .rule import Rule, Cardinality


def reduce_like_parent_child(call_graph, rule_type, merge_function):
    """Given a call_graph, reduce parent, child nodes of rule_type
    using merge_function.

    Returns a modified call_graph
    """
    for path, edge in call_graph.edges.items():
        parent = edge.setter
        if not parent:
            continue
        if not isinstance(parent.rule.function, rule_type):
            continue

        children = [
            child for child in edge.getters
            if isinstance(child.rule.function, rule_type)
        ]
        for child in children:
            print(child, parent)

            function = merge_function(
                parent.rule.function, child.rule.function
            )

            inputs = parent.rule.inputs
            outputs = parent.rule.outputs + child.rule.outputs

            rule = Rule(function, inputs, outputs, Cardinality.one)

            incoming_paths = parent.incoming_paths
            outgoing_paths = parent.outgoing_paths + child.outgoing_paths

            # TODO: another operation can remove unneeded computation

            call_graph.remove_node(edge.setter)
            call_graph.remove_node(child)

            call_graph.add_node(incoming_paths, outgoing_paths, rule)

    return call_graph
