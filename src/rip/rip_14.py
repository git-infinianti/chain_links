from .utils import sign


def data(*args): return list(args)
def is_for_sale(for_sale=False): return for_sale

class MData14:
	def __init__(self,
        icon: str, name: str, description: str, asset_type: str, restrictions: list, keywords: list,
        issuer: str, website: str, website_url: str, contact_name: str, contact_email: str, address: str,
        sell_price: float, curreny: str, other:dict, attachments: list, recipients: dict, algorithm: str,
		ipfs: list, url: list
	) -> None:
		_asset = {
			'icon': icon,
			'name': name,
			'description': description,
			'asset_type': asset_type,
			'restrictions': restrictions,
			'keywords': keywords
		}
		_admin = {
			'issuer': issuer, 
			'website': website, 
			'contact_name': contact_name, 
			'website_url': website_url, 
			'contact_email': contact_email, 
			'address': address
		}
		_sell = {
			'sell_price': sell_price, 
			'curreny': curreny
		}
		_encryption = {
			'algorithm': algorithm, 
			'attachments': attachments, 
			'recipients': recipients
		}
		self.metadata = {
			'asset_data': _asset, 
			'admin_data': _admin, 
			'sell_data' : _sell, 
			'other_data': other, 
			'encryption': _encryption, 
			'ipfs_cids': ipfs,
			'url_links': url
		}
		self.signed_metadata = sign(self.metadata)


example = {
    'rip_14': {
	    'metadata': {
	    	'asset_data': {
			    'icon': '<base 64 encoded png (64x64 is recommended)>',
			    'name': '<full asset name>',
			    'description': '<asset description>',
			    'asset_type': '<e.g., Title, Points, Shares, Tickets>',
			    'restrictions': '<e.g., Rule 144, Members Only>',
			    'keywords': '<Baseball Cards, Coins, Book Of The Month Club>'
	    	},
	    	'admin_data': {
			    'issuer': '<issuer>',
			    'website': '<website>',
			    'contact_name': '<contact name>',
			    'website_url': '<website>',
			    'contact_email': '<contact email>',
			    'address': '<physical address>'
			},
			'for_sale': False,
			'sell_data': {
				'sale_price': '<price for the admin token>',
				'coin': '<3 letter ticker for currency, e.g., RVN, BTC, USD>'
			},
			'other_data': {
				'<key1>': '<value>',
				'<key2>': '<value>',
				'<key3>': '<value>'
			},
			'encryption': {
				'algorithm': '<e.g., AES, TripleSec>',
				'attachments': [
					'<IPFS hash encrypted attachment 1 created per. RIP11>',
					'<IPFS hash for encrypted attachment 2 created per. RIP11>',
					'<IPFS hash for encrypted attachment n created per. RIP11>'
				],
				'recipients': {
					'<recipient 1 encryption address>': '<PGP encrypted symmetric key of recipient 1 per. RIP11>',
					'<recipient 2 encryption address>': '<PGP encrypted symmetric key of recipient 2 per. RIP11>',
					'<recipient n encryption address>': '<PGP encrypted symmetric key of recipient n per. RIP11>'
				}
			},
			'ipfs_attachments': [
				'<IPFS hash for unencrypted attachment 1>',
				'<IPFS hash for unencrypted attachment 2>',
				'<IPFS hash for unencrypted attachment n>'
			],
			'url_links': [
				'<url link 1>',
				'<url link 2>',
				'<url link n>'
			]
		},
		'metadata_signature': {
			'signed_metadata': '<SHA256 hash of the immediately preceding metadata JSON object {...}>',
			'signature': '<Ravencoin signed signature_hash>'
		}
	}
}