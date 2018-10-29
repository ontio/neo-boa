| Package | Name | Parameter |      |
| ---- | ---- | ---- | ---- |
|           boa.interop.Ontology.Attribute |                  GetUsage |                                   transaction_attr | get transaction attribute usage |
|           boa.interop.Ontology.Attribute |                   GetData |                                   transaction_attr | get transaction attribute data |
|            boa.interop.Ontology.Contract |                 GetScript |                                           contract | get contract script hash |
|            boa.interop.Ontology.Contract |                    Create | script, need_storage, name, version, author, email, description | create a contract |
|            boa.interop.Ontology.Contract |                   Migrate | script, need_storage, name, version, author, email, description | migrate  contract |
|              boa.interop.Ontology.Header |                GetVersion |                                             header | get the version of header |
|              boa.interop.Ontology.Header |             GetMerkleRoot |                                             header | get the merkle root of the transactions contained in the block |
|              boa.interop.Ontology.Header |          GetConsensusData |                                             header | get the address of the consensus |
|              boa.interop.Ontology.Header |          GetNextConsensus |                                             header | get the address where the next consensus will occur |
|              boa.interop.Ontology.Native |                    Invoke |                   param,method,contractAddress,ver | nvoke native contract |
|             boa.interop.Ontology.Runtime |           Base58ToAddress |                                                arg | transfer base58 address to byte array |
|             boa.interop.Ontology.Runtime |           AddressToBase58 |                                                arg | byte array address to base58 |
|             boa.interop.Ontology.Runtime |             GetRandomHash |                                                    | get current block hash |
|         boa.interop.Ontology.Transaction |                   GetType |                                        transaction | get transaction type |
|         boa.interop.Ontology.Transaction |             GetAttributes |                                        transaction | get transaction attributes |
|                boa.interop.System.Action |            RegisterAction |                                  event_name, *args | register a notirfy event |
|                   boa.interop.System.App |           RegisterAppCall |                         smart_contract_hash, *args | call other smart contract |
|            boa.interop.System.Blockchain |                 GetHeight |                                                    | get height of block chain |
|            boa.interop.System.Blockchain |                 GetHeader |                                     height_or_hash | get header by height or hash |
|            boa.interop.System.Blockchain |                  GetBlock |                                     height_or_hash | get block by height or hash |
|            boa.interop.System.Blockchain |            GetTransaction |                                               hash | get transaction by hash |
|            boa.interop.System.Blockchain |               GetContract |                                        script_hash | get contract by script hash |
| boa.interop.System.Blockchain | GetTransactionHeight | heigh of transaction |  |
|                 boa.interop.System.Block |       GetTransactionCount |                                              block | get transaction count of block |
|                 boa.interop.System.Block |           GetTransactions |                                              block | get transactions of block |
|                 boa.interop.System.Block |            GetTransaction |                                       block, index | get the transaction by index |
|              boa.interop.System.Contract |         GetStorageContext |                                           contract | get contract storage context |
|              boa.interop.System.Contract |                   Destroy |                                                    | destroy current contract(self) |
|       boa.interop.System.ExecutionEngine |        GetScriptContainer |                                                    | get the current script container of a smart contract execution |
|       boa.interop.System.ExecutionEngine |    GetExecutingScriptHash |                                                    | get the hash of the script ( smart contract ) which is currently being executed |
|       boa.interop.System.ExecutionEngine |      GetCallingScriptHash |                                                    | get the hash of the script ( smart contract ) which began execution of the current script. |
|       boa.interop.System.ExecutionEngine |        GetEntryScriptHash |                                                    | get the hash of the script ( smart contract ) which began execution of the smart contract. |
|                boa.interop.System.Header |                  GetIndex |                                             header | get the height/index of header |
|                boa.interop.System.Header |                   GetHash |                                             header | get the hash of header |
|                boa.interop.System.Header |               GetPrevHash |                                             header | get the hash of the previous header in the blockchain        |
|                boa.interop.System.Header |              GetTimestamp |                                             header | get the timestamp of when the header was created |
|               boa.interop.System.Runtime |                GetTrigger |                                                    | get trigger |
|               boa.interop.System.Runtime |              CheckWitness |                                     hash_or_pubkey | check the witness of address |
|               boa.interop.System.Runtime |                       Log |                                            message | print log on node |
|               boa.interop.System.Runtime |                    Notify |                                                arg | add notify to event |
|               boa.interop.System.Runtime |                   GetTime |                                                    | get timestamp of most recent block |
|               boa.interop.System.Runtime |                 Serialize |                                               item | serialize item to byte array |
|               boa.interop.System.Runtime |               Deserialize |                                               item | deserialize byte array to item |
|        boa.interop.System.StorageContext |                AsReadOnly |                                                    | Convert Storage Context to ReadOnly |
|               boa.interop.System.Storage |                GetContext |                                                    | get the storage context |
|               boa.interop.System.Storage |        GetReadOnlyContext |                                                    | get the readOnly Storage Context |
|               boa.interop.System.Storage |                       Get |                                       context, key | get the storage by key |
|               boa.interop.System.Storage |                       Put |                                context, key, value | put the key-value storage |
|               boa.interop.System.Storage |                    Delete |                                       context, key | delete storage by key |
|           boa.interop.System.Transaction |                   GetHash |                                        transaction | Get the Transaction of hash |



