"""Five SPARQL queries against fixtures/mini_kg.ttl.

Each function returns a SPARQL query string. The autograder parses the
fixture into an `rdflib.Graph` and runs your query against it.
"""

def q1():
    """Q1 — Return all (book, title) pairs."""
    return """
    SELECT ?book ?title
    WHERE {
      ?book :title ?title .
    }
    """

def q2():
    """Q2 — Return all books and their year, filtered to books published after 2010."""
    return """
    SELECT ?book ?year
    WHERE {
      ?book :year ?year .
      FILTER (?year > 2010)
    }
    """

def q3():
    """Q3 — Return all (book, author_name) pairs."""
    return """
    SELECT ?book ?author_name
    WHERE {
      ?book :author ?author .
      ?author rdfs:label ?author_name .
    }
    """

def q4():
    """Q4 — Return all books and their topic, with the topic OPTIONAL."""
    return """
    SELECT ?book ?topic
    WHERE {
      ?book a :Book .
      OPTIONAL { ?book :topic ?topic . }
    }
    """

def q5():
    """Q5 — Return TRUE if any book has more than one :author triple; otherwise FALSE."""
    return """
    ASK {
      ?book :author ?a1, ?a2 .
      FILTER (?a1 != ?a2)
    }
    """