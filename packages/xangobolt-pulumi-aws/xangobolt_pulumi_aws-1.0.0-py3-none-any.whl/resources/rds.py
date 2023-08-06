from arpeggio.cleanpeg import NOT, prefix
from pulumi.resource import ResourceOptions
import pulumi_aws.rds as rds
import pulumi_aws_native.rds as rds_native

def Instance(stem, props, provider=None, parent=None, depends_on=None):
    db_instance = rds.Instance(
        f'rds-{stem}',
        # name=f'rds-{stem}',
        instance_class="db.m5.large",
        engine='sqlserver-se',
        engine_version="15.00.4073.23.v1",
        allocated_storage=100,
        username="set_uname",
        password="Testing123",
        license_model="license-included",
        skip_final_snapshot="True",
        tags=props.base_tags,
        opts=ResourceOptions(provider=provider, parent=parent, depends_on=depends_on)
    )
    return db_instance