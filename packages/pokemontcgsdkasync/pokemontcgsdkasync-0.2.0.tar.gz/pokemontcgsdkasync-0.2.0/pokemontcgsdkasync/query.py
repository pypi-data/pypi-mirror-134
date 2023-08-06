from pokemontcgsdkasync import AsyncClientContext


class ArrayQuery:

    def __init__(self, resource_type):
        self.url = resource_type

    async def get(self):
        """Get all resources and return the result as an array

        Returns:
            array of str: Array of resources
        """
        return (await AsyncClientContext.get(self.url))['data']


class SingleQuery:

    def __init__(self, resource_type, transform, url, params):
        self.type = resource_type
        self.transform = transform
        self.url = url
        self.params = params

    async def get(self):
        """Get the resource for the specified id"""
        response = (await AsyncClientContext.get(self.url))['data']

        if self.transform:
            response = self.transform(response)

        return response


class MultipleQuery:

    def __init__(self, resource_type, transform, url, params):
        self.type = resource_type
        self.transform = transform
        self.url = url
        self.params = params

    async def get(self):
        """Get all resources, automatically paging through data

        Returns:
            list of object: List of resource objects
        """

        result_list = []
        fetch_all = True

        if 'page' in self.params:
            fetch_all = False
        else:
            self.params['page'] = 1

        while True:
            response = (await AsyncClientContext.get(self.url, self.params))['data']
            if len(response) > 0:

                if self.transform:
                    response = [self.transform(i) for i in response]

                for item in response:
                    result_list.append(item)

                if fetch_all:
                    self.params['page'] += 1
                else:
                    break
            else:
                break

        return result_list

    async def generator(self):
        """Get all resources as an iterator, automatically paging through data

        Returns:
            list of object: List of resource objects
        """

        fetch_all = True

        if 'page' in self.params:
            fetch_all = False
        else:
            self.params['page'] = 1

        while True:

            response = (await AsyncClientContext.get(self.url, self.params))['data']

            if len(response) > 0:

                if self.transform:
                    response = [self.transform(i) for i in response]

                for item in response:
                    yield item

                if fetch_all:
                    self.params['page'] += 1
                else:
                    break
            else:
                break
