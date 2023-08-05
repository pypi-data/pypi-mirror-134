'''
# Route53 Alias Record Targets for the CDK Route53 Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library contains Route53 Alias Record targets for:

* API Gateway custom domains

  ```python
  import aws_cdk.aws_apigateway as apigw

  # zone is of type HostedZone
  # rest_api is of type LambdaRestApi


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.ApiGateway(rest_api))
  )
  ```
* API Gateway V2 custom domains

  ```python
  import aws_cdk.aws_apigatewayv2 as apigwv2

  # zone is of type HostedZone
  # domain_name is of type DomainName


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.ApiGatewayv2DomainProperties(domain_name.regional_domain_name, domain_name.regional_hosted_zone_id))
  )
  ```
* CloudFront distributions

  ```python
  import aws_cdk.aws_cloudfront as cloudfront

  # zone is of type HostedZone
  # distribution is of type CloudFrontWebDistribution


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(distribution))
  )
  ```
* ELBv2 load balancers

  ```python
  import aws_cdk.aws_elasticloadbalancingv2 as elbv2

  # zone is of type HostedZone
  # lb is of type ApplicationLoadBalancer


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(lb))
  )
  ```
* Classic load balancers

  ```python
  import aws_cdk.aws_elasticloadbalancing as elb

  # zone is of type HostedZone
  # lb is of type LoadBalancer


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.ClassicLoadBalancerTarget(lb))
  )
  ```

**Important:** Based on [AWS documentation](https://aws.amazon.com/de/premiumsupport/knowledge-center/alias-resource-record-set-route53-cli/), all alias record in Route 53 that points to a Elastic Load Balancer will always include *dualstack* for the DNSName to resolve IPv4/IPv6 addresses (without *dualstack* IPv6 will not resolve).

For example, if the Amazon-provided DNS for the load balancer is `ALB-xxxxxxx.us-west-2.elb.amazonaws.com`, CDK will create alias target in Route 53 will be `dualstack.ALB-xxxxxxx.us-west-2.elb.amazonaws.com`.

* GlobalAccelerator

  ```python
  import aws_cdk.aws_globalaccelerator as globalaccelerator

  # zone is of type HostedZone
  # accelerator is of type Accelerator


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.GlobalAcceleratorTarget(accelerator))
  )
  ```

**Important:** If you use GlobalAcceleratorDomainTarget, passing a string rather than an instance of IAccelerator, ensure that the string is a valid domain name of an existing Global Accelerator instance.
See [the documentation on DNS addressing](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html) with Global Accelerator for more info.

* InterfaceVpcEndpoints

**Important:** Based on the CFN docs for VPCEndpoints - [see here](attrDnsEntries) - the attributes returned for DnsEntries in CloudFormation is a combination of the hosted zone ID and the DNS name. The entries are ordered as follows: regional public DNS, zonal public DNS, private DNS, and wildcard DNS. This order is not enforced for AWS Marketplace services, and therefore this CDK construct is ONLY guaranteed to work with non-marketplace services.

```python
import aws_cdk.aws_ec2 as ec2

# zone is of type HostedZone
# interface_vpc_endpoint is of type InterfaceVpcEndpoint


route53.ARecord(self, "AliasRecord",
    zone=zone,
    target=route53.RecordTarget.from_alias(targets.InterfaceVpcEndpointTarget(interface_vpc_endpoint))
)
```

* S3 Bucket Website:

**Important:** The Bucket name must strictly match the full DNS name.
See [the Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html) for more info.

```python
import aws_cdk.aws_s3 as s3


record_name = "www"
domain_name = "example.com"

bucket_website = s3.Bucket(self, "BucketWebsite",
    bucket_name=[record_name, domain_name].join("."),  # www.example.com
    public_read_access=True,
    website_index_document="index.html"
)

zone = route53.HostedZone.from_lookup(self, "Zone", domain_name=domain_name) # example.com

route53.ARecord(self, "AliasRecord",
    zone=zone,
    record_name=record_name,  # www
    target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket_website))
)
```

* User pool domain

  ```python
  import aws_cdk.aws_cognito as cognito

  # zone is of type HostedZone
  # domain is of type UserPoolDomain

  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.UserPoolDomainTarget(domain))
  )
  ```
* Route 53 record

  ```python
  # zone is of type HostedZone
  # record is of type ARecord

  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.Route53RecordTarget(record))
  )
  ```
* Elastic Beanstalk environment:

**Important:** Only supports Elastic Beanstalk environments created after 2016 that have a regional endpoint.

```python
# zone is of type HostedZone
# ebs_environment_url is of type string


route53.ARecord(self, "AliasRecord",
    zone=zone,
    target=route53.RecordTarget.from_alias(targets.ElasticBeanstalkEnvironmentEndpointTarget(ebs_environment_url))
)
```

See the documentation of `@aws-cdk/aws-route53` for more information.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_apigateway
import aws_cdk.aws_cloudfront
import aws_cdk.aws_cognito
import aws_cdk.aws_ec2
import aws_cdk.aws_elasticloadbalancing
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_globalaccelerator
import aws_cdk.aws_route53
import aws_cdk.aws_s3
import aws_cdk.core


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class ApiGatewayDomain(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.ApiGatewayDomain",
):
    '''Defines an API Gateway domain name as the alias target.

    Use the ``ApiGateway`` class if you wish to map the alias to an REST API with a
    domain name defined through the ``RestApiProps.domainName`` prop.

    :exampleMetadata: infused

    Example::

        # hosted_zone_for_example_com is of type object
        # domain_name is of type DomainName
        
        import aws_cdk.aws_route53 as route53
        import aws_cdk.aws_route53_targets as targets
        
        
        route53.ARecord(self, "CustomDomainAliasRecord",
            zone=hosted_zone_for_example_com,
            target=route53.RecordTarget.from_alias(targets.ApiGatewayDomain(domain_name))
        )
    '''

    def __init__(self, domain_name: aws_cdk.aws_apigateway.IDomainName) -> None:
        '''
        :param domain_name: -
        '''
        jsii.create(self.__class__, self, [domain_name])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class ApiGatewayv2DomainProperties(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.ApiGatewayv2DomainProperties",
):
    '''Defines an API Gateway V2 domain name as the alias target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_apigatewayv2 as apigwv2
        
        # zone is of type HostedZone
        # domain_name is of type DomainName
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ApiGatewayv2DomainProperties(domain_name.regional_domain_name, domain_name.regional_hosted_zone_id))
        )
    '''

    def __init__(
        self,
        regional_domain_name: builtins.str,
        regional_hosted_zone_id: builtins.str,
    ) -> None:
        '''
        :param regional_domain_name: the domain name associated with the regional endpoint for this custom domain name.
        :param regional_hosted_zone_id: the region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint.
        '''
        jsii.create(self.__class__, self, [regional_domain_name, regional_hosted_zone_id])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class BucketWebsiteTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.BucketWebsiteTarget",
):
    '''Use a S3 as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        
        
        record_name = "www"
        domain_name = "example.com"
        
        bucket_website = s3.Bucket(self, "BucketWebsite",
            bucket_name=[record_name, domain_name].join("."),  # www.example.com
            public_read_access=True,
            website_index_document="index.html"
        )
        
        zone = route53.HostedZone.from_lookup(self, "Zone", domain_name=domain_name) # example.com
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            record_name=record_name,  # www
            target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket_website))
        )
    '''

    def __init__(self, bucket: aws_cdk.aws_s3.IBucket) -> None:
        '''
        :param bucket: -
        '''
        jsii.create(self.__class__, self, [bucket])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class ClassicLoadBalancerTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.ClassicLoadBalancerTarget",
):
    '''Use a classic ELB as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancing as elb
        
        # zone is of type HostedZone
        # lb is of type LoadBalancer
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ClassicLoadBalancerTarget(lb))
        )
    '''

    def __init__(
        self,
        load_balancer: aws_cdk.aws_elasticloadbalancing.LoadBalancer,
    ) -> None:
        '''
        :param load_balancer: -
        '''
        jsii.create(self.__class__, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class CloudFrontTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.CloudFrontTarget",
):
    '''Use a CloudFront Distribution as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudfront as cloudfront
        
        # my_zone is of type HostedZone
        # distribution is of type CloudFrontWebDistribution
        
        route53.AaaaRecord(self, "Alias",
            zone=my_zone,
            target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(distribution))
        )
    '''

    def __init__(self, distribution: aws_cdk.aws_cloudfront.IDistribution) -> None:
        '''
        :param distribution: -
        '''
        jsii.create(self.__class__, self, [distribution])

    @jsii.member(jsii_name="getHostedZoneId") # type: ignore[misc]
    @builtins.classmethod
    def get_hosted_zone_id(cls, scope: aws_cdk.core.IConstruct) -> builtins.str:
        '''Get the hosted zone id for the current scope.

        :param scope: - scope in which this resource is defined.
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getHostedZoneId", [scope]))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CLOUDFRONT_ZONE_ID")
    def CLOUDFRONT_ZONE_ID(cls) -> builtins.str:
        '''The hosted zone Id if using an alias record in Route53.

        This value never changes.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ZONE_ID"))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class ElasticBeanstalkEnvironmentEndpointTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.ElasticBeanstalkEnvironmentEndpointTarget",
):
    '''Use an Elastic Beanstalk environment URL as an alias record target. E.g. mysampleenvironment.xyz.us-east-1.elasticbeanstalk.com.

    Only supports Elastic Beanstalk environments created after 2016 that have a regional endpoint.

    :exampleMetadata: infused

    Example::

        # zone is of type HostedZone
        # ebs_environment_url is of type string
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ElasticBeanstalkEnvironmentEndpointTarget(ebs_environment_url))
        )
    '''

    def __init__(self, environment_endpoint: builtins.str) -> None:
        '''
        :param environment_endpoint: -
        '''
        jsii.create(self.__class__, self, [environment_endpoint])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class GlobalAcceleratorDomainTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.GlobalAcceleratorDomainTarget",
):
    '''Use a Global Accelerator domain name as an alias record target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_route53_targets as route53_targets
        
        global_accelerator_domain_target = route53_targets.GlobalAcceleratorDomainTarget("acceleratorDomainName")
    '''

    def __init__(self, accelerator_domain_name: builtins.str) -> None:
        '''Create an Alias Target for a Global Accelerator domain name.

        :param accelerator_domain_name: -
        '''
        jsii.create(self.__class__, self, [accelerator_domain_name])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GLOBAL_ACCELERATOR_ZONE_ID")
    def GLOBAL_ACCELERATOR_ZONE_ID(cls) -> builtins.str:
        '''The hosted zone Id if using an alias record in Route53.

        This value never changes.
        Ref: https://docs.aws.amazon.com/general/latest/gr/global_accelerator.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GLOBAL_ACCELERATOR_ZONE_ID"))


class GlobalAcceleratorTarget(
    GlobalAcceleratorDomainTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.GlobalAcceleratorTarget",
):
    '''Use a Global Accelerator instance domain name as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_globalaccelerator as globalaccelerator
        
        # zone is of type HostedZone
        # accelerator is of type Accelerator
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.GlobalAcceleratorTarget(accelerator))
        )
    '''

    def __init__(self, accelerator: aws_cdk.aws_globalaccelerator.IAccelerator) -> None:
        '''Create an Alias Target for a Global Accelerator instance.

        :param accelerator: -
        '''
        jsii.create(self.__class__, self, [accelerator])


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class InterfaceVpcEndpointTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.InterfaceVpcEndpointTarget",
):
    '''Set an InterfaceVpcEndpoint as a target for an ARecord.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ec2 as ec2
        
        # zone is of type HostedZone
        # interface_vpc_endpoint is of type InterfaceVpcEndpoint
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.InterfaceVpcEndpointTarget(interface_vpc_endpoint))
        )
    '''

    def __init__(self, vpc_endpoint: aws_cdk.aws_ec2.IInterfaceVpcEndpoint) -> None:
        '''
        :param vpc_endpoint: -
        '''
        jsii.create(self.__class__, self, [vpc_endpoint])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class LoadBalancerTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.LoadBalancerTarget",
):
    '''Use an ELBv2 as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancingv2 as elbv2
        
        # zone is of type HostedZone
        # lb is of type ApplicationLoadBalancer
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(lb))
        )
    '''

    def __init__(
        self,
        load_balancer: aws_cdk.aws_elasticloadbalancingv2.ILoadBalancerV2,
    ) -> None:
        '''
        :param load_balancer: -
        '''
        jsii.create(self.__class__, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class Route53RecordTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.Route53RecordTarget",
):
    '''Use another Route 53 record as an alias record target.

    :exampleMetadata: infused

    Example::

        # zone is of type HostedZone
        # record is of type ARecord
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.Route53RecordTarget(record))
        )
    '''

    def __init__(self, record: aws_cdk.aws_route53.IRecordSet) -> None:
        '''
        :param record: -
        '''
        jsii.create(self.__class__, self, [record])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, zone]))


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class UserPoolDomainTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.UserPoolDomainTarget",
):
    '''Use a user pool domain as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cognito as cognito
        
        # zone is of type HostedZone
        # domain is of type UserPoolDomain
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.UserPoolDomainTarget(domain))
        )
    '''

    def __init__(self, domain: aws_cdk.aws_cognito.UserPoolDomain) -> None:
        '''
        :param domain: -
        '''
        jsii.create(self.__class__, self, [domain])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


class ApiGateway(
    ApiGatewayDomain,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53-targets.ApiGateway",
):
    '''Defines an API Gateway REST API as the alias target. Requires that the domain name will be defined through ``RestApiProps.domainName``.

    You can direct the alias to any ``apigateway.DomainName`` resource through the
    ``ApiGatewayDomain`` class.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_route53 as route53
        import aws_cdk.aws_route53_targets as targets
        
        # api is of type RestApi
        # hosted_zone_for_example_com is of type object
        
        
        route53.ARecord(self, "CustomDomainAliasRecord",
            zone=hosted_zone_for_example_com,
            target=route53.RecordTarget.from_alias(targets.ApiGateway(api))
        )
    '''

    def __init__(self, api: aws_cdk.aws_apigateway.RestApiBase) -> None:
        '''
        :param api: -
        '''
        jsii.create(self.__class__, self, [api])


__all__ = [
    "ApiGateway",
    "ApiGatewayDomain",
    "ApiGatewayv2DomainProperties",
    "BucketWebsiteTarget",
    "ClassicLoadBalancerTarget",
    "CloudFrontTarget",
    "ElasticBeanstalkEnvironmentEndpointTarget",
    "GlobalAcceleratorDomainTarget",
    "GlobalAcceleratorTarget",
    "InterfaceVpcEndpointTarget",
    "LoadBalancerTarget",
    "Route53RecordTarget",
    "UserPoolDomainTarget",
]

publication.publish()
