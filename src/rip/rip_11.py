
from .utils import sign, p2pkh_chksum


class MData11_Recieve:
    def __init__(self,
        p2pkh: str, pgp_block: str
        ) -> None:
        self.metadata = {
            'tag_type': 'AET',
            'p2pkh_address': p2pkh,
            'pgp_public_key': pgp_block
        }
        self.signed = sign(self.metadata)
        self.chksum = p2pkh_chksum(p2pkh)


class MData11_Send:
    def __init__(self,
        p2pkh: list[str], pgp_block: list[str]
        ) -> None:
        recipients = {_p2pkh: _pgp_block for _p2pkh, _pgp_block in zip(p2pkh, pgp_block)}
        self.metadata = {
            'algorithm': 'ECDH',
            'recipients': recipients
        }
        self.signed = sign(self.metadata)
        self.chksum = p2pkh_chksum(p2pkh)


example = {
    "rip_11": {
    	"tag": {
    		"tag_type": "AET",
    		"ravencoin_address": "<Ravencoin address from step 1>",
    		"pgp_pubkey": "<recipient's PGP public key block>"		
    	},
    	"metadata_signature": {
    		"signed_metadata": "<SHA256 hash of the immediately preceding tag JSON object {...}>",
    		"signature": "<Ravencoin signed signature_hash>"
    	},
        "encryption": {
            "algorithm": "<e.g., AES, TripleSec>",
            "recipients": {
                "<recipient 1 encryption address>": "<PGP encrypted symmetric key to recipient 1>",
                "<recipient 2 encryption address>": "<PGP encrypted symmetric key to recipient 2>",
                "<recipient n encryption address>": "<PGP encrypted symmetric key to recipient n>"
            }
        }
    }
}