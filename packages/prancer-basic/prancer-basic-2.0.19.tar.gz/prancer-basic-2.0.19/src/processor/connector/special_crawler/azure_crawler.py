from processor.helper.config.rundata_utils import get_from_currentdata, put_in_currentdata
from processor.connector.special_crawler.base_crawler import BaseCrawler
from processor.helper.httpapi.http_utils import http_get_request

class AzureCrawler(BaseCrawler):

    def __init__(self, resources, **kwargs):
        super().__init__(resources, **kwargs)
        self.token = kwargs.get("token")
        self.apiversions = kwargs.get("apiversions")
        self.subscription_id = kwargs.get("subscription_id")
        self.version = kwargs.get("version")

        self.special_resource_types = {
            # "Microsoft.Sql/servers/securityAlertPolicies" : self.crawl_server_security_alert_policies,
            # "Microsoft.Sql/servers/auditingSettings" : self.crawl_server_audit_settings,
            "Microsoft.Authorization/roleDefinitions": self.crawl_role_definitions,
            # "Microsoft.KeyVault/vaults/secrets": self.crawl_keyvault_secrets,
            # "Microsoft.Web/sites/config": self.crawl_website_config
        }
    
    def check_for_special_crawl(self, resource_type):
        """ 
        check the resource type need special crawling or not. if it need special crawling then 
        it will process the special crawler and returns the updated resources
        """
        if resource_type in self.special_resource_types:
            crawl_function = self.special_resource_types.get(resource_type)
            crawl_function(resource_type)
        else:
            self.crawl_child_resources(resource_type)
        return self.resources
    
    def get_version_of_resource_type(self, resource_type):
        """Url version of the resource."""
        if not self.version and self.apiversions:
            if resource_type in self.apiversions:
                self.version = self.apiversions[resource_type]['version']
        return self.version
    
    def call_azure_api(self, url):
        hdrs = {
            'Authorization': 'Bearer %s' % self.token
        }
        status, data = http_get_request(url, hdrs, name='\tRESOURCE:')
        if status and isinstance(status, int) and status == 200:
            for resource in data.get("value", []):
                put_in_currentdata('resources', resource)
            self.resources += data.get("value", [])
            
    def crawl_child_resources(self, child_resource_type):
        """
        crawl child resources
        """
        version = self.get_version_of_resource_type(child_resource_type)
        child_resource_type_list = child_resource_type.split("/")
        child_resource = child_resource_type_list[-1]
        main_resource = "/".join(child_resource_type_list[:-1])
        if version:
            for resource in self.resources:
                if resource.get("type") == main_resource:
                    url = 'https://management.azure.com%s/%s?api-version=%s' % (resource.get("id"), child_resource, version)
                    self.call_azure_api(url)
        return self.resources

    def crawl_server_security_alert_policies(self, resource_type):
        """
        crawl "Microsoft.Sql/servers/securityAlertPolicies" resource type
        """
        version = self.get_version_of_resource_type(resource_type)
        if version:
            for resource in self.resources:
                if resource.get("type") == "Microsoft.Sql/servers":
                    url = 'https://management.azure.com%s/%s?api-version=%s' % (resource.get("id"), "securityAlertPolicies", version)
                    self.call_azure_api(url)

    def crawl_server_audit_settings(self, resource_type):
        """
        crawl "Microsoft.Sql/servers/auditingSettings" resource type
        """
        version = self.get_version_of_resource_type(resource_type)
        if version:
            for resource in self.resources:
                if resource.get("type") == "Microsoft.Sql/servers":
                    url = 'https://management.azure.com%s/%s?api-version=%s' % (resource.get("id"), "auditingSettings", version)
                    self.call_azure_api(url)
    
    def crawl_role_definitions(self, resource_type):
        """
        crawl "Microsoft.Authorization/roleDefinitions" resource type
        """
        version = self.get_version_of_resource_type(resource_type)
        if version:
            url = 'https://management.azure.com/subscriptions/%s/providers/%s?api-version=%s' % (self.subscription_id, resource_type, version)
            self.call_azure_api(url)


    def crawl_keyvault_secrets(self, resource_type):
        """
        crawl "Microsoft.KeyVault/vaults/secrets" resource type
        """
        version = self.get_version_of_resource_type(resource_type)
        if version:
            for resource in self.resources:
                if resource['type'] == "Microsoft.KeyVault/vaults":
                    hdrs = {
                        'Authorization': 'Bearer %s' % self.token
                    }
                    url = 'https://management.azure.com%s/secrets?api-version=%s' % (resource['id'], version)
                    status, data = http_get_request(url, hdrs, name='\tRESOURCE:')
                    if status and isinstance(status, int) and status == 200:
                        for resource in data.get("value", []):
                            put_in_currentdata('resources', resource)
                        self.resources += data.get("value", [])

    def crawl_website_config(self, resource_type):
        """
        crawl "Microsoft.Web/sites/config" resource type
        """
        version = self.get_version_of_resource_type(resource_type)
        if version:
            for resource in self.resources:
                if resource['type'] == "Microsoft.Web/sites":
                    hdrs = {
                        'Authorization': 'Bearer %s' % self.token
                    }
                    url = 'https://management.azure.com%s/config?api-version=%s' % (resource['id'], version)
                    status, data = http_get_request(url, hdrs, name='\tRESOURCE:')
                    if status and isinstance(status, int) and status == 200:
                        for resource in data.get("value", []):
                            if resource.get("type") == "Microsoft.Web/sites/config":
                                put_in_currentdata('resources', resource)
                                self.resources.append(resource)