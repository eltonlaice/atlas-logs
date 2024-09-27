def perform_search(query, data):
    """
    Perform a search on the given data based on the query.

    Args:
        query (str): The search query.
        data (list): The list of items to search through.

    Returns:
        list: A list of items that match the search query.
    """
    results = []
    query = query.lower()
    for item in data:
        if query in str(item).lower():
            results.append(item)
    return results
