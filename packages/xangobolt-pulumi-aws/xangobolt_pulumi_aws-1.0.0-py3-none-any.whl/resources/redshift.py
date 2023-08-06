from arpeggio.cleanpeg import NOT, prefix
from pulumi.resource import ResourceOptions
import pulumi_aws.redshift as redshift
import pulumi_aws_native.redshift as redshift_native

def Cluster(stem, props, provider=None, parent=None, depends_on=None):
    rs_cluster = redshift.Cluster(
        f'redshift-{stem}',
        cluster_identifier=f'redshift-{stem}',
        cluster_type="multi-node",
        node_type="dc2.large",
        master_username="set_uname",
        master_password="Testing123",
        skip_final_snapshot="True",
        tags=props.base_tags,
        opts=ResourceOptions(provider=provider, parent=parent, depends_on=depends_on)
    )
    return rs_cluster