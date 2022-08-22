import json
from cardano.wallet import WalletService
from cardano.backends.walletrest import WalletREST
from blockfrost import BlockFrostApi, ApiError, ApiUrls


# stakepool address
stake_pool_address = 'stake_test1ury6fcjrzzz3he9xt9dpf40par5j3dwesj3n7vq25zfgxfcf0fs0m'

api = BlockFrostApi(
    project_id='testnetoZMQNoHmV7Q5jlS5kGrpqwzUO2IrCoJ5', 
    base_url=ApiUrls.testnet.value,
)

def cardano_response():
    try:
        health = api.health()
        health = api.health(return_type='json')
        print(health)

        if health["is_healthy"]:
            account_rewards = api.account_rewards(
                stake_address=stake_pool_address,
                count=20
            )
            print(account_rewards)
            print(len(account_rewards))  

            account_rewards = api.account_rewards(
                stake_address=stake_pool_address,
                count=20,
                gather_pages=True,
            )
            print(account_rewards[0].epoch) 
            print(len(account_rewards))

            address = api.address(
                address= stake_pool_address)
            print(address.type)  
            for amount in address.amount:
                print(amount.unit)
        else:
            print(json.dumps({
                "Error" : "Could not complete "
            }))

    except ApiError as e:
        print(e)

cardano_response()