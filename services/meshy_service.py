import requests

class MeshyService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.meshy.ai"

    def create_image_to_3d_task(self, image_url, enable_pbr=True):
        """
        Create an Image To 3D Task.
        :param image_url: URL to the image for Meshy to create the model from.
        :param enable_pbr: Generate PBR Maps (metallic, roughness, normal) in addition to the base color.
        :return: Task ID of the newly created Image To 3D task.
        """
        endpoint = "/v1/image-to-3d"
        payload = {
            "image_url": image_url,
            "enable_pbr": enable_pbr,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(f"{self.base_url}{endpoint}", headers=headers, json=payload)
        print(response.json())
        response.raise_for_status()
        return response.json().get("result")

    def retrieve_image_to_3d_task(self, task_id):
        """
        Retrieve an Image To 3D Task.
        :param task_id: Unique identifier for the Image To 3D task to retrieve.
        :return: Image To 3D task object.
        """
        endpoint = f"/v1/image-to-3d/{task_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(f"{self.base_url}{endpoint}", headers=headers)
        response.raise_for_status()
        return response.json()