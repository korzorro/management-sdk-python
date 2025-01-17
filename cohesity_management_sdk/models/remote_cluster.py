# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.bandwidth_limit
import cohesity_management_sdk.models.access_token_credential
import cohesity_management_sdk.models.view_box_pair_info

class RemoteCluster(object):

    """Implementation of the 'RemoteCluster' model.

    Specifies information about a remote Cluster that has been registered
    for replication.

    Attributes:
        all_endpoints_reachable (bool): Specifies whether any endpoint (such
            as a Node) on the remote Cluster is reachable from this local
            Cluster. If true, a service running on the local Cluster can
            communicate directly with any of its peers running on the remote
            Cluster, without using a proxy.
        auto_register_target (bool): Specifies whether the remote cluster
            needs to be kept in sync. This will be set to true by default.
        auto_registration (bool): Specifies whether the remote registration
            has happened automatically
            (due to registration on the other site).
            Can't think of other states (other than manually & automatically)
            so this isn't an enum.
            For a manual registration, this field will not be set.
        bandwidth_limit (BandwidthLimit): Specifies settings for limiting the
            data transfer rate between the local and remote Clusters.
        cluster_id (long|int): Specifies the unique id of the remote Cluster.
        cluster_incarnation_id (long|int): Specifies the unique incarnation id
            of the remote Cluster. This id is determined dynamically by
            contacting the remote Cluster.
        compression_enabled (bool): Specifies whether to compress the outbound
            data when transferring the replication data over the network to
            the remote Cluster.
        encryption_key (string): Specifies the encryption key used for
            encrypting the replication data from a local Cluster to a remote
            Cluster. If a key is not specified, replication traffic encryption
            is disabled. When Snapshots are replicated from a local Cluster to
            a remote Cluster, the encryption key specified on the local
            Cluster must be the same as the key specified on the remote
            Cluster.
        local_ips (list of string): Array of Local IP Addresses.  Specifies
            the IP addresses of the interfaces in the local Cluster which will
            be used for communicating with the remote Cluster.
        name (string): Specifies the name of the remote cluster. This field is
            determined dynamically by contacting the remote cluster.
        network_interface (string): Specifies the group name of the
            network interfaces to use for communicating with the remote
            Cluster.
        purpose_remote_access (bool): Whether the remote cluster will be used
            for remote access for SPOG.
        purpose_replication (bool): Whether the remote cluster will be used
            for replication.
        remote_access_credentials (AccessTokenCredential): Specifies the
            Cohesity credentials required for generating an access token.
        remote_ips (list of string): Array of Remote Node IP Addresses.
            Specifies the IP addresses of the Nodes on the remote Cluster to
            connect with. These IP addresses can also be VIPS. Specifying
            hostnames is not supported.
        tenant_id (string): Specifies the tenant Id of the organization that
            created this remote cluster configuration.
        user_name (string): Specifies the Cohesity user name used to connect
            to the remote Cluster.
        view_box_pair_info (list of ViewBoxPairInfo): Array of Storage Domain
            (View Box) Pairs.  Specifies pairings between Storage Domains
            (View Boxes) on the local Cluster with Storage Domains (View
            Boxes) on a remote Cluster that are used in replication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all_endpoints_reachable":'allEndpointsReachable',
        "auto_register_target":'autoRegisterTarget',
        "auto_registration":'autoRegistration',
        "bandwidth_limit":'bandwidthLimit',
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "compression_enabled":'compressionEnabled',
        "encryption_key":'encryptionKey',
        "local_ips":'localIps',
        "name":'name',
        "network_interface":'networkInterface',
        "purpose_remote_access":'purposeRemoteAccess',
        "purpose_replication":'purposeReplication',
        "remote_access_credentials":'remoteAccessCredentials',
        "remote_ips":'remoteIps',
        "tenant_id":'tenantId',
        "user_name":'userName',
        "view_box_pair_info":'viewBoxPairInfo'
    }

    def __init__(self,
                 all_endpoints_reachable=None,
                 auto_register_target=None,
                 auto_registration=None,
                 bandwidth_limit=None,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 compression_enabled=None,
                 encryption_key=None,
                 local_ips=None,
                 name=None,
                 network_interface=None,
                 purpose_remote_access=None,
                 purpose_replication=None,
                 remote_access_credentials=None,
                 remote_ips=None,
                 tenant_id=None,
                 user_name=None,
                 view_box_pair_info=None):
        """Constructor for the RemoteCluster class"""

        # Initialize members of the class
        self.all_endpoints_reachable = all_endpoints_reachable
        self.auto_register_target = auto_register_target
        self.auto_registration = auto_registration
        self.bandwidth_limit = bandwidth_limit
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.compression_enabled = compression_enabled
        self.encryption_key = encryption_key
        self.local_ips = local_ips
        self.name = name
        self.network_interface = network_interface
        self.purpose_remote_access = purpose_remote_access
        self.purpose_replication = purpose_replication
        self.remote_access_credentials = remote_access_credentials
        self.remote_ips = remote_ips
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.view_box_pair_info = view_box_pair_info


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        all_endpoints_reachable = dictionary.get('allEndpointsReachable')
        auto_register_target = dictionary.get('autoRegisterTarget')
        auto_registration = dictionary.get('autoRegistration')
        bandwidth_limit = cohesity_management_sdk.models.bandwidth_limit.BandwidthLimit.from_dictionary(dictionary.get('bandwidthLimit')) if dictionary.get('bandwidthLimit') else None
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        compression_enabled = dictionary.get('compressionEnabled')
        encryption_key = dictionary.get('encryptionKey')
        local_ips = dictionary.get('localIps')
        name = dictionary.get('name')
        network_interface = dictionary.get('networkInterface')
        purpose_remote_access = dictionary.get('purposeRemoteAccess')
        purpose_replication = dictionary.get('purposeReplication')
        remote_access_credentials = cohesity_management_sdk.models.access_token_credential.AccessTokenCredential.from_dictionary(dictionary.get('remoteAccessCredentials')) if dictionary.get('remoteAccessCredentials') else None
        remote_ips = dictionary.get('remoteIps')
        tenant_id = dictionary.get('tenantId')
        user_name = dictionary.get('userName')
        view_box_pair_info = None
        if dictionary.get('viewBoxPairInfo') != None:
            view_box_pair_info = list()
            for structure in dictionary.get('viewBoxPairInfo'):
                view_box_pair_info.append(cohesity_management_sdk.models.view_box_pair_info.ViewBoxPairInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(all_endpoints_reachable,
                   auto_register_target,
                   auto_registration,
                   bandwidth_limit,
                   cluster_id,
                   cluster_incarnation_id,
                   compression_enabled,
                   encryption_key,
                   local_ips,
                   name,
                   network_interface,
                   purpose_remote_access,
                   purpose_replication,
                   remote_access_credentials,
                   remote_ips,
                   tenant_id,
                   user_name,
                   view_box_pair_info)


