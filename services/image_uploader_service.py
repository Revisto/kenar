import requests

class ImageUploader:
    def __init__(self, url):
        self.base_url = f"http://{url}"

    def upload_image_from_file(self, file_path):
        """
        Uploads an image from a local file.
        
        :param file_path: Path to the local file to upload.
        :return: Filename of the uploaded image.
        """
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(self.base_url, files=files)
            response.raise_for_status()
            return self.base_url + '/' + response.json()['filename']