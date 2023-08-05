from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import ContentSettings


class GossAzureBlobClient(object):

    def __init__(self, secret_id, secret_key, region, bucket):
        self._client = BlobServiceClient.from_connection_string(conn_str=secret_id)
        self._bucket = bucket
        self._region = region

    def _blob_client(self, container_name, blob_name):
        return self._client.get_blob_client(container_name, blob_name)

    def _get_object_url(self, key):
        """
        Get object URL from azure cloud
        """
        return self._blob_client(self._bucket, key).url
    
    def _get_object_information(self, key, url=None):
        if url:
            download_info = self._blob_client(self._bucket, key).from_blob_url(url).download_blob(validate_content=True)
            return self._blob_client(self._bucket, key).from_blob_url(url).get_blob_properties(), download_info
        download_info = self._blob_client(self._bucket, key).download_blob(validate_content=True)
        return self._blob_client(self._bucket, key).get_blob_properties(), download_info
    
    def _get_download_data(self, key, url=None):
        if url:
            return self._blob_client(self._bucket, key).from_blob_url(url).download_blob(validate_content=True).readall()
        return self._blob_client(self._bucket, key).download_blob(validate_content=True).readall()

    def _upload_object(self, local_path, key):
        """
        Upload object to azure cloud
        """
        try:
            blob_client = self._blob_client(self._bucket, key)
            with open(local_path, "rb") as data:
                self._delete_object(key)
                if self._region:
                    blob_client.upload_blob(data, content_settings=ContentSettings(content_type=self._region))
                else:
                    blob_client.upload_blob(data)
        except Exception as err:
            if not isinstance(err, ResourceExistsError):
                return "", err
        return self._get_object_url(key), None
    
    def _upload_object_by_block(self, local_path, key, content_settings=None):
        """
        Upload object to azure cloud by block
        """
        try:
            blob_client = self._blob_client(self._bucket, key)
            with open(local_path, "rb") as data:
                blob_client.upload_blob(data, blob_type="AppendBlob", content_settings=content_settings)
        except Exception as err:
            if not isinstance(err, ResourceExistsError):
                return "", err
        return self._get_object_url(key), None

    def _list_objects(self, prefix):
        """
        List objects from cloud
        """
        return []

    def _check_object(self, key):
        """
        Check object exists from cloude
        """
        try:
            return self._get_object_url(key), True
            raise
        except Exception:
            return '', False

    def _delete_object(self, key):
        """
        Delete object from azure cloud
        """
        blob_client = self._blob_client(self._bucket, key)
        try:
            blob_client.delete_blob()
            return True
        except Exception:
            return False
