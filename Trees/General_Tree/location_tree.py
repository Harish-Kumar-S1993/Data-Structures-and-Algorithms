class TreeNode:

    def __init__(self, location):
        self.location = location
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "!--" if self.parent else ""
        print(prefix + self.location)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_location_tree():

    root_node = TreeNode("Global")
    country1_node = TreeNode("India")
    country2_node = TreeNode("USA")
    country1_state1_node = TreeNode("Gujarat")
    country1_state2_node = TreeNode("Karnataka")

    country1_state1_node.add_child(TreeNode("Ahmedabad"))
    country1_state1_node.add_child(TreeNode("Baroda"))
    country1_state2_node.add_child(TreeNode("Bengaluru"))
    country1_state2_node.add_child(TreeNode("Mysore"))

    country2_state1_node = TreeNode("New Jersey")
    country2_state2_node = TreeNode("California")

    country2_state1_node.add_child(TreeNode("Princeton"))
    country2_state1_node.add_child(TreeNode("Trenton"))
    country2_state2_node.add_child(TreeNode("San Francisco"))
    country2_state2_node.add_child(TreeNode("Mountain View"))
    country2_state2_node.add_child(TreeNode("Palo Alto"))

    country1_node.add_child(country1_state1_node)
    country1_node.add_child(country1_state2_node)
    country2_node.add_child(country2_state1_node)
    country2_node.add_child(country2_state2_node)

    root_node.add_child(country1_node)
    root_node.add_child(country2_node)

    return root_node


if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(2)


