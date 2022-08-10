# %%capture
# !pip install shroomdk
def query_flipside(sql="select max(block_timestamp)from ethereum.core.fact_blocks"):
    from shroomdk import ShroomDK
    import os
    import pandas as pd
    flipside_api = os.environ["FLIPSIDE_API"]
    sdk = ShroomDK(flipside_api)
    results = sdk.query(sql, ttl_minutes=1440)
    df = pd.DataFrame(results.records)
    return df

    
