from dacite import from_dict

from pokemontcgsdkasync.asyncclientcontext import AsyncClientContext


class QueryBuilder:

    def __init__(self, resource_type, transform=None):
        self.params = {}
        self.type = resource_type
        self.transform = transform

    async def find(self, resource_id: str):
        """Get a resource by its id
        
        Args:
            resource_id (string): Resource id
        Returns:
            object: Instance of the resource type
        """
        url = "{}/{}".format(self.type.RESOURCE, resource_id)
        response = (await AsyncClientContext.get(url))['data']

        # Transform json keys into names that are safe for python properties
        if self.transform:
            response = self.transform(response)

        return from_dict(self.type, response)

    async def where(self, **kwargs):
        """Adds a parameter to the dictionary of query parameters
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            list of object: List of resource objects
        """
        for key, value in kwargs.items():
            self.params[key] = value

        return await self.all()

    async def all(self):
        """Get all resources, automatically paging through data

        Returns:
            list of object: List of resource objects
        """

        result_list = []
        fetch_all = True
        url = self.type.RESOURCE

        if 'page' in self.params:
            fetch_all = False
        else:
            self.params['page'] = 1

        while True:
            response = (await AsyncClientContext.get(url, self.params))['data']
            if len(response) > 0:
                if self.transform:
                    response = [self.transform(i) for i in response]

                result_list.extend([from_dict(self.type, item) for item in response])

                if fetch_all:
                    self.params['page'] += 1
                else:
                    break
            else:
                break

        return result_list

    async def array(self):
        """Get all resources and return the result as an array

        Returns:
            array of str: Array of resources
        """
        url = self.type.RESOURCE
        return (await AsyncClientContext.get(url, self.params))['data']
