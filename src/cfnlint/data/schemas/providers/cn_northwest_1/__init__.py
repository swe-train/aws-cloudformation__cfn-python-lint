from typing import List

# pylint: disable=too-many-lines
types = [
    "AWS::CDK::Metadata",
    "AWS::ApiGatewayV2::Integration",
    "AWS::ApiGatewayV2::ApiMapping",
    "AWS::CE::AnomalySubscription",
    "AWS::Glue::Partition",
    "AWS::EC2::TransitGatewayRouteTablePropagation",
    "AWS::ApiGateway::BasePathMapping",
    "AWS::WAFRegional::GeoMatchSet",
    "AWS::GuardDuty::Filter",
    "AWS::ECS::Service",
    "AWS::ServiceCatalog::PortfolioPrincipalAssociation",
    "AWS::RAM::ResourceShare",
    "AWS::DynamoDB::Table",
    "AWS::AmazonMQ::ConfigurationAssociation",
    "AWS::WAFRegional::IPSet",
    "AWS::EC2::SecurityGroupEgress",
    "AWS::Config::OrganizationConfigRule",
    "AWS::Config::ConfigurationRecorder",
    "AWS::AppConfig::ExtensionAssociation",
    "AWS::IoT::TopicRuleDestination",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::RDS::DBInstance",
    "AWS::EC2::VPCDHCPOptionsAssociation",
    "AWS::ApiGateway::Model",
    "AWS::ApiGatewayV2::IntegrationResponse",
    "AWS::EC2::NetworkAcl",
    "AWS::Lambda::EventSourceMapping",
    "AWS::Budgets::BudgetsAction",
    "AWS::Logs::ResourcePolicy",
    "AWS::ServiceCatalog::LaunchNotificationConstraint",
    "AWS::IoT::CACertificate",
    "AWS::EC2::NetworkAclEntry",
    "AWS::Transfer::Certificate",
    "AWS::ApiGateway::DocumentationPart",
    "AWS::CloudWatch::CompositeAlarm",
    "AWS::Route53Resolver::FirewallDomainList",
    "AWS::AppConfig::Application",
    "AWS::OpsWorks::Stack",
    "AWS::GameLift::Fleet",
    "AWS::DataSync::LocationFSxWindows",
    "AWS::GameLift::Build",
    "AWS::ApiGateway::RequestValidator",
    "AWS::AutoScaling::WarmPool",
    "AWS::ApplicationAutoScaling::ScalableTarget",
    "AWS::ApiGatewayV2::Model",
    "AWS::Neptune::DBSubnetGroup",
    "AWS::Cassandra::Keyspace",
    "AWS::ApiGateway::DomainName",
    "AWS::ECS::PrimaryTaskSet",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::WAFv2::RegexPatternSet",
    "AWS::EKS::FargateProfile",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::Route53::RecordSet",
    "AWS::ElastiCache::SecurityGroup",
    "AWS::OpsWorks::Layer",
    "AWS::KinesisFirehose::DeliveryStream",
    "AWS::MediaConvert::Queue",
    "AWS::SageMaker::CodeRepository",
    "AWS::ImageBuilder::Component",
    "AWS::Glue::Connection",
    "AWS::IAM::Group",
    "AWS::WAFRegional::WebACLAssociation",
    "AWS::EC2::TransitGatewayMulticastGroupSource",
    "AWS::Transfer::Profile",
    "AWS::DataBrew::Recipe",
    "AWS::GameLift::Alias",
    "AWS::ApiGateway::UsagePlanKey",
    "AWS::FMS::Policy",
    "AWS::CloudFront::RealtimeLogConfig",
    "AWS::SageMaker::Pipeline",
    "AWS::DocDB::DBInstance",
    "AWS::LakeFormation::DataCellsFilter",
    "AWS::DataSync::LocationHDFS",
    "AWS::Events::Archive",
    "AWS::MSK::Cluster",
    "AWS::EC2::VPCEndpointConnectionNotification",
    "AWS::CodePipeline::Pipeline",
    "AWS::OpsWorks::Instance",
    "AWS::ImageBuilder::ImagePipeline",
    "AWS::ElasticLoadBalancingV2::ListenerCertificate",
    "AWS::CloudFormation::ModuleVersion",
    "AWS::Cloud9::EnvironmentEC2",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::Synthetics::Canary",
    "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption",
    "AWS::SNS::Subscription",
    "AWS::EC2::NatGateway",
    "AWS::Transfer::Workflow",
    "AWS::AppConfig::DeploymentStrategy",
    "AWS::Glue::DevEndpoint",
    "AWS::SageMaker::ModelPackage",
    "AWS::WAFRegional::SizeConstraintSet",
    "AWS::ElastiCache::UserGroup",
    "AWS::IoT::ThingGroup",
    "AWS::ImageBuilder::ImageRecipe",
    "AWS::ApiGateway::RestApi",
    "AWS::OpsWorks::ElasticLoadBalancerAttachment",
    "AWS::MediaConvert::JobTemplate",
    "AWS::S3ObjectLambda::AccessPointPolicy",
    "AWS::ElastiCache::ReplicationGroup",
    "AWS::StepFunctions::StateMachineAlias",
    "AWS::Cassandra::Table",
    "AWS::RDS::GlobalCluster",
    "AWS::CloudFormation::ModuleDefaultVersion",
    "AWS::CE::CostCategory",
    "AWS::Glue::Job",
    "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
    "AWS::Route53::HostedZone",
    "AWS::Glue::Table",
    "AWS::WAFRegional::WebACL",
    "AWS::Logs::MetricFilter",
    "AWS::Lambda::Function",
    "AWS::SNS::Topic",
    "AWS::Backup::BackupSelection",
    "AWS::DataSync::LocationFSxLustre",
    "AWS::SageMaker::App",
    "AWS::EC2::VPCGatewayAttachment",
    "AWS::CloudTrail::Trail",
    "AWS::EC2::VPNConnectionRoute",
    "AWS::GameLift::GameServerGroup",
    "AWS::AppStream::Stack",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::GatewayRouteTableAssociation",
    "AWS::WAFv2::IPSet",
    "AWS::SSM::Document",
    "AWS::IAM::Role",
    "AWS::DMS::Endpoint",
    "AWS::CloudFront::CloudFrontOriginAccessIdentity",
    "AWS::SageMaker::EndpointConfig",
    "AWS::ApiGateway::ApiKey",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::ApiGateway::ClientCertificate",
    "AWS::KinesisAnalyticsV2::Application",
    "AWS::Lambda::Alias",
    "AWS::WAF::IPSet",
    "AWS::EC2::TransitGatewayMulticastDomainAssociation",
    "AWS::WAF::SizeConstraintSet",
    "AWS::EC2::TransitGatewayRouteTableAssociation",
    "AWS::AppConfig::Environment",
    "AWS::ImageBuilder::Image",
    "AWS::ElastiCache::SecurityGroupIngress",
    "AWS::WAFRegional::XssMatchSet",
    "AWS::RDS::DBProxyTargetGroup",
    "AWS::CloudWatch::Dashboard",
    "AWS::CloudWatch::Alarm",
    "AWS::IoT::ThingType",
    "AWS::GuardDuty::Member",
    "AWS::CloudFormation::CustomResource",
    "AWS::KinesisAnalytics::ApplicationOutput",
    "AWS::WAFv2::RuleGroup",
    "AWS::ElastiCache::ParameterGroup",
    "AWS::Glue::Classifier",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CloudFormation::StackSet",
    "AWS::EC2::Route",
    "AWS::CodeCommit::Repository",
    "AWS::RolesAnywhere::Profile",
    "AWS::XRay::ResourcePolicy",
    "AWS::IoT::ResourceSpecificLogging",
    "AWS::ServiceCatalog::LaunchTemplateConstraint",
    "AWS::WAFv2::LoggingConfiguration",
    "AWS::DynamoDB::GlobalTable",
    "AWS::Backup::BackupPlan",
    "AWS::ImageBuilder::DistributionConfiguration",
    "AWS::LakeFormation::Permissions",
    "AWS::Glue::DataCatalogEncryptionSettings",
    "AWS::CloudFront::PublicKey",
    "AWS::RAM::Permission",
    "AWS::DataSync::Task",
    "AWS::ECS::TaskDefinition",
    "AWS::SageMaker::Model",
    "AWS::AppSync::FunctionConfiguration",
    "AWS::EC2::SpotFleet",
    "AWS::Glue::SchemaVersion",
    "AWS::IoT::PolicyPrincipalAttachment",
    "AWS::FraudDetector::List",
    "AWS::MSK::BatchScramSecret",
    "AWS::DMS::Certificate",
    "AWS::S3::Bucket",
    "AWS::GuardDuty::IPSet",
    "AWS::ServiceDiscovery::HttpNamespace",
    "AWS::EMR::SecurityConfiguration",
    "AWS::CloudWatch::InsightRule",
    "AWS::ApiGateway::UsagePlan",
    "AWS::Batch::SchedulingPolicy",
    "AWS::IoT::Authorizer",
    "AWS::ApiGatewayV2::VpcLink",
    "AWS::IoT::JobTemplate",
    "AWS::ServiceCatalog::PortfolioProductAssociation",
    "AWS::DataBrew::Project",
    "AWS::Athena::WorkGroup",
    "AWS::SageMaker::ImageVersion",
    "AWS::ApiGatewayV2::Api",
    "AWS::CUR::ReportDefinition",
    "AWS::ServiceCatalog::PortfolioShare",
    "AWS::ApiGateway::VpcLink",
    "AWS::IAM::ServerCertificate",
    "AWS::IoT::SecurityProfile",
    "AWS::Events::EventBus",
    "AWS::SQS::QueueInlinePolicy",
    "AWS::Organizations::Organization",
    "AWS::AutoScalingPlans::ScalingPlan",
    "AWS::SSM::MaintenanceWindowTarget",
    "AWS::ApiGateway::Authorizer",
    "AWS::AppStream::ImageBuilder",
    "AWS::IAM::Policy",
    "AWS::DataBrew::Schedule",
    "AWS::RDS::DBSecurityGroupIngress",
    "AWS::AppStream::StackFleetAssociation",
    "AWS::EC2::TransitGatewayMulticastGroupMember",
    "AWS::EC2::VolumeAttachment",
    "AWS::Glue::SecurityConfiguration",
    "AWS::DataBrew::Ruleset",
    "AWS::GameLift::MatchmakingConfiguration",
    "AWS::ApplicationInsights::Application",
    "AWS::ECS::ClusterCapacityProviderAssociations",
    "AWS::AppConfig::ConfigurationProfile",
    "AWS::Route53Resolver::FirewallRuleGroup",
    "AWS::MSK::Configuration",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::VPCEndpointServicePermissions",
    "AWS::SSM::MaintenanceWindowTask",
    "AWS::EC2::TransitGatewayMulticastDomain",
    "AWS::EKS::Cluster",
    "AWS::CodeBuild::Project",
    "AWS::EFS::FileSystem",
    "AWS::Logs::QueryDefinition",
    "AWS::IAM::InstanceProfile",
    "AWS::IoT::BillingGroup",
    "AWS::DataSync::LocationNFS",
    "AWS::KinesisAnalyticsV2::ApplicationOutput",
    "AWS::SageMaker::Domain",
    "AWS::CertificateManager::Certificate",
    "AWS::Glue::SchemaVersionMetadata",
    "AWS::SDB::Domain",
    "AWS::EC2::SubnetRouteTableAssociation",
    "AWS::SageMaker::NotebookInstanceLifecycleConfig",
    "AWS::ImageBuilder::ContainerRecipe",
    "AWS::EFS::AccessPoint",
    "AWS::Redshift::ClusterSecurityGroupIngress",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::OpenSearchService::Domain",
    "AWS::ServiceDiscovery::Instance",
    "AWS::Elasticsearch::Domain",
    "AWS::KinesisAnalytics::Application",
    "AWS::ApiGatewayV2::Deployment",
    "AWS::ServiceCatalog::StackSetConstraint",
    "AWS::EC2::NetworkInterfacePermission",
    "AWS::ServiceCatalog::TagOption",
    "AWS::ServiceDiscovery::PrivateDnsNamespace",
    "AWS::ServiceCatalog::LaunchRoleConstraint",
    "AWS::IoT::RoleAlias",
    "AWS::SecretsManager::ResourcePolicy",
    "AWS::Config::ConfigRule",
    "AWS::ECS::TaskSet",
    "AWS::AppSync::ApiKey",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::WAFRegional::RateBasedRule",
    "AWS::EC2::VPC",
    "AWS::MSK::VpcConnection",
    "AWS::DAX::Cluster",
    "AWS::Logs::LogStream",
    "AWS::DMS::ReplicationSubnetGroup",
    "AWS::Route53::RecordSetGroup",
    "AWS::KinesisAnalytics::ApplicationReferenceDataSource",
    "AWS::OpsWorks::App",
    "AWS::Kinesis::Stream",
    "AWS::Batch::JobDefinition",
    "AWS::IAM::SAMLProvider",
    "AWS::CloudFront::KeyGroup",
    "AWS::EC2::NetworkInterfaceAttachment",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::StepFunctions::StateMachineVersion",
    "AWS::Glue::Database",
    "AWS::Neptune::DBCluster",
    "AWS::Backup::BackupVault",
    "AWS::EC2::CustomerGateway",
    "AWS::IAM::GroupPolicy",
    "AWS::WAF::ByteMatchSet",
    "AWS::Neptune::DBClusterParameterGroup",
    "AWS::EMRServerless::Application",
    "AWS::EC2::Host",
    "AWS::AppStream::User",
    "AWS::DMS::ReplicationTask",
    "AWS::EC2::RouteTable",
    "AWS::RDS::DBProxyEndpoint",
    "AWS::DataSync::LocationSMB",
    "AWS::SecurityHub::Standard",
    "AWS::RolesAnywhere::CRL",
    "AWS::SNS::TopicInlinePolicy",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Glue::Trigger",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::SNS::TopicPolicy",
    "AWS::MWAA::Environment",
    "AWS::ElastiCache::GlobalReplicationGroup",
    "AWS::KMS::Key",
    "AWS::ServiceCatalog::AcceptedPortfolioShare",
    "AWS::Route53Resolver::FirewallRuleGroupAssociation",
    "AWS::Route53Resolver::ResolverQueryLoggingConfig",
    "AWS::EC2::Subnet",
    "AWS::S3ObjectLambda::AccessPoint",
    "AWS::WAF::Rule",
    "AWS::ElasticBeanstalk::ConfigurationTemplate",
    "AWS::SQS::QueuePolicy",
    "AWS::AppSync::ApiCache",
    "AWS::ApiGateway::Account",
    "AWS::WAFv2::WebACL",
    "AWS::EC2::TransitGatewayConnect",
    "AWS::EC2::SecurityGroup",
    "AWS::OpsWorks::Volume",
    "AWS::IAM::UserToGroupAddition",
    "AWS::Events::Rule",
    "AWS::GameLift::GameSessionQueue",
    "AWS::DataBrew::Dataset",
    "AWS::EC2::VPNGatewayRoutePropagation",
    "AWS::Glue::Crawler",
    "AWS::ApiGateway::Method",
    "AWS::WAFRegional::RegexPatternSet",
    "AWS::SSM::PatchBaseline",
    "AWS::ServiceDiscovery::Service",
    "AWS::EFS::MountTarget",
    "AWS::EC2::VPNConnection",
    "AWS::WAF::WebACL",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::IAM::User",
    "AWS::EMR::InstanceGroupConfig",
    "AWS::StepFunctions::Activity",
    "AWS::S3::BucketPolicy",
    "AWS::AppSync::GraphQLSchema",
    "AWS::IoT::CustomMetric",
    "AWS::Redshift::Cluster",
    "AWS::CodeBuild::SourceCredential",
    "AWS::EMR::InstanceFleetConfig",
    "AWS::EMR::Cluster",
    "AWS::ApiGatewayV2::DomainName",
    "AWS::RDS::DBCluster",
    "AWS::ServiceCatalog::ResourceUpdateConstraint",
    "AWS::Transfer::Agreement",
    "AWS::CloudFront::Distribution",
    "AWS::ElastiCache::SubnetGroup",
    "AWS::XRay::Group",
    "AWS::Oam::Link",
    "AWS::IoT::DomainConfiguration",
    "AWS::SageMaker::Endpoint",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Route53::CidrCollection",
    "AWS::AppConfig::HostedConfigurationVersion",
    "AWS::DataSync::LocationEFS",
    "AWS::ApiGateway::Resource",
    "AWS::SageMaker::AppImageConfig",
    "AWS::ElasticLoadBalancingV2::TargetGroup",
    "AWS::ApplicationAutoScaling::ScalingPolicy",
    "AWS::CloudFormation::Macro",
    "AWS::SageMaker::Workteam",
    "AWS::Lambda::LayerVersionPermission",
    "AWS::SecretsManager::Secret",
    "AWS::Route53Resolver::ResolverConfig",
    "AWS::ElastiCache::User",
    "AWS::Neptune::DBInstance",
    "AWS::SageMaker::Image",
    "AWS::Logs::SubscriptionFilter",
    "AWS::CodeDeploy::Application",
    "AWS::DMS::EventSubscription",
    "AWS::IoT::TopicRule",
    "AWS::LakeFormation::PrincipalPermissions",
    "AWS::DataSync::LocationS3",
    "AWS::MediaConvert::Preset",
    "AWS::AutoScaling::LifecycleHook",
    "AWS::FSx::DataRepositoryAssociation",
    "AWS::EC2::NetworkInterface",
    "AWS::SageMaker::FeatureGroup",
    "AWS::AppSync::Resolver",
    "AWS::RolesAnywhere::TrustAnchor",
    "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation",
    "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource",
    "AWS::Lambda::EventInvokeConfig",
    "AWS::Lambda::LayerVersion",
    "AWS::RDS::OptionGroup",
    "AWS::OpsWorks::UserProfile",
    "AWS::Glue::Schema",
    "AWS::DocDB::DBSubnetGroup",
    "AWS::ServiceCatalog::Portfolio",
    "AWS::IoT::Policy",
    "AWS::EC2::TransitGatewayRoute",
    "AWS::SSM::MaintenanceWindow",
    "AWS::LakeFormation::TagAssociation",
    "AWS::ImageBuilder::InfrastructureConfiguration",
    "AWS::IoT::Logging",
    "AWS::CloudFormation::WaitCondition",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::IoT::ScheduledAudit",
    "AWS::SageMaker::NotebookInstance",
    "AWS::WAFRegional::ByteMatchSet",
    "AWS::CloudWatch::AnomalyDetector",
    "AWS::EC2::SubnetNetworkAclAssociation",
    "AWS::IAM::UserPolicy",
    "AWS::IoT::MitigationAction",
    "AWS::SecretsManager::RotationSchedule",
    "AWS::Lambda::Permission",
    "AWS::EKS::IdentityProviderConfig",
    "AWS::AppSync::GraphQLApi",
    "AWS::GameLift::MatchmakingRuleSet",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::VPCCidrBlock",
    "AWS::GameLift::Script",
    "AWS::IAM::VirtualMFADevice",
    "AWS::Neptune::DBParameterGroup",
    "AWS::Athena::PreparedStatement",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::ApiGatewayV2::Route",
    "AWS::LakeFormation::Resource",
    "AWS::DirectoryService::SimpleAD",
    "AWS::CloudFront::StreamingDistribution",
    "AWS::EC2::VPCEndpoint",
    "AWS::RDS::EventSubscription",
    "AWS::Config::AggregationAuthorization",
    "AWS::DataSync::Agent",
    "AWS::AppStream::StackUserAssociation",
    "AWS::IoT::Dimension",
    "AWS::Logs::LogGroup",
    "AWS::ECS::Cluster",
    "AWS::EC2::TrafficMirrorFilterRule",
    "AWS::EC2::PlacementGroup",
    "AWS::Organizations::Account",
    "AWS::ECR::Repository",
    "AWS::IoT::FleetMetric",
    "AWS::AppStream::Fleet",
    "AWS::AppConfig::Extension",
    "AWS::ElasticLoadBalancingV2::ListenerRule",
    "AWS::Glue::Registry",
    "AWS::EC2::KeyPair",
    "AWS::FSx::FileSystem",
    "AWS::EC2::EIPAssociation",
    "AWS::ElasticBeanstalk::Application",
    "AWS::IoT::ThingPrincipalAttachment",
    "AWS::DLM::LifecyclePolicy",
    "AWS::EC2::CapacityReservation",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::Transfer::User",
    "AWS::IAM::RolePolicy",
    "AWS::EC2::TrafficMirrorTarget",
    "AWS::StepFunctions::StateMachine",
    "AWS::RDS::DBClusterParameterGroup",
    "AWS::WAF::XssMatchSet",
    "AWS::AppStream::DirectoryConfig",
    "AWS::Config::RemediationConfiguration",
    "AWS::Athena::DataCatalog",
    "AWS::DocDB::DBCluster",
    "AWS::Glue::Workflow",
    "AWS::ApiGatewayV2::Authorizer",
    "AWS::IoT::AccountAuditConfiguration",
    "AWS::SageMaker::UserProfile",
    "AWS::EC2::PrefixList",
    "AWS::EC2::Instance",
    "AWS::EC2::SubnetCidrBlock",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::WAF::SqlInjectionMatchSet",
    "AWS::EC2::TransitGatewayVpcAttachment",
    "AWS::EC2::FlowLog",
    "AWS::AmazonMQ::Broker",
    "AWS::EMR::Step",
    "AWS::SSM::Association",
    "AWS::CloudFront::ResponseHeadersPolicy",
    "AWS::SecurityHub::AutomationRule",
    "AWS::MSK::ClusterPolicy",
    "AWS::GuardDuty::Master",
    "AWS::KMS::Alias",
    "AWS::XRay::SamplingRule",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::Transfer::Connector",
    "AWS::ApiGateway::DocumentationVersion",
    "AWS::WAFv2::WebACLAssociation",
    "AWS::Oam::Sink",
    "AWS::CodeBuild::ReportGroup",
    "AWS::ApiGateway::GatewayResponse",
    "AWS::WorkSpaces::Workspace",
    "AWS::EMR::Studio",
    "AWS::DAX::ParameterGroup",
    "AWS::DirectoryService::MicrosoftAD",
    "AWS::AppSync::SourceApiAssociation",
    "AWS::DataSync::LocationObjectStorage",
    "AWS::ECS::CapacityProvider",
    "AWS::ElastiCache::CacheCluster",
    "AWS::SageMaker::ModelCard",
    "AWS::Logs::Destination",
    "AWS::EKS::Nodegroup",
    "AWS::Organizations::OrganizationalUnit",
    "AWS::AppSync::DataSource",
    "AWS::SQS::Queue",
    "AWS::EC2::SecurityGroupIngress",
    "AWS::GuardDuty::Detector",
    "AWS::IoT::ProvisioningTemplate",
    "AWS::ApiGateway::Stage",
    "AWS::Budgets::Budget",
    "AWS::Batch::ComputeEnvironment",
    "AWS::DataPipeline::Pipeline",
    "AWS::IoT::Thing",
    "AWS::Route53::HealthCheck",
    "AWS::Events::EventBusPolicy",
    "AWS::Athena::NamedQuery",
    "AWS::EC2::TrafficMirrorFilter",
    "AWS::ApiGateway::Deployment",
    "AWS::WAFRegional::Rule",
    "AWS::LakeFormation::DataLakeSettings",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::RDS::DBSecurityGroup",
    "AWS::ApiGatewayV2::RouteResponse",
    "AWS::CloudWatch::MetricStream",
    "AWS::SSM::Parameter",
    "AWS::ApiGatewayV2::ApiGatewayManagedOverrides",
    "AWS::Config::DeliveryChannel",
    "AWS::CertificateManager::Account",
    "AWS::SageMaker::MonitoringSchedule",
    "AWS::IAM::OIDCProvider",
    "AWS::LakeFormation::Tag",
    "AWS::CE::AnomalyMonitor",
    "AWS::EC2::VPNGateway",
    "AWS::CloudFormation::Stack",
    "AWS::ResourceGroups::Group",
    "AWS::CloudFormation::ResourceDefaultVersion",
    "AWS::SSM::ResourceDataSync",
    "AWS::DocDB::DBClusterParameterGroup",
    "AWS::ServiceCatalog::TagOptionAssociation",
    "AWS::DataBrew::Job",
    "AWS::EC2::TransitGatewayPeeringAttachment",
    "AWS::CloudFront::CachePolicy",
    "AWS::IAM::AccessKey",
    "AWS::RDS::DBSubnetGroup",
    "AWS::SecretsManager::SecretTargetAttachment",
    "AWS::AmazonMQ::Configuration",
    "AWS::AppConfig::Deployment",
    "AWS::CodePipeline::CustomActionType",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::EC2::EC2Fleet",
    "AWS::DMS::ReplicationInstance",
    "AWS::DAX::SubnetGroup",
    "AWS::ServiceCatalog::CloudFormationProduct",
    "AWS::EC2::VPCEndpointService",
    "AWS::IAM::ManagedPolicy",
    "AWS::EC2::LaunchTemplate",
    "AWS::CloudFront::OriginRequestPolicy",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::WAFRegional::SqlInjectionMatchSet",
    "AWS::Lambda::Version",
    "AWS::EC2::DHCPOptions",
    "AWS::Kinesis::StreamConsumer",
    "AWS::IAM::ServiceLinkedRole",
    "AWS::EC2::Volume",
    "AWS::IoT::Certificate",
    "AWS::EC2::EIP",
    "AWS::CloudFormation::ResourceVersion",
    "AWS::ApiGatewayV2::Stage",
    "AWS::RDS::DBProxy",
    "AWS::RDS::DBParameterGroup",
    "AWS::SecurityHub::Hub",
    "AWS::S3::AccessPoint",
    "AWS::EC2::TrafficMirrorSession",
    "AWS::Batch::JobQueue",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::CloudFormation::WaitConditionHandle",
    "AWS::EKS::Addon",
]

# pylint: disable=too-many-lines
cached: List[str] = [
    "aws-apigatewayv2-integration.json",
    "aws-apigatewayv2-apimapping.json",
    "aws-ce-anomalysubscription.json",
    "aws-glue-partition.json",
    "aws-ec2-transitgatewayroutetablepropagation.json",
    "aws-guardduty-filter.json",
    "aws-ecs-service.json",
    "aws-ram-resourceshare.json",
    "aws-dynamodb-table.json",
    "aws-ec2-securitygroupegress.json",
    "aws-config-organizationconfigrule.json",
    "aws-config-configurationrecorder.json",
    "aws-appconfig-extensionassociation.json",
    "aws-iot-topicruledestination.json",
    "aws-rds-dbinstance.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-apigateway-model.json",
    "aws-apigatewayv2-integrationresponse.json",
    "aws-ec2-networkacl.json",
    "aws-lambda-eventsourcemapping.json",
    "aws-budgets-budgetsaction.json",
    "aws-logs-resourcepolicy.json",
    "aws-servicecatalog-launchnotificationconstraint.json",
    "aws-iot-cacertificate.json",
    "aws-transfer-certificate.json",
    "aws-apigateway-documentationpart.json",
    "aws-cloudwatch-compositealarm.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-appconfig-application.json",
    "aws-opsworks-stack.json",
    "aws-datasync-locationfsxwindows.json",
    "aws-gamelift-build.json",
    "aws-apigateway-requestvalidator.json",
    "aws-autoscaling-warmpool.json",
    "aws-applicationautoscaling-scalabletarget.json",
    "aws-apigatewayv2-model.json",
    "aws-neptune-dbsubnetgroup.json",
    "aws-cassandra-keyspace.json",
    "aws-apigateway-domainname.json",
    "aws-ecs-primarytaskset.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-ec2-transitgatewayroutetable.json",
    "aws-route53-recordset.json",
    "aws-elasticache-securitygroup.json",
    "aws-opsworks-layer.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-mediaconvert-queue.json",
    "aws-sagemaker-coderepository.json",
    "aws-glue-connection.json",
    "aws-iam-group.json",
    "aws-wafregional-webaclassociation.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-transfer-profile.json",
    "aws-databrew-recipe.json",
    "aws-gamelift-alias.json",
    "aws-fms-policy.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-sagemaker-pipeline.json",
    "aws-docdb-dbinstance.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-datasync-locationhdfs.json",
    "aws-events-archive.json",
    "aws-msk-cluster.json",
    "aws-ec2-vpcendpointconnectionnotification.json",
    "aws-codepipeline-pipeline.json",
    "aws-opsworks-instance.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-cloudformation-moduleversion.json",
    "aws-cloud9-environmentec2.json",
    "aws-route53resolver-resolverruleassociation.json",
    "aws-synthetics-canary.json",
    "aws-sns-subscription.json",
    "aws-ec2-natgateway.json",
    "aws-transfer-workflow.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-glue-devendpoint.json",
    "aws-sagemaker-modelpackage.json",
    "aws-elasticache-usergroup.json",
    "aws-iot-thinggroup.json",
    "aws-apigateway-restapi.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-mediaconvert-jobtemplate.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-elasticache-replicationgroup.json",
    "aws-stepfunctions-statemachinealias.json",
    "aws-cassandra-table.json",
    "aws-rds-globalcluster.json",
    "aws-cloudformation-moduledefaultversion.json",
    "aws-ce-costcategory.json",
    "aws-servicecatalog-cloudformationprovisionedproduct.json",
    "aws-lambda-function.json",
    "aws-sns-topic.json",
    "aws-backup-backupselection.json",
    "aws-datasync-locationfsxlustre.json",
    "aws-ec2-vpcgatewayattachment.json",
    "aws-gamelift-gameservergroup.json",
    "aws-ec2-internetgateway.json",
    "aws-ssm-document.json",
    "aws-iam-role.json",
    "aws-dms-endpoint.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-sagemaker-endpointconfig.json",
    "aws-apigateway-apikey.json",
    "aws-autoscaling-launchconfiguration.json",
    "aws-apigateway-clientcertificate.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-lambda-alias.json",
    "aws-waf-ipset.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-waf-sizeconstraintset.json",
    "aws-ec2-transitgatewayroutetableassociation.json",
    "aws-appconfig-environment.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-wafregional-xssmatchset.json",
    "aws-rds-dbproxytargetgroup.json",
    "aws-cloudwatch-dashboard.json",
    "aws-cloudwatch-alarm.json",
    "aws-iot-thingtype.json",
    "aws-guardduty-member.json",
    "aws-cloudformation-customresource.json",
    "aws-kinesisanalytics-applicationoutput.json",
    "aws-elasticache-parametergroup.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-cloudformation-stackset.json",
    "aws-ec2-route.json",
    "aws-codecommit-repository.json",
    "aws-rolesanywhere-profile.json",
    "aws-xray-resourcepolicy.json",
    "aws-iot-resourcespecificlogging.json",
    "aws-servicecatalog-launchtemplateconstraint.json",
    "aws-wafv2-loggingconfiguration.json",
    "aws-dynamodb-globaltable.json",
    "aws-backup-backupplan.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-lakeformation-permissions.json",
    "aws-cloudfront-publickey.json",
    "aws-ram-permission.json",
    "aws-datasync-task.json",
    "aws-ecs-taskdefinition.json",
    "aws-sagemaker-model.json",
    "aws-appsync-functionconfiguration.json",
    "aws-ec2-spotfleet.json",
    "aws-glue-schemaversion.json",
    "aws-iot-policyprincipalattachment.json",
    "aws-msk-batchscramsecret.json",
    "aws-dms-certificate.json",
    "aws-guardduty-ipset.json",
    "aws-servicediscovery-httpnamespace.json",
    "aws-emr-securityconfiguration.json",
    "aws-cloudwatch-insightrule.json",
    "aws-batch-schedulingpolicy.json",
    "aws-iot-authorizer.json",
    "aws-apigatewayv2-vpclink.json",
    "aws-iot-jobtemplate.json",
    "aws-databrew-project.json",
    "aws-athena-workgroup.json",
    "aws-sagemaker-imageversion.json",
    "aws-apigatewayv2-api.json",
    "aws-cur-reportdefinition.json",
    "aws-servicecatalog-portfolioshare.json",
    "aws-iam-servercertificate.json",
    "aws-iot-securityprofile.json",
    "aws-events-eventbus.json",
    "aws-sqs-queueinlinepolicy.json",
    "aws-organizations-organization.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-databrew-schedule.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-appstream-stackfleetassociation.json",
    "aws-ec2-transitgatewaymulticastgroupmember.json",
    "aws-ec2-volumeattachment.json",
    "aws-glue-securityconfiguration.json",
    "aws-databrew-ruleset.json",
    "aws-gamelift-matchmakingconfiguration.json",
    "aws-applicationinsights-application.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-appconfig-configurationprofile.json",
    "aws-route53resolver-firewallrulegroup.json",
    "aws-msk-configuration.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-eks-cluster.json",
    "aws-codebuild-project.json",
    "aws-efs-filesystem.json",
    "aws-logs-querydefinition.json",
    "aws-iam-instanceprofile.json",
    "aws-iot-billinggroup.json",
    "aws-datasync-locationnfs.json",
    "aws-kinesisanalyticsv2-applicationoutput.json",
    "aws-certificatemanager-certificate.json",
    "aws-glue-schemaversionmetadata.json",
    "aws-sdb-domain.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-sagemaker-notebookinstancelifecycleconfig.json",
    "aws-efs-accesspoint.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-opensearchservice-domain.json",
    "aws-servicediscovery-instance.json",
    "aws-elasticsearch-domain.json",
    "aws-apigatewayv2-deployment.json",
    "aws-servicecatalog-stacksetconstraint.json",
    "aws-ec2-networkinterfacepermission.json",
    "aws-servicecatalog-tagoption.json",
    "aws-servicediscovery-privatednsnamespace.json",
    "aws-servicecatalog-launchroleconstraint.json",
    "aws-iot-rolealias.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-ecs-taskset.json",
    "aws-appsync-apikey.json",
    "aws-guardduty-threatintelset.json",
    "aws-ec2-vpc.json",
    "aws-msk-vpcconnection.json",
    "aws-dax-cluster.json",
    "aws-logs-logstream.json",
    "aws-dms-replicationsubnetgroup.json",
    "aws-route53-recordsetgroup.json",
    "aws-opsworks-app.json",
    "aws-batch-jobdefinition.json",
    "aws-iam-samlprovider.json",
    "aws-cloudfront-keygroup.json",
    "aws-ec2-networkinterfaceattachment.json",
    "aws-ec2-transitgatewayattachment.json",
    "aws-stepfunctions-statemachineversion.json",
    "aws-neptune-dbcluster.json",
    "aws-backup-backupvault.json",
    "aws-iam-grouppolicy.json",
    "aws-waf-bytematchset.json",
    "aws-emrserverless-application.json",
    "aws-ec2-host.json",
    "aws-dms-replicationtask.json",
    "aws-ec2-routetable.json",
    "aws-rds-dbproxyendpoint.json",
    "aws-datasync-locationsmb.json",
    "aws-securityhub-standard.json",
    "aws-rolesanywhere-crl.json",
    "aws-sns-topicinlinepolicy.json",
    "aws-glue-trigger.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-sns-topicpolicy.json",
    "aws-mwaa-environment.json",
    "aws-elasticache-globalreplicationgroup.json",
    "aws-kms-key.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-ec2-subnet.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-waf-rule.json",
    "aws-elasticbeanstalk-configurationtemplate.json",
    "aws-sqs-queuepolicy.json",
    "aws-appsync-apicache.json",
    "aws-apigateway-account.json",
    "aws-ec2-transitgatewayconnect.json",
    "aws-ec2-securitygroup.json",
    "aws-opsworks-volume.json",
    "aws-iam-usertogroupaddition.json",
    "aws-events-rule.json",
    "aws-gamelift-gamesessionqueue.json",
    "aws-databrew-dataset.json",
    "aws-ec2-vpngatewayroutepropagation.json",
    "aws-wafregional-regexpatternset.json",
    "aws-ssm-patchbaseline.json",
    "aws-servicediscovery-service.json",
    "aws-waf-webacl.json",
    "aws-servicediscovery-publicdnsnamespace.json",
    "aws-iam-user.json",
    "aws-emr-instancegroupconfig.json",
    "aws-s3-bucketpolicy.json",
    "aws-appsync-graphqlschema.json",
    "aws-iot-custommetric.json",
    "aws-codebuild-sourcecredential.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-cluster.json",
    "aws-apigatewayv2-domainname.json",
    "aws-rds-dbcluster.json",
    "aws-servicecatalog-resourceupdateconstraint.json",
    "aws-transfer-agreement.json",
    "aws-cloudfront-distribution.json",
    "aws-elasticache-subnetgroup.json",
    "aws-xray-group.json",
    "aws-oam-link.json",
    "aws-iot-domainconfiguration.json",
    "aws-sagemaker-endpoint.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-route53-cidrcollection.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-datasync-locationefs.json",
    "aws-apigateway-resource.json",
    "aws-sagemaker-appimageconfig.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-applicationautoscaling-scalingpolicy.json",
    "aws-cloudformation-macro.json",
    "aws-sagemaker-workteam.json",
    "aws-secretsmanager-secret.json",
    "aws-route53resolver-resolverconfig.json",
    "aws-elasticache-user.json",
    "aws-sagemaker-image.json",
    "aws-dms-eventsubscription.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-datasync-locations3.json",
    "aws-mediaconvert-preset.json",
    "aws-autoscaling-lifecyclehook.json",
    "aws-fsx-datarepositoryassociation.json",
    "aws-ec2-networkinterface.json",
    "aws-sagemaker-featuregroup.json",
    "aws-appsync-resolver.json",
    "aws-rolesanywhere-trustanchor.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-lambda-eventinvokeconfig.json",
    "aws-lambda-layerversion.json",
    "aws-rds-optiongroup.json",
    "aws-opsworks-userprofile.json",
    "aws-glue-schema.json",
    "aws-docdb-dbsubnetgroup.json",
    "aws-iot-policy.json",
    "aws-ssm-maintenancewindow.json",
    "aws-lakeformation-tagassociation.json",
    "aws-iot-logging.json",
    "aws-cloudformation-waitcondition.json",
    "aws-route53resolver-resolverendpoint.json",
    "aws-iot-scheduledaudit.json",
    "aws-sagemaker-notebookinstance.json",
    "aws-wafregional-bytematchset.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-ec2-subnetnetworkaclassociation.json",
    "aws-iam-userpolicy.json",
    "aws-iot-mitigationaction.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-lambda-permission.json",
    "aws-eks-identityproviderconfig.json",
    "aws-appsync-graphqlapi.json",
    "aws-gamelift-matchmakingruleset.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-ec2-vpccidrblock.json",
    "aws-gamelift-script.json",
    "aws-iam-virtualmfadevice.json",
    "aws-athena-preparedstatement.json",
    "aws-autoscaling-scheduledaction.json",
    "aws-apigatewayv2-route.json",
    "aws-lakeformation-resource.json",
    "aws-ec2-vpcendpoint.json",
    "aws-rds-eventsubscription.json",
    "aws-datasync-agent.json",
    "aws-iot-dimension.json",
    "aws-ec2-placementgroup.json",
    "aws-organizations-account.json",
    "aws-ecr-repository.json",
    "aws-iot-fleetmetric.json",
    "aws-appconfig-extension.json",
    "aws-glue-registry.json",
    "aws-ec2-keypair.json",
    "aws-fsx-filesystem.json",
    "aws-ec2-eipassociation.json",
    "aws-elasticbeanstalk-application.json",
    "aws-iot-thingprincipalattachment.json",
    "aws-dlm-lifecyclepolicy.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-transfer-user.json",
    "aws-iam-rolepolicy.json",
    "aws-ec2-trafficmirrortarget.json",
    "aws-stepfunctions-statemachine.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-waf-xssmatchset.json",
    "aws-config-remediationconfiguration.json",
    "aws-athena-datacatalog.json",
    "aws-docdb-dbcluster.json",
    "aws-glue-workflow.json",
    "aws-apigatewayv2-authorizer.json",
    "aws-iot-accountauditconfiguration.json",
    "aws-ec2-prefixlist.json",
    "aws-ec2-instance.json",
    "aws-ec2-subnetcidrblock.json",
    "aws-elasticbeanstalk-applicationversion.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-ec2-flowlog.json",
    "aws-amazonmq-broker.json",
    "aws-emr-step.json",
    "aws-ssm-association.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-securityhub-automationrule.json",
    "aws-msk-clusterpolicy.json",
    "aws-kms-alias.json",
    "aws-xray-samplingrule.json",
    "aws-route53resolver-resolverrule.json",
    "aws-transfer-connector.json",
    "aws-wafv2-webaclassociation.json",
    "aws-oam-sink.json",
    "aws-codebuild-reportgroup.json",
    "aws-apigateway-gatewayresponse.json",
    "aws-workspaces-workspace.json",
    "aws-emr-studio.json",
    "aws-dax-parametergroup.json",
    "aws-directoryservice-microsoftad.json",
    "aws-appsync-sourceapiassociation.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-ecs-capacityprovider.json",
    "aws-elasticache-cachecluster.json",
    "aws-sagemaker-modelcard.json",
    "aws-eks-nodegroup.json",
    "aws-organizations-organizationalunit.json",
    "aws-appsync-datasource.json",
    "aws-sqs-queue.json",
    "aws-ec2-securitygroupingress.json",
    "aws-guardduty-detector.json",
    "aws-iot-provisioningtemplate.json",
    "aws-budgets-budget.json",
    "aws-batch-computeenvironment.json",
    "aws-iot-thing.json",
    "aws-events-eventbuspolicy.json",
    "aws-ec2-trafficmirrorfilter.json",
    "aws-apigateway-deployment.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-autoscaling-scalingpolicy.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-apigatewayv2-routeresponse.json",
    "aws-cloudwatch-metricstream.json",
    "aws-ssm-parameter.json",
    "aws-apigatewayv2-apigatewaymanagedoverrides.json",
    "aws-config-deliverychannel.json",
    "aws-certificatemanager-account.json",
    "aws-sagemaker-monitoringschedule.json",
    "aws-iam-oidcprovider.json",
    "aws-lakeformation-tag.json",
    "aws-ce-anomalymonitor.json",
    "aws-cloudformation-stack.json",
    "aws-resourcegroups-group.json",
    "aws-cloudformation-resourcedefaultversion.json",
    "aws-databrew-job.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-iam-accesskey.json",
    "aws-rds-dbsubnetgroup.json",
    "aws-amazonmq-configuration.json",
    "aws-appconfig-deployment.json",
    "aws-codepipeline-customactiontype.json",
    "aws-accessanalyzer-analyzer.json",
    "aws-ec2-ec2fleet.json",
    "aws-dms-replicationinstance.json",
    "aws-dax-subnetgroup.json",
    "aws-servicecatalog-cloudformationproduct.json",
    "aws-iam-managedpolicy.json",
    "aws-ec2-launchtemplate.json",
    "aws-elasticbeanstalk-environment.json",
    "aws-wafregional-sqlinjectionmatchset.json",
    "aws-lambda-version.json",
    "aws-ec2-dhcpoptions.json",
    "aws-kinesis-streamconsumer.json",
    "aws-iam-servicelinkedrole.json",
    "aws-ec2-volume.json",
    "aws-iot-certificate.json",
    "aws-apigatewayv2-stage.json",
    "aws-rds-dbproxy.json",
    "aws-rds-dbparametergroup.json",
    "aws-securityhub-hub.json",
    "aws-s3-accesspoint.json",
    "aws-batch-jobqueue.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-eks-addon.json",
]
