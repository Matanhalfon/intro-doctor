# FILE: ex7.py
# Exercise: Intro_2_cs ext10 2017-2018

import ex10



def test_1(diagnoser):
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)
    tiny_data = r'Data\tiny_data.txt'
    records_tiny = ex10.parse_data(tiny_data)
    calc_tiny = diagnoser.calculate_error_rate(records_tiny)
    if calc_tiny == 2 / 3:
        print("Test passed")
    else:
        print("Test failed. Should have returned", str(2 / 3), " returned: ",
              str(calc_tiny))
    small_data = r'Data\small_data.txt'
    records_small = ex10.parse_data(small_data)
    calc_small = diagnoser.calculate_error_rate(records_small)
    if calc_small == 2 / 3:
        print("Test passed")
    else:
        print("Test failed. Should have returned", str(2 / 3), " returned: ",
              str(calc_small))
    all_illnesses = diagnoser.all_illnesses()
    if all_illnesses == ['cold', 'healthy', 'influenza']:
        print("Test passed")
    else:
        print("Test failed. Should have returned ['cold', 'healthy', "
              "'influenza'], instead returned: ", all_illnesses)
    common_illness = diagnoser.most_common_illness(records_tiny)
    if common_illness == 'healthy':
        print("Test passed")
    else:
        print(
            "Test failed. Should have returned 'healthy'. instead returned: ",
            common_illness)


def build_tree_1():
    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No    Yes/     \No
    # influenza   cold   healthy   healthy
    flu_leaf = ex10.Node("influenza", None, None)
    cold_leaf = ex10.Node("cold", None, None)
    inner_vertex = ex10.Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = ex10.Node("healthy", None, None)
    healthy_vertex = ex10.Node("healthy", healthy_leaf, healthy_leaf)
    root = ex10.Node("cough", inner_vertex, healthy_vertex)
    diagnoser = ex10.Diagnoser(root)
    return diagnoser


def build_tree_2():
    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        Headache           Headache
    #   Yes /     \ No    Yes/     \No
    # influenza   cold   cold   healthy
    flu_leaf = ex10.Node("Influenza", None, None)
    healthy_leaf = ex10.Node("Healthy", None, None)
    cold_leaf = ex10.Node("Cold", None, None)
    inner_vertex_1 = ex10.Node("Headache", flu_leaf, cold_leaf)
    inner_vertex_2 = ex10.Node("Headache", cold_leaf, healthy_leaf)
    root = ex10.Node("Cough", inner_vertex_1, inner_vertex_2)
    diagnoser = ex10.Diagnoser(root)
    return diagnoser


def build_tree_3():
    # Manually build a simple tree.
    #                fever
    #          Yes /       \ No
    #        cough           cough
    #   Yes /     \ No    Yes/     \No
    # influenza   strep   cold   healthy
    flu_leaf = ex10.Node("influenza", None, None)
    strep_leaf = ex10.Node("strep", None, None)
    cold_leaf = ex10.Node("cold", None, None)
    healthy_leaf = ex10.Node("healthy", None, None)
    cough_yes = ex10.Node("cough", flu_leaf, strep_leaf)
    cough_no = ex10.Node("cough", cold_leaf, healthy_leaf)
    root = ex10.Node("fever", cough_yes, cough_no)
    return root


def test_2(diagnoser):
    paths = diagnoser.paths_to_illness("Cold")
    if paths == [[False, True], [True, False]]:
        print("Test passed")
    else:
        print(
            "Test failed. Should have returned [[False, True], [True, False]]. instead returned: ",
            paths)


def test_3():
    data = r'test_data.txt'
    records = ex10.parse_data(data)
    symp = ['fever', 'cough']
    tested_tree = ex10.build_tree(records, symp)
    result_tree = build_tree_3()
    if tested_tree.positive_child.positive_child.data == result_tree.positive_child.positive_child.data:
        print("Test passed")
    else:
        print(
            "Test failed. should have been: " + result_tree.positive_child.positive_child.data)

    if tested_tree.positive_child.negative_child.data == result_tree.positive_child.negative_child.data:
        print("Test passed")
    else:
        print(
            "Test failed. should have been: " + result_tree.positive_child.negative_child.data)

    if tested_tree.negative_child.positive_child.data == result_tree.negative_child.positive_child.data:
        print("Test passed")
    else:
        print(
            "Test failed. should have been: " + result_tree.negative_child.positive_child.data)

    if tested_tree.negative_child.negative_child.data == result_tree.negative_child.negative_child.data:
        print("Test passed")
    else:
        print(
            "Test failed. should have been: " + result_tree.negative_child.negative_child.data)

def test_4():
    record1 = ex10.Record("influenza", ["cough", "fever"])
    record2 = ex10.Record("cold", ["cough"])
    records = [record1, record2]
    test_1 = ex10.build_tree(records, ['fever'])
    if test_1.data == 'fever':
        print('test passed')
    else:
        print('test failed. data:', test_1.data, 'expected: fever')
    if test_1.positive_child.data == 'influenza':
        print('test passed')
    else:
        print('test failed. pos:', test_1.positive_child.data, 'expected: influenza')
    if test_1.negative_child.data == 'cold':
        print('test passed')
    else:
        print('test failed. neg:', test_1.negative_child.data, 'expected: cold')


def test_5():
    record1 = ex10.Record("influenza", ["cough", "fever"])
    record2 = ex10.Record("cold", ["cough"])
    records = [record1, record2]
    test_1 = ex10.optimal_tree(records, ['fever'],1)
    if test_1.data == 'fever':
        print('test passed')
    else:
        print('test failed. data:', test_1.data, 'expected: fever')
    if test_1.positive_child.data == 'influenza':
        print('test passed')
    else:
        print('test failed. pos:', test_1.positive_child.data, 'expected: influenza')
    if test_1.negative_child.data == 'cold':
        print('test passed')
    else:
        print('test failed. neg:', test_1.negative_child.data, 'expected: cold')

if __name__ == "__main__":
    diagnoser = build_tree_1()
    test_1(diagnoser)
    diagnoser = build_tree_2()
    test_2(diagnoser)
    test_3()
    test_4()
