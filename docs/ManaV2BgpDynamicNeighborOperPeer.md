# ManaV2BgpDynamicNeighborOperPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_oper_status_change** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**local_address** | **str** | Local address used for this peer session, if known from oper | [optional] 
**oper_status** | **bool** | True when the BGP session to this peer is operationally up (e.g. established) | [optional] 
**peer_asn** | **int** | Peer ASN from oper, if reported | [optional] 
**remote_address** | **str** | Peer address from device oper state (IPv4/IPv6; may include IPv6 zone id) | [optional] 
**state** | **str** | BGP FSM state for this peer session | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_bgp_dynamic_neighbor_oper_peer import ManaV2BgpDynamicNeighborOperPeer

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2BgpDynamicNeighborOperPeer from a JSON string
mana_v2_bgp_dynamic_neighbor_oper_peer_instance = ManaV2BgpDynamicNeighborOperPeer.from_json(json)
# print the JSON string representation of the object
print(ManaV2BgpDynamicNeighborOperPeer.to_json())

# convert the object into a dict
mana_v2_bgp_dynamic_neighbor_oper_peer_dict = mana_v2_bgp_dynamic_neighbor_oper_peer_instance.to_dict()
# create an instance of ManaV2BgpDynamicNeighborOperPeer from a dict
mana_v2_bgp_dynamic_neighbor_oper_peer_from_dict = ManaV2BgpDynamicNeighborOperPeer.from_dict(mana_v2_bgp_dynamic_neighbor_oper_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


