from boa.interop.System.Block import GetTransactionByIndex
from boa.interop.System.Blockchain import GetTransactionByHash
from boa.interop.System.Header import GetBlockHash
from boa.interop.System.Transaction import GetTransactionHash

from boa.interop.System.Blockchain import GetBlock

def main(Height):
    Block   = GetBlock(Height)
    index   = 0
    Tx      = GetTransactionByIndex(Block, index)
    Txhash  = GetTransactionHash(Tx)
    NewTx   = GetTransactionByHash(Txhash)
    BlkHash = GetBlockHash(Block)
    print("all done")
