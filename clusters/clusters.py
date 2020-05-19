from functools import lru_cache

import psycopg2
from collections import deque


@lru_cache(maxsize=1)
def get_graph_from_db():
    graph = {}

    conn = psycopg2.connect("dbname=avitotest user=avitotest password=verystrongpassword host=localhost")
    cur = conn.cursor()
    cur.execute("select n1, n2 from edges;")

    for i in cur.fetchall():
        if not i[0] in graph:
            graph[i[0]] = list()
        if not i[1] in graph:
            graph[i[1]] = list()

        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    cur.close()
    conn.close()

    return graph


@lru_cache(maxsize=1)
def get_list_of_all_edges():
    edges = []
    conn = psycopg2.connect("dbname=avitotest user=avitotest password=verystrongpassword host=localhost")
    cur = conn.cursor()
    cur.execute('''select distinct n1 from (SELECT n1 FROM edges
                   UNION
                   SELECT n2 FROM edges) t
                   order by n1;''')

    for i in cur.fetchall():
        edges.append(i[0])

    cur.close()
    conn.close()

    return edges


def write_edges_to_number_to_db(data):
    conn = psycopg2.connect("dbname=avitotest user=avitotest password=verystrongpassword host=localhost")
    cur = conn.cursor()

    query = "INSERT INTO clusters (n, c) VALUES "

    for number in data:
        for edge in data[number]:
            query += f"({number}, {edge}),"

    query = query[:-1]
    query += ";"
    cur.execute(query)

    cur.close()
    conn.commit()
    conn.close()


def breadth_first_search(check_graph, edge1, edge2):
    if edge1 == edge2:
        return True

    search_queue = deque()
    search_queue += check_graph[edge1]
    searched = []

    while search_queue:
        checking_edge = search_queue.popleft()
        if checking_edge in searched:
            continue
        else:
            if checking_edge == edge2:
                return True
            else:
                searched.append(checking_edge)
                search_queue += check_graph[checking_edge]
    return False


if __name__ == "__main__":
    edge_to_com = {}
    c_num = 0

    checked_edges = list()

    for edge_1 in get_list_of_all_edges():
        if len(checked_edges) >= len(get_list_of_all_edges()):
            break
        edge_to_com[c_num] = list()
        if edge_1 in checked_edges:
            continue
        for edge_2 in get_list_of_all_edges():
            if breadth_first_search(get_graph_from_db(), edge_1, edge_2):
                edge_to_com[c_num].append(edge_2)
                checked_edges.append(edge_2)
        c_num = c_num + 1

    write_edges_to_number_to_db(edge_to_com)
