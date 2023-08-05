# coding: utf-8

from __future__ import absolute_import

# import KafkaClient
from huaweicloudsdkkafka.v2.kafka_client import KafkaClient
from huaweicloudsdkkafka.v2.kafka_async_client import KafkaAsyncClient
# import models into sdk package
from huaweicloudsdkkafka.v2.model.access_policy_entity import AccessPolicyEntity
from huaweicloudsdkkafka.v2.model.access_policy_topic_entity import AccessPolicyTopicEntity
from huaweicloudsdkkafka.v2.model.batch_create_or_delete_kafka_tag_request import BatchCreateOrDeleteKafkaTagRequest
from huaweicloudsdkkafka.v2.model.batch_create_or_delete_kafka_tag_response import BatchCreateOrDeleteKafkaTagResponse
from huaweicloudsdkkafka.v2.model.batch_create_or_delete_tag_req import BatchCreateOrDeleteTagReq
from huaweicloudsdkkafka.v2.model.batch_delete_instance_topic_req import BatchDeleteInstanceTopicReq
from huaweicloudsdkkafka.v2.model.batch_delete_instance_topic_request import BatchDeleteInstanceTopicRequest
from huaweicloudsdkkafka.v2.model.batch_delete_instance_topic_resp_topics import BatchDeleteInstanceTopicRespTopics
from huaweicloudsdkkafka.v2.model.batch_delete_instance_topic_response import BatchDeleteInstanceTopicResponse
from huaweicloudsdkkafka.v2.model.batch_delete_instance_users_req import BatchDeleteInstanceUsersReq
from huaweicloudsdkkafka.v2.model.batch_delete_instance_users_request import BatchDeleteInstanceUsersRequest
from huaweicloudsdkkafka.v2.model.batch_delete_instance_users_response import BatchDeleteInstanceUsersResponse
from huaweicloudsdkkafka.v2.model.batch_restart_or_delete_instance_req import BatchRestartOrDeleteInstanceReq
from huaweicloudsdkkafka.v2.model.batch_restart_or_delete_instance_resp_results import BatchRestartOrDeleteInstanceRespResults
from huaweicloudsdkkafka.v2.model.batch_restart_or_delete_instances_request import BatchRestartOrDeleteInstancesRequest
from huaweicloudsdkkafka.v2.model.batch_restart_or_delete_instances_response import BatchRestartOrDeleteInstancesResponse
from huaweicloudsdkkafka.v2.model.create_connector_req import CreateConnectorReq
from huaweicloudsdkkafka.v2.model.create_connector_request import CreateConnectorRequest
from huaweicloudsdkkafka.v2.model.create_connector_response import CreateConnectorResponse
from huaweicloudsdkkafka.v2.model.create_instance_topic_req import CreateInstanceTopicReq
from huaweicloudsdkkafka.v2.model.create_instance_topic_request import CreateInstanceTopicRequest
from huaweicloudsdkkafka.v2.model.create_instance_topic_response import CreateInstanceTopicResponse
from huaweicloudsdkkafka.v2.model.create_instance_user_req import CreateInstanceUserReq
from huaweicloudsdkkafka.v2.model.create_instance_user_request import CreateInstanceUserRequest
from huaweicloudsdkkafka.v2.model.create_instance_user_response import CreateInstanceUserResponse
from huaweicloudsdkkafka.v2.model.create_partition_req import CreatePartitionReq
from huaweicloudsdkkafka.v2.model.create_partition_request import CreatePartitionRequest
from huaweicloudsdkkafka.v2.model.create_partition_response import CreatePartitionResponse
from huaweicloudsdkkafka.v2.model.create_post_paid_instance_req import CreatePostPaidInstanceReq
from huaweicloudsdkkafka.v2.model.create_post_paid_instance_request import CreatePostPaidInstanceRequest
from huaweicloudsdkkafka.v2.model.create_post_paid_instance_response import CreatePostPaidInstanceResponse
from huaweicloudsdkkafka.v2.model.create_sink_task_req import CreateSinkTaskReq
from huaweicloudsdkkafka.v2.model.create_sink_task_request import CreateSinkTaskRequest
from huaweicloudsdkkafka.v2.model.create_sink_task_response import CreateSinkTaskResponse
from huaweicloudsdkkafka.v2.model.delete_background_task_request import DeleteBackgroundTaskRequest
from huaweicloudsdkkafka.v2.model.delete_background_task_response import DeleteBackgroundTaskResponse
from huaweicloudsdkkafka.v2.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkkafka.v2.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkkafka.v2.model.delete_sink_task_request import DeleteSinkTaskRequest
from huaweicloudsdkkafka.v2.model.delete_sink_task_response import DeleteSinkTaskResponse
from huaweicloudsdkkafka.v2.model.diskusage_entity import DiskusageEntity
from huaweicloudsdkkafka.v2.model.diskusage_topic_entity import DiskusageTopicEntity
from huaweicloudsdkkafka.v2.model.list_available_zones_request import ListAvailableZonesRequest
from huaweicloudsdkkafka.v2.model.list_available_zones_resp_available_zones import ListAvailableZonesRespAvailableZones
from huaweicloudsdkkafka.v2.model.list_available_zones_response import ListAvailableZonesResponse
from huaweicloudsdkkafka.v2.model.list_background_tasks_request import ListBackgroundTasksRequest
from huaweicloudsdkkafka.v2.model.list_background_tasks_resp_tasks import ListBackgroundTasksRespTasks
from huaweicloudsdkkafka.v2.model.list_background_tasks_response import ListBackgroundTasksResponse
from huaweicloudsdkkafka.v2.model.list_instance_topics_request import ListInstanceTopicsRequest
from huaweicloudsdkkafka.v2.model.list_instance_topics_response import ListInstanceTopicsResponse
from huaweicloudsdkkafka.v2.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkkafka.v2.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkkafka.v2.model.list_products_request import ListProductsRequest
from huaweicloudsdkkafka.v2.model.list_products_resp_detail import ListProductsRespDetail
from huaweicloudsdkkafka.v2.model.list_products_resp_hourly import ListProductsRespHourly
from huaweicloudsdkkafka.v2.model.list_products_resp_io import ListProductsRespIo
from huaweicloudsdkkafka.v2.model.list_products_resp_values import ListProductsRespValues
from huaweicloudsdkkafka.v2.model.list_products_response import ListProductsResponse
from huaweicloudsdkkafka.v2.model.list_sink_tasks_request import ListSinkTasksRequest
from huaweicloudsdkkafka.v2.model.list_sink_tasks_resp_tasks import ListSinkTasksRespTasks
from huaweicloudsdkkafka.v2.model.list_sink_tasks_response import ListSinkTasksResponse
from huaweicloudsdkkafka.v2.model.maintain_windows_entity import MaintainWindowsEntity
from huaweicloudsdkkafka.v2.model.messages_entity import MessagesEntity
from huaweicloudsdkkafka.v2.model.obs_destination_descriptor import ObsDestinationDescriptor
from huaweicloudsdkkafka.v2.model.policy_entity import PolicyEntity
from huaweicloudsdkkafka.v2.model.reset_manager_password_req import ResetManagerPasswordReq
from huaweicloudsdkkafka.v2.model.reset_manager_password_request import ResetManagerPasswordRequest
from huaweicloudsdkkafka.v2.model.reset_manager_password_response import ResetManagerPasswordResponse
from huaweicloudsdkkafka.v2.model.reset_message_offset_req import ResetMessageOffsetReq
from huaweicloudsdkkafka.v2.model.reset_message_offset_request import ResetMessageOffsetRequest
from huaweicloudsdkkafka.v2.model.reset_message_offset_response import ResetMessageOffsetResponse
from huaweicloudsdkkafka.v2.model.reset_password_req import ResetPasswordReq
from huaweicloudsdkkafka.v2.model.reset_password_request import ResetPasswordRequest
from huaweicloudsdkkafka.v2.model.reset_password_response import ResetPasswordResponse
from huaweicloudsdkkafka.v2.model.reset_replica_req import ResetReplicaReq
from huaweicloudsdkkafka.v2.model.reset_replica_req_partitions import ResetReplicaReqPartitions
from huaweicloudsdkkafka.v2.model.reset_user_passwrod_req import ResetUserPasswrodReq
from huaweicloudsdkkafka.v2.model.reset_user_passwrod_request import ResetUserPasswrodRequest
from huaweicloudsdkkafka.v2.model.reset_user_passwrod_response import ResetUserPasswrodResponse
from huaweicloudsdkkafka.v2.model.resize_instance_req import ResizeInstanceReq
from huaweicloudsdkkafka.v2.model.resize_instance_request import ResizeInstanceRequest
from huaweicloudsdkkafka.v2.model.resize_instance_response import ResizeInstanceResponse
from huaweicloudsdkkafka.v2.model.restart_manager_request import RestartManagerRequest
from huaweicloudsdkkafka.v2.model.restart_manager_response import RestartManagerResponse
from huaweicloudsdkkafka.v2.model.show_background_task_request import ShowBackgroundTaskRequest
from huaweicloudsdkkafka.v2.model.show_background_task_response import ShowBackgroundTaskResponse
from huaweicloudsdkkafka.v2.model.show_ces_hierarchy_request import ShowCesHierarchyRequest
from huaweicloudsdkkafka.v2.model.show_ces_hierarchy_response import ShowCesHierarchyResponse
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_children import ShowCeshierarchyRespChildren
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_dimensions import ShowCeshierarchyRespDimensions
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_groups import ShowCeshierarchyRespGroups
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_instance_ids import ShowCeshierarchyRespInstanceIds
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_nodes import ShowCeshierarchyRespNodes
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_partitions import ShowCeshierarchyRespPartitions
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_queues import ShowCeshierarchyRespQueues
from huaweicloudsdkkafka.v2.model.show_ceshierarchy_resp_queues1 import ShowCeshierarchyRespQueues1
from huaweicloudsdkkafka.v2.model.show_cluster_request import ShowClusterRequest
from huaweicloudsdkkafka.v2.model.show_cluster_resp_cluster import ShowClusterRespCluster
from huaweicloudsdkkafka.v2.model.show_cluster_resp_cluster_brokers import ShowClusterRespClusterBrokers
from huaweicloudsdkkafka.v2.model.show_cluster_response import ShowClusterResponse
from huaweicloudsdkkafka.v2.model.show_coordinators_request import ShowCoordinatorsRequest
from huaweicloudsdkkafka.v2.model.show_coordinators_resp_coordinators import ShowCoordinatorsRespCoordinators
from huaweicloudsdkkafka.v2.model.show_coordinators_response import ShowCoordinatorsResponse
from huaweicloudsdkkafka.v2.model.show_groups_request import ShowGroupsRequest
from huaweicloudsdkkafka.v2.model.show_groups_resp_group import ShowGroupsRespGroup
from huaweicloudsdkkafka.v2.model.show_groups_resp_group_assignment import ShowGroupsRespGroupAssignment
from huaweicloudsdkkafka.v2.model.show_groups_resp_group_group_message_offsets import ShowGroupsRespGroupGroupMessageOffsets
from huaweicloudsdkkafka.v2.model.show_groups_resp_group_members import ShowGroupsRespGroupMembers
from huaweicloudsdkkafka.v2.model.show_groups_response import ShowGroupsResponse
from huaweicloudsdkkafka.v2.model.show_instance_extend_product_info_request import ShowInstanceExtendProductInfoRequest
from huaweicloudsdkkafka.v2.model.show_instance_extend_product_info_response import ShowInstanceExtendProductInfoResponse
from huaweicloudsdkkafka.v2.model.show_instance_messages_request import ShowInstanceMessagesRequest
from huaweicloudsdkkafka.v2.model.show_instance_messages_response import ShowInstanceMessagesResponse
from huaweicloudsdkkafka.v2.model.show_instance_request import ShowInstanceRequest
from huaweicloudsdkkafka.v2.model.show_instance_resp import ShowInstanceResp
from huaweicloudsdkkafka.v2.model.show_instance_response import ShowInstanceResponse
from huaweicloudsdkkafka.v2.model.show_instance_topic_detail_request import ShowInstanceTopicDetailRequest
from huaweicloudsdkkafka.v2.model.show_instance_topic_detail_resp_partitions import ShowInstanceTopicDetailRespPartitions
from huaweicloudsdkkafka.v2.model.show_instance_topic_detail_resp_replicas import ShowInstanceTopicDetailRespReplicas
from huaweicloudsdkkafka.v2.model.show_instance_topic_detail_response import ShowInstanceTopicDetailResponse
from huaweicloudsdkkafka.v2.model.show_instance_users_entity import ShowInstanceUsersEntity
from huaweicloudsdkkafka.v2.model.show_instance_users_request import ShowInstanceUsersRequest
from huaweicloudsdkkafka.v2.model.show_instance_users_response import ShowInstanceUsersResponse
from huaweicloudsdkkafka.v2.model.show_kafka_project_tags_request import ShowKafkaProjectTagsRequest
from huaweicloudsdkkafka.v2.model.show_kafka_project_tags_response import ShowKafkaProjectTagsResponse
from huaweicloudsdkkafka.v2.model.show_kafka_tags_request import ShowKafkaTagsRequest
from huaweicloudsdkkafka.v2.model.show_kafka_tags_response import ShowKafkaTagsResponse
from huaweicloudsdkkafka.v2.model.show_kafka_topic_partition_diskusage_request import ShowKafkaTopicPartitionDiskusageRequest
from huaweicloudsdkkafka.v2.model.show_kafka_topic_partition_diskusage_response import ShowKafkaTopicPartitionDiskusageResponse
from huaweicloudsdkkafka.v2.model.show_maintain_windows_request import ShowMaintainWindowsRequest
from huaweicloudsdkkafka.v2.model.show_maintain_windows_response import ShowMaintainWindowsResponse
from huaweicloudsdkkafka.v2.model.show_messages_request import ShowMessagesRequest
from huaweicloudsdkkafka.v2.model.show_messages_resp_messages import ShowMessagesRespMessages
from huaweicloudsdkkafka.v2.model.show_messages_response import ShowMessagesResponse
from huaweicloudsdkkafka.v2.model.show_partition_beginning_message_request import ShowPartitionBeginningMessageRequest
from huaweicloudsdkkafka.v2.model.show_partition_beginning_message_response import ShowPartitionBeginningMessageResponse
from huaweicloudsdkkafka.v2.model.show_partition_end_message_request import ShowPartitionEndMessageRequest
from huaweicloudsdkkafka.v2.model.show_partition_end_message_response import ShowPartitionEndMessageResponse
from huaweicloudsdkkafka.v2.model.show_partition_message_entity import ShowPartitionMessageEntity
from huaweicloudsdkkafka.v2.model.show_partition_message_request import ShowPartitionMessageRequest
from huaweicloudsdkkafka.v2.model.show_partition_message_response import ShowPartitionMessageResponse
from huaweicloudsdkkafka.v2.model.show_sink_task_detail_request import ShowSinkTaskDetailRequest
from huaweicloudsdkkafka.v2.model.show_sink_task_detail_resp_obs_destination_descriptor import ShowSinkTaskDetailRespObsDestinationDescriptor
from huaweicloudsdkkafka.v2.model.show_sink_task_detail_resp_partitions import ShowSinkTaskDetailRespPartitions
from huaweicloudsdkkafka.v2.model.show_sink_task_detail_resp_topics_info import ShowSinkTaskDetailRespTopicsInfo
from huaweicloudsdkkafka.v2.model.show_sink_task_detail_response import ShowSinkTaskDetailResponse
from huaweicloudsdkkafka.v2.model.show_topic_access_policy_request import ShowTopicAccessPolicyRequest
from huaweicloudsdkkafka.v2.model.show_topic_access_policy_response import ShowTopicAccessPolicyResponse
from huaweicloudsdkkafka.v2.model.tag_entity import TagEntity
from huaweicloudsdkkafka.v2.model.tag_multy_value_entity import TagMultyValueEntity
from huaweicloudsdkkafka.v2.model.topic_entity import TopicEntity
from huaweicloudsdkkafka.v2.model.update_instance_auto_create_topic_req import UpdateInstanceAutoCreateTopicReq
from huaweicloudsdkkafka.v2.model.update_instance_auto_create_topic_request import UpdateInstanceAutoCreateTopicRequest
from huaweicloudsdkkafka.v2.model.update_instance_auto_create_topic_response import UpdateInstanceAutoCreateTopicResponse
from huaweicloudsdkkafka.v2.model.update_instance_cross_vpc_ip_req import UpdateInstanceCrossVpcIpReq
from huaweicloudsdkkafka.v2.model.update_instance_cross_vpc_ip_request import UpdateInstanceCrossVpcIpRequest
from huaweicloudsdkkafka.v2.model.update_instance_cross_vpc_ip_resp_results import UpdateInstanceCrossVpcIpRespResults
from huaweicloudsdkkafka.v2.model.update_instance_cross_vpc_ip_response import UpdateInstanceCrossVpcIpResponse
from huaweicloudsdkkafka.v2.model.update_instance_req import UpdateInstanceReq
from huaweicloudsdkkafka.v2.model.update_instance_request import UpdateInstanceRequest
from huaweicloudsdkkafka.v2.model.update_instance_response import UpdateInstanceResponse
from huaweicloudsdkkafka.v2.model.update_instance_topic_req import UpdateInstanceTopicReq
from huaweicloudsdkkafka.v2.model.update_instance_topic_req_topics import UpdateInstanceTopicReqTopics
from huaweicloudsdkkafka.v2.model.update_instance_topic_request import UpdateInstanceTopicRequest
from huaweicloudsdkkafka.v2.model.update_instance_topic_response import UpdateInstanceTopicResponse
from huaweicloudsdkkafka.v2.model.update_sink_task_quota_req import UpdateSinkTaskQuotaReq
from huaweicloudsdkkafka.v2.model.update_sink_task_quota_request import UpdateSinkTaskQuotaRequest
from huaweicloudsdkkafka.v2.model.update_sink_task_quota_response import UpdateSinkTaskQuotaResponse
from huaweicloudsdkkafka.v2.model.update_topic_access_policy_req import UpdateTopicAccessPolicyReq
from huaweicloudsdkkafka.v2.model.update_topic_access_policy_request import UpdateTopicAccessPolicyRequest
from huaweicloudsdkkafka.v2.model.update_topic_access_policy_response import UpdateTopicAccessPolicyResponse
from huaweicloudsdkkafka.v2.model.update_topic_replica_request import UpdateTopicReplicaRequest
from huaweicloudsdkkafka.v2.model.update_topic_replica_response import UpdateTopicReplicaResponse

