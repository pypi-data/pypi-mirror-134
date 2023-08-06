from pokemontcgsdkasync.query import SingleQuery, MultipleQuery, ArrayQuery


class QueryBuilder:

    def __init__(self, resource_type, transform=None):
        self.params = {}
        self.type = resource_type
        self.transform = transform

    def find(self, resource_id: str) -> SingleQuery:
        """Builds a SingleQuery
        
        Args:
            resource_id (string): Resource id
        Returns:
            SingleQuery: SingleQuery to retrieve the data
        """

        url = "{}/{}".format(self.type.RESOURCE, resource_id)
        return SingleQuery(self.type, self.transform, url, self.params)

    def where(self, **kwargs) -> MultipleQuery:
        """Adds a parameter to the dictionary of query parameters
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            MultipleQuery: Multiple query to retrieve the data
        """

        for key, value in kwargs.items():
            self.params[key] = value

        return self.all()

    def all(self) -> MultipleQuery:
        return MultipleQuery(self.type, self.transform, self.type.RESOURCE, self.params)

    def array(self) -> ArrayQuery:
        return ArrayQuery(self.type.RESOURCE)

