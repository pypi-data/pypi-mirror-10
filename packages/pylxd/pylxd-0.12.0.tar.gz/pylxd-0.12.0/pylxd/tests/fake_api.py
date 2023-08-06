# Copyright (c) 2015 Canonical Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

def fake_image_list_empty():
    return {
        "type": "sync",
        "status": "Success",
        "status_code": 200,
        "metadata": []
    }


def fake_image_list():
    return {
        "type": "sync",
        "status": "Success",
        "status_code": 200,
        "metadata": ['chuck']
    }


def fake_image_info():
    return {
        "type": "sync",
        "status": "Success",
        "status_code": 200,
        "metadata": {
            "aliases": [
                {
                    "target": "ubuntu",
                    "description": "ubuntu"
                }
            ],
                "architecture": 2,
                "fingerprint": "04aac4257341478b49c25d22cea8a6ce0489dc6c42d835367945e7596368a37f",
                "filename": "",
                "properties": {},
                "public": 0,
                "size": 67043148,
                "created_at": 0,
                "expires_at": 0,
                "uploaded_at": 1435669853
        }
    }

def fake_alias_list():
    return 	{
		"type": "sync",
		"status": "Success",
		"status_code": 200,
		"metadata": []
	}
