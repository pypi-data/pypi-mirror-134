'''
# cdk-bootstrapless-synthesizer

[![npm version](https://img.shields.io/npm/v/cdk-bootstrapless-synthesizer)](https://www.npmjs.com/package/cdk-bootstrapless-synthesizer)
[![PyPI](https://img.shields.io/pypi/v/cdk-bootstrapless-synthesizer)](https://pypi.org/project/cdk-bootstrapless-synthesizer)
[![npm](https://img.shields.io/npm/dw/cdk-bootstrapless-synthesizer?label=npm%20downloads)](https://www.npmjs.com/package/cdk-bootstrapless-synthesizer)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/cdk-bootstrapless-synthesizer?label=pypi%20downloads)](https://pypi.org/project/cdk-bootstrapless-synthesizer)

A bootstrapless stack synthesizer that is designated to generate templates that can be directly used by AWS CloudFormation.

Please use ^1.0.0 for cdk version 1.x.x, use ^2.0.0 for cdk version 2.x.x

## Usage

```python
# Example automatically generated from non-compiling source. May contain errors.
import { BootstraplessStackSynthesizer } from 'cdk-bootstrapless-synthesizer';
```

[main.ts](sample/src/main.ts)

```python
# Example automatically generated from non-compiling source. May contain errors.
const app = new App();

new MyStack(app, 'my-stack-dev', {
  synthesizer: new BootstraplessStackSynthesizer({
    templateBucketName: 'cfn-template-bucket',

    fileAssetBucketName: 'file-asset-bucket-${AWS::Region}',
    fileAssetRegionSet: ['us-west-1', 'us-west-2'],
    fileAssetPrefix: 'file-asset-prefix/latest/',

    imageAssetRepositoryName: 'your-ecr-repo-name',
    imageAssetAccountId: '1234567890',
    imageAssetTagPrefix: 'latest-',
    imageAssetRegionSet: ['us-west-1', 'us-west-2'],
  }),
});

// Or by environment variables
env.BSS_TEMPLATE_BUCKET_NAME = 'cfn-template-bucket';

env.BSS_FILE_ASSET_BUCKET_NAME = 'file-asset-bucket-\${AWS::Region}';
env.BSS_FILE_ASSET_REGION_SET = 'us-west-1,us-west-2';
env.BSS_FILE_ASSET_PREFIX = 'file-asset-prefix/latest/';

env.BSS_IMAGE_ASSET_REPOSITORY_NAME = 'your-ecr-repo-name';
env.BSS_IMAGE_ASSET_ACCOUNT_ID = '1234567890';
env.BSS_IMAGE_ASSET_TAG_PREFIX = 'latest-';
env.BSS_IMAGE_ASSET_REGION_SET = 'us-west-1,us-west-2';

new MyStack(app, 'my-stack-dev2', {
  synthesizer: new BootstraplessStackSynthesizer(),
});

// use Aspect to grant the role to pull ECR repository from account BSS_IMAGE_ASSET_ACCOUNT_ID
```

[main.ts](sample/src/main.ts)

Synth AWS CloudFormation templates, assets and upload them

```shell
$ cdk synth
$ npx cdk-assets publish -p cdk.out/my-stack-dev.assets.json -v
```

## Limitations

When using `BSS_IMAGE_ASSET_ACCOUNT_ID` to push ECR repository to shared account, you need use `Aspect` to grant the role with policy to pull the repository from cross account. Or using the following `WithCrossAccount`  techniques.

Currently only below scenarios are supported,

* ECS
* SageMaker training job integrated with Step Functions

For other scenarios, the feature request or pull request are welcome.

```python
# Example automatically generated from non-compiling source. May contain errors.
function OverrideRepositoryAccount(scope: Construct, id: string, repo: IRepository): IRepository {
  class Import extends RepositoryBase {
    public repositoryName = repo.repositoryName;
    public repositoryArn = Repository.arnForLocalRepository(repo.repositoryName, scope, env.BSS_IMAGE_ASSET_ACCOUNT_ID);

    public addToResourcePolicy(_statement: iam.PolicyStatement): iam.AddToResourcePolicyResult {
      // dropped
      return { statementAdded: false };
    }
  }

  return new Import(scope, id);
}

function WithCrossAccount(image: DockerImageAsset): DockerImageAsset {
  image.repository = OverrideRepositoryAccount(image, 'CrossAccountRepo', image.repository);
  return image;
}

export class SampleStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps = {}) {
    super(scope, id, props);

    const image = WithCrossAccount(new DockerImageAsset(this, 'MyBuildImage', {
      directory: path.join(__dirname, '../docker'),
    }));

    new CfnOutput(this, 'output', { value: image.imageUri });

    const taskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDef');
    taskDefinition.addContainer('DefaultContainer', {
      image: ecs.ContainerImage.fromDockerImageAsset(image),
      memoryLimitMiB: 512,
    });

    fromAsset(this, 'stepfunctions', {
      directory: path.join(__dirname, '../docker'),
    });
  }
}
```

[main.ts](sample/src/main.ts)

## Sample Project

See [Sample Project](./sample/README.md)

## API Reference

See [API Reference](./API.md) for API details.
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

import aws_cdk
import aws_cdk.aws_ecs
import aws_cdk.aws_iam
import constructs


class BootstraplessStackSynthesizer(
    aws_cdk.StackSynthesizer,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-bootstrapless-synthesizer.BootstraplessStackSynthesizer",
):
    '''A Bootstrapless stack synthesizer that is designated to generate templates that can be directly used by Cloudformation.'''

    def __init__(
        self,
        *,
        file_asset_bucket_name: typing.Optional[builtins.str] = None,
        file_asset_prefix: typing.Optional[builtins.str] = None,
        file_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        file_asset_region_set: typing.Optional[typing.Sequence[builtins.str]] = None,
        image_asset_account_id: typing.Optional[builtins.str] = None,
        image_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        image_asset_region_set: typing.Optional[typing.Sequence[builtins.str]] = None,
        image_asset_repository_name: typing.Optional[builtins.str] = None,
        image_asset_tag_prefix: typing.Optional[builtins.str] = None,
        template_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_asset_bucket_name: Name of the S3 bucket to hold file assets. You must supply this if you have given a non-standard name to the staging bucket. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_FILE_ASSET_BUCKET_NAME
        :param file_asset_prefix: Object key prefix to use while storing S3 Assets. Default: - process.env.BSS_FILE_ASSET_PREFIX
        :param file_asset_publishing_role_arn: The role to use to publish file assets to the S3 bucket in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_FILE_ASSET_PUBLISHING_ROLE_ARN
        :param file_asset_region_set: The regions set of file assets to be published only when ``fileAssetBucketName`` contains ``${AWS::Region}``. For examples: ``['us-east-1', 'us-west-1']`` Default: - process.env.BSS_FILE_ASSET_REGION_SET // comma delimited list
        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        :param image_asset_publishing_role_arn: The role to use to publish image assets to the ECR repository in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_IMAGE_ASSET_PUBLISHING_ROLE_ARN
        :param image_asset_region_set: Override the ECR repository region of the Docker Image assets. For examples: ``['us-east-1', 'us-west-1']`` Default: - process.env.BSS_IMAGE_ASSET_REGION_SET // comma delimited list
        :param image_asset_repository_name: Name of the ECR repository to hold Docker Image assets. You must supply this if you have given a non-standard name to the ECR repository. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_IMAGE_ASSET_REPOSITORY_NAME
        :param image_asset_tag_prefix: Override the tag of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_TAG_PREFIX
        :param template_bucket_name: Override the name of the S3 bucket to hold Cloudformation template. Default: - process.env.BSS_TEMPLATE_BUCKET_NAME
        '''
        props = BootstraplessStackSynthesizerProps(
            file_asset_bucket_name=file_asset_bucket_name,
            file_asset_prefix=file_asset_prefix,
            file_asset_publishing_role_arn=file_asset_publishing_role_arn,
            file_asset_region_set=file_asset_region_set,
            image_asset_account_id=image_asset_account_id,
            image_asset_publishing_role_arn=image_asset_publishing_role_arn,
            image_asset_region_set=image_asset_region_set,
            image_asset_repository_name=image_asset_repository_name,
            image_asset_tag_prefix=image_asset_tag_prefix,
            template_bucket_name=template_bucket_name,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_hash: builtins.str,
    ) -> aws_cdk.DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        '''
        asset = aws_cdk.DockerImageAssetSource(
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            source_hash=source_hash,
        )

        return typing.cast(aws_cdk.DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[aws_cdk.FileAssetPackaging] = None,
        source_hash: builtins.str,
    ) -> aws_cdk.FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        '''
        asset = aws_cdk.FileAssetSource(
            executable=executable,
            file_name=file_name,
            packaging=packaging,
            source_hash=source_hash,
        )

        return typing.cast(aws_cdk.FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="bind")
    def bind(self, stack: aws_cdk.Stack) -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [stack]))

    @jsii.member(jsii_name="dumps")
    def dumps(self) -> builtins.str:
        '''Dumps current manifest into JSON format.'''
        return typing.cast(builtins.str, jsii.invoke(self, "dumps", []))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: aws_cdk.ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def _stack(self) -> typing.Optional[aws_cdk.Stack]:
        return typing.cast(typing.Optional[aws_cdk.Stack], jsii.get(self, "stack"))


@jsii.data_type(
    jsii_type="cdk-bootstrapless-synthesizer.BootstraplessStackSynthesizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_asset_bucket_name": "fileAssetBucketName",
        "file_asset_prefix": "fileAssetPrefix",
        "file_asset_publishing_role_arn": "fileAssetPublishingRoleArn",
        "file_asset_region_set": "fileAssetRegionSet",
        "image_asset_account_id": "imageAssetAccountId",
        "image_asset_publishing_role_arn": "imageAssetPublishingRoleArn",
        "image_asset_region_set": "imageAssetRegionSet",
        "image_asset_repository_name": "imageAssetRepositoryName",
        "image_asset_tag_prefix": "imageAssetTagPrefix",
        "template_bucket_name": "templateBucketName",
    },
)
class BootstraplessStackSynthesizerProps:
    def __init__(
        self,
        *,
        file_asset_bucket_name: typing.Optional[builtins.str] = None,
        file_asset_prefix: typing.Optional[builtins.str] = None,
        file_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        file_asset_region_set: typing.Optional[typing.Sequence[builtins.str]] = None,
        image_asset_account_id: typing.Optional[builtins.str] = None,
        image_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        image_asset_region_set: typing.Optional[typing.Sequence[builtins.str]] = None,
        image_asset_repository_name: typing.Optional[builtins.str] = None,
        image_asset_tag_prefix: typing.Optional[builtins.str] = None,
        template_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration properties for BootstraplessStackSynthesizer.

        :param file_asset_bucket_name: Name of the S3 bucket to hold file assets. You must supply this if you have given a non-standard name to the staging bucket. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_FILE_ASSET_BUCKET_NAME
        :param file_asset_prefix: Object key prefix to use while storing S3 Assets. Default: - process.env.BSS_FILE_ASSET_PREFIX
        :param file_asset_publishing_role_arn: The role to use to publish file assets to the S3 bucket in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_FILE_ASSET_PUBLISHING_ROLE_ARN
        :param file_asset_region_set: The regions set of file assets to be published only when ``fileAssetBucketName`` contains ``${AWS::Region}``. For examples: ``['us-east-1', 'us-west-1']`` Default: - process.env.BSS_FILE_ASSET_REGION_SET // comma delimited list
        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        :param image_asset_publishing_role_arn: The role to use to publish image assets to the ECR repository in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_IMAGE_ASSET_PUBLISHING_ROLE_ARN
        :param image_asset_region_set: Override the ECR repository region of the Docker Image assets. For examples: ``['us-east-1', 'us-west-1']`` Default: - process.env.BSS_IMAGE_ASSET_REGION_SET // comma delimited list
        :param image_asset_repository_name: Name of the ECR repository to hold Docker Image assets. You must supply this if you have given a non-standard name to the ECR repository. The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: - process.env.BSS_IMAGE_ASSET_REPOSITORY_NAME
        :param image_asset_tag_prefix: Override the tag of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_TAG_PREFIX
        :param template_bucket_name: Override the name of the S3 bucket to hold Cloudformation template. Default: - process.env.BSS_TEMPLATE_BUCKET_NAME
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if file_asset_bucket_name is not None:
            self._values["file_asset_bucket_name"] = file_asset_bucket_name
        if file_asset_prefix is not None:
            self._values["file_asset_prefix"] = file_asset_prefix
        if file_asset_publishing_role_arn is not None:
            self._values["file_asset_publishing_role_arn"] = file_asset_publishing_role_arn
        if file_asset_region_set is not None:
            self._values["file_asset_region_set"] = file_asset_region_set
        if image_asset_account_id is not None:
            self._values["image_asset_account_id"] = image_asset_account_id
        if image_asset_publishing_role_arn is not None:
            self._values["image_asset_publishing_role_arn"] = image_asset_publishing_role_arn
        if image_asset_region_set is not None:
            self._values["image_asset_region_set"] = image_asset_region_set
        if image_asset_repository_name is not None:
            self._values["image_asset_repository_name"] = image_asset_repository_name
        if image_asset_tag_prefix is not None:
            self._values["image_asset_tag_prefix"] = image_asset_tag_prefix
        if template_bucket_name is not None:
            self._values["template_bucket_name"] = template_bucket_name

    @builtins.property
    def file_asset_bucket_name(self) -> typing.Optional[builtins.str]:
        '''Name of the S3 bucket to hold file assets.

        You must supply this if you have given a non-standard name to the staging bucket.

        The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: - process.env.BSS_FILE_ASSET_BUCKET_NAME

        :required: if you have file assets
        '''
        result = self._values.get("file_asset_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_asset_prefix(self) -> typing.Optional[builtins.str]:
        '''Object key prefix to use while storing S3 Assets.

        :default: - process.env.BSS_FILE_ASSET_PREFIX
        '''
        result = self._values.get("file_asset_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_asset_publishing_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role to use to publish file assets to the S3 bucket in this environment.

        You must supply this if you have given a non-standard name to the publishing role.

        The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: - process.env.BSS_FILE_ASSET_PUBLISHING_ROLE_ARN
        '''
        result = self._values.get("file_asset_publishing_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_asset_region_set(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The regions set of file assets to be published only when ``fileAssetBucketName`` contains ``${AWS::Region}``.

        For examples:
        ``['us-east-1', 'us-west-1']``

        :default: - process.env.BSS_FILE_ASSET_REGION_SET // comma delimited list
        '''
        result = self._values.get("file_asset_region_set")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def image_asset_account_id(self) -> typing.Optional[builtins.str]:
        '''Override the ECR repository account id of the Docker Image assets.

        :default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        result = self._values.get("image_asset_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_asset_publishing_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role to use to publish image assets to the ECR repository in this environment.

        You must supply this if you have given a non-standard name to the publishing role.

        The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: - process.env.BSS_IMAGE_ASSET_PUBLISHING_ROLE_ARN
        '''
        result = self._values.get("image_asset_publishing_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_asset_region_set(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Override the ECR repository region of the Docker Image assets.

        For examples:
        ``['us-east-1', 'us-west-1']``

        :default: - process.env.BSS_IMAGE_ASSET_REGION_SET // comma delimited list
        '''
        result = self._values.get("image_asset_region_set")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def image_asset_repository_name(self) -> typing.Optional[builtins.str]:
        '''Name of the ECR repository to hold Docker Image assets.

        You must supply this if you have given a non-standard name to the ECR repository.

        The placeholders ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: - process.env.BSS_IMAGE_ASSET_REPOSITORY_NAME

        :required: if you have docker image assets
        '''
        result = self._values.get("image_asset_repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_asset_tag_prefix(self) -> typing.Optional[builtins.str]:
        '''Override the tag of the Docker Image assets.

        :default: - process.env.BSS_IMAGE_ASSET_TAG_PREFIX
        '''
        result = self._values.get("image_asset_tag_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_bucket_name(self) -> typing.Optional[builtins.str]:
        '''Override the name of the S3 bucket to hold Cloudformation template.

        :default: - process.env.BSS_TEMPLATE_BUCKET_NAME
        '''
        result = self._values.get("template_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BootstraplessStackSynthesizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.IAspect)
class ECRRepositoryAspect(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdk-bootstrapless-synthesizer.ECRRepositoryAspect",
):
    '''Abtract aspect for ECR repository.

    You must provide the account id in props or set BSS_IMAGE_ASSET_ACCOUNT_ID in env
    '''

    def __init__(
        self,
        *,
        image_asset_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        props = ECRRepositoryAspectProps(image_asset_account_id=image_asset_account_id)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="crossAccountECRPolicy")
    def _cross_account_ecr_policy(
        self,
        stack: aws_cdk.Stack,
        repo_name: builtins.str,
    ) -> aws_cdk.aws_iam.Policy:
        '''
        :param stack: -
        :param repo_name: -
        '''
        return typing.cast(aws_cdk.aws_iam.Policy, jsii.invoke(self, "crossAccountECRPolicy", [stack, repo_name]))

    @jsii.member(jsii_name="getRepoName")
    def _get_repo_name(self, image_uri: builtins.str) -> typing.Optional[builtins.str]:
        '''
        :param image_uri: -
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "getRepoName", [image_uri]))

    @jsii.member(jsii_name="visit") # type: ignore[misc]
    @abc.abstractmethod
    def visit(self, construct: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "account"))


class _ECRRepositoryAspectProxy(ECRRepositoryAspect):
    @jsii.member(jsii_name="visit")
    def visit(self, construct: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [construct]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ECRRepositoryAspect).__jsii_proxy_class__ = lambda : _ECRRepositoryAspectProxy


@jsii.data_type(
    jsii_type="cdk-bootstrapless-synthesizer.ECRRepositoryAspectProps",
    jsii_struct_bases=[],
    name_mapping={"image_asset_account_id": "imageAssetAccountId"},
)
class ECRRepositoryAspectProps:
    def __init__(
        self,
        *,
        image_asset_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration properties for ECRRepositoryAspect.

        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if image_asset_account_id is not None:
            self._values["image_asset_account_id"] = image_asset_account_id

    @builtins.property
    def image_asset_account_id(self) -> typing.Optional[builtins.str]:
        '''Override the ECR repository account id of the Docker Image assets.

        :default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        result = self._values.get("image_asset_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ECRRepositoryAspectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ECSTaskDefinition(
    ECRRepositoryAspect,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-bootstrapless-synthesizer.ECSTaskDefinition",
):
    '''Process the image assets in ECS task definition.'''

    def __init__(
        self,
        *,
        image_asset_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        props = ECRRepositoryAspectProps(image_asset_account_id=image_asset_account_id)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="hasBeReplaced")
    def _has_be_replaced(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.ContainerDependencyProperty, aws_cdk.IResolvable]]]] = None,
        disable_networking: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        dns_search_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        docker_labels: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        docker_security_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.KeyValuePairProperty, aws_cdk.IResolvable]]]] = None,
        environment_files: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.EnvironmentFileProperty, aws_cdk.IResolvable]]]] = None,
        essential: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        extra_hosts: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.HostEntryProperty, aws_cdk.IResolvable]]]] = None,
        firelens_configuration: typing.Optional[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.FirelensConfigurationProperty, aws_cdk.IResolvable]] = None,
        health_check: typing.Optional[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.HealthCheckProperty, aws_cdk.IResolvable]] = None,
        hostname: typing.Optional[builtins.str] = None,
        image: typing.Optional[builtins.str] = None,
        interactive: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        links: typing.Optional[typing.Sequence[builtins.str]] = None,
        linux_parameters: typing.Optional[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.LinuxParametersProperty, aws_cdk.IResolvable]] = None,
        log_configuration: typing.Optional[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.LogConfigurationProperty, aws_cdk.IResolvable]] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_reservation: typing.Optional[jsii.Number] = None,
        mount_points: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.MountPointProperty, aws_cdk.IResolvable]]]] = None,
        name: typing.Optional[builtins.str] = None,
        port_mappings: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.PortMappingProperty, aws_cdk.IResolvable]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        pseudo_terminal: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        readonly_root_filesystem: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        repository_credentials: typing.Optional[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.RepositoryCredentialsProperty, aws_cdk.IResolvable]] = None,
        resource_requirements: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.ResourceRequirementProperty, aws_cdk.IResolvable]]]] = None,
        secrets: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.SecretProperty, aws_cdk.IResolvable]]]] = None,
        start_timeout: typing.Optional[jsii.Number] = None,
        stop_timeout: typing.Optional[jsii.Number] = None,
        system_controls: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.SystemControlProperty, aws_cdk.IResolvable]]]] = None,
        ulimits: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.UlimitProperty, aws_cdk.IResolvable]]]] = None,
        user: typing.Optional[builtins.str] = None,
        volumes_from: typing.Optional[typing.Union[aws_cdk.IResolvable, typing.Sequence[typing.Union[aws_cdk.aws_ecs.CfnTaskDefinition.VolumeFromProperty, aws_cdk.IResolvable]]]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> typing.Optional[builtins.str]:
        '''
        :param command: ``CfnTaskDefinition.ContainerDefinitionProperty.Command``.
        :param cpu: ``CfnTaskDefinition.ContainerDefinitionProperty.Cpu``.
        :param depends_on: ``CfnTaskDefinition.ContainerDefinitionProperty.DependsOn``.
        :param disable_networking: ``CfnTaskDefinition.ContainerDefinitionProperty.DisableNetworking``.
        :param dns_search_domains: ``CfnTaskDefinition.ContainerDefinitionProperty.DnsSearchDomains``.
        :param dns_servers: ``CfnTaskDefinition.ContainerDefinitionProperty.DnsServers``.
        :param docker_labels: ``CfnTaskDefinition.ContainerDefinitionProperty.DockerLabels``.
        :param docker_security_options: ``CfnTaskDefinition.ContainerDefinitionProperty.DockerSecurityOptions``.
        :param entry_point: ``CfnTaskDefinition.ContainerDefinitionProperty.EntryPoint``.
        :param environment: ``CfnTaskDefinition.ContainerDefinitionProperty.Environment``.
        :param environment_files: ``CfnTaskDefinition.ContainerDefinitionProperty.EnvironmentFiles``.
        :param essential: ``CfnTaskDefinition.ContainerDefinitionProperty.Essential``.
        :param extra_hosts: ``CfnTaskDefinition.ContainerDefinitionProperty.ExtraHosts``.
        :param firelens_configuration: ``CfnTaskDefinition.ContainerDefinitionProperty.FirelensConfiguration``.
        :param health_check: ``CfnTaskDefinition.ContainerDefinitionProperty.HealthCheck``.
        :param hostname: ``CfnTaskDefinition.ContainerDefinitionProperty.Hostname``.
        :param image: ``CfnTaskDefinition.ContainerDefinitionProperty.Image``.
        :param interactive: ``CfnTaskDefinition.ContainerDefinitionProperty.Interactive``.
        :param links: ``CfnTaskDefinition.ContainerDefinitionProperty.Links``.
        :param linux_parameters: ``CfnTaskDefinition.ContainerDefinitionProperty.LinuxParameters``.
        :param log_configuration: ``CfnTaskDefinition.ContainerDefinitionProperty.LogConfiguration``.
        :param memory: ``CfnTaskDefinition.ContainerDefinitionProperty.Memory``.
        :param memory_reservation: ``CfnTaskDefinition.ContainerDefinitionProperty.MemoryReservation``.
        :param mount_points: ``CfnTaskDefinition.ContainerDefinitionProperty.MountPoints``.
        :param name: ``CfnTaskDefinition.ContainerDefinitionProperty.Name``.
        :param port_mappings: ``CfnTaskDefinition.ContainerDefinitionProperty.PortMappings``.
        :param privileged: ``CfnTaskDefinition.ContainerDefinitionProperty.Privileged``.
        :param pseudo_terminal: ``CfnTaskDefinition.ContainerDefinitionProperty.PseudoTerminal``.
        :param readonly_root_filesystem: ``CfnTaskDefinition.ContainerDefinitionProperty.ReadonlyRootFilesystem``.
        :param repository_credentials: ``CfnTaskDefinition.ContainerDefinitionProperty.RepositoryCredentials``.
        :param resource_requirements: ``CfnTaskDefinition.ContainerDefinitionProperty.ResourceRequirements``.
        :param secrets: ``CfnTaskDefinition.ContainerDefinitionProperty.Secrets``.
        :param start_timeout: ``CfnTaskDefinition.ContainerDefinitionProperty.StartTimeout``.
        :param stop_timeout: ``CfnTaskDefinition.ContainerDefinitionProperty.StopTimeout``.
        :param system_controls: ``CfnTaskDefinition.ContainerDefinitionProperty.SystemControls``.
        :param ulimits: ``CfnTaskDefinition.ContainerDefinitionProperty.Ulimits``.
        :param user: ``CfnTaskDefinition.ContainerDefinitionProperty.User``.
        :param volumes_from: ``CfnTaskDefinition.ContainerDefinitionProperty.VolumesFrom``.
        :param working_directory: ``CfnTaskDefinition.ContainerDefinitionProperty.WorkingDirectory``.
        '''
        prop = aws_cdk.aws_ecs.CfnTaskDefinition.ContainerDefinitionProperty(
            command=command,
            cpu=cpu,
            depends_on=depends_on,
            disable_networking=disable_networking,
            dns_search_domains=dns_search_domains,
            dns_servers=dns_servers,
            docker_labels=docker_labels,
            docker_security_options=docker_security_options,
            entry_point=entry_point,
            environment=environment,
            environment_files=environment_files,
            essential=essential,
            extra_hosts=extra_hosts,
            firelens_configuration=firelens_configuration,
            health_check=health_check,
            hostname=hostname,
            image=image,
            interactive=interactive,
            links=links,
            linux_parameters=linux_parameters,
            log_configuration=log_configuration,
            memory=memory,
            memory_reservation=memory_reservation,
            mount_points=mount_points,
            name=name,
            port_mappings=port_mappings,
            privileged=privileged,
            pseudo_terminal=pseudo_terminal,
            readonly_root_filesystem=readonly_root_filesystem,
            repository_credentials=repository_credentials,
            resource_requirements=resource_requirements,
            secrets=secrets,
            start_timeout=start_timeout,
            stop_timeout=stop_timeout,
            system_controls=system_controls,
            ulimits=ulimits,
            user=user,
            volumes_from=volumes_from,
            working_directory=working_directory,
        )

        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "hasBeReplaced", [prop]))

    @jsii.member(jsii_name="visit")
    def visit(self, construct: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [construct]))


class StepFunctionsSageMakerTrainingJob(
    ECRRepositoryAspect,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-bootstrapless-synthesizer.StepFunctionsSageMakerTrainingJob",
):
    '''Process the image assets in SageMaker training job in Step Functions.'''

    def __init__(
        self,
        *,
        image_asset_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        props = ECRRepositoryAspectProps(image_asset_account_id=image_asset_account_id)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, construct: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [construct]))


class CompositeECRRepositoryAspect(
    ECRRepositoryAspect,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-bootstrapless-synthesizer.CompositeECRRepositoryAspect",
):
    '''Default ECR asset aspect, support using ECR assets in below services,.

    - ECS task definition
    - SageMaker training job in Step Functions
    '''

    def __init__(
        self,
        *,
        image_asset_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_asset_account_id: Override the ECR repository account id of the Docker Image assets. Default: - process.env.BSS_IMAGE_ASSET_ACCOUNT_ID
        '''
        props = ECRRepositoryAspectProps(image_asset_account_id=image_asset_account_id)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, construct: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [construct]))


__all__ = [
    "BootstraplessStackSynthesizer",
    "BootstraplessStackSynthesizerProps",
    "CompositeECRRepositoryAspect",
    "ECRRepositoryAspect",
    "ECRRepositoryAspectProps",
    "ECSTaskDefinition",
    "StepFunctionsSageMakerTrainingJob",
]

publication.publish()
