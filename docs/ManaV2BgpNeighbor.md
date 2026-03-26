# ManaV2BgpNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | [**List[ManaV2BgpNeighborAddressFamily]**](ManaV2BgpNeighborAddressFamily.md) |  | [optional] 
**allow_as_in** | **int** |  | [optional] 
**as_override** | **bool** |  | [optional] 
**bfd** | [**ManaV2BfdInstance**](ManaV2BfdInstance.md) |  | [optional] 
**bfd_neighbor** | [**ManaV2BfdNeighbor**](ManaV2BfdNeighbor.md) |  | [optional] 
**bgp_type** | **str** |  | [optional] 
**default_originate** | **str** | Set when default route needs to be advertised in BGP domain | [optional] 
**dynamic_neighbor_peers** | [**List[ManaV2BgpDynamicNeighborOperPeer]**](ManaV2BgpDynamicNeighborOperPeer.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**hold_timer** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**keepalive_timer** | **int** |  | [optional] 
**local_address** | **str** |  | [optional] 
**local_interface** | **str** |  | [optional] 
**max_prefix** | **int** | Maximum number of prefixes that can be received from neighbor | [optional] 
**md5_password** | **str** |  | [optional] 
**multi_hop** | **int** | Set when EBGP multi-hop functionality is enabled | [optional] 
**peer_asn** | **int** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**remove_private_as** | **bool** |  | [optional] 
**send_community** | **bool** | Flag for sending standard, extended, and large communities | [optional] 
**state** | **str** |  | [optional] 
**time_since_last_oper_change** | [**GoogleProtobufDuration**](GoogleProtobufDuration.md) |  | [optional] 
**up** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_bgp_neighbor import ManaV2BgpNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2BgpNeighbor from a JSON string
mana_v2_bgp_neighbor_instance = ManaV2BgpNeighbor.from_json(json)
# print the JSON string representation of the object
print(ManaV2BgpNeighbor.to_json())

# convert the object into a dict
mana_v2_bgp_neighbor_dict = mana_v2_bgp_neighbor_instance.to_dict()
# create an instance of ManaV2BgpNeighbor from a dict
mana_v2_bgp_neighbor_from_dict = ManaV2BgpNeighbor.from_dict(mana_v2_bgp_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


