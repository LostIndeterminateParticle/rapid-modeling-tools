import unittest
import pandas as pd
import networkx as nx

from utils import (create_column_values,
                   create_vertex_objects)
from graph_objects import UML_ID, Vertex, get_uml_id


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_column_values(self):
        data = ['Car', 'Wheel', 'Engine']
        data_2 = ['chassis', 'hub', 'drive output']
        columns = ['A_"composite owner"_component', 'composite owner']
        expected_output = {'A_"composite owner"_component':
                           ['A_car_chassis', 'A_wheel_hub',
                            'A_engine_drive output'],
                           'composite owner':
                           ['car qua chassis context',
                            'wheel qua hub context',
                            'engine qua drive output context']
                           }
        for col in columns:
            list_out = create_column_values(col_name=col, data=data,
                                            aux_data=data_2)
            self.assertListEqual(expected_output[col], list_out)

    def test_create_vertex_objects(self):
        # This also tests the Vertex.to_dict() method in a round about way
        data_dict = {'Component': ['Car', 'engine'],
                     'Position': ['engine', 'Car'],
                     'edge type': ['owner', 'type']}
        test_graph_df = pd.DataFrame(data=data_dict)
        Test_Graph = nx.DiGraph()
        Temp_Graph = nx.DiGraph()
        Temp_Graph = nx.from_pandas_edgelist(
            df=test_graph_df, source='Component',
            target='Position', edge_attr='edge type',
            create_using=Temp_Graph)
        edge_label_dict = {'edge type': 'owner'}
        Test_Graph.add_nodes_from(Temp_Graph)
        Test_Graph.add_edge('Car', 'engine', edge_attribute='owner')
        Test_Graph.add_edge('engine', 'Car',
                            edge_attribute='type')

        verticies = create_vertex_objects(
            df=test_graph_df, graph=Test_Graph)

        vertex_1_dict = {'name': 'Car',
                         'node types': {'Component', 'Position'},
                         'successors': {'engine': {'edge_attribute': 'owner'}},
                         'predecessors': {'engine':
                                          {'edge_attribute': 'type'}}}
        vertex_2_dict = {'name': 'engine',
                         'node types': {'Component', 'Position'},
                         'successors': {'Car': {'edge_attribute': 'type'}},
                         'predecessors': {'Car': {'edge_attribute': 'owner'}}}
        vertex_dicts = [vertex_1_dict, vertex_2_dict]

        for index, vertex in enumerate(verticies):
            self.assertDictEqual(vertex_dicts[index], vertex.to_dict())
            # print(('Vertex {0}: \n{{succ node: '
            #        + '{{edge_attribute: edge_name}}}}').format(
            #     vertex.name))
            # print(vertex.successors)
            # print('{pred node: ' '{{edge_attribute: edge_name}}')
            # print(vertex.predecessors)

    # def test_get_spanning_tree(self):
    #     # So far incomplete test and subject to change.
    #     span_nodes = self.data['Pattern Spanning Tree Edges']
    #     span_edges = self.data['Pattern Spanning Tree Edge Labels']
    #     span_tree = [(tuple(pair), span_edges[index])
    #                  for index, pair in enumerate(span_nodes)]
    #     span_tree_set = set(span_tree)
    #
    #     node_attr_dict = {
    #         'A': 'Composite Thing',
    #         'B': 'component',
    #         'C': 'Atomic Thing',
    #         'D': 'A_"composite owner"_component',
    #         'E': 'composite owner'
    #     }
    #     Tree_Graph = nx.DiGraph()
    #
    #     for key in node_attr_dict:
    #         Tree_Graph.add_node(key, vertex_attribute=node_attr_dict[key])
    #
    #     Tree_Graph.add_edge('B', 'A', edge_attribute='owner')
    #     Tree_Graph.add_edge('B', 'C', edge_attribute='type')
    #     Tree_Graph.add_edge('D', 'B', edge_attribute='memberEnd')
    #     Tree_Graph.add_edge('E', 'D', edge_attribute='owner')
    #
    #     # vertex_list = []
    #     for vertex in Tree_Graph.nodes:
    #         vert = Vertex(
    #             name=vertex,
    #             node_types=nx.get_node_attributes(Tree_Graph,
    #                                               'vertex_attribute')[
    #                                               vertex],
    #             successors=Tree_Graph.succ[vertex],
    #             predecessors=Tree_Graph.pred[vertex])
    #         # vertex_list.append(vert)
    #
    #     # root_node_a = next((
    #     #   node for node in vertex_list if node.name == 'A'))
    #     spanning_tree = get_spanning_tree(
    #         root_node='A',
    #         root_node_type='Composite Thing',
    #         tree_pattern=span_nodes,
    #         tree_edge_pattern=span_edges)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
