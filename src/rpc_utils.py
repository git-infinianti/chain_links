def inputs(txids: list, vouts: list, sequences: list | None=None):
    def _input(txid, vout, sequence=None):
        return {'txid': txid, 'vout': vout, 'sequence': sequence}
    return [
        _input(txid, vout, sequence) 
        for txid, vout, sequence 
        in zip(txids, vouts, sequences) 
    ] if sequences else [
        _input(txid, vout) 
        for txid, vout 
        in zip(txids, vouts)]


def outputs(addresses: list, amounts: list):
    return {address: amount for address, amount in zip(addresses, amounts)}