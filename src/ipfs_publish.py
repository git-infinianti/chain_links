from json import dump
from ipfs_api import pin, publish
from src.rip.utils import encoding


class PublishMData:
    def __init__(self,
            data_type: str, metadata: dict, signed_metadata: str, signature: str 
        ) -> None:
        with open(filepath := f'src/ipfs_json/{signed_metadata}.json', 'x') as file:
            data = {
                data_type: metadata,
                'metadata_signature': {
                    'signed_metadata': signed_metadata,
                    'signature': bytes(signature, encoding).hex()
                }
            }
            dump(data, file)
        self.cid = publish(filepath)
        pin(self.cid) # type: ignore