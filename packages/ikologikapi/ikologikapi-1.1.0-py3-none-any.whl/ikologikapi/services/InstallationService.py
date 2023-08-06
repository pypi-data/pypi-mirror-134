import requests
import json
from ikologikapi.IkologikApiCredentials import IkologikApiCredentials
from ikologikapi.domain.Search import Search
from ikologikapi.services.AbstractIkologikCustomerService import AbstractIkologikCustomerService


class InstallationService(AbstractIkologikCustomerService):

    def __init__(self, jwtHelper: IkologikApiCredentials):
        super().__init__(jwtHelper)

    # CRUD Actions

    def get_url(self, customer: str):
        return f'{self.jwtHelper.get_url()}/api/v2/customer/{customer}/installation'



    def get_by_name(self, customer: str,  installation_name: str):
        search = Search()
        search.add_filter([("name", "EQ", [installation_name])])
        search.add_order("name", "ASC")

        # Query
        result = self.search(customer, search)
        if result and len(result) == 1:
            return result[0]
        else:
            return None