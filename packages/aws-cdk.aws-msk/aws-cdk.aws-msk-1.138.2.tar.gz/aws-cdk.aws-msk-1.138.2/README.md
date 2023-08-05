# Amazon Managed Streaming for Apache Kafka Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

[Amazon MSK](https://aws.amazon.com/msk/) is a fully managed service that makes it easy for you to build and run applications that use Apache Kafka to process streaming data.

The following example creates an MSK Cluster.

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_msk as msk

cluster = Cluster(self, "Cluster",
    kafka_version=msk.KafkaVersion.V2_8_1,
    vpc=vpc
)
```

## Allowing Connections

To control who can access the Cluster, use the `.connections` attribute. For a list of ports used by MSK, refer to the [MSK documentation](https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html#port-info).

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_msk as msk
import aws_cdk.aws_ec2 as ec2

cluster = msk.Cluster(self, "Cluster", ...)

cluster.connections.allow_from(
    ec2.Peer.ipv4("1.2.3.4/8"),
    ec2.Port.tcp(2181))
cluster.connections.allow_from(
    ec2.Peer.ipv4("1.2.3.4/8"),
    ec2.Port.tcp(9094))
```

## Cluster Endpoints

You can use the following attributes to get a list of the Kafka broker or ZooKeeper node endpoints

```python
# Example automatically generated from non-compiling source. May contain errors.
cdk.CfnOutput(self, "BootstrapBrokers", value=cluster.bootstrap_brokers)
cdk.CfnOutput(self, "BootstrapBrokersTls", value=cluster.bootstrap_brokers_tls)
cdk.CfnOutput(self, "BootstrapBrokersSaslScram", value=cluster.bootstrap_brokers_sasl_scram)
cdk.CfnOutput(self, "ZookeeperConnection", value=cluster.zookeeper_connection_string)
cdk.CfnOutput(self, "ZookeeperConnectionTls", value=cluster.zookeeper_connection_string_tls)
```

## Importing an existing Cluster

To import an existing MSK cluster into your CDK app use the `.fromClusterArn()` method.

```python
# Example automatically generated from non-compiling source. May contain errors.
cluster = msk.Cluster.from_cluster_arn(self, "Cluster", "arn:aws:kafka:us-west-2:1234567890:cluster/a-cluster/11111111-1111-1111-1111-111111111111-1")
```

## Client Authentication

[MSK supports](https://docs.aws.amazon.com/msk/latest/developerguide/kafka_apis_iam.html) the following authentication mechanisms.

> Only one authentication method can be enabled.

### TLS

To enable client authentication with TLS set the `certificateAuthorityArns` property to reference your ACM Private CA. [More info on Private CAs.](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html)

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_msk as msk
import aws_cdk.aws_acmpca as acmpca

cluster = msk.Cluster(self, "Cluster", msk.ClusterProps(
    (SpreadAssignment ...
        encryptionInTransit
      encryption_in_transit)
), {
    "client_broker": msk.ClientBrokerEncryption.TLS
}, client_authentication, msk.ClientAuthentication.tls(
    certificate_authorities=[
        acmpca.CertificateAuthority.from_certificate_authority_arn(stack, "CertificateAuthority", "arn:aws:acm-pca:us-west-2:1234567890:certificate-authority/11111111-1111-1111-1111-111111111111")
    ]
))
```

### SASL/SCRAM

Enable client authentication with [SASL/SCRAM](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html):

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_msk as msk

cluster = msk.cluster(self, "cluster", {
    (SpreadAssignment ...
      encryptionInTransit
      encryption_in_transit)
}, {
    "client_broker": msk.ClientBrokerEncryption.TLS
}, client_authentication, msk.ClientAuthentication.sasl(
    scram=True
))
```

### SASL/IAM

Enable client authentication with [IAM](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html):

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_msk as msk

cluster = msk.cluster(self, "cluster", {
    (SpreadAssignment ...
      encryptionInTransit
      encryption_in_transit)
}, {
    "client_broker": msk.ClientBrokerEncryption.TLS
}, client_authentication, msk.ClientAuthentication.sasl(
    iam=True
))
```
