class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node is not None:
        return "{}[{}]{{{}}}".format(node.val,
                                     serialize(node.left),
                                     serialize(node.right))
    else:
        return ""


def deserialize(nodestr: str):
    def get_subsection_end(start_index, opening_delimiter, closing_delimiter):
        src_slice = nodestr[start_index:]
        subsection_depth = 0
        for i, character in enumerate(src_slice):
            if character == opening_delimiter:
                subsection_depth += 1
            elif character == closing_delimiter:
                if subsection_depth == 0:
                    return start_index + i
                else:
                    subsection_depth -= 1

    if nodestr == "":
        return None
    else:
        left_start = nodestr.find('[')+1 # index marking start of left child
        left_end = get_subsection_end(left_start, '[', ']')
        right_start = left_end+2
        right_end = get_subsection_end(right_start, '{', '}')
        return Node(
            nodestr[:left_start-1],
            deserialize(nodestr[left_start:left_end]),
            deserialize(nodestr[right_start:right_end])
        )

