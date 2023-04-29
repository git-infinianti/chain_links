from .utils import sign


class MData13:
    def __init__(self,
        p2pkh, algorithm, identity_document
        ) -> None:
        self.metadata = {
            'tag_type': 'AIT',
            'p2pkh_address': p2pkh,
            'algorithm': algorithm,
            'identity_document': identity_document
        }
        self.signed_metadata = sign(self.metadata)

example = {
    "tag": {
        "tag_type": "AIT",
        "ravencoin_address": "<Ravencoin address from step 1>",
        "algorithm": "<algorithm used to encrypt the identity document from step 2>",
        "identity_document": "<IPFS hash of the encrypted identity document from step 3>"
    },
    "metadata_signature": {
        "signature_hash": "<SHA256 hash of the immediately preceding metadata JSON object {...}>",
        "signature": "<Ravencoin signed signature_hash>"
    }
}   