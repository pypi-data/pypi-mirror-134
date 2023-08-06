#!/usr/bin/env python
# coding=utf-8

def execute(cnx, queries):
    queries_responses = []
    cursor = cnx.cursor()
    for query in queries:
        cursor.execute(query)
        for res in cursor:
            queries_responses.append(res[0])
    cursor.close()
    return queries_responses
