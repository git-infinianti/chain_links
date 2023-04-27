from .utils import sign


class MData12:
    def __init__(self,
        icon, name, p2pkh
        ) -> None:
        self.metadata = {
            'tag_type': 'ANT',
            'icon': icon,
            'address_name': name,
            'address_name_mime': 'text/x-markdown; charset=UTF-8',
            'p2pkh_address': p2pkh
        }
        self.signed_metadata = sign(self.metadata)


example = {
    "rip_12": {
        "tag": {
            "tag_type": "ANT",
            "icon": "<base64 encoded png image at 64x64>",
            "address_name": "<name that you want to give to the Ravencoin address>",
            "address_name_mime": "text/x-markdown; charset=UTF-8",
            "ravencoin_address": "<Ravencoin address from step 1>"
        },
        "metadata_signature": {
            "signature_hash": "<SHA256 hash of the immediately preceding metadata JSON object {...}>",
            "signature": "<Ravencoin signed signature_hash>"
        }
    }
}