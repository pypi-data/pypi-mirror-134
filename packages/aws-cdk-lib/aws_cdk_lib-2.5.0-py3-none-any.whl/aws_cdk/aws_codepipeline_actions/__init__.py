'''
# AWS CodePipeline Actions

This package contains Actions that can be used in a CodePipeline.

```python
import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_codepipeline_actions as codepipeline_actions
```

## Sources

### AWS CodeCommit

To use a CodeCommit Repository in a CodePipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
repo = codecommit.Repository(self, "Repo",
    repository_name="MyRepo"
)

pipeline = codepipeline.Pipeline(self, "MyPipeline",
    pipeline_name="MyPipeline"
)
source_output = codepipeline.Artifact()
source_action = codepipeline_actions.CodeCommitSourceAction(
    action_name="CodeCommit",
    repository=repo,
    output=source_output
)
pipeline.add_stage(
    stage_name="Source",
    actions=[source_action]
)
```

If you want to use existing role which can be used by on commit event rule.
You can specify the role object in eventRole property.

```python
# Example automatically generated from non-compiling source. May contain errors.
# repo is of type Repository
event_role = iam.Role.from_role_arn(self, "Event-role", "roleArn")
source_action = codepipeline_actions.CodeCommitSourceAction(
    action_name="CodeCommit",
    repository=repo,
    output=codepipeline.Artifact(),
    event_role=event_role
)
```

If you want to clone the entire CodeCommit repository (only available for CodeBuild actions),
you can set the `codeBuildCloneOutput` property to `true`:

```python
# Example automatically generated from non-compiling source. May contain errors.
# project is of type PipelineProject
# repo is of type Repository

source_output = codepipeline.Artifact()
source_action = codepipeline_actions.CodeCommitSourceAction(
    action_name="CodeCommit",
    repository=repo,
    output=source_output,
    code_build_clone_output=True
)

build_action = codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,  # The build action must use the CodeCommitSourceAction output as input.
    outputs=[codepipeline.Artifact()]
)
```

The CodeCommit source action emits variables:

```python
# Example automatically generated from non-compiling source. May contain errors.
# project is of type PipelineProject
# repo is of type Repository

source_output = codepipeline.Artifact()
source_action = codepipeline_actions.CodeCommitSourceAction(
    action_name="CodeCommit",
    repository=repo,
    output=source_output,
    variables_namespace="MyNamespace"
)

# later:

codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "COMMIT_ID": codebuild.BuildEnvironmentVariable(
            value=source_action.variables.commit_id
        )
    }
)
```

### GitHub

If you want to use a GitHub repository as the source, you must create:

* A [GitHub Access Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line),
  with scopes **repo** and **admin:repo_hook**.
* A [Secrets Manager Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html)
  with the value of the **GitHub Access Token**. Pick whatever name you want (for example `my-github-token`).
  This token can be stored either as Plaintext or as a Secret key/value.
  If you stored the token as Plaintext,
  set `SecretValue.secretsManager('my-github-token')` as the value of `oauthToken`.
  If you stored it as a Secret key/value,
  you must set `SecretValue.secretsManager('my-github-token', { jsonField : 'my-github-token' })` as the value of `oauthToken`.

To use GitHub as the source of a CodePipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
# Read the secret from Secrets Manager
pipeline = codepipeline.Pipeline(self, "MyPipeline")
source_output = codepipeline.Artifact()
source_action = codepipeline_actions.GitHubSourceAction(
    action_name="GitHub_Source",
    owner="awslabs",
    repo="aws-cdk",
    oauth_token=SecretValue.secrets_manager("my-github-token"),
    output=source_output,
    branch="develop"
)
pipeline.add_stage(
    stage_name="Source",
    actions=[source_action]
)
```

The GitHub source action emits variables:

```python
# Example automatically generated from non-compiling source. May contain errors.
# source_output is of type Artifact
# project is of type PipelineProject


source_action = codepipeline_actions.GitHubSourceAction(
    action_name="Github_Source",
    output=source_output,
    owner="my-owner",
    repo="my-repo",
    oauth_token=SecretValue.secrets_manager("my-github-token"),
    variables_namespace="MyNamespace"
)

# later:

codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "COMMIT_URL": codebuild.BuildEnvironmentVariable(
            value=source_action.variables.commit_url
        )
    }
)
```

### BitBucket

CodePipeline can use a BitBucket Git repository as a source:

**Note**: you have to manually connect CodePipeline through the AWS Console with your BitBucket account.
This is a one-time operation for a given AWS account in a given region.
The simplest way to do that is to either start creating a new CodePipeline,
or edit an existing one, while being logged in to BitBucket.
Choose BitBucket as the source,
and grant CodePipeline permissions to your BitBucket account.
Copy & paste the Connection ARN that you get in the console,
or use the [`codestar-connections list-connections` AWS CLI operation](https://docs.aws.amazon.com/cli/latest/reference/codestar-connections/list-connections.html)
to find it.
After that, you can safely abort creating or editing the pipeline -
the connection has already been created.

```python
# Example automatically generated from non-compiling source. May contain errors.
source_output = codepipeline.Artifact()
source_action = codepipeline_actions.CodeStarConnectionsSourceAction(
    action_name="BitBucket_Source",
    owner="aws",
    repo="aws-cdk",
    output=source_output,
    connection_arn="arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-abcd-12ab-34cdef5678gh"
)
```

You can also use the `CodeStarConnectionsSourceAction` to connect to GitHub, in the same way
(you just have to select GitHub as the source when creating the connection in the console).

Similarly to `GitHubSourceAction`, `CodeStarConnectionsSourceAction` also emits the variables:

```python
# Example automatically generated from non-compiling source. May contain errors.
# project is of type Project


source_output = codepipeline.Artifact()
source_action = codepipeline_actions.CodeStarConnectionsSourceAction(
    action_name="BitBucket_Source",
    owner="aws",
    repo="aws-cdk",
    output=source_output,
    connection_arn="arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-abcd-12ab-34cdef5678gh",
    variables_namespace="SomeSpace"
)

# later:

codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "COMMIT_ID": codebuild.BuildEnvironmentVariable(
            value=source_action.variables.commit_id
        )
    }
)
```

### AWS S3 Source

To use an S3 Bucket as a source in CodePipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
source_bucket = s3.Bucket(self, "MyBucket",
    versioned=True
)

pipeline = codepipeline.Pipeline(self, "MyPipeline")
source_output = codepipeline.Artifact()
source_action = codepipeline_actions.S3SourceAction(
    action_name="S3Source",
    bucket=source_bucket,
    bucket_key="path/to/file.zip",
    output=source_output
)
pipeline.add_stage(
    stage_name="Source",
    actions=[source_action]
)
```

The region of the action will be determined by the region the bucket itself is in.
When using a newly created bucket,
that region will be taken from the stack the bucket belongs to;
for an imported bucket,
you can specify the region explicitly:

```python
# Example automatically generated from non-compiling source. May contain errors.
source_bucket = s3.Bucket.from_bucket_attributes(self, "SourceBucket",
    bucket_name="my-bucket",
    region="ap-southeast-1"
)
```

By default, the Pipeline will poll the Bucket to detect changes.
You can change that behavior to use CloudWatch Events by setting the `trigger`
property to `S3Trigger.EVENTS` (it's `S3Trigger.POLL` by default).
If you do that, make sure the source Bucket is part of an AWS CloudTrail Trail -
otherwise, the CloudWatch Events will not be emitted,
and your Pipeline will not react to changes in the Bucket.
You can do it through the CDK:

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_cloudtrail as cloudtrail

# source_bucket is of type Bucket

source_output = codepipeline.Artifact()
key = "some/key.zip"
trail = cloudtrail.Trail(self, "CloudTrail")
trail.add_s3_event_selector([cloudtrail.S3EventSelector(
    bucket=source_bucket,
    object_prefix=key
)],
    read_write_type=cloudtrail.ReadWriteType.WRITE_ONLY
)
source_action = codepipeline_actions.S3SourceAction(
    action_name="S3Source",
    bucket_key=key,
    bucket=source_bucket,
    output=source_output,
    trigger=codepipeline_actions.S3Trigger.EVENTS
)
```

The S3 source action emits variables:

```python
# Example automatically generated from non-compiling source. May contain errors.
# source_bucket is of type Bucket

# later:
# project is of type PipelineProject
key = "some/key.zip"
source_output = codepipeline.Artifact()
source_action = codepipeline_actions.S3SourceAction(
    action_name="S3Source",
    bucket_key=key,
    bucket=source_bucket,
    output=source_output,
    variables_namespace="MyNamespace"
)
codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "VERSION_ID": codebuild.BuildEnvironmentVariable(
            value=source_action.variables.version_id
        )
    }
)
```

### AWS ECR

To use an ECR Repository as a source in a Pipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_ecr as ecr

# ecr_repository is of type Repository

pipeline = codepipeline.Pipeline(self, "MyPipeline")
source_output = codepipeline.Artifact()
source_action = codepipeline_actions.EcrSourceAction(
    action_name="ECR",
    repository=ecr_repository,
    image_tag="some-tag",  # optional, default: 'latest'
    output=source_output
)
pipeline.add_stage(
    stage_name="Source",
    actions=[source_action]
)
```

The ECR source action emits variables:

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_ecr as ecr
# ecr_repository is of type Repository

# later:
# project is of type PipelineProject


source_output = codepipeline.Artifact()
source_action = codepipeline_actions.EcrSourceAction(
    action_name="Source",
    output=source_output,
    repository=ecr_repository,
    variables_namespace="MyNamespace"
)
codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "IMAGE_URI": codebuild.BuildEnvironmentVariable(
            value=source_action.variables.image_uri
        )
    }
)
```

## Build & test

### AWS CodeBuild

Example of a CodeBuild Project used in a Pipeline, alongside CodeCommit:

```python
# Example automatically generated from non-compiling source. May contain errors.
# project is of type PipelineProject

repository = codecommit.Repository(self, "MyRepository",
    repository_name="MyRepository"
)
project = codebuild.PipelineProject(self, "MyProject")

source_output = codepipeline.Artifact()
source_action = codepipeline_actions.CodeCommitSourceAction(
    action_name="CodeCommit",
    repository=repository,
    output=source_output
)
build_action = codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    outputs=[codepipeline.Artifact()],  # optional
    execute_batch_build=True,  # optional, defaults to false
    combine_batch_build_artifacts=True
)

codepipeline.Pipeline(self, "MyPipeline",
    stages=[codepipeline.StageProps(
        stage_name="Source",
        actions=[source_action]
    ), codepipeline.StageProps(
        stage_name="Build",
        actions=[build_action]
    )
    ]
)
```

The default category of the CodeBuild Action is `Build`;
if you want a `Test` Action instead,
override the `type` property:

```python
# Example automatically generated from non-compiling source. May contain errors.
# project is of type PipelineProject

source_output = codepipeline.Artifact()
test_action = codepipeline_actions.CodeBuildAction(
    action_name="IntegrationTest",
    project=project,
    input=source_output,
    type=codepipeline_actions.CodeBuildActionType.TEST
)
```

#### Multiple inputs and outputs

When you want to have multiple inputs and/or outputs for a Project used in a
Pipeline, instead of using the `secondarySources` and `secondaryArtifacts`
properties of the `Project` class, you need to use the `extraInputs` and
`outputs` properties of the CodeBuild CodePipeline
Actions. Example:

```python
# Example automatically generated from non-compiling source. May contain errors.
# repository1 is of type Repository
# repository2 is of type Repository

# project is of type PipelineProject

source_output1 = codepipeline.Artifact()
source_action1 = codepipeline_actions.CodeCommitSourceAction(
    action_name="Source1",
    repository=repository1,
    output=source_output1
)
source_output2 = codepipeline.Artifact("source2")
source_action2 = codepipeline_actions.CodeCommitSourceAction(
    action_name="Source2",
    repository=repository2,
    output=source_output2
)
build_action = codepipeline_actions.CodeBuildAction(
    action_name="Build",
    project=project,
    input=source_output1,
    extra_inputs=[source_output2
    ],
    outputs=[
        codepipeline.Artifact("artifact1"),  # for better buildspec readability - see below
        codepipeline.Artifact("artifact2")
    ]
)
```

**Note**: when a CodeBuild Action in a Pipeline has more than one output, it
only uses the `secondary-artifacts` field of the buildspec, never the
primary output specification directly under `artifacts`. Because of that, it
pays to explicitly name all output artifacts of that Action, like we did
above, so that you know what name to use in the buildspec.

Example buildspec for the above project:

```python
# Example automatically generated from non-compiling source. May contain errors.
project = codebuild.PipelineProject(self, "MyProject",
    build_spec=codebuild.BuildSpec.from_object({
        "version": "0.2",
        "phases": {
            "build": {
                "commands": []
            }
        },
        "artifacts": {
            "secondary-artifacts": {
                "artifact1": {},
                "artifact2": {}
            }
        }
    })
)
```

#### Variables

The CodeBuild action emits variables.
Unlike many other actions, the variables are not static,
but dynamic, defined in the buildspec,
in the 'exported-variables' subsection of the 'env' section.
Example:

```python
# Example automatically generated from non-compiling source. May contain errors.
# later:
# project is of type PipelineProject
source_output = codepipeline.Artifact()
build_action = codepipeline_actions.CodeBuildAction(
    action_name="Build1",
    input=source_output,
    project=codebuild.PipelineProject(self, "Project",
        build_spec=codebuild.BuildSpec.from_object({
            "version": "0.2",
            "env": {
                "exported-variables": ["MY_VAR"
                ]
            },
            "phases": {
                "build": {
                    "commands": "export MY_VAR=\"some value\""
                }
            }
        })
    ),
    variables_namespace="MyNamespace"
)
codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "MyVar": codebuild.BuildEnvironmentVariable(
            value=build_action.variable("MY_VAR")
        )
    }
)
```

### Jenkins

In order to use Jenkins Actions in the Pipeline,
you first need to create a `JenkinsProvider`:

```python
# Example automatically generated from non-compiling source. May contain errors.
jenkins_provider = codepipeline_actions.JenkinsProvider(self, "JenkinsProvider",
    provider_name="MyJenkinsProvider",
    server_url="http://my-jenkins.com:8080",
    version="2"
)
```

If you've registered a Jenkins provider in a different CDK app,
or outside the CDK (in the CodePipeline AWS Console, for example),
you can import it:

```python
# Example automatically generated from non-compiling source. May contain errors.
jenkins_provider = codepipeline_actions.JenkinsProvider.from_jenkins_provider_attributes(self, "JenkinsProvider",
    provider_name="MyJenkinsProvider",
    server_url="http://my-jenkins.com:8080",
    version="2"
)
```

Note that a Jenkins provider
(identified by the provider name-category(build/test)-version tuple)
must always be registered in the given account, in the given AWS region,
before it can be used in CodePipeline.

With a `JenkinsProvider`,
we can create a Jenkins Action:

```python
# Example automatically generated from non-compiling source. May contain errors.
# jenkins_provider is of type JenkinsProvider

build_action = codepipeline_actions.JenkinsAction(
    action_name="JenkinsBuild",
    jenkins_provider=jenkins_provider,
    project_name="MyProject",
    type=codepipeline_actions.JenkinsActionType.BUILD
)
```

## Deploy

### AWS CloudFormation

This module contains Actions that allows you to deploy to CloudFormation from AWS CodePipeline.

For example, the following code fragment defines a pipeline that automatically deploys a CloudFormation template
directly from a CodeCommit repository, with a manual approval step in between to confirm the changes:

[example Pipeline to deploy CloudFormation](test/integ.cfn-template-from-repo.lit.ts)

See [the AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline.html)
for more details about using CloudFormation in CodePipeline.

#### Actions defined by this package

This package contains the following CloudFormation actions:

* **CloudFormationCreateUpdateStackAction** - Deploy a CloudFormation template directly from the pipeline. The indicated stack is created,
  or updated if it already exists. If the stack is in a failure state, deployment will fail (unless `replaceOnFailure`
  is set to `true`, in which case it will be destroyed and recreated).
* **CloudFormationDeleteStackAction** - Delete the stack with the given name.
* **CloudFormationCreateReplaceChangeSetAction** - Prepare a change set to be applied later. You will typically use change sets if you want
  to manually verify the changes that are being staged, or if you want to separate the people (or system) preparing the
  changes from the people (or system) applying the changes.
* **CloudFormationExecuteChangeSetAction** - Execute a change set prepared previously.

#### Lambda deployed through CodePipeline

If you want to deploy your Lambda through CodePipeline,
and you don't use assets (for example, because your CDK code and Lambda code are separate),
you can use a special Lambda `Code` class, `CfnParametersCode`.
Note that your Lambda must be in a different Stack than your Pipeline.
The Lambda itself will be deployed, alongside the entire Stack it belongs to,
using a CloudFormation CodePipeline Action. Example:

[Example of deploying a Lambda through CodePipeline](test/integ.lambda-deployed-through-codepipeline.lit.ts)

#### Cross-account actions

If you want to update stacks in a different account,
pass the `account` property when creating the action:

```python
# Example automatically generated from non-compiling source. May contain errors.
source_output = codepipeline.Artifact()
codepipeline_actions.CloudFormationCreateUpdateStackAction(
    action_name="CloudFormationCreateUpdate",
    stack_name="MyStackName",
    admin_permissions=True,
    template_path=source_output.at_path("template.yaml"),
    account="123456789012"
)
```

This will create a new stack, called `<PipelineStackName>-support-123456789012`, in your `App`,
that will contain the role that the pipeline will assume in account 123456789012 before executing this action.
This support stack will automatically be deployed before the stack containing the pipeline.

You can also pass a role explicitly when creating the action -
in that case, the `account` property is ignored,
and the action will operate in the same account the role belongs to:

```python
# Example automatically generated from non-compiling source. May contain errors.
from aws_cdk import PhysicalName

# in stack for account 123456789012...
# other_account_stack is of type Stack

action_role = iam.Role(other_account_stack, "ActionRole",
    assumed_by=iam.AccountPrincipal("123456789012"),
    # the role has to have a physical name set
    role_name=PhysicalName.GENERATE_IF_NEEDED
)

# in the pipeline stack...
source_output = codepipeline.Artifact()
codepipeline_actions.CloudFormationCreateUpdateStackAction(
    action_name="CloudFormationCreateUpdate",
    stack_name="MyStackName",
    admin_permissions=True,
    template_path=source_output.at_path("template.yaml"),
    role=action_role
)
```

### AWS CodeDeploy

#### Server deployments

To use CodeDeploy for EC2/on-premise deployments in a Pipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
# deployment_group is of type ServerDeploymentGroup
pipeline = codepipeline.Pipeline(self, "MyPipeline",
    pipeline_name="MyPipeline"
)

# add the source and build Stages to the Pipeline...
build_output = codepipeline.Artifact()
deploy_action = codepipeline_actions.CodeDeployServerDeployAction(
    action_name="CodeDeploy",
    input=build_output,
    deployment_group=deployment_group
)
pipeline.add_stage(
    stage_name="Deploy",
    actions=[deploy_action]
)
```

##### Lambda deployments

To use CodeDeploy for blue-green Lambda deployments in a Pipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
lambda_code = lambda_.Code.from_cfn_parameters()
func = lambda_.Function(self, "Lambda",
    code=lambda_code,
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_12_X
)
# used to make sure each CDK synthesis produces a different Version
version = func.add_version("NewVersion")
alias = lambda_.Alias(self, "LambdaAlias",
    alias_name="Prod",
    version=version
)

codedeploy.LambdaDeploymentGroup(self, "DeploymentGroup",
    alias=alias,
    deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE
)
```

Then, you need to create your Pipeline Stack,
where you will define your Pipeline,
and deploy the `lambdaStack` using a CloudFormation CodePipeline Action
(see above for a complete example).

### ECS

CodePipeline can deploy an ECS service.
The deploy Action receives one input Artifact which contains the [image definition file](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html#pipelines-create-image-definitions):

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_ecs as ecs

# service is of type FargateService

pipeline = codepipeline.Pipeline(self, "MyPipeline")
build_output = codepipeline.Artifact()
deploy_stage = pipeline.add_stage(
    stage_name="Deploy",
    actions=[
        codepipeline_actions.EcsDeployAction(
            action_name="DeployAction",
            service=service,
            # if your file is called imagedefinitions.json,
            # use the `input` property,
            # and leave out the `imageFile` property
            input=build_output,
            # if your file name is _not_ imagedefinitions.json,
            # use the `imageFile` property,
            # and leave out the `input` property
            image_file=build_output.at_path("imageDef.json"),
            deployment_timeout=Duration.minutes(60)
        )
    ]
)
```

#### Deploying ECS applications stored in a separate source code repository

The idiomatic CDK way of deploying an ECS application is to have your Dockerfiles and your CDK code in the same source code repository,
leveraging [Docker Assets](https://docs.aws.amazon.com/cdk/latest/guide/assets.html#assets_types_docker),
and use the [CDK Pipelines module](https://docs.aws.amazon.com/cdk/api/latest/docs/pipelines-readme.html).

However, if you want to deploy a Docker application whose source code is kept in a separate version control repository than the CDK code,
you can use the `TagParameterContainerImage` class from the ECS module.
Here's an example:

[example ECS pipeline for an application in a separate source code repository](test/integ.pipeline-ecs-separate-source.lit.ts)

### AWS S3 Deployment

To use an S3 Bucket as a deployment target in CodePipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
source_output = codepipeline.Artifact()
target_bucket = s3.Bucket(self, "MyBucket")

pipeline = codepipeline.Pipeline(self, "MyPipeline")
deploy_action = codepipeline_actions.S3DeployAction(
    action_name="S3Deploy",
    bucket=target_bucket,
    input=source_output
)
deploy_stage = pipeline.add_stage(
    stage_name="Deploy",
    actions=[deploy_action]
)
```

#### Invalidating the CloudFront cache when deploying to S3

There is currently no native support in CodePipeline for invalidating a CloudFront cache after deployment.
One workaround is to add another build step after the deploy step,
and use the AWS CLI to invalidate the cache:

```python
# Example automatically generated from non-compiling source. May contain errors.
# Create a Cloudfront Web Distribution
import aws_cdk.aws_cloudfront as cloudfront
# distribution is of type Distribution


# Create the build project that will invalidate the cache
invalidate_build_project = codebuild.PipelineProject(self, "InvalidateProject",
    build_spec=codebuild.BuildSpec.from_object({
        "version": "0.2",
        "phases": {
            "build": {
                "commands": ["aws cloudfront create-invalidation --distribution-id ${CLOUDFRONT_ID} --paths \"/*\""
                ]
            }
        }
    }),
    environment_variables={
        "CLOUDFRONT_ID": codebuild.BuildEnvironmentVariable(value=distribution.distribution_id)
    }
)

# Add Cloudfront invalidation permissions to the project
distribution_arn = f"arn:aws:cloudfront::{this.account}:distribution/{distribution.distributionId}"
invalidate_build_project.add_to_role_policy(iam.PolicyStatement(
    resources=[distribution_arn],
    actions=["cloudfront:CreateInvalidation"
    ]
))

# Create the pipeline (here only the S3 deploy and Invalidate cache build)
deploy_bucket = s3.Bucket(self, "DeployBucket")
deploy_input = codepipeline.Artifact()
codepipeline.Pipeline(self, "Pipeline",
    stages=[codepipeline.StageProps(
        stage_name="Deploy",
        actions=[
            codepipeline_actions.S3DeployAction(
                action_name="S3Deploy",
                bucket=deploy_bucket,
                input=deploy_input,
                run_order=1
            ),
            codepipeline_actions.CodeBuildAction(
                action_name="InvalidateCache",
                project=invalidate_build_project,
                input=deploy_input,
                run_order=2
            )
        ]
    )
    ]
)
```

### Alexa Skill

You can deploy to Alexa using CodePipeline with the following Action:

```python
# Example automatically generated from non-compiling source. May contain errors.
# Read the secrets from ParameterStore
client_id = SecretValue.secrets_manager("AlexaClientId")
client_secret = SecretValue.secrets_manager("AlexaClientSecret")
refresh_token = SecretValue.secrets_manager("AlexaRefreshToken")

# Add deploy action
source_output = codepipeline.Artifact()
codepipeline_actions.AlexaSkillDeployAction(
    action_name="DeploySkill",
    run_order=1,
    input=source_output,
    client_id=client_id.to_string(),
    client_secret=client_secret,
    refresh_token=refresh_token,
    skill_id="amzn1.ask.skill.12345678-1234-1234-1234-123456789012"
)
```

If you need manifest overrides you can specify them as `parameterOverridesArtifact` in the action:

```python
# Example automatically generated from non-compiling source. May contain errors.
# Deploy some CFN change set and store output
execute_output = codepipeline.Artifact("CloudFormation")
execute_change_set_action = codepipeline_actions.CloudFormationExecuteChangeSetAction(
    action_name="ExecuteChangesTest",
    run_order=2,
    stack_name="MyStack",
    change_set_name="MyChangeSet",
    output_file_name="overrides.json",
    output=execute_output
)

# Provide CFN output as manifest overrides
client_id = SecretValue.secrets_manager("AlexaClientId")
client_secret = SecretValue.secrets_manager("AlexaClientSecret")
refresh_token = SecretValue.secrets_manager("AlexaRefreshToken")
source_output = codepipeline.Artifact()
codepipeline_actions.AlexaSkillDeployAction(
    action_name="DeploySkill",
    run_order=1,
    input=source_output,
    parameter_overrides_artifact=execute_output,
    client_id=client_id.to_string(),
    client_secret=client_secret,
    refresh_token=refresh_token,
    skill_id="amzn1.ask.skill.12345678-1234-1234-1234-123456789012"
)
```

### AWS Service Catalog

You can deploy a CloudFormation template to an existing Service Catalog product with the following Action:

```python
# Example automatically generated from non-compiling source. May contain errors.
cdk_build_output = codepipeline.Artifact()
service_catalog_deploy_action = codepipeline_actions.ServiceCatalogDeployActionBeta1(
    action_name="ServiceCatalogDeploy",
    template_path=cdk_build_output.at_path("Sample.template.json"),
    product_version_name="Version - " + Date.now.to_string,
    product_version_description="This is a version from the pipeline with a new description.",
    product_id="prod-XXXXXXXX"
)
```

## Approve & invoke

### Manual approval Action

This package contains an Action that stops the Pipeline until someone manually clicks the approve button:

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_sns as sns


pipeline = codepipeline.Pipeline(self, "MyPipeline")
approve_stage = pipeline.add_stage(stage_name="Approve")
manual_approval_action = codepipeline_actions.ManualApprovalAction(
    action_name="Approve",
    notification_topic=sns.Topic(self, "Topic"),  # optional
    notify_emails=["some_email@example.com"
    ],  # optional
    additional_information="additional info"
)
approve_stage.add_action(manual_approval_action)
```

If the `notificationTopic` has not been provided,
but `notifyEmails` were,
a new SNS Topic will be created
(and accessible through the `notificationTopic` property of the Action).

If you want to grant a principal permissions to approve the changes,
you can invoke the method `grantManualApproval` passing it a `IGrantable`:

```python
# Example automatically generated from non-compiling source. May contain errors.
pipeline = codepipeline.Pipeline(self, "MyPipeline")
approve_stage = pipeline.add_stage(stage_name="Approve")
manual_approval_action = codepipeline_actions.ManualApprovalAction(
    action_name="Approve"
)
approve_stage.add_action(manual_approval_action)

role = iam.Role.from_role_arn(self, "Admin", Arn.format(ArnComponents(service="iam", resource="role", resource_name="Admin"), self))
manual_approval_action.grant_manual_approval(role)
```

### AWS Lambda

This module contains an Action that allows you to invoke a Lambda function in a Pipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
# fn is of type Function

pipeline = codepipeline.Pipeline(self, "MyPipeline")
lambda_action = codepipeline_actions.LambdaInvokeAction(
    action_name="Lambda",
    lambda_=fn
)
pipeline.add_stage(
    stage_name="Lambda",
    actions=[lambda_action]
)
```

The Lambda Action can have up to 5 inputs,
and up to 5 outputs:

```python
# Example automatically generated from non-compiling source. May contain errors.
# fn is of type Function

source_output = codepipeline.Artifact()
build_output = codepipeline.Artifact()
lambda_action = codepipeline_actions.LambdaInvokeAction(
    action_name="Lambda",
    inputs=[source_output, build_output
    ],
    outputs=[
        codepipeline.Artifact("Out1"),
        codepipeline.Artifact("Out2")
    ],
    lambda_=fn
)
```

The Lambda Action supports custom user parameters that pipeline
will pass to the Lambda function:

```python
# Example automatically generated from non-compiling source. May contain errors.
# fn is of type Function


pipeline = codepipeline.Pipeline(self, "MyPipeline")
lambda_action = codepipeline_actions.LambdaInvokeAction(
    action_name="Lambda",
    lambda_=fn,
    user_parameters={
        "foo": "bar",
        "baz": "qux"
    },
    # OR
    user_parameters_string="my-parameter-string"
)
```

The Lambda invoke action emits variables.
Unlike many other actions, the variables are not static,
but dynamic, defined by the function calling the `PutJobSuccessResult`
API with the `outputVariables` property filled with the map of variables
Example:

```python
# Example automatically generated from non-compiling source. May contain errors.
# later:
# project is of type PipelineProject
lambda_invoke_action = codepipeline_actions.LambdaInvokeAction(
    action_name="Lambda",
    lambda_=lambda_.Function(self, "Func",
        runtime=lambda_.Runtime.NODEJS_12_X,
        handler="index.handler",
        code=lambda_.Code.from_inline("""
                    const AWS = require('aws-sdk');

                    exports.handler = async function(event, context) {
                        const codepipeline = new AWS.CodePipeline();
                        await codepipeline.putJobSuccessResult({
                            jobId: event['CodePipeline.job'].id,
                            outputVariables: {
                                MY_VAR: "some value",
                            },
                        }).promise();
                    }
                """)
    ),
    variables_namespace="MyNamespace"
)
source_output = codepipeline.Artifact()
codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    environment_variables={
        "MyVar": codebuild.BuildEnvironmentVariable(
            value=lambda_invoke_action.variable("MY_VAR")
        )
    }
)
```

See [the AWS documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html)
on how to write a Lambda function invoked from CodePipeline.

### AWS Step Functions

This module contains an Action that allows you to invoke a Step Function in a Pipeline:

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_stepfunctions as stepfunctions

pipeline = codepipeline.Pipeline(self, "MyPipeline")
start_state = stepfunctions.Pass(self, "StartState")
simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
    definition=start_state
)
step_function_action = codepipeline_actions.StepFunctionInvokeAction(
    action_name="Invoke",
    state_machine=simple_state_machine,
    state_machine_input=codepipeline_actions.StateMachineInput.literal({"IsHelloWorldExample": True})
)
pipeline.add_stage(
    stage_name="StepFunctions",
    actions=[step_function_action]
)
```

The `StateMachineInput` can be created with one of 2 static factory methods:
`literal`, which takes an arbitrary map as its only argument, or `filePath`:

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_stepfunctions as stepfunctions


pipeline = codepipeline.Pipeline(self, "MyPipeline")
input_artifact = codepipeline.Artifact()
start_state = stepfunctions.Pass(self, "StartState")
simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
    definition=start_state
)
step_function_action = codepipeline_actions.StepFunctionInvokeAction(
    action_name="Invoke",
    state_machine=simple_state_machine,
    state_machine_input=codepipeline_actions.StateMachineInput.file_path(input_artifact.at_path("assets/input.json"))
)
pipeline.add_stage(
    stage_name="StepFunctions",
    actions=[step_function_action]
)
```

See [the AWS documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-StepFunctions.html)
for information on Action structure reference.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnCapabilities as _CfnCapabilities_f5c35b06,
    Duration as _Duration_4839e8c3,
    IResource as _IResource_c80c4260,
    SecretValue as _SecretValue_3dd0ddae,
)
from ..aws_codebuild import (
    BuildEnvironmentVariable as _BuildEnvironmentVariable_7df4fa0c,
    IProject as _IProject_aafae30a,
)
from ..aws_codecommit import IRepository as _IRepository_e7c062a1
from ..aws_codedeploy import (
    IEcsDeploymentGroup as _IEcsDeploymentGroup_6a266745,
    IServerDeploymentGroup as _IServerDeploymentGroup_b9e40f62,
)
from ..aws_codepipeline import (
    Action as _Action_db979c56,
    ActionArtifactBounds as _ActionArtifactBounds_02f3d1f6,
    ActionBindOptions as _ActionBindOptions_3a612254,
    ActionCategory as _ActionCategory_0e233e69,
    ActionConfig as _ActionConfig_846fc217,
    ActionProperties as _ActionProperties_026c42e3,
    Artifact as _Artifact_0cb05964,
    ArtifactPath as _ArtifactPath_bf444090,
    CommonActionProps as _CommonActionProps_e3aaeecb,
    CommonAwsActionProps as _CommonAwsActionProps_8b809bb6,
    IStage as _IStage_415fc571,
)
from ..aws_ecr import IRepository as _IRepository_e6004aa6
from ..aws_ecs import IBaseService as _IBaseService_3fcdd913
from ..aws_iam import (
    IGrantable as _IGrantable_71c4f5de,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_s3 import (
    BucketAccessControl as _BucketAccessControl_466c7e1b, IBucket as _IBucket_42e086fd
)
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_stepfunctions import IStateMachine as _IStateMachine_73e8d2b0


class Action(
    _Action_db979c56,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.Action",
):
    '''Low-level class for generic CodePipeline Actions.

    If you're implementing your own IAction,
    prefer to use the Action class from the codepipeline module.
    '''

    def __init__(
        self,
        *,
        action_name: builtins.str,
        artifact_bounds: _ActionArtifactBounds_02f3d1f6,
        category: _ActionCategory_0e233e69,
        provider: builtins.str,
        account: typing.Optional[builtins.str] = None,
        inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        owner: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        resource: typing.Optional[_IResource_c80c4260] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_name: 
        :param artifact_bounds: 
        :param category: The category of the action. The category defines which action type the owner (the entity that performs the action) performs.
        :param provider: The service provider that the action calls.
        :param account: The account the Action is supposed to live in. For Actions backed by resources, this is inferred from the Stack {@link resource} is part of. However, some Actions, like the CloudFormation ones, are not backed by any resource, and they still might want to be cross-account. In general, a concrete Action class should specify either {@link resource}, or {@link account} - but not both.
        :param inputs: 
        :param outputs: 
        :param owner: 
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param resource: The optional resource that is backing this Action. This is used for automatically handling Actions backed by resources from a different account and/or region.
        :param role: 
        :param run_order: The order in which AWS CodePipeline runs this action. For more information, see the AWS CodePipeline User Guide. https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names
        :param version: 
        '''
        action_properties = _ActionProperties_026c42e3(
            action_name=action_name,
            artifact_bounds=artifact_bounds,
            category=category,
            provider=provider,
            account=account,
            inputs=inputs,
            outputs=outputs,
            owner=owner,
            region=region,
            resource=resource,
            role=role,
            run_order=run_order,
            variables_namespace=variables_namespace,
            version=version,
        )

        jsii.create(self.__class__, self, [action_properties])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providedActionProperties")
    def _provided_action_properties(self) -> _ActionProperties_026c42e3:
        '''This is a renamed version of the {@link IAction.actionProperties} property.'''
        return typing.cast(_ActionProperties_026c42e3, jsii.get(self, "providedActionProperties"))


class _ActionProxy(
    Action, jsii.proxy_for(_Action_db979c56) # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Action).__jsii_proxy_class__ = lambda : _ActionProxy


class AlexaSkillDeployAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.AlexaSkillDeployAction",
):
    '''Deploys the skill to Alexa.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # Read the secrets from ParameterStore
        client_id = SecretValue.secrets_manager("AlexaClientId")
        client_secret = SecretValue.secrets_manager("AlexaClientSecret")
        refresh_token = SecretValue.secrets_manager("AlexaRefreshToken")
        
        # Add deploy action
        source_output = codepipeline.Artifact()
        codepipeline_actions.AlexaSkillDeployAction(
            action_name="DeploySkill",
            run_order=1,
            input=source_output,
            client_id=client_id.to_string(),
            client_secret=client_secret,
            refresh_token=refresh_token,
            skill_id="amzn1.ask.skill.12345678-1234-1234-1234-123456789012"
        )
    '''

    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: _SecretValue_3dd0ddae,
        input: _Artifact_0cb05964,
        refresh_token: _SecretValue_3dd0ddae,
        skill_id: builtins.str,
        parameter_overrides_artifact: typing.Optional[_Artifact_0cb05964] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The client id of the developer console token.
        :param client_secret: The client secret of the developer console token.
        :param input: The source artifact containing the voice model and skill manifest.
        :param refresh_token: The refresh token of the developer console token.
        :param skill_id: The Alexa skill id.
        :param parameter_overrides_artifact: An optional artifact containing overrides for the skill manifest.
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = AlexaSkillDeployActionProps(
            client_id=client_id,
            client_secret=client_secret,
            input=input,
            refresh_token=refresh_token,
            skill_id=skill_id,
            parameter_overrides_artifact=parameter_overrides_artifact,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        _options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, _options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.AlexaSkillDeployActionProps",
    jsii_struct_bases=[_CommonActionProps_e3aaeecb],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "input": "input",
        "refresh_token": "refreshToken",
        "skill_id": "skillId",
        "parameter_overrides_artifact": "parameterOverridesArtifact",
    },
)
class AlexaSkillDeployActionProps(_CommonActionProps_e3aaeecb):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        client_id: builtins.str,
        client_secret: _SecretValue_3dd0ddae,
        input: _Artifact_0cb05964,
        refresh_token: _SecretValue_3dd0ddae,
        skill_id: builtins.str,
        parameter_overrides_artifact: typing.Optional[_Artifact_0cb05964] = None,
    ) -> None:
        '''Construction properties of the {@link AlexaSkillDeployAction Alexa deploy Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param client_id: The client id of the developer console token.
        :param client_secret: The client secret of the developer console token.
        :param input: The source artifact containing the voice model and skill manifest.
        :param refresh_token: The refresh token of the developer console token.
        :param skill_id: The Alexa skill id.
        :param parameter_overrides_artifact: An optional artifact containing overrides for the skill manifest.

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # Read the secrets from ParameterStore
            client_id = SecretValue.secrets_manager("AlexaClientId")
            client_secret = SecretValue.secrets_manager("AlexaClientSecret")
            refresh_token = SecretValue.secrets_manager("AlexaRefreshToken")
            
            # Add deploy action
            source_output = codepipeline.Artifact()
            codepipeline_actions.AlexaSkillDeployAction(
                action_name="DeploySkill",
                run_order=1,
                input=source_output,
                client_id=client_id.to_string(),
                client_secret=client_secret,
                refresh_token=refresh_token,
                skill_id="amzn1.ask.skill.12345678-1234-1234-1234-123456789012"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "client_id": client_id,
            "client_secret": client_secret,
            "input": input,
            "refresh_token": refresh_token,
            "skill_id": skill_id,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if parameter_overrides_artifact is not None:
            self._values["parameter_overrides_artifact"] = parameter_overrides_artifact

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The client id of the developer console token.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> _SecretValue_3dd0ddae:
        '''The client secret of the developer console token.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(_SecretValue_3dd0ddae, result)

    @builtins.property
    def input(self) -> _Artifact_0cb05964:
        '''The source artifact containing the voice model and skill manifest.'''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def refresh_token(self) -> _SecretValue_3dd0ddae:
        '''The refresh token of the developer console token.'''
        result = self._values.get("refresh_token")
        assert result is not None, "Required property 'refresh_token' is missing"
        return typing.cast(_SecretValue_3dd0ddae, result)

    @builtins.property
    def skill_id(self) -> builtins.str:
        '''The Alexa skill id.'''
        result = self._values.get("skill_id")
        assert result is not None, "Required property 'skill_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_overrides_artifact(self) -> typing.Optional[_Artifact_0cb05964]:
        '''An optional artifact containing overrides for the skill manifest.'''
        result = self._values.get("parameter_overrides_artifact")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlexaSkillDeployActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CacheControl(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CacheControl",
):
    '''Used for HTTP cache-control header, which influences downstream caches.

    Use the provided static factory methods to construct instances of this class.
    Used in the {@link S3DeployActionProps.cacheControl} property.

    :see: https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codepipeline_actions as codepipeline_actions
        
        cache_control = codepipeline_actions.CacheControl.from_string("s")
    '''

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, s: builtins.str) -> "CacheControl":
        '''Allows you to create an arbitrary cache control directive, in case our support is missing a method for a particular directive.

        :param s: -
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "fromString", [s]))

    @jsii.member(jsii_name="maxAge") # type: ignore[misc]
    @builtins.classmethod
    def max_age(cls, t: _Duration_4839e8c3) -> "CacheControl":
        '''The 'max-age' cache control directive.

        :param t: -
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "maxAge", [t]))

    @jsii.member(jsii_name="mustRevalidate") # type: ignore[misc]
    @builtins.classmethod
    def must_revalidate(cls) -> "CacheControl":
        '''The 'must-revalidate' cache control directive.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "mustRevalidate", []))

    @jsii.member(jsii_name="noCache") # type: ignore[misc]
    @builtins.classmethod
    def no_cache(cls) -> "CacheControl":
        '''The 'no-cache' cache control directive.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noCache", []))

    @jsii.member(jsii_name="noTransform") # type: ignore[misc]
    @builtins.classmethod
    def no_transform(cls) -> "CacheControl":
        '''The 'no-transform' cache control directive.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noTransform", []))

    @jsii.member(jsii_name="proxyRevalidate") # type: ignore[misc]
    @builtins.classmethod
    def proxy_revalidate(cls) -> "CacheControl":
        '''The 'proxy-revalidate' cache control directive.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "proxyRevalidate", []))

    @jsii.member(jsii_name="setPrivate") # type: ignore[misc]
    @builtins.classmethod
    def set_private(cls) -> "CacheControl":
        '''The 'private' cache control directive.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "setPrivate", []))

    @jsii.member(jsii_name="setPublic") # type: ignore[misc]
    @builtins.classmethod
    def set_public(cls) -> "CacheControl":
        '''The 'public' cache control directive.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "setPublic", []))

    @jsii.member(jsii_name="sMaxAge") # type: ignore[misc]
    @builtins.classmethod
    def s_max_age(cls, t: _Duration_4839e8c3) -> "CacheControl":
        '''The 's-max-age' cache control directive.

        :param t: -
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "sMaxAge", [t]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''the actual text value of the created directive.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        jsii.set(self, "value", value)


class CloudFormationCreateReplaceChangeSetAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationCreateReplaceChangeSetAction",
):
    '''CodePipeline action to prepare a change set.

    Creates the change set if it doesn't exist based on the stack name and template that you submit.
    If the change set exists, AWS CloudFormation deletes it, and then creates a new one.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_codepipeline as codepipeline
        from aws_cdk import aws_codepipeline_actions as codepipeline_actions
        from aws_cdk import aws_iam as iam
        
        # artifact is of type Artifact
        # artifact_path is of type ArtifactPath
        # parameter_overrides is of type object
        # role is of type Role
        
        cloud_formation_create_replace_change_set_action = codepipeline_actions.CloudFormationCreateReplaceChangeSetAction(
            action_name="actionName",
            admin_permissions=False,
            change_set_name="changeSetName",
            stack_name="stackName",
            template_path=artifact_path,
        
            # the properties below are optional
            account="account",
            cfn_capabilities=[cdk.CfnCapabilities.NONE],
            deployment_role=role,
            extra_inputs=[artifact],
            output=artifact,
            output_file_name="outputFileName",
            parameter_overrides={
                "parameter_overrides_key": parameter_overrides
            },
            region="region",
            role=role,
            run_order=123,
            template_configuration=artifact_path,
            variables_namespace="variablesNamespace"
        )
    '''

    def __init__(
        self,
        *,
        admin_permissions: builtins.bool,
        change_set_name: builtins.str,
        stack_name: builtins.str,
        template_path: _ArtifactPath_bf444090,
        account: typing.Optional[builtins.str] = None,
        cfn_capabilities: typing.Optional[typing.Sequence[_CfnCapabilities_f5c35b06]] = None,
        deployment_role: typing.Optional[_IRole_235f5d8e] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        parameter_overrides: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
        template_configuration: typing.Optional[_ArtifactPath_bf444090] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
        :param change_set_name: Name of the change set to create or update.
        :param stack_name: The name of the stack to apply this action to.
        :param template_path: Input artifact with the ChangeSet's CloudFormation template.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param cfn_capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement is required that AWS CloudFormation might create or update those resources. For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information, see the link below. Default: None, unless ``adminPermissions`` is true
        :param deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        :param extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have: parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CloudFormationCreateReplaceChangeSetActionProps(
            admin_permissions=admin_permissions,
            change_set_name=change_set_name,
            stack_name=stack_name,
            template_path=template_path,
            account=account,
            cfn_capabilities=cfn_capabilities,
            deployment_role=deployment_role,
            extra_inputs=extra_inputs,
            output=output,
            output_file_name=output_file_name,
            parameter_overrides=parameter_overrides,
            region=region,
            template_configuration=template_configuration,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addToDeploymentRolePolicy")
    def add_to_deployment_role_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> builtins.bool:
        '''Add statement to the service role assumed by CloudFormation while executing this action.

        :param statement: -
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "addToDeploymentRolePolicy", [statement]))

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentRole")
    def deployment_role(self) -> _IRole_235f5d8e:
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "deploymentRole"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationCreateReplaceChangeSetActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "admin_permissions": "adminPermissions",
        "change_set_name": "changeSetName",
        "stack_name": "stackName",
        "template_path": "templatePath",
        "account": "account",
        "cfn_capabilities": "cfnCapabilities",
        "deployment_role": "deploymentRole",
        "extra_inputs": "extraInputs",
        "output": "output",
        "output_file_name": "outputFileName",
        "parameter_overrides": "parameterOverrides",
        "region": "region",
        "template_configuration": "templateConfiguration",
    },
)
class CloudFormationCreateReplaceChangeSetActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        admin_permissions: builtins.bool,
        change_set_name: builtins.str,
        stack_name: builtins.str,
        template_path: _ArtifactPath_bf444090,
        account: typing.Optional[builtins.str] = None,
        cfn_capabilities: typing.Optional[typing.Sequence[_CfnCapabilities_f5c35b06]] = None,
        deployment_role: typing.Optional[_IRole_235f5d8e] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        parameter_overrides: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
        template_configuration: typing.Optional[_ArtifactPath_bf444090] = None,
    ) -> None:
        '''Properties for the CloudFormationCreateReplaceChangeSetAction.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
        :param change_set_name: Name of the change set to create or update.
        :param stack_name: The name of the stack to apply this action to.
        :param template_path: Input artifact with the ChangeSet's CloudFormation template.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param cfn_capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement is required that AWS CloudFormation might create or update those resources. For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information, see the link below. Default: None, unless ``adminPermissions`` is true
        :param deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        :param extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have: parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_codepipeline as codepipeline
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            from aws_cdk import aws_iam as iam
            
            # artifact is of type Artifact
            # artifact_path is of type ArtifactPath
            # parameter_overrides is of type object
            # role is of type Role
            
            cloud_formation_create_replace_change_set_action_props = codepipeline_actions.CloudFormationCreateReplaceChangeSetActionProps(
                action_name="actionName",
                admin_permissions=False,
                change_set_name="changeSetName",
                stack_name="stackName",
                template_path=artifact_path,
            
                # the properties below are optional
                account="account",
                cfn_capabilities=[cdk.CfnCapabilities.NONE],
                deployment_role=role,
                extra_inputs=[artifact],
                output=artifact,
                output_file_name="outputFileName",
                parameter_overrides={
                    "parameter_overrides_key": parameter_overrides
                },
                region="region",
                role=role,
                run_order=123,
                template_configuration=artifact_path,
                variables_namespace="variablesNamespace"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "admin_permissions": admin_permissions,
            "change_set_name": change_set_name,
            "stack_name": stack_name,
            "template_path": template_path,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if account is not None:
            self._values["account"] = account
        if cfn_capabilities is not None:
            self._values["cfn_capabilities"] = cfn_capabilities
        if deployment_role is not None:
            self._values["deployment_role"] = deployment_role
        if extra_inputs is not None:
            self._values["extra_inputs"] = extra_inputs
        if output is not None:
            self._values["output"] = output
        if output_file_name is not None:
            self._values["output_file_name"] = output_file_name
        if parameter_overrides is not None:
            self._values["parameter_overrides"] = parameter_overrides
        if region is not None:
            self._values["region"] = region
        if template_configuration is not None:
            self._values["template_configuration"] = template_configuration

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def admin_permissions(self) -> builtins.bool:
        '''Whether to grant full permissions to CloudFormation while deploying this template.

        Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you
        don't specify any alternatives.

        The default role that will be created for you will have full (i.e., ``*``)
        permissions on all resources, and the deployment will have named IAM
        capabilities (i.e., able to create all IAM resources).

        This is a shorthand that you can use if you fully trust the templates that
        are deployed in this pipeline. If you want more fine-grained permissions,
        use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation
        deployment is allowed to do.
        '''
        result = self._values.get("admin_permissions")
        assert result is not None, "Required property 'admin_permissions' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def change_set_name(self) -> builtins.str:
        '''Name of the change set to create or update.'''
        result = self._values.get("change_set_name")
        assert result is not None, "Required property 'change_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack to apply this action to.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_path(self) -> _ArtifactPath_bf444090:
        '''Input artifact with the ChangeSet's CloudFormation template.'''
        result = self._values.get("template_path")
        assert result is not None, "Required property 'template_path' is missing"
        return typing.cast(_ArtifactPath_bf444090, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account this Action is supposed to operate in.

        **Note**: if you specify the ``role`` property,
        this is ignored - the action will operate in the same region the passed role does.

        :default: - action resides in the same account as the pipeline
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cfn_capabilities(
        self,
    ) -> typing.Optional[typing.List[_CfnCapabilities_f5c35b06]]:
        '''Acknowledge certain changes made as part of deployment.

        For stacks that contain certain resources,
        explicit acknowledgement is required that AWS CloudFormation might create or update those resources.
        For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS
        Identity and Access Management (IAM) resources.
        For more information, see the link below.

        :default: None, unless ``adminPermissions`` is true

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
        '''
        result = self._values.get("cfn_capabilities")
        return typing.cast(typing.Optional[typing.List[_CfnCapabilities_f5c35b06]], result)

    @builtins.property
    def deployment_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''IAM role to assume when deploying changes.

        If not specified, a fresh role is created. The role is created with zero
        permissions unless ``adminPermissions`` is true, in which case the role will have
        full permissions.

        :default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        '''
        result = self._values.get("deployment_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def extra_inputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The list of additional input Artifacts for this Action.

        This is especially useful when used in conjunction with the ``parameterOverrides`` property.
        For example, if you have:

        parameterOverrides: {
        'Param1': action1.outputArtifact.bucketName,
        'Param2': action2.outputArtifact.objectKey,
        }

        , if the output Artifacts of ``action1`` and ``action2`` were not used to
        set either the ``templateConfiguration`` or the ``templatePath`` properties,
        you need to make sure to include them in the ``extraInputs`` -
        otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        '''
        result = self._values.get("extra_inputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def output(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The name of the output artifact to generate.

        Only applied if ``outputFileName`` is set as well.

        :default: Automatically generated artifact name.
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def output_file_name(self) -> typing.Optional[builtins.str]:
        '''A name for the filename in the output artifact to store the AWS CloudFormation call's result.

        The file will contain the result of the call to AWS CloudFormation (for example
        the call to UpdateStack or CreateChangeSet).

        AWS CodePipeline adds the file to the output artifact after performing
        the specified action.

        :default: No output artifact generated
        '''
        result = self._values.get("output_file_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional template parameters.

        Template parameters specified here take precedence over template parameters
        found in the artifact specified by the ``templateConfiguration`` property.

        We recommend that you use the template configuration file to specify
        most of your parameter values. Use parameter overrides to specify only
        dynamic parameter values (values that are unknown until you run the
        pipeline).

        All parameter names must be present in the stack template.

        Note: the entire object cannot be more than 1kB.

        :default: No overrides
        '''
        result = self._values.get("parameter_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region the given Action resides in.

        Note that a cross-region Pipeline requires replication buckets to function correctly.
        You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property.
        If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets,
        that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

        :default: the Action resides in the same region as the Pipeline
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_configuration(self) -> typing.Optional[_ArtifactPath_bf444090]:
        '''Input artifact to use for template parameters values and stack policy.

        The template configuration file should contain a JSON object that should look like this:
        ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information,
        see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_.

        Note that if you include sensitive information, such as passwords, restrict access to this
        file.

        :default: No template configuration based on input artifacts
        '''
        result = self._values.get("template_configuration")
        return typing.cast(typing.Optional[_ArtifactPath_bf444090], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationCreateReplaceChangeSetActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationCreateUpdateStackAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationCreateUpdateStackAction",
):
    '''CodePipeline action to deploy a stack.

    Creates the stack if the specified stack doesn't exist. If the stack exists,
    AWS CloudFormation updates the stack. Use this action to update existing
    stacks.

    AWS CodePipeline won't replace the stack, and will fail deployment if the
    stack is in a failed state. Use ``ReplaceOnFailure`` for an action that
    will delete and recreate the stack to try and recover from failed states.

    Use this action to automatically replace failed stacks without recovering or
    troubleshooting them. You would typically choose this mode for testing.

    :exampleMetadata: infused

    Example::

        # Actions that don't accept a resource objet accept an explicit `account` parameter
        # stage is of type IStage
        # template_path is of type ArtifactPath
        
        stage.add_action(codepipeline_actions.CloudFormationCreateUpdateStackAction(
            account="123456789012",
            template_path=template_path,
            admin_permissions=False,
            stack_name=Stack.of(self).stack_name,
            action_name="cloudformation-create-update"
        ))
    '''

    def __init__(
        self,
        *,
        admin_permissions: builtins.bool,
        stack_name: builtins.str,
        template_path: _ArtifactPath_bf444090,
        account: typing.Optional[builtins.str] = None,
        cfn_capabilities: typing.Optional[typing.Sequence[_CfnCapabilities_f5c35b06]] = None,
        deployment_role: typing.Optional[_IRole_235f5d8e] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        parameter_overrides: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
        replace_on_failure: typing.Optional[builtins.bool] = None,
        template_configuration: typing.Optional[_ArtifactPath_bf444090] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
        :param stack_name: The name of the stack to apply this action to.
        :param template_path: Input artifact with the CloudFormation template to deploy.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param cfn_capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement is required that AWS CloudFormation might create or update those resources. For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information, see the link below. Default: None, unless ``adminPermissions`` is true
        :param deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        :param extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have: parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param replace_on_failure: Replace the stack if it's in a failed state. If this is set to true and the stack is in a failed state (one of ROLLBACK_COMPLETE, ROLLBACK_FAILED, CREATE_FAILED, DELETE_FAILED, or UPDATE_ROLLBACK_FAILED), AWS CloudFormation deletes the stack and then creates a new stack. If this is not set to true and the stack is in a failed state, the deployment fails. Default: false
        :param template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CloudFormationCreateUpdateStackActionProps(
            admin_permissions=admin_permissions,
            stack_name=stack_name,
            template_path=template_path,
            account=account,
            cfn_capabilities=cfn_capabilities,
            deployment_role=deployment_role,
            extra_inputs=extra_inputs,
            output=output,
            output_file_name=output_file_name,
            parameter_overrides=parameter_overrides,
            region=region,
            replace_on_failure=replace_on_failure,
            template_configuration=template_configuration,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addToDeploymentRolePolicy")
    def add_to_deployment_role_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> builtins.bool:
        '''Add statement to the service role assumed by CloudFormation while executing this action.

        :param statement: -
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "addToDeploymentRolePolicy", [statement]))

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentRole")
    def deployment_role(self) -> _IRole_235f5d8e:
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "deploymentRole"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationCreateUpdateStackActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "admin_permissions": "adminPermissions",
        "stack_name": "stackName",
        "template_path": "templatePath",
        "account": "account",
        "cfn_capabilities": "cfnCapabilities",
        "deployment_role": "deploymentRole",
        "extra_inputs": "extraInputs",
        "output": "output",
        "output_file_name": "outputFileName",
        "parameter_overrides": "parameterOverrides",
        "region": "region",
        "replace_on_failure": "replaceOnFailure",
        "template_configuration": "templateConfiguration",
    },
)
class CloudFormationCreateUpdateStackActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        admin_permissions: builtins.bool,
        stack_name: builtins.str,
        template_path: _ArtifactPath_bf444090,
        account: typing.Optional[builtins.str] = None,
        cfn_capabilities: typing.Optional[typing.Sequence[_CfnCapabilities_f5c35b06]] = None,
        deployment_role: typing.Optional[_IRole_235f5d8e] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        parameter_overrides: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
        replace_on_failure: typing.Optional[builtins.bool] = None,
        template_configuration: typing.Optional[_ArtifactPath_bf444090] = None,
    ) -> None:
        '''Properties for the CloudFormationCreateUpdateStackAction.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
        :param stack_name: The name of the stack to apply this action to.
        :param template_path: Input artifact with the CloudFormation template to deploy.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param cfn_capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement is required that AWS CloudFormation might create or update those resources. For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information, see the link below. Default: None, unless ``adminPermissions`` is true
        :param deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        :param extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have: parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param replace_on_failure: Replace the stack if it's in a failed state. If this is set to true and the stack is in a failed state (one of ROLLBACK_COMPLETE, ROLLBACK_FAILED, CREATE_FAILED, DELETE_FAILED, or UPDATE_ROLLBACK_FAILED), AWS CloudFormation deletes the stack and then creates a new stack. If this is not set to true and the stack is in a failed state, the deployment fails. Default: false
        :param template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts

        :exampleMetadata: infused

        Example::

            # Actions that don't accept a resource objet accept an explicit `account` parameter
            # stage is of type IStage
            # template_path is of type ArtifactPath
            
            stage.add_action(codepipeline_actions.CloudFormationCreateUpdateStackAction(
                account="123456789012",
                template_path=template_path,
                admin_permissions=False,
                stack_name=Stack.of(self).stack_name,
                action_name="cloudformation-create-update"
            ))
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "admin_permissions": admin_permissions,
            "stack_name": stack_name,
            "template_path": template_path,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if account is not None:
            self._values["account"] = account
        if cfn_capabilities is not None:
            self._values["cfn_capabilities"] = cfn_capabilities
        if deployment_role is not None:
            self._values["deployment_role"] = deployment_role
        if extra_inputs is not None:
            self._values["extra_inputs"] = extra_inputs
        if output is not None:
            self._values["output"] = output
        if output_file_name is not None:
            self._values["output_file_name"] = output_file_name
        if parameter_overrides is not None:
            self._values["parameter_overrides"] = parameter_overrides
        if region is not None:
            self._values["region"] = region
        if replace_on_failure is not None:
            self._values["replace_on_failure"] = replace_on_failure
        if template_configuration is not None:
            self._values["template_configuration"] = template_configuration

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def admin_permissions(self) -> builtins.bool:
        '''Whether to grant full permissions to CloudFormation while deploying this template.

        Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you
        don't specify any alternatives.

        The default role that will be created for you will have full (i.e., ``*``)
        permissions on all resources, and the deployment will have named IAM
        capabilities (i.e., able to create all IAM resources).

        This is a shorthand that you can use if you fully trust the templates that
        are deployed in this pipeline. If you want more fine-grained permissions,
        use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation
        deployment is allowed to do.
        '''
        result = self._values.get("admin_permissions")
        assert result is not None, "Required property 'admin_permissions' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack to apply this action to.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_path(self) -> _ArtifactPath_bf444090:
        '''Input artifact with the CloudFormation template to deploy.'''
        result = self._values.get("template_path")
        assert result is not None, "Required property 'template_path' is missing"
        return typing.cast(_ArtifactPath_bf444090, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account this Action is supposed to operate in.

        **Note**: if you specify the ``role`` property,
        this is ignored - the action will operate in the same region the passed role does.

        :default: - action resides in the same account as the pipeline
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cfn_capabilities(
        self,
    ) -> typing.Optional[typing.List[_CfnCapabilities_f5c35b06]]:
        '''Acknowledge certain changes made as part of deployment.

        For stacks that contain certain resources,
        explicit acknowledgement is required that AWS CloudFormation might create or update those resources.
        For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS
        Identity and Access Management (IAM) resources.
        For more information, see the link below.

        :default: None, unless ``adminPermissions`` is true

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
        '''
        result = self._values.get("cfn_capabilities")
        return typing.cast(typing.Optional[typing.List[_CfnCapabilities_f5c35b06]], result)

    @builtins.property
    def deployment_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''IAM role to assume when deploying changes.

        If not specified, a fresh role is created. The role is created with zero
        permissions unless ``adminPermissions`` is true, in which case the role will have
        full permissions.

        :default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        '''
        result = self._values.get("deployment_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def extra_inputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The list of additional input Artifacts for this Action.

        This is especially useful when used in conjunction with the ``parameterOverrides`` property.
        For example, if you have:

        parameterOverrides: {
        'Param1': action1.outputArtifact.bucketName,
        'Param2': action2.outputArtifact.objectKey,
        }

        , if the output Artifacts of ``action1`` and ``action2`` were not used to
        set either the ``templateConfiguration`` or the ``templatePath`` properties,
        you need to make sure to include them in the ``extraInputs`` -
        otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        '''
        result = self._values.get("extra_inputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def output(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The name of the output artifact to generate.

        Only applied if ``outputFileName`` is set as well.

        :default: Automatically generated artifact name.
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def output_file_name(self) -> typing.Optional[builtins.str]:
        '''A name for the filename in the output artifact to store the AWS CloudFormation call's result.

        The file will contain the result of the call to AWS CloudFormation (for example
        the call to UpdateStack or CreateChangeSet).

        AWS CodePipeline adds the file to the output artifact after performing
        the specified action.

        :default: No output artifact generated
        '''
        result = self._values.get("output_file_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional template parameters.

        Template parameters specified here take precedence over template parameters
        found in the artifact specified by the ``templateConfiguration`` property.

        We recommend that you use the template configuration file to specify
        most of your parameter values. Use parameter overrides to specify only
        dynamic parameter values (values that are unknown until you run the
        pipeline).

        All parameter names must be present in the stack template.

        Note: the entire object cannot be more than 1kB.

        :default: No overrides
        '''
        result = self._values.get("parameter_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region the given Action resides in.

        Note that a cross-region Pipeline requires replication buckets to function correctly.
        You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property.
        If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets,
        that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

        :default: the Action resides in the same region as the Pipeline
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replace_on_failure(self) -> typing.Optional[builtins.bool]:
        '''Replace the stack if it's in a failed state.

        If this is set to true and the stack is in a failed state (one of
        ROLLBACK_COMPLETE, ROLLBACK_FAILED, CREATE_FAILED, DELETE_FAILED, or
        UPDATE_ROLLBACK_FAILED), AWS CloudFormation deletes the stack and then
        creates a new stack.

        If this is not set to true and the stack is in a failed state,
        the deployment fails.

        :default: false
        '''
        result = self._values.get("replace_on_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def template_configuration(self) -> typing.Optional[_ArtifactPath_bf444090]:
        '''Input artifact to use for template parameters values and stack policy.

        The template configuration file should contain a JSON object that should look like this:
        ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information,
        see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_.

        Note that if you include sensitive information, such as passwords, restrict access to this
        file.

        :default: No template configuration based on input artifacts
        '''
        result = self._values.get("template_configuration")
        return typing.cast(typing.Optional[_ArtifactPath_bf444090], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationCreateUpdateStackActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationDeleteStackAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationDeleteStackAction",
):
    '''CodePipeline action to delete a stack.

    Deletes a stack. If you specify a stack that doesn't exist, the action completes successfully
    without deleting a stack.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_codepipeline as codepipeline
        from aws_cdk import aws_codepipeline_actions as codepipeline_actions
        from aws_cdk import aws_iam as iam
        
        # artifact is of type Artifact
        # artifact_path is of type ArtifactPath
        # parameter_overrides is of type object
        # role is of type Role
        
        cloud_formation_delete_stack_action = codepipeline_actions.CloudFormationDeleteStackAction(
            action_name="actionName",
            admin_permissions=False,
            stack_name="stackName",
        
            # the properties below are optional
            account="account",
            cfn_capabilities=[cdk.CfnCapabilities.NONE],
            deployment_role=role,
            extra_inputs=[artifact],
            output=artifact,
            output_file_name="outputFileName",
            parameter_overrides={
                "parameter_overrides_key": parameter_overrides
            },
            region="region",
            role=role,
            run_order=123,
            template_configuration=artifact_path,
            variables_namespace="variablesNamespace"
        )
    '''

    def __init__(
        self,
        *,
        admin_permissions: builtins.bool,
        stack_name: builtins.str,
        account: typing.Optional[builtins.str] = None,
        cfn_capabilities: typing.Optional[typing.Sequence[_CfnCapabilities_f5c35b06]] = None,
        deployment_role: typing.Optional[_IRole_235f5d8e] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        parameter_overrides: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
        template_configuration: typing.Optional[_ArtifactPath_bf444090] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
        :param stack_name: The name of the stack to apply this action to.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param cfn_capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement is required that AWS CloudFormation might create or update those resources. For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information, see the link below. Default: None, unless ``adminPermissions`` is true
        :param deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        :param extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have: parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CloudFormationDeleteStackActionProps(
            admin_permissions=admin_permissions,
            stack_name=stack_name,
            account=account,
            cfn_capabilities=cfn_capabilities,
            deployment_role=deployment_role,
            extra_inputs=extra_inputs,
            output=output,
            output_file_name=output_file_name,
            parameter_overrides=parameter_overrides,
            region=region,
            template_configuration=template_configuration,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addToDeploymentRolePolicy")
    def add_to_deployment_role_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> builtins.bool:
        '''Add statement to the service role assumed by CloudFormation while executing this action.

        :param statement: -
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "addToDeploymentRolePolicy", [statement]))

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentRole")
    def deployment_role(self) -> _IRole_235f5d8e:
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "deploymentRole"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationDeleteStackActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "admin_permissions": "adminPermissions",
        "stack_name": "stackName",
        "account": "account",
        "cfn_capabilities": "cfnCapabilities",
        "deployment_role": "deploymentRole",
        "extra_inputs": "extraInputs",
        "output": "output",
        "output_file_name": "outputFileName",
        "parameter_overrides": "parameterOverrides",
        "region": "region",
        "template_configuration": "templateConfiguration",
    },
)
class CloudFormationDeleteStackActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        admin_permissions: builtins.bool,
        stack_name: builtins.str,
        account: typing.Optional[builtins.str] = None,
        cfn_capabilities: typing.Optional[typing.Sequence[_CfnCapabilities_f5c35b06]] = None,
        deployment_role: typing.Optional[_IRole_235f5d8e] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        parameter_overrides: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
        template_configuration: typing.Optional[_ArtifactPath_bf444090] = None,
    ) -> None:
        '''Properties for the CloudFormationDeleteStackAction.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
        :param stack_name: The name of the stack to apply this action to.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param cfn_capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement is required that AWS CloudFormation might create or update those resources. For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information, see the link below. Default: None, unless ``adminPermissions`` is true
        :param deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        :param extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have: parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_codepipeline as codepipeline
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            from aws_cdk import aws_iam as iam
            
            # artifact is of type Artifact
            # artifact_path is of type ArtifactPath
            # parameter_overrides is of type object
            # role is of type Role
            
            cloud_formation_delete_stack_action_props = codepipeline_actions.CloudFormationDeleteStackActionProps(
                action_name="actionName",
                admin_permissions=False,
                stack_name="stackName",
            
                # the properties below are optional
                account="account",
                cfn_capabilities=[cdk.CfnCapabilities.NONE],
                deployment_role=role,
                extra_inputs=[artifact],
                output=artifact,
                output_file_name="outputFileName",
                parameter_overrides={
                    "parameter_overrides_key": parameter_overrides
                },
                region="region",
                role=role,
                run_order=123,
                template_configuration=artifact_path,
                variables_namespace="variablesNamespace"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "admin_permissions": admin_permissions,
            "stack_name": stack_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if account is not None:
            self._values["account"] = account
        if cfn_capabilities is not None:
            self._values["cfn_capabilities"] = cfn_capabilities
        if deployment_role is not None:
            self._values["deployment_role"] = deployment_role
        if extra_inputs is not None:
            self._values["extra_inputs"] = extra_inputs
        if output is not None:
            self._values["output"] = output
        if output_file_name is not None:
            self._values["output_file_name"] = output_file_name
        if parameter_overrides is not None:
            self._values["parameter_overrides"] = parameter_overrides
        if region is not None:
            self._values["region"] = region
        if template_configuration is not None:
            self._values["template_configuration"] = template_configuration

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def admin_permissions(self) -> builtins.bool:
        '''Whether to grant full permissions to CloudFormation while deploying this template.

        Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you
        don't specify any alternatives.

        The default role that will be created for you will have full (i.e., ``*``)
        permissions on all resources, and the deployment will have named IAM
        capabilities (i.e., able to create all IAM resources).

        This is a shorthand that you can use if you fully trust the templates that
        are deployed in this pipeline. If you want more fine-grained permissions,
        use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation
        deployment is allowed to do.
        '''
        result = self._values.get("admin_permissions")
        assert result is not None, "Required property 'admin_permissions' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack to apply this action to.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account this Action is supposed to operate in.

        **Note**: if you specify the ``role`` property,
        this is ignored - the action will operate in the same region the passed role does.

        :default: - action resides in the same account as the pipeline
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cfn_capabilities(
        self,
    ) -> typing.Optional[typing.List[_CfnCapabilities_f5c35b06]]:
        '''Acknowledge certain changes made as part of deployment.

        For stacks that contain certain resources,
        explicit acknowledgement is required that AWS CloudFormation might create or update those resources.
        For example, you must specify ``ANONYMOUS_IAM`` or ``NAMED_IAM`` if your stack template contains AWS
        Identity and Access Management (IAM) resources.
        For more information, see the link below.

        :default: None, unless ``adminPermissions`` is true

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
        '''
        result = self._values.get("cfn_capabilities")
        return typing.cast(typing.Optional[typing.List[_CfnCapabilities_f5c35b06]], result)

    @builtins.property
    def deployment_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''IAM role to assume when deploying changes.

        If not specified, a fresh role is created. The role is created with zero
        permissions unless ``adminPermissions`` is true, in which case the role will have
        full permissions.

        :default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
        '''
        result = self._values.get("deployment_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def extra_inputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The list of additional input Artifacts for this Action.

        This is especially useful when used in conjunction with the ``parameterOverrides`` property.
        For example, if you have:

        parameterOverrides: {
        'Param1': action1.outputArtifact.bucketName,
        'Param2': action2.outputArtifact.objectKey,
        }

        , if the output Artifacts of ``action1`` and ``action2`` were not used to
        set either the ``templateConfiguration`` or the ``templatePath`` properties,
        you need to make sure to include them in the ``extraInputs`` -
        otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
        '''
        result = self._values.get("extra_inputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def output(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The name of the output artifact to generate.

        Only applied if ``outputFileName`` is set as well.

        :default: Automatically generated artifact name.
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def output_file_name(self) -> typing.Optional[builtins.str]:
        '''A name for the filename in the output artifact to store the AWS CloudFormation call's result.

        The file will contain the result of the call to AWS CloudFormation (for example
        the call to UpdateStack or CreateChangeSet).

        AWS CodePipeline adds the file to the output artifact after performing
        the specified action.

        :default: No output artifact generated
        '''
        result = self._values.get("output_file_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional template parameters.

        Template parameters specified here take precedence over template parameters
        found in the artifact specified by the ``templateConfiguration`` property.

        We recommend that you use the template configuration file to specify
        most of your parameter values. Use parameter overrides to specify only
        dynamic parameter values (values that are unknown until you run the
        pipeline).

        All parameter names must be present in the stack template.

        Note: the entire object cannot be more than 1kB.

        :default: No overrides
        '''
        result = self._values.get("parameter_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region the given Action resides in.

        Note that a cross-region Pipeline requires replication buckets to function correctly.
        You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property.
        If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets,
        that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

        :default: the Action resides in the same region as the Pipeline
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_configuration(self) -> typing.Optional[_ArtifactPath_bf444090]:
        '''Input artifact to use for template parameters values and stack policy.

        The template configuration file should contain a JSON object that should look like this:
        ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information,
        see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_.

        Note that if you include sensitive information, such as passwords, restrict access to this
        file.

        :default: No template configuration based on input artifacts
        '''
        result = self._values.get("template_configuration")
        return typing.cast(typing.Optional[_ArtifactPath_bf444090], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationDeleteStackActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationExecuteChangeSetAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationExecuteChangeSetAction",
):
    '''CodePipeline action to execute a prepared change set.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # Deploy some CFN change set and store output
        execute_output = codepipeline.Artifact("CloudFormation")
        execute_change_set_action = codepipeline_actions.CloudFormationExecuteChangeSetAction(
            action_name="ExecuteChangesTest",
            run_order=2,
            stack_name="MyStack",
            change_set_name="MyChangeSet",
            output_file_name="overrides.json",
            output=execute_output
        )
        
        # Provide CFN output as manifest overrides
        client_id = SecretValue.secrets_manager("AlexaClientId")
        client_secret = SecretValue.secrets_manager("AlexaClientSecret")
        refresh_token = SecretValue.secrets_manager("AlexaRefreshToken")
        source_output = codepipeline.Artifact()
        codepipeline_actions.AlexaSkillDeployAction(
            action_name="DeploySkill",
            run_order=1,
            input=source_output,
            parameter_overrides_artifact=execute_output,
            client_id=client_id.to_string(),
            client_secret=client_secret,
            refresh_token=refresh_token,
            skill_id="amzn1.ask.skill.12345678-1234-1234-1234-123456789012"
        )
    '''

    def __init__(
        self,
        *,
        change_set_name: builtins.str,
        stack_name: builtins.str,
        account: typing.Optional[builtins.str] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param change_set_name: Name of the change set to execute.
        :param stack_name: The name of the stack to apply this action to.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CloudFormationExecuteChangeSetActionProps(
            change_set_name=change_set_name,
            stack_name=stack_name,
            account=account,
            output=output,
            output_file_name=output_file_name,
            region=region,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CloudFormationExecuteChangeSetActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "change_set_name": "changeSetName",
        "stack_name": "stackName",
        "account": "account",
        "output": "output",
        "output_file_name": "outputFileName",
        "region": "region",
    },
)
class CloudFormationExecuteChangeSetActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        change_set_name: builtins.str,
        stack_name: builtins.str,
        account: typing.Optional[builtins.str] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        output_file_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for the CloudFormationExecuteChangeSetAction.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param change_set_name: Name of the change set to execute.
        :param stack_name: The name of the stack to apply this action to.
        :param account: The AWS account this Action is supposed to operate in. **Note**: if you specify the ``role`` property, this is ignored - the action will operate in the same region the passed role does. Default: - action resides in the same account as the pipeline
        :param output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
        :param output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
        :param region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # Deploy some CFN change set and store output
            execute_output = codepipeline.Artifact("CloudFormation")
            execute_change_set_action = codepipeline_actions.CloudFormationExecuteChangeSetAction(
                action_name="ExecuteChangesTest",
                run_order=2,
                stack_name="MyStack",
                change_set_name="MyChangeSet",
                output_file_name="overrides.json",
                output=execute_output
            )
            
            # Provide CFN output as manifest overrides
            client_id = SecretValue.secrets_manager("AlexaClientId")
            client_secret = SecretValue.secrets_manager("AlexaClientSecret")
            refresh_token = SecretValue.secrets_manager("AlexaRefreshToken")
            source_output = codepipeline.Artifact()
            codepipeline_actions.AlexaSkillDeployAction(
                action_name="DeploySkill",
                run_order=1,
                input=source_output,
                parameter_overrides_artifact=execute_output,
                client_id=client_id.to_string(),
                client_secret=client_secret,
                refresh_token=refresh_token,
                skill_id="amzn1.ask.skill.12345678-1234-1234-1234-123456789012"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "change_set_name": change_set_name,
            "stack_name": stack_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if account is not None:
            self._values["account"] = account
        if output is not None:
            self._values["output"] = output
        if output_file_name is not None:
            self._values["output_file_name"] = output_file_name
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def change_set_name(self) -> builtins.str:
        '''Name of the change set to execute.'''
        result = self._values.get("change_set_name")
        assert result is not None, "Required property 'change_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack to apply this action to.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account this Action is supposed to operate in.

        **Note**: if you specify the ``role`` property,
        this is ignored - the action will operate in the same region the passed role does.

        :default: - action resides in the same account as the pipeline
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The name of the output artifact to generate.

        Only applied if ``outputFileName`` is set as well.

        :default: Automatically generated artifact name.
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def output_file_name(self) -> typing.Optional[builtins.str]:
        '''A name for the filename in the output artifact to store the AWS CloudFormation call's result.

        The file will contain the result of the call to AWS CloudFormation (for example
        the call to UpdateStack or CreateChangeSet).

        AWS CodePipeline adds the file to the output artifact after performing
        the specified action.

        :default: No output artifact generated
        '''
        result = self._values.get("output_file_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region the given Action resides in.

        Note that a cross-region Pipeline requires replication buckets to function correctly.
        You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property.
        If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets,
        that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

        :default: the Action resides in the same region as the Pipeline
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationExecuteChangeSetActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodeBuildAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeBuildAction",
):
    '''CodePipeline build action that uses AWS CodeBuild.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # source_bucket is of type Bucket
        
        # later:
        # project is of type PipelineProject
        key = "some/key.zip"
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.S3SourceAction(
            action_name="S3Source",
            bucket_key=key,
            bucket=source_bucket,
            output=source_output,
            variables_namespace="MyNamespace"
        )
        codepipeline_actions.CodeBuildAction(
            action_name="CodeBuild",
            project=project,
            input=source_output,
            environment_variables={
                "VERSION_ID": codebuild.BuildEnvironmentVariable(
                    value=source_action.variables.version_id
                )
            }
        )
    '''

    def __init__(
        self,
        *,
        input: _Artifact_0cb05964,
        project: _IProject_aafae30a,
        check_secrets_in_plain_text_env_variables: typing.Optional[builtins.bool] = None,
        combine_batch_build_artifacts: typing.Optional[builtins.bool] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, _BuildEnvironmentVariable_7df4fa0c]] = None,
        execute_batch_build: typing.Optional[builtins.bool] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        type: typing.Optional["CodeBuildActionType"] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input: The source to use as input for this action.
        :param project: The action's Project.
        :param check_secrets_in_plain_text_env_variables: Whether to check for the presence of any secrets in the environment variables of the default type, BuildEnvironmentVariableType.PLAINTEXT. Since using a secret for the value of that kind of variable would result in it being displayed in plain text in the AWS Console, the construct will throw an exception if it detects a secret was passed there. Pass this property as false if you want to skip this validation, and keep using a secret in a plain text environment variable. Default: true
        :param combine_batch_build_artifacts: Combine the build artifacts for a batch builds. Enabling this will combine the build artifacts into the same location for batch builds. If ``executeBatchBuild`` is not set to ``true``, this property is ignored. Default: false
        :param environment_variables: The environment variables to pass to the CodeBuild project when this action executes. If a variable with the same name was set both on the project level, and here, this value will take precedence. Default: - No additional environment variables are specified.
        :param execute_batch_build: Trigger a batch build. Enabling this will enable batch builds on the CodeBuild project. Default: false
        :param extra_inputs: The list of additional input Artifacts for this action. The directories the additional inputs will be available at are available during the project's build in the CODEBUILD_SRC_DIR_ environment variables. The project's build always starts in the directory with the primary input artifact checked out, the one pointed to by the {@link input} property. For more information, see https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html .
        :param outputs: The list of output Artifacts for this action. **Note**: if you specify more than one output Artifact here, you cannot use the primary 'artifacts' section of the buildspec; you have to use the 'secondary-artifacts' section instead. See https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html for details. Default: the action will not have any outputs
        :param type: The type of the action that determines its CodePipeline Category - Build, or Test. Default: CodeBuildActionType.BUILD
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodeBuildActionProps(
            input=input,
            project=project,
            check_secrets_in_plain_text_env_variables=check_secrets_in_plain_text_env_variables,
            combine_batch_build_artifacts=combine_batch_build_artifacts,
            environment_variables=environment_variables,
            execute_batch_build=execute_batch_build,
            extra_inputs=extra_inputs,
            outputs=outputs,
            type=type,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, _stage, options]))

    @jsii.member(jsii_name="variable")
    def variable(self, variable_name: builtins.str) -> builtins.str:
        '''Reference a CodePipeline variable defined by the CodeBuild project this action points to.

        Variables in CodeBuild actions are defined using the 'exported-variables' subsection of the 'env'
        section of the buildspec.

        :param variable_name: the name of the variable to reference. A variable by this name must be present in the 'exported-variables' section of the buildspec

        :see: https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-syntax
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "variable", [variable_name]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeBuildActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "input": "input",
        "project": "project",
        "check_secrets_in_plain_text_env_variables": "checkSecretsInPlainTextEnvVariables",
        "combine_batch_build_artifacts": "combineBatchBuildArtifacts",
        "environment_variables": "environmentVariables",
        "execute_batch_build": "executeBatchBuild",
        "extra_inputs": "extraInputs",
        "outputs": "outputs",
        "type": "type",
    },
)
class CodeBuildActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        input: _Artifact_0cb05964,
        project: _IProject_aafae30a,
        check_secrets_in_plain_text_env_variables: typing.Optional[builtins.bool] = None,
        combine_batch_build_artifacts: typing.Optional[builtins.bool] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, _BuildEnvironmentVariable_7df4fa0c]] = None,
        execute_batch_build: typing.Optional[builtins.bool] = None,
        extra_inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        type: typing.Optional["CodeBuildActionType"] = None,
    ) -> None:
        '''Construction properties of the {@link CodeBuildAction CodeBuild build CodePipeline action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param input: The source to use as input for this action.
        :param project: The action's Project.
        :param check_secrets_in_plain_text_env_variables: Whether to check for the presence of any secrets in the environment variables of the default type, BuildEnvironmentVariableType.PLAINTEXT. Since using a secret for the value of that kind of variable would result in it being displayed in plain text in the AWS Console, the construct will throw an exception if it detects a secret was passed there. Pass this property as false if you want to skip this validation, and keep using a secret in a plain text environment variable. Default: true
        :param combine_batch_build_artifacts: Combine the build artifacts for a batch builds. Enabling this will combine the build artifacts into the same location for batch builds. If ``executeBatchBuild`` is not set to ``true``, this property is ignored. Default: false
        :param environment_variables: The environment variables to pass to the CodeBuild project when this action executes. If a variable with the same name was set both on the project level, and here, this value will take precedence. Default: - No additional environment variables are specified.
        :param execute_batch_build: Trigger a batch build. Enabling this will enable batch builds on the CodeBuild project. Default: false
        :param extra_inputs: The list of additional input Artifacts for this action. The directories the additional inputs will be available at are available during the project's build in the CODEBUILD_SRC_DIR_ environment variables. The project's build always starts in the directory with the primary input artifact checked out, the one pointed to by the {@link input} property. For more information, see https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html .
        :param outputs: The list of output Artifacts for this action. **Note**: if you specify more than one output Artifact here, you cannot use the primary 'artifacts' section of the buildspec; you have to use the 'secondary-artifacts' section instead. See https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html for details. Default: the action will not have any outputs
        :param type: The type of the action that determines its CodePipeline Category - Build, or Test. Default: CodeBuildActionType.BUILD

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # source_bucket is of type Bucket
            
            # later:
            # project is of type PipelineProject
            key = "some/key.zip"
            source_output = codepipeline.Artifact()
            source_action = codepipeline_actions.S3SourceAction(
                action_name="S3Source",
                bucket_key=key,
                bucket=source_bucket,
                output=source_output,
                variables_namespace="MyNamespace"
            )
            codepipeline_actions.CodeBuildAction(
                action_name="CodeBuild",
                project=project,
                input=source_output,
                environment_variables={
                    "VERSION_ID": codebuild.BuildEnvironmentVariable(
                        value=source_action.variables.version_id
                    )
                }
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "input": input,
            "project": project,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if check_secrets_in_plain_text_env_variables is not None:
            self._values["check_secrets_in_plain_text_env_variables"] = check_secrets_in_plain_text_env_variables
        if combine_batch_build_artifacts is not None:
            self._values["combine_batch_build_artifacts"] = combine_batch_build_artifacts
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if execute_batch_build is not None:
            self._values["execute_batch_build"] = execute_batch_build
        if extra_inputs is not None:
            self._values["extra_inputs"] = extra_inputs
        if outputs is not None:
            self._values["outputs"] = outputs
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def input(self) -> _Artifact_0cb05964:
        '''The source to use as input for this action.'''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def project(self) -> _IProject_aafae30a:
        '''The action's Project.'''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(_IProject_aafae30a, result)

    @builtins.property
    def check_secrets_in_plain_text_env_variables(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Whether to check for the presence of any secrets in the environment variables of the default type, BuildEnvironmentVariableType.PLAINTEXT. Since using a secret for the value of that kind of variable would result in it being displayed in plain text in the AWS Console, the construct will throw an exception if it detects a secret was passed there. Pass this property as false if you want to skip this validation, and keep using a secret in a plain text environment variable.

        :default: true
        '''
        result = self._values.get("check_secrets_in_plain_text_env_variables")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def combine_batch_build_artifacts(self) -> typing.Optional[builtins.bool]:
        '''Combine the build artifacts for a batch builds.

        Enabling this will combine the build artifacts into the same location for batch builds.
        If ``executeBatchBuild`` is not set to ``true``, this property is ignored.

        :default: false
        '''
        result = self._values.get("combine_batch_build_artifacts")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _BuildEnvironmentVariable_7df4fa0c]]:
        '''The environment variables to pass to the CodeBuild project when this action executes.

        If a variable with the same name was set both on the project level, and here,
        this value will take precedence.

        :default: - No additional environment variables are specified.
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _BuildEnvironmentVariable_7df4fa0c]], result)

    @builtins.property
    def execute_batch_build(self) -> typing.Optional[builtins.bool]:
        '''Trigger a batch build.

        Enabling this will enable batch builds on the CodeBuild project.

        :default: false
        '''
        result = self._values.get("execute_batch_build")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_inputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The list of additional input Artifacts for this action.

        The directories the additional inputs will be available at are available
        during the project's build in the CODEBUILD_SRC_DIR_ environment variables.
        The project's build always starts in the directory with the primary input artifact checked out,
        the one pointed to by the {@link input} property.
        For more information,
        see https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html .
        '''
        result = self._values.get("extra_inputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The list of output Artifacts for this action.

        **Note**: if you specify more than one output Artifact here,
        you cannot use the primary 'artifacts' section of the buildspec;
        you have to use the 'secondary-artifacts' section instead.
        See https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html
        for details.

        :default: the action will not have any outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def type(self) -> typing.Optional["CodeBuildActionType"]:
        '''The type of the action that determines its CodePipeline Category - Build, or Test.

        :default: CodeBuildActionType.BUILD
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CodeBuildActionType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeBuildActionType")
class CodeBuildActionType(enum.Enum):
    '''The type of the CodeBuild action that determines its CodePipeline Category - Build, or Test.

    The default is Build.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # project is of type PipelineProject
        
        source_output = codepipeline.Artifact()
        test_action = codepipeline_actions.CodeBuildAction(
            action_name="IntegrationTest",
            project=project,
            input=source_output,
            type=codepipeline_actions.CodeBuildActionType.TEST
        )
    '''

    BUILD = "BUILD"
    '''The action will have the Build Category.

    This is the default.
    '''
    TEST = "TEST"
    '''The action will have the Test Category.'''


class CodeCommitSourceAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeCommitSourceAction",
):
    '''CodePipeline Source that is provided by an AWS CodeCommit repository.

    If the CodeCommit repository is in a different account, you must use
    ``CodeCommitTrigger.EVENTS`` to trigger the pipeline.

    (That is because the Pipeline structure normally only has a ``RepositoryName``
    field, and that is not enough for the pipeline to locate the repository's
    source account. However, if the pipeline is triggered via an EventBridge
    event, the event itself has the full repository ARN in there, allowing the
    pipeline to locate the repository).

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # project is of type PipelineProject
        # repo is of type Repository
        
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.CodeCommitSourceAction(
            action_name="CodeCommit",
            repository=repo,
            output=source_output,
            code_build_clone_output=True
        )
        
        build_action = codepipeline_actions.CodeBuildAction(
            action_name="CodeBuild",
            project=project,
            input=source_output,  # The build action must use the CodeCommitSourceAction output as input.
            outputs=[codepipeline.Artifact()]
        )
    '''

    def __init__(
        self,
        *,
        output: _Artifact_0cb05964,
        repository: _IRepository_e7c062a1,
        branch: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        trigger: typing.Optional["CodeCommitTrigger"] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param output: 
        :param repository: The CodeCommit repository.
        :param branch: Default: 'master'
        :param code_build_clone_output: Whether the output should be the contents of the repository (which is the default), or a link that allows CodeBuild to clone the repository before building. **Note**: if this option is true, then only CodeBuild actions can use the resulting {@link output}. Default: false
        :param event_role: Role to be used by on commit event rule. Used only when trigger value is CodeCommitTrigger.EVENTS. Default: a new role will be created.
        :param trigger: How should CodePipeline detect source changes for this Action. Default: CodeCommitTrigger.EVENTS
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodeCommitSourceActionProps(
            output=output,
            repository=repository,
            branch=branch,
            code_build_clone_output=code_build_clone_output,
            event_role=event_role,
            trigger=trigger,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variables")
    def variables(self) -> "CodeCommitSourceVariables":
        '''The variables emitted by this action.'''
        return typing.cast("CodeCommitSourceVariables", jsii.get(self, "variables"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeCommitSourceActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "output": "output",
        "repository": "repository",
        "branch": "branch",
        "code_build_clone_output": "codeBuildCloneOutput",
        "event_role": "eventRole",
        "trigger": "trigger",
    },
)
class CodeCommitSourceActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        output: _Artifact_0cb05964,
        repository: _IRepository_e7c062a1,
        branch: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        trigger: typing.Optional["CodeCommitTrigger"] = None,
    ) -> None:
        '''Construction properties of the {@link CodeCommitSourceAction CodeCommit source CodePipeline Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param output: 
        :param repository: The CodeCommit repository.
        :param branch: Default: 'master'
        :param code_build_clone_output: Whether the output should be the contents of the repository (which is the default), or a link that allows CodeBuild to clone the repository before building. **Note**: if this option is true, then only CodeBuild actions can use the resulting {@link output}. Default: false
        :param event_role: Role to be used by on commit event rule. Used only when trigger value is CodeCommitTrigger.EVENTS. Default: a new role will be created.
        :param trigger: How should CodePipeline detect source changes for this Action. Default: CodeCommitTrigger.EVENTS

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # project is of type PipelineProject
            # repo is of type Repository
            
            source_output = codepipeline.Artifact()
            source_action = codepipeline_actions.CodeCommitSourceAction(
                action_name="CodeCommit",
                repository=repo,
                output=source_output,
                code_build_clone_output=True
            )
            
            build_action = codepipeline_actions.CodeBuildAction(
                action_name="CodeBuild",
                project=project,
                input=source_output,  # The build action must use the CodeCommitSourceAction output as input.
                outputs=[codepipeline.Artifact()]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "output": output,
            "repository": repository,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if branch is not None:
            self._values["branch"] = branch
        if code_build_clone_output is not None:
            self._values["code_build_clone_output"] = code_build_clone_output
        if event_role is not None:
            self._values["event_role"] = event_role
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def output(self) -> _Artifact_0cb05964:
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def repository(self) -> _IRepository_e7c062a1:
        '''The CodeCommit repository.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(_IRepository_e7c062a1, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''
        :default: 'master'
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_build_clone_output(self) -> typing.Optional[builtins.bool]:
        '''Whether the output should be the contents of the repository (which is the default), or a link that allows CodeBuild to clone the repository before building.

        **Note**: if this option is true,
        then only CodeBuild actions can use the resulting {@link output}.

        :default: false

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeCommit.html
        '''
        result = self._values.get("code_build_clone_output")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Role to be used by on commit event rule.

        Used only when trigger value is CodeCommitTrigger.EVENTS.

        :default: a new role will be created.
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def trigger(self) -> typing.Optional["CodeCommitTrigger"]:
        '''How should CodePipeline detect source changes for this Action.

        :default: CodeCommitTrigger.EVENTS
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["CodeCommitTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeCommitSourceActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeCommitSourceVariables",
    jsii_struct_bases=[],
    name_mapping={
        "author_date": "authorDate",
        "branch_name": "branchName",
        "commit_id": "commitId",
        "commit_message": "commitMessage",
        "committer_date": "committerDate",
        "repository_name": "repositoryName",
    },
)
class CodeCommitSourceVariables:
    def __init__(
        self,
        *,
        author_date: builtins.str,
        branch_name: builtins.str,
        commit_id: builtins.str,
        commit_message: builtins.str,
        committer_date: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''The CodePipeline variables emitted by the CodeCommit source Action.

        :param author_date: The date the currently last commit on the tracked branch was authored, in ISO-8601 format.
        :param branch_name: The name of the branch this action tracks.
        :param commit_id: The SHA1 hash of the currently last commit on the tracked branch.
        :param commit_message: The message of the currently last commit on the tracked branch.
        :param committer_date: The date the currently last commit on the tracked branch was committed, in ISO-8601 format.
        :param repository_name: The name of the repository this action points to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            
            code_commit_source_variables = codepipeline_actions.CodeCommitSourceVariables(
                author_date="authorDate",
                branch_name="branchName",
                commit_id="commitId",
                commit_message="commitMessage",
                committer_date="committerDate",
                repository_name="repositoryName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "author_date": author_date,
            "branch_name": branch_name,
            "commit_id": commit_id,
            "commit_message": commit_message,
            "committer_date": committer_date,
            "repository_name": repository_name,
        }

    @builtins.property
    def author_date(self) -> builtins.str:
        '''The date the currently last commit on the tracked branch was authored, in ISO-8601 format.'''
        result = self._values.get("author_date")
        assert result is not None, "Required property 'author_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> builtins.str:
        '''The name of the branch this action tracks.'''
        result = self._values.get("branch_name")
        assert result is not None, "Required property 'branch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_id(self) -> builtins.str:
        '''The SHA1 hash of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_id")
        assert result is not None, "Required property 'commit_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_message(self) -> builtins.str:
        '''The message of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_message")
        assert result is not None, "Required property 'commit_message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def committer_date(self) -> builtins.str:
        '''The date the currently last commit on the tracked branch was committed, in ISO-8601 format.'''
        result = self._values.get("committer_date")
        assert result is not None, "Required property 'committer_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The name of the repository this action points to.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeCommitSourceVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeCommitTrigger")
class CodeCommitTrigger(enum.Enum):
    '''How should the CodeCommit Action detect changes.

    This is the type of the {@link CodeCommitSourceAction.trigger} property.
    '''

    NONE = "NONE"
    '''The Action will never detect changes - the Pipeline it's part of will only begin a run when explicitly started.'''
    POLL = "POLL"
    '''CodePipeline will poll the repository to detect changes.'''
    EVENTS = "EVENTS"
    '''CodePipeline will use CloudWatch Events to be notified of changes.

    This is the default method of detecting changes.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeDeployEcsContainerImageInput",
    jsii_struct_bases=[],
    name_mapping={
        "input": "input",
        "task_definition_placeholder": "taskDefinitionPlaceholder",
    },
)
class CodeDeployEcsContainerImageInput:
    def __init__(
        self,
        *,
        input: _Artifact_0cb05964,
        task_definition_placeholder: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration for replacing a placeholder string in the ECS task definition template file with an image URI.

        :param input: The artifact that contains an ``imageDetails.json`` file with the image URI. The artifact's ``imageDetails.json`` file must be a JSON file containing an ``ImageURI`` property. For example: ``{ "ImageURI": "ACCOUNTID.dkr.ecr.us-west-2.amazonaws.com/dk-image-repo@sha256:example3" }``
        :param task_definition_placeholder: The placeholder string in the ECS task definition template file that will be replaced with the image URI. The placeholder string must be surrounded by angle brackets in the template file. For example, if the task definition template file contains a placeholder like ``"image": "<PLACEHOLDER>"``, then the ``taskDefinitionPlaceholder`` value should be ``PLACEHOLDER``. Default: IMAGE

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline as codepipeline
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            
            # artifact is of type Artifact
            
            code_deploy_ecs_container_image_input = codepipeline_actions.CodeDeployEcsContainerImageInput(
                input=artifact,
            
                # the properties below are optional
                task_definition_placeholder="taskDefinitionPlaceholder"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "input": input,
        }
        if task_definition_placeholder is not None:
            self._values["task_definition_placeholder"] = task_definition_placeholder

    @builtins.property
    def input(self) -> _Artifact_0cb05964:
        '''The artifact that contains an ``imageDetails.json`` file with the image URI.

        The artifact's ``imageDetails.json`` file must be a JSON file containing an
        ``ImageURI`` property.  For example:
        ``{ "ImageURI": "ACCOUNTID.dkr.ecr.us-west-2.amazonaws.com/dk-image-repo@sha256:example3" }``
        '''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def task_definition_placeholder(self) -> typing.Optional[builtins.str]:
        '''The placeholder string in the ECS task definition template file that will be replaced with the image URI.

        The placeholder string must be surrounded by angle brackets in the template file.
        For example, if the task definition template file contains a placeholder like
        ``"image": "<PLACEHOLDER>"``, then the ``taskDefinitionPlaceholder`` value should
        be ``PLACEHOLDER``.

        :default: IMAGE
        '''
        result = self._values.get("task_definition_placeholder")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeDeployEcsContainerImageInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodeDeployEcsDeployAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeDeployEcsDeployAction",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codedeploy as codedeploy
        from aws_cdk import aws_codepipeline as codepipeline
        from aws_cdk import aws_codepipeline_actions as codepipeline_actions
        from aws_cdk import aws_iam as iam
        
        # artifact is of type Artifact
        # artifact_path is of type ArtifactPath
        # ecs_deployment_group is of type IEcsDeploymentGroup
        # role is of type Role
        
        code_deploy_ecs_deploy_action = codepipeline_actions.CodeDeployEcsDeployAction(
            action_name="actionName",
            deployment_group=ecs_deployment_group,
        
            # the properties below are optional
            app_spec_template_file=artifact_path,
            app_spec_template_input=artifact,
            container_image_inputs=[codepipeline_actions.CodeDeployEcsContainerImageInput(
                input=artifact,
        
                # the properties below are optional
                task_definition_placeholder="taskDefinitionPlaceholder"
            )],
            role=role,
            run_order=123,
            task_definition_template_file=artifact_path,
            task_definition_template_input=artifact,
            variables_namespace="variablesNamespace"
        )
    '''

    def __init__(
        self,
        *,
        deployment_group: _IEcsDeploymentGroup_6a266745,
        app_spec_template_file: typing.Optional[_ArtifactPath_bf444090] = None,
        app_spec_template_input: typing.Optional[_Artifact_0cb05964] = None,
        container_image_inputs: typing.Optional[typing.Sequence[CodeDeployEcsContainerImageInput]] = None,
        task_definition_template_file: typing.Optional[_ArtifactPath_bf444090] = None,
        task_definition_template_input: typing.Optional[_Artifact_0cb05964] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_group: The CodeDeploy ECS Deployment Group to deploy to.
        :param app_spec_template_file: The name of the CodeDeploy AppSpec file. During deployment, a new task definition will be registered with ECS, and the new task definition ID will be inserted into the CodeDeploy AppSpec file. The AppSpec file contents will be provided to CodeDeploy for the deployment. Use this property if you want to use a different name for this file than the default 'appspec.yaml'. If you use this property, you don't need to specify the ``appSpecTemplateInput`` property. Default: - one of this property, or ``appSpecTemplateInput``, is required
        :param app_spec_template_input: The artifact containing the CodeDeploy AppSpec file. During deployment, a new task definition will be registered with ECS, and the new task definition ID will be inserted into the CodeDeploy AppSpec file. The AppSpec file contents will be provided to CodeDeploy for the deployment. If you use this property, it's assumed the file is called 'appspec.yaml'. If your AppSpec file uses a different filename, leave this property empty, and use the ``appSpecTemplateFile`` property instead. Default: - one of this property, or ``appSpecTemplateFile``, is required
        :param container_image_inputs: Configuration for dynamically updated images in the task definition. Provide pairs of an image details input artifact and a placeholder string that will be used to dynamically update the ECS task definition template file prior to deployment. A maximum of 4 images can be given.
        :param task_definition_template_file: The name of the ECS task definition template file. During deployment, the task definition template file contents will be registered with ECS. Use this property if you want to use a different name for this file than the default 'taskdef.json'. If you use this property, you don't need to specify the ``taskDefinitionTemplateInput`` property. Default: - one of this property, or ``taskDefinitionTemplateInput``, is required
        :param task_definition_template_input: The artifact containing the ECS task definition template file. During deployment, the task definition template file contents will be registered with ECS. If you use this property, it's assumed the file is called 'taskdef.json'. If your task definition template uses a different filename, leave this property empty, and use the ``taskDefinitionTemplateFile`` property instead. Default: - one of this property, or ``taskDefinitionTemplateFile``, is required
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodeDeployEcsDeployActionProps(
            deployment_group=deployment_group,
            app_spec_template_file=app_spec_template_file,
            app_spec_template_input=app_spec_template_input,
            container_image_inputs=container_image_inputs,
            task_definition_template_file=task_definition_template_file,
            task_definition_template_input=task_definition_template_input,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeDeployEcsDeployActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "deployment_group": "deploymentGroup",
        "app_spec_template_file": "appSpecTemplateFile",
        "app_spec_template_input": "appSpecTemplateInput",
        "container_image_inputs": "containerImageInputs",
        "task_definition_template_file": "taskDefinitionTemplateFile",
        "task_definition_template_input": "taskDefinitionTemplateInput",
    },
)
class CodeDeployEcsDeployActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        deployment_group: _IEcsDeploymentGroup_6a266745,
        app_spec_template_file: typing.Optional[_ArtifactPath_bf444090] = None,
        app_spec_template_input: typing.Optional[_Artifact_0cb05964] = None,
        container_image_inputs: typing.Optional[typing.Sequence[CodeDeployEcsContainerImageInput]] = None,
        task_definition_template_file: typing.Optional[_ArtifactPath_bf444090] = None,
        task_definition_template_input: typing.Optional[_Artifact_0cb05964] = None,
    ) -> None:
        '''Construction properties of the {@link CodeDeployEcsDeployAction CodeDeploy ECS deploy CodePipeline Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param deployment_group: The CodeDeploy ECS Deployment Group to deploy to.
        :param app_spec_template_file: The name of the CodeDeploy AppSpec file. During deployment, a new task definition will be registered with ECS, and the new task definition ID will be inserted into the CodeDeploy AppSpec file. The AppSpec file contents will be provided to CodeDeploy for the deployment. Use this property if you want to use a different name for this file than the default 'appspec.yaml'. If you use this property, you don't need to specify the ``appSpecTemplateInput`` property. Default: - one of this property, or ``appSpecTemplateInput``, is required
        :param app_spec_template_input: The artifact containing the CodeDeploy AppSpec file. During deployment, a new task definition will be registered with ECS, and the new task definition ID will be inserted into the CodeDeploy AppSpec file. The AppSpec file contents will be provided to CodeDeploy for the deployment. If you use this property, it's assumed the file is called 'appspec.yaml'. If your AppSpec file uses a different filename, leave this property empty, and use the ``appSpecTemplateFile`` property instead. Default: - one of this property, or ``appSpecTemplateFile``, is required
        :param container_image_inputs: Configuration for dynamically updated images in the task definition. Provide pairs of an image details input artifact and a placeholder string that will be used to dynamically update the ECS task definition template file prior to deployment. A maximum of 4 images can be given.
        :param task_definition_template_file: The name of the ECS task definition template file. During deployment, the task definition template file contents will be registered with ECS. Use this property if you want to use a different name for this file than the default 'taskdef.json'. If you use this property, you don't need to specify the ``taskDefinitionTemplateInput`` property. Default: - one of this property, or ``taskDefinitionTemplateInput``, is required
        :param task_definition_template_input: The artifact containing the ECS task definition template file. During deployment, the task definition template file contents will be registered with ECS. If you use this property, it's assumed the file is called 'taskdef.json'. If your task definition template uses a different filename, leave this property empty, and use the ``taskDefinitionTemplateFile`` property instead. Default: - one of this property, or ``taskDefinitionTemplateFile``, is required

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            from aws_cdk import aws_codepipeline as codepipeline
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            from aws_cdk import aws_iam as iam
            
            # artifact is of type Artifact
            # artifact_path is of type ArtifactPath
            # ecs_deployment_group is of type IEcsDeploymentGroup
            # role is of type Role
            
            code_deploy_ecs_deploy_action_props = codepipeline_actions.CodeDeployEcsDeployActionProps(
                action_name="actionName",
                deployment_group=ecs_deployment_group,
            
                # the properties below are optional
                app_spec_template_file=artifact_path,
                app_spec_template_input=artifact,
                container_image_inputs=[codepipeline_actions.CodeDeployEcsContainerImageInput(
                    input=artifact,
            
                    # the properties below are optional
                    task_definition_placeholder="taskDefinitionPlaceholder"
                )],
                role=role,
                run_order=123,
                task_definition_template_file=artifact_path,
                task_definition_template_input=artifact,
                variables_namespace="variablesNamespace"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "deployment_group": deployment_group,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if app_spec_template_file is not None:
            self._values["app_spec_template_file"] = app_spec_template_file
        if app_spec_template_input is not None:
            self._values["app_spec_template_input"] = app_spec_template_input
        if container_image_inputs is not None:
            self._values["container_image_inputs"] = container_image_inputs
        if task_definition_template_file is not None:
            self._values["task_definition_template_file"] = task_definition_template_file
        if task_definition_template_input is not None:
            self._values["task_definition_template_input"] = task_definition_template_input

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def deployment_group(self) -> _IEcsDeploymentGroup_6a266745:
        '''The CodeDeploy ECS Deployment Group to deploy to.'''
        result = self._values.get("deployment_group")
        assert result is not None, "Required property 'deployment_group' is missing"
        return typing.cast(_IEcsDeploymentGroup_6a266745, result)

    @builtins.property
    def app_spec_template_file(self) -> typing.Optional[_ArtifactPath_bf444090]:
        '''The name of the CodeDeploy AppSpec file.

        During deployment, a new task definition will be registered
        with ECS, and the new task definition ID will be inserted into
        the CodeDeploy AppSpec file.  The AppSpec file contents will be
        provided to CodeDeploy for the deployment.

        Use this property if you want to use a different name for this file than the default 'appspec.yaml'.
        If you use this property, you don't need to specify the ``appSpecTemplateInput`` property.

        :default: - one of this property, or ``appSpecTemplateInput``, is required
        '''
        result = self._values.get("app_spec_template_file")
        return typing.cast(typing.Optional[_ArtifactPath_bf444090], result)

    @builtins.property
    def app_spec_template_input(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The artifact containing the CodeDeploy AppSpec file.

        During deployment, a new task definition will be registered
        with ECS, and the new task definition ID will be inserted into
        the CodeDeploy AppSpec file.  The AppSpec file contents will be
        provided to CodeDeploy for the deployment.

        If you use this property, it's assumed the file is called 'appspec.yaml'.
        If your AppSpec file uses a different filename, leave this property empty,
        and use the ``appSpecTemplateFile`` property instead.

        :default: - one of this property, or ``appSpecTemplateFile``, is required
        '''
        result = self._values.get("app_spec_template_input")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def container_image_inputs(
        self,
    ) -> typing.Optional[typing.List[CodeDeployEcsContainerImageInput]]:
        '''Configuration for dynamically updated images in the task definition.

        Provide pairs of an image details input artifact and a placeholder string
        that will be used to dynamically update the ECS task definition template
        file prior to deployment. A maximum of 4 images can be given.
        '''
        result = self._values.get("container_image_inputs")
        return typing.cast(typing.Optional[typing.List[CodeDeployEcsContainerImageInput]], result)

    @builtins.property
    def task_definition_template_file(self) -> typing.Optional[_ArtifactPath_bf444090]:
        '''The name of the ECS task definition template file.

        During deployment, the task definition template file contents
        will be registered with ECS.

        Use this property if you want to use a different name for this file than the default 'taskdef.json'.
        If you use this property, you don't need to specify the ``taskDefinitionTemplateInput`` property.

        :default: - one of this property, or ``taskDefinitionTemplateInput``, is required
        '''
        result = self._values.get("task_definition_template_file")
        return typing.cast(typing.Optional[_ArtifactPath_bf444090], result)

    @builtins.property
    def task_definition_template_input(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The artifact containing the ECS task definition template file.

        During deployment, the task definition template file contents
        will be registered with ECS.

        If you use this property, it's assumed the file is called 'taskdef.json'.
        If your task definition template uses a different filename, leave this property empty,
        and use the ``taskDefinitionTemplateFile`` property instead.

        :default: - one of this property, or ``taskDefinitionTemplateFile``, is required
        '''
        result = self._values.get("task_definition_template_input")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeDeployEcsDeployActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodeDeployServerDeployAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeDeployServerDeployAction",
):
    '''
    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # deployment_group is of type ServerDeploymentGroup
        pipeline = codepipeline.Pipeline(self, "MyPipeline",
            pipeline_name="MyPipeline"
        )
        
        # add the source and build Stages to the Pipeline...
        build_output = codepipeline.Artifact()
        deploy_action = codepipeline_actions.CodeDeployServerDeployAction(
            action_name="CodeDeploy",
            input=build_output,
            deployment_group=deployment_group
        )
        pipeline.add_stage(
            stage_name="Deploy",
            actions=[deploy_action]
        )
    '''

    def __init__(
        self,
        *,
        deployment_group: _IServerDeploymentGroup_b9e40f62,
        input: _Artifact_0cb05964,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_group: The CodeDeploy server Deployment Group to deploy to.
        :param input: The source to use as input for deployment.
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodeDeployServerDeployActionProps(
            deployment_group=deployment_group,
            input=input,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeDeployServerDeployActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "deployment_group": "deploymentGroup",
        "input": "input",
    },
)
class CodeDeployServerDeployActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        deployment_group: _IServerDeploymentGroup_b9e40f62,
        input: _Artifact_0cb05964,
    ) -> None:
        '''Construction properties of the {@link CodeDeployServerDeployAction CodeDeploy server deploy CodePipeline Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param deployment_group: The CodeDeploy server Deployment Group to deploy to.
        :param input: The source to use as input for deployment.

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # deployment_group is of type ServerDeploymentGroup
            pipeline = codepipeline.Pipeline(self, "MyPipeline",
                pipeline_name="MyPipeline"
            )
            
            # add the source and build Stages to the Pipeline...
            build_output = codepipeline.Artifact()
            deploy_action = codepipeline_actions.CodeDeployServerDeployAction(
                action_name="CodeDeploy",
                input=build_output,
                deployment_group=deployment_group
            )
            pipeline.add_stage(
                stage_name="Deploy",
                actions=[deploy_action]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "deployment_group": deployment_group,
            "input": input,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def deployment_group(self) -> _IServerDeploymentGroup_b9e40f62:
        '''The CodeDeploy server Deployment Group to deploy to.'''
        result = self._values.get("deployment_group")
        assert result is not None, "Required property 'deployment_group' is missing"
        return typing.cast(_IServerDeploymentGroup_b9e40f62, result)

    @builtins.property
    def input(self) -> _Artifact_0cb05964:
        '''The source to use as input for deployment.'''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeDeployServerDeployActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodeStarConnectionsSourceAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeStarConnectionsSourceAction",
):
    '''A CodePipeline source action for the CodeStar Connections source, which allows connecting to GitHub and BitBucket.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.CodeStarConnectionsSourceAction(
            action_name="BitBucket_Source",
            owner="aws",
            repo="aws-cdk",
            output=source_output,
            connection_arn="arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-abcd-12ab-34cdef5678gh"
        )
    '''

    def __init__(
        self,
        *,
        connection_arn: builtins.str,
        output: _Artifact_0cb05964,
        owner: builtins.str,
        repo: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        trigger_on_push: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection_arn: The ARN of the CodeStar Connection created in the AWS console that has permissions to access this GitHub or BitBucket repository.
        :param output: The output artifact that this action produces. Can be used as input for further pipeline actions.
        :param owner: The owning user or organization of the repository.
        :param repo: The name of the repository.
        :param branch: The branch to build. Default: 'master'
        :param code_build_clone_output: Whether the output should be the contents of the repository (which is the default), or a link that allows CodeBuild to clone the repository before building. **Note**: if this option is true, then only CodeBuild actions can use the resulting {@link output}. Default: false
        :param trigger_on_push: Controls automatically starting your pipeline when a new commit is made on the configured repository and branch. If unspecified, the default value is true, and the field does not display by default. Default: true
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodeStarConnectionsSourceActionProps(
            connection_arn=connection_arn,
            output=output,
            owner=owner,
            repo=repo,
            branch=branch,
            code_build_clone_output=code_build_clone_output,
            trigger_on_push=trigger_on_push,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variables")
    def variables(self) -> "CodeStarSourceVariables":
        '''The variables emitted by this action.'''
        return typing.cast("CodeStarSourceVariables", jsii.get(self, "variables"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeStarConnectionsSourceActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "connection_arn": "connectionArn",
        "output": "output",
        "owner": "owner",
        "repo": "repo",
        "branch": "branch",
        "code_build_clone_output": "codeBuildCloneOutput",
        "trigger_on_push": "triggerOnPush",
    },
)
class CodeStarConnectionsSourceActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        connection_arn: builtins.str,
        output: _Artifact_0cb05964,
        owner: builtins.str,
        repo: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        trigger_on_push: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Construction properties for {@link CodeStarConnectionsSourceAction}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param connection_arn: The ARN of the CodeStar Connection created in the AWS console that has permissions to access this GitHub or BitBucket repository.
        :param output: The output artifact that this action produces. Can be used as input for further pipeline actions.
        :param owner: The owning user or organization of the repository.
        :param repo: The name of the repository.
        :param branch: The branch to build. Default: 'master'
        :param code_build_clone_output: Whether the output should be the contents of the repository (which is the default), or a link that allows CodeBuild to clone the repository before building. **Note**: if this option is true, then only CodeBuild actions can use the resulting {@link output}. Default: false
        :param trigger_on_push: Controls automatically starting your pipeline when a new commit is made on the configured repository and branch. If unspecified, the default value is true, and the field does not display by default. Default: true

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            source_output = codepipeline.Artifact()
            source_action = codepipeline_actions.CodeStarConnectionsSourceAction(
                action_name="BitBucket_Source",
                owner="aws",
                repo="aws-cdk",
                output=source_output,
                connection_arn="arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-abcd-12ab-34cdef5678gh"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "connection_arn": connection_arn,
            "output": output,
            "owner": owner,
            "repo": repo,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if branch is not None:
            self._values["branch"] = branch
        if code_build_clone_output is not None:
            self._values["code_build_clone_output"] = code_build_clone_output
        if trigger_on_push is not None:
            self._values["trigger_on_push"] = trigger_on_push

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ARN of the CodeStar Connection created in the AWS console that has permissions to access this GitHub or BitBucket repository.

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-create.html

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-abcd-12ab-34cdef5678gh"
        '''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output(self) -> _Artifact_0cb05964:
        '''The output artifact that this action produces.

        Can be used as input for further pipeline actions.
        '''
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def owner(self) -> builtins.str:
        '''The owning user or organization of the repository.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "aws"
        '''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> builtins.str:
        '''The name of the repository.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "aws-cdk"
        '''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The branch to build.

        :default: 'master'
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_build_clone_output(self) -> typing.Optional[builtins.bool]:
        '''Whether the output should be the contents of the repository (which is the default), or a link that allows CodeBuild to clone the repository before building.

        **Note**: if this option is true,
        then only CodeBuild actions can use the resulting {@link output}.

        :default: false

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html#action-reference-CodestarConnectionSource-config
        '''
        result = self._values.get("code_build_clone_output")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def trigger_on_push(self) -> typing.Optional[builtins.bool]:
        '''Controls automatically starting your pipeline when a new commit is made on the configured repository and branch.

        If unspecified,
        the default value is true, and the field does not display by default.

        :default: true

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html
        '''
        result = self._values.get("trigger_on_push")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeStarConnectionsSourceActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.CodeStarSourceVariables",
    jsii_struct_bases=[],
    name_mapping={
        "author_date": "authorDate",
        "branch_name": "branchName",
        "commit_id": "commitId",
        "commit_message": "commitMessage",
        "connection_arn": "connectionArn",
        "full_repository_name": "fullRepositoryName",
    },
)
class CodeStarSourceVariables:
    def __init__(
        self,
        *,
        author_date: builtins.str,
        branch_name: builtins.str,
        commit_id: builtins.str,
        commit_message: builtins.str,
        connection_arn: builtins.str,
        full_repository_name: builtins.str,
    ) -> None:
        '''The CodePipeline variables emitted by CodeStar source Action.

        :param author_date: The date the currently last commit on the tracked branch was authored, in ISO-8601 format.
        :param branch_name: The name of the branch this action tracks.
        :param commit_id: The SHA1 hash of the currently last commit on the tracked branch.
        :param commit_message: The message of the currently last commit on the tracked branch.
        :param connection_arn: The connection ARN this source uses.
        :param full_repository_name: The name of the repository this action points to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            
            code_star_source_variables = codepipeline_actions.CodeStarSourceVariables(
                author_date="authorDate",
                branch_name="branchName",
                commit_id="commitId",
                commit_message="commitMessage",
                connection_arn="connectionArn",
                full_repository_name="fullRepositoryName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "author_date": author_date,
            "branch_name": branch_name,
            "commit_id": commit_id,
            "commit_message": commit_message,
            "connection_arn": connection_arn,
            "full_repository_name": full_repository_name,
        }

    @builtins.property
    def author_date(self) -> builtins.str:
        '''The date the currently last commit on the tracked branch was authored, in ISO-8601 format.'''
        result = self._values.get("author_date")
        assert result is not None, "Required property 'author_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> builtins.str:
        '''The name of the branch this action tracks.'''
        result = self._values.get("branch_name")
        assert result is not None, "Required property 'branch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_id(self) -> builtins.str:
        '''The SHA1 hash of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_id")
        assert result is not None, "Required property 'commit_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_message(self) -> builtins.str:
        '''The message of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_message")
        assert result is not None, "Required property 'commit_message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The connection ARN this source uses.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def full_repository_name(self) -> builtins.str:
        '''The name of the repository this action points to.'''
        result = self._values.get("full_repository_name")
        assert result is not None, "Required property 'full_repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeStarSourceVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcrSourceAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.EcrSourceAction",
):
    '''The ECR Repository source CodePipeline Action.

    Will trigger the pipeline as soon as the target tag in the repository
    changes, but only if there is a CloudTrail Trail in the account that
    captures the ECR event.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_ecr as ecr
        
        # ecr_repository is of type Repository
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.EcrSourceAction(
            action_name="ECR",
            repository=ecr_repository,
            image_tag="some-tag",  # optional, default: 'latest'
            output=source_output
        )
        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action]
        )
    '''

    def __init__(
        self,
        *,
        output: _Artifact_0cb05964,
        repository: _IRepository_e6004aa6,
        image_tag: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param output: 
        :param repository: The repository that will be watched for changes.
        :param image_tag: The image tag that will be checked for changes. Provide an empty string to trigger on changes to any tag. Default: 'latest'
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = EcrSourceActionProps(
            output=output,
            repository=repository,
            image_tag=image_tag,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variables")
    def variables(self) -> "EcrSourceVariables":
        '''The variables emitted by this action.'''
        return typing.cast("EcrSourceVariables", jsii.get(self, "variables"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.EcrSourceActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "output": "output",
        "repository": "repository",
        "image_tag": "imageTag",
    },
)
class EcrSourceActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        output: _Artifact_0cb05964,
        repository: _IRepository_e6004aa6,
        image_tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties of {@link EcrSourceAction}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param output: 
        :param repository: The repository that will be watched for changes.
        :param image_tag: The image tag that will be checked for changes. Provide an empty string to trigger on changes to any tag. Default: 'latest'

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            import aws_cdk.aws_ecr as ecr
            
            # ecr_repository is of type Repository
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            source_output = codepipeline.Artifact()
            source_action = codepipeline_actions.EcrSourceAction(
                action_name="ECR",
                repository=ecr_repository,
                image_tag="some-tag",  # optional, default: 'latest'
                output=source_output
            )
            pipeline.add_stage(
                stage_name="Source",
                actions=[source_action]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "output": output,
            "repository": repository,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if image_tag is not None:
            self._values["image_tag"] = image_tag

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def output(self) -> _Artifact_0cb05964:
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def repository(self) -> _IRepository_e6004aa6:
        '''The repository that will be watched for changes.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(_IRepository_e6004aa6, result)

    @builtins.property
    def image_tag(self) -> typing.Optional[builtins.str]:
        '''The image tag that will be checked for changes.

        Provide an empty string to trigger on changes to any tag.

        :default: 'latest'
        '''
        result = self._values.get("image_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcrSourceActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.EcrSourceVariables",
    jsii_struct_bases=[],
    name_mapping={
        "image_digest": "imageDigest",
        "image_tag": "imageTag",
        "image_uri": "imageUri",
        "registry_id": "registryId",
        "repository_name": "repositoryName",
    },
)
class EcrSourceVariables:
    def __init__(
        self,
        *,
        image_digest: builtins.str,
        image_tag: builtins.str,
        image_uri: builtins.str,
        registry_id: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''The CodePipeline variables emitted by the ECR source Action.

        :param image_digest: The digest of the current image, in the form ':'.
        :param image_tag: The Docker tag of the current image.
        :param image_uri: The full ECR Docker URI of the current image.
        :param registry_id: The identifier of the registry. In ECR, this is usually the ID of the AWS account owning it.
        :param repository_name: The physical name of the repository that this action tracks.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            
            ecr_source_variables = codepipeline_actions.EcrSourceVariables(
                image_digest="imageDigest",
                image_tag="imageTag",
                image_uri="imageUri",
                registry_id="registryId",
                repository_name="repositoryName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image_digest": image_digest,
            "image_tag": image_tag,
            "image_uri": image_uri,
            "registry_id": registry_id,
            "repository_name": repository_name,
        }

    @builtins.property
    def image_digest(self) -> builtins.str:
        '''The digest of the current image, in the form ':'.'''
        result = self._values.get("image_digest")
        assert result is not None, "Required property 'image_digest' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_tag(self) -> builtins.str:
        '''The Docker tag of the current image.'''
        result = self._values.get("image_tag")
        assert result is not None, "Required property 'image_tag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_uri(self) -> builtins.str:
        '''The full ECR Docker URI of the current image.'''
        result = self._values.get("image_uri")
        assert result is not None, "Required property 'image_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def registry_id(self) -> builtins.str:
        '''The identifier of the registry.

        In ECR, this is usually the ID of the AWS account owning it.
        '''
        result = self._values.get("registry_id")
        assert result is not None, "Required property 'registry_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The physical name of the repository that this action tracks.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcrSourceVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsDeployAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.EcsDeployAction",
):
    '''CodePipeline Action to deploy an ECS Service.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_ecs as ecs
        
        # service is of type FargateService
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        build_output = codepipeline.Artifact()
        deploy_stage = pipeline.add_stage(
            stage_name="Deploy",
            actions=[
                codepipeline_actions.EcsDeployAction(
                    action_name="DeployAction",
                    service=service,
                    # if your file is called imagedefinitions.json,
                    # use the `input` property,
                    # and leave out the `imageFile` property
                    input=build_output,
                    # if your file name is _not_ imagedefinitions.json,
                    # use the `imageFile` property,
                    # and leave out the `input` property
                    image_file=build_output.at_path("imageDef.json"),
                    deployment_timeout=Duration.minutes(60)
                )
            ]
        )
    '''

    def __init__(
        self,
        *,
        service: _IBaseService_3fcdd913,
        deployment_timeout: typing.Optional[_Duration_4839e8c3] = None,
        image_file: typing.Optional[_ArtifactPath_bf444090] = None,
        input: typing.Optional[_Artifact_0cb05964] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: The ECS Service to deploy.
        :param deployment_timeout: Timeout for the ECS deployment in minutes. Value must be between 1-60. Default: - 60 minutes
        :param image_file: The name of the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. Use this property if you want to use a different name for this file than the default 'imagedefinitions.json'. If you use this property, you don't need to specify the ``input`` property. Default: - one of this property, or ``input``, is required
        :param input: The input artifact that contains the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. If you use this property, it's assumed the file is called 'imagedefinitions.json'. If your build uses a different file, leave this property empty, and use the ``imageFile`` property instead. Default: - one of this property, or ``imageFile``, is required
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = EcsDeployActionProps(
            service=service,
            deployment_timeout=deployment_timeout,
            image_file=image_file,
            input=input,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.EcsDeployActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "service": "service",
        "deployment_timeout": "deploymentTimeout",
        "image_file": "imageFile",
        "input": "input",
    },
)
class EcsDeployActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        service: _IBaseService_3fcdd913,
        deployment_timeout: typing.Optional[_Duration_4839e8c3] = None,
        image_file: typing.Optional[_ArtifactPath_bf444090] = None,
        input: typing.Optional[_Artifact_0cb05964] = None,
    ) -> None:
        '''Construction properties of {@link EcsDeployAction}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param service: The ECS Service to deploy.
        :param deployment_timeout: Timeout for the ECS deployment in minutes. Value must be between 1-60. Default: - 60 minutes
        :param image_file: The name of the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. Use this property if you want to use a different name for this file than the default 'imagedefinitions.json'. If you use this property, you don't need to specify the ``input`` property. Default: - one of this property, or ``input``, is required
        :param input: The input artifact that contains the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. If you use this property, it's assumed the file is called 'imagedefinitions.json'. If your build uses a different file, leave this property empty, and use the ``imageFile`` property instead. Default: - one of this property, or ``imageFile``, is required

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            import aws_cdk.aws_ecs as ecs
            
            # service is of type FargateService
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            build_output = codepipeline.Artifact()
            deploy_stage = pipeline.add_stage(
                stage_name="Deploy",
                actions=[
                    codepipeline_actions.EcsDeployAction(
                        action_name="DeployAction",
                        service=service,
                        # if your file is called imagedefinitions.json,
                        # use the `input` property,
                        # and leave out the `imageFile` property
                        input=build_output,
                        # if your file name is _not_ imagedefinitions.json,
                        # use the `imageFile` property,
                        # and leave out the `input` property
                        image_file=build_output.at_path("imageDef.json"),
                        deployment_timeout=Duration.minutes(60)
                    )
                ]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "service": service,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if deployment_timeout is not None:
            self._values["deployment_timeout"] = deployment_timeout
        if image_file is not None:
            self._values["image_file"] = image_file
        if input is not None:
            self._values["input"] = input

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def service(self) -> _IBaseService_3fcdd913:
        '''The ECS Service to deploy.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(_IBaseService_3fcdd913, result)

    @builtins.property
    def deployment_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Timeout for the ECS deployment in minutes.

        Value must be between 1-60.

        :default: - 60 minutes

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECS.html
        '''
        result = self._values.get("deployment_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def image_file(self) -> typing.Optional[_ArtifactPath_bf444090]:
        '''The name of the JSON image definitions file to use for deployments.

        The JSON file is a list of objects,
        each with 2 keys: ``name`` is the name of the container in the Task Definition,
        and ``imageUri`` is the Docker image URI you want to update your service with.
        Use this property if you want to use a different name for this file than the default 'imagedefinitions.json'.
        If you use this property, you don't need to specify the ``input`` property.

        :default: - one of this property, or ``input``, is required

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html#pipelines-create-image-definitions
        '''
        result = self._values.get("image_file")
        return typing.cast(typing.Optional[_ArtifactPath_bf444090], result)

    @builtins.property
    def input(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The input artifact that contains the JSON image definitions file to use for deployments.

        The JSON file is a list of objects,
        each with 2 keys: ``name`` is the name of the container in the Task Definition,
        and ``imageUri`` is the Docker image URI you want to update your service with.
        If you use this property, it's assumed the file is called 'imagedefinitions.json'.
        If your build uses a different file, leave this property empty,
        and use the ``imageFile`` property instead.

        :default: - one of this property, or ``imageFile``, is required

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html#pipelines-create-image-definitions
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsDeployActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GitHubSourceAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.GitHubSourceAction",
):
    '''Source that is provided by a GitHub repository.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # Read the secret from Secrets Manager
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner="awslabs",
            repo="aws-cdk",
            oauth_token=SecretValue.secrets_manager("my-github-token"),
            output=source_output,
            branch="develop"
        )
        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action]
        )
    '''

    def __init__(
        self,
        *,
        oauth_token: _SecretValue_3dd0ddae,
        output: _Artifact_0cb05964,
        owner: builtins.str,
        repo: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        trigger: typing.Optional["GitHubTrigger"] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param oauth_token: A GitHub OAuth token to use for authentication. It is recommended to use a Secrets Manager ``Secret`` to obtain the token: const oauth = cdk.SecretValue.secretsManager('my-github-token'); new GitHubSource(this, 'GitHubAction', { oauthToken: oauth, ... }); The GitHub Personal Access Token should have these scopes: - **repo** - to read the repository - **admin:repo_hook** - if you plan to use webhooks (true by default)
        :param output: 
        :param owner: The GitHub account/user that owns the repo.
        :param repo: The name of the repo, without the username.
        :param branch: The branch to use. Default: "master"
        :param trigger: How AWS CodePipeline should be triggered. With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action With "POLL", CodePipeline periodically checks the source for changes With "None", the action is not triggered through changes in the source To use ``WEBHOOK``, your GitHub Personal Access Token should have **admin:repo_hook** scope (in addition to the regular **repo** scope). Default: GitHubTrigger.WEBHOOK
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = GitHubSourceActionProps(
            oauth_token=oauth_token,
            output=output,
            owner=owner,
            repo=repo,
            branch=branch,
            trigger=trigger,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        _options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, stage, _options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variables")
    def variables(self) -> "GitHubSourceVariables":
        '''The variables emitted by this action.'''
        return typing.cast("GitHubSourceVariables", jsii.get(self, "variables"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.GitHubSourceActionProps",
    jsii_struct_bases=[_CommonActionProps_e3aaeecb],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "oauth_token": "oauthToken",
        "output": "output",
        "owner": "owner",
        "repo": "repo",
        "branch": "branch",
        "trigger": "trigger",
    },
)
class GitHubSourceActionProps(_CommonActionProps_e3aaeecb):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        oauth_token: _SecretValue_3dd0ddae,
        output: _Artifact_0cb05964,
        owner: builtins.str,
        repo: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        trigger: typing.Optional["GitHubTrigger"] = None,
    ) -> None:
        '''Construction properties of the {@link GitHubSourceAction GitHub source action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param oauth_token: A GitHub OAuth token to use for authentication. It is recommended to use a Secrets Manager ``Secret`` to obtain the token: const oauth = cdk.SecretValue.secretsManager('my-github-token'); new GitHubSource(this, 'GitHubAction', { oauthToken: oauth, ... }); The GitHub Personal Access Token should have these scopes: - **repo** - to read the repository - **admin:repo_hook** - if you plan to use webhooks (true by default)
        :param output: 
        :param owner: The GitHub account/user that owns the repo.
        :param repo: The name of the repo, without the username.
        :param branch: The branch to use. Default: "master"
        :param trigger: How AWS CodePipeline should be triggered. With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action With "POLL", CodePipeline periodically checks the source for changes With "None", the action is not triggered through changes in the source To use ``WEBHOOK``, your GitHub Personal Access Token should have **admin:repo_hook** scope (in addition to the regular **repo** scope). Default: GitHubTrigger.WEBHOOK

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # Read the secret from Secrets Manager
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            source_output = codepipeline.Artifact()
            source_action = codepipeline_actions.GitHubSourceAction(
                action_name="GitHub_Source",
                owner="awslabs",
                repo="aws-cdk",
                oauth_token=SecretValue.secrets_manager("my-github-token"),
                output=source_output,
                branch="develop"
            )
            pipeline.add_stage(
                stage_name="Source",
                actions=[source_action]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "oauth_token": oauth_token,
            "output": output,
            "owner": owner,
            "repo": repo,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if branch is not None:
            self._values["branch"] = branch
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_token(self) -> _SecretValue_3dd0ddae:
        '''A GitHub OAuth token to use for authentication.

        It is recommended to use a Secrets Manager ``Secret`` to obtain the token:

        const oauth = cdk.SecretValue.secretsManager('my-github-token');
        new GitHubSource(this, 'GitHubAction', { oauthToken: oauth, ... });

        The GitHub Personal Access Token should have these scopes:

        - **repo** - to read the repository
        - **admin:repo_hook** - if you plan to use webhooks (true by default)

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html#GitHub-create-personal-token-CLI
        '''
        result = self._values.get("oauth_token")
        assert result is not None, "Required property 'oauth_token' is missing"
        return typing.cast(_SecretValue_3dd0ddae, result)

    @builtins.property
    def output(self) -> _Artifact_0cb05964:
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def owner(self) -> builtins.str:
        '''The GitHub account/user that owns the repo.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> builtins.str:
        '''The name of the repo, without the username.'''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The branch to use.

        :default: "master"
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger(self) -> typing.Optional["GitHubTrigger"]:
        '''How AWS CodePipeline should be triggered.

        With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action
        With "POLL", CodePipeline periodically checks the source for changes
        With "None", the action is not triggered through changes in the source

        To use ``WEBHOOK``, your GitHub Personal Access Token should have
        **admin:repo_hook** scope (in addition to the regular **repo** scope).

        :default: GitHubTrigger.WEBHOOK
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GitHubTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubSourceActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.GitHubSourceVariables",
    jsii_struct_bases=[],
    name_mapping={
        "author_date": "authorDate",
        "branch_name": "branchName",
        "commit_id": "commitId",
        "commit_message": "commitMessage",
        "committer_date": "committerDate",
        "commit_url": "commitUrl",
        "repository_name": "repositoryName",
    },
)
class GitHubSourceVariables:
    def __init__(
        self,
        *,
        author_date: builtins.str,
        branch_name: builtins.str,
        commit_id: builtins.str,
        commit_message: builtins.str,
        committer_date: builtins.str,
        commit_url: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''The CodePipeline variables emitted by GitHub source Action.

        :param author_date: The date the currently last commit on the tracked branch was authored, in ISO-8601 format.
        :param branch_name: The name of the branch this action tracks.
        :param commit_id: The SHA1 hash of the currently last commit on the tracked branch.
        :param commit_message: The message of the currently last commit on the tracked branch.
        :param committer_date: The date the currently last commit on the tracked branch was committed, in ISO-8601 format.
        :param commit_url: The GitHub API URL of the currently last commit on the tracked branch.
        :param repository_name: The name of the repository this action points to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            
            git_hub_source_variables = codepipeline_actions.GitHubSourceVariables(
                author_date="authorDate",
                branch_name="branchName",
                commit_id="commitId",
                commit_message="commitMessage",
                committer_date="committerDate",
                commit_url="commitUrl",
                repository_name="repositoryName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "author_date": author_date,
            "branch_name": branch_name,
            "commit_id": commit_id,
            "commit_message": commit_message,
            "committer_date": committer_date,
            "commit_url": commit_url,
            "repository_name": repository_name,
        }

    @builtins.property
    def author_date(self) -> builtins.str:
        '''The date the currently last commit on the tracked branch was authored, in ISO-8601 format.'''
        result = self._values.get("author_date")
        assert result is not None, "Required property 'author_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> builtins.str:
        '''The name of the branch this action tracks.'''
        result = self._values.get("branch_name")
        assert result is not None, "Required property 'branch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_id(self) -> builtins.str:
        '''The SHA1 hash of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_id")
        assert result is not None, "Required property 'commit_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_message(self) -> builtins.str:
        '''The message of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_message")
        assert result is not None, "Required property 'commit_message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def committer_date(self) -> builtins.str:
        '''The date the currently last commit on the tracked branch was committed, in ISO-8601 format.'''
        result = self._values.get("committer_date")
        assert result is not None, "Required property 'committer_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_url(self) -> builtins.str:
        '''The GitHub API URL of the currently last commit on the tracked branch.'''
        result = self._values.get("commit_url")
        assert result is not None, "Required property 'commit_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The name of the repository this action points to.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubSourceVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codepipeline_actions.GitHubTrigger")
class GitHubTrigger(enum.Enum):
    '''If and how the GitHub source action should be triggered.'''

    NONE = "NONE"
    POLL = "POLL"
    WEBHOOK = "WEBHOOK"


@jsii.interface(jsii_type="aws-cdk-lib.aws_codepipeline_actions.IJenkinsProvider")
class IJenkinsProvider(constructs.IConstruct, typing_extensions.Protocol):
    '''A Jenkins provider.

    If you want to create a new Jenkins provider managed alongside your CDK code,
    instantiate the {@link JenkinsProvider} class directly.

    If you want to reference an already registered provider,
    use the {@link JenkinsProvider#fromJenkinsProviderAttributes} method.
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> builtins.str:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        ...


class _IJenkinsProviderProxy(
    jsii.proxy_for(constructs.IConstruct) # type: ignore[misc]
):
    '''A Jenkins provider.

    If you want to create a new Jenkins provider managed alongside your CDK code,
    instantiate the {@link JenkinsProvider} class directly.

    If you want to reference an already registered provider,
    use the {@link JenkinsProvider#fromJenkinsProviderAttributes} method.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codepipeline_actions.IJenkinsProvider"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJenkinsProvider).__jsii_proxy_class__ = lambda : _IJenkinsProviderProxy


class JenkinsAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.JenkinsAction",
):
    '''Jenkins build CodePipeline Action.

    :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-four-stage-pipeline.html
    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # jenkins_provider is of type JenkinsProvider
        
        build_action = codepipeline_actions.JenkinsAction(
            action_name="JenkinsBuild",
            jenkins_provider=jenkins_provider,
            project_name="MyProject",
            type=codepipeline_actions.JenkinsActionType.BUILD
        )
    '''

    def __init__(
        self,
        *,
        jenkins_provider: IJenkinsProvider,
        project_name: builtins.str,
        type: "JenkinsActionType",
        inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param jenkins_provider: The Jenkins Provider for this Action.
        :param project_name: The name of the project (sometimes also called job, or task) on your Jenkins installation that will be invoked by this Action.
        :param type: The type of the Action - Build, or Test.
        :param inputs: The source to use as input for this build.
        :param outputs: 
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = JenkinsActionProps(
            jenkins_provider=jenkins_provider,
            project_name=project_name,
            type=type,
            inputs=inputs,
            outputs=outputs,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        _options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, _options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.JenkinsActionProps",
    jsii_struct_bases=[_CommonActionProps_e3aaeecb],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "jenkins_provider": "jenkinsProvider",
        "project_name": "projectName",
        "type": "type",
        "inputs": "inputs",
        "outputs": "outputs",
    },
)
class JenkinsActionProps(_CommonActionProps_e3aaeecb):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        jenkins_provider: IJenkinsProvider,
        project_name: builtins.str,
        type: "JenkinsActionType",
        inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
    ) -> None:
        '''Construction properties of {@link JenkinsAction}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param jenkins_provider: The Jenkins Provider for this Action.
        :param project_name: The name of the project (sometimes also called job, or task) on your Jenkins installation that will be invoked by this Action.
        :param type: The type of the Action - Build, or Test.
        :param inputs: The source to use as input for this build.
        :param outputs: 

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # jenkins_provider is of type JenkinsProvider
            
            build_action = codepipeline_actions.JenkinsAction(
                action_name="JenkinsBuild",
                jenkins_provider=jenkins_provider,
                project_name="MyProject",
                type=codepipeline_actions.JenkinsActionType.BUILD
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "jenkins_provider": jenkins_provider,
            "project_name": project_name,
            "type": type,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if inputs is not None:
            self._values["inputs"] = inputs
        if outputs is not None:
            self._values["outputs"] = outputs

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jenkins_provider(self) -> IJenkinsProvider:
        '''The Jenkins Provider for this Action.'''
        result = self._values.get("jenkins_provider")
        assert result is not None, "Required property 'jenkins_provider' is missing"
        return typing.cast(IJenkinsProvider, result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''The name of the project (sometimes also called job, or task) on your Jenkins installation that will be invoked by this Action.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "MyJob"
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "JenkinsActionType":
        '''The type of the Action - Build, or Test.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("JenkinsActionType", result)

    @builtins.property
    def inputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The source to use as input for this build.'''
        result = self._values.get("inputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codepipeline_actions.JenkinsActionType")
class JenkinsActionType(enum.Enum):
    '''The type of the Jenkins Action that determines its CodePipeline Category - Build, or Test.

    Note that a Jenkins provider, even if it has the same name,
    must be separately registered for each type.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # jenkins_provider is of type JenkinsProvider
        
        build_action = codepipeline_actions.JenkinsAction(
            action_name="JenkinsBuild",
            jenkins_provider=jenkins_provider,
            project_name="MyProject",
            type=codepipeline_actions.JenkinsActionType.BUILD
        )
    '''

    BUILD = "BUILD"
    '''The Action will have the Build Category.'''
    TEST = "TEST"
    '''The Action will have the Test Category.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.JenkinsProviderAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "provider_name": "providerName",
        "server_url": "serverUrl",
        "version": "version",
    },
)
class JenkinsProviderAttributes:
    def __init__(
        self,
        *,
        provider_name: builtins.str,
        server_url: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for importing an existing Jenkins provider.

        :param provider_name: The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.
        :param server_url: The base URL of your Jenkins server.
        :param version: The version of your provider. Default: '1'

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            jenkins_provider = codepipeline_actions.JenkinsProvider.from_jenkins_provider_attributes(self, "JenkinsProvider",
                provider_name="MyJenkinsProvider",
                server_url="http://my-jenkins.com:8080",
                version="2"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "provider_name": provider_name,
            "server_url": server_url,
        }
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "MyJenkinsProvider"
        '''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_url(self) -> builtins.str:
        '''The base URL of your Jenkins server.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "http://myjenkins.com:8080"
        '''
        result = self._values.get("server_url")
        assert result is not None, "Required property 'server_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of your provider.

        :default: '1'
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsProviderAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.JenkinsProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "provider_name": "providerName",
        "server_url": "serverUrl",
        "for_build": "forBuild",
        "for_test": "forTest",
        "version": "version",
    },
)
class JenkinsProviderProps:
    def __init__(
        self,
        *,
        provider_name: builtins.str,
        server_url: builtins.str,
        for_build: typing.Optional[builtins.bool] = None,
        for_test: typing.Optional[builtins.bool] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param provider_name: The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.
        :param server_url: The base URL of your Jenkins server.
        :param for_build: Whether to immediately register a Jenkins Provider for the build category. The Provider will always be registered if you create a {@link JenkinsAction}. Default: false
        :param for_test: Whether to immediately register a Jenkins Provider for the test category. The Provider will always be registered if you create a {@link JenkinsTestAction}. Default: false
        :param version: The version of your provider. Default: '1'

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            jenkins_provider = codepipeline_actions.JenkinsProvider(self, "JenkinsProvider",
                provider_name="MyJenkinsProvider",
                server_url="http://my-jenkins.com:8080",
                version="2"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "provider_name": provider_name,
            "server_url": server_url,
        }
        if for_build is not None:
            self._values["for_build"] = for_build
        if for_test is not None:
            self._values["for_test"] = for_test
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "MyJenkinsProvider"
        '''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_url(self) -> builtins.str:
        '''The base URL of your Jenkins server.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "http://myjenkins.com:8080"
        '''
        result = self._values.get("server_url")
        assert result is not None, "Required property 'server_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def for_build(self) -> typing.Optional[builtins.bool]:
        '''Whether to immediately register a Jenkins Provider for the build category.

        The Provider will always be registered if you create a {@link JenkinsAction}.

        :default: false
        '''
        result = self._values.get("for_build")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def for_test(self) -> typing.Optional[builtins.bool]:
        '''Whether to immediately register a Jenkins Provider for the test category.

        The Provider will always be registered if you create a {@link JenkinsTestAction}.

        :default: false
        '''
        result = self._values.get("for_test")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of your provider.

        :default: '1'
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaInvokeAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.LambdaInvokeAction",
):
    '''CodePipeline invoke Action that is provided by an AWS Lambda function.

    :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html
    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        # fn is of type Function
        
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()
        lambda_action = codepipeline_actions.LambdaInvokeAction(
            action_name="Lambda",
            inputs=[source_output, build_output
            ],
            outputs=[
                codepipeline.Artifact("Out1"),
                codepipeline.Artifact("Out2")
            ],
            lambda_=fn
        )
    '''

    def __init__(
        self,
        *,
        lambda_: _IFunction_6adb0ab8,
        inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        user_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        user_parameters_string: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_: The lambda function to invoke.
        :param inputs: The optional input Artifacts of the Action. A Lambda Action can have up to 5 inputs. The inputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.inputArtifacts`` path. Default: the Action will not have any inputs
        :param outputs: The optional names of the output Artifacts of the Action. A Lambda Action can have up to 5 outputs. The outputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.outputArtifacts`` path. It is the responsibility of the Lambda to upload ZIP files with the Artifact contents to the provided locations. Default: the Action will not have any outputs
        :param user_parameters: A set of key-value pairs that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with. Only one of ``userParameters`` or ``userParametersString`` can be specified. Default: - no user parameters will be passed
        :param user_parameters_string: The string representation of the user parameters that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with. Only one of ``userParametersString`` or ``userParameters`` can be specified. Default: - no user parameters will be passed
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = LambdaInvokeActionProps(
            lambda_=lambda_,
            inputs=inputs,
            outputs=outputs,
            user_parameters=user_parameters,
            user_parameters_string=user_parameters_string,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, _stage, options]))

    @jsii.member(jsii_name="variable")
    def variable(self, variable_name: builtins.str) -> builtins.str:
        '''Reference a CodePipeline variable defined by the Lambda function this action points to.

        Variables in Lambda invoke actions are defined by calling the PutJobSuccessResult CodePipeline API call
        with the 'outputVariables' property filled.

        :param variable_name: the name of the variable to reference. A variable by this name must be present in the 'outputVariables' section of the PutJobSuccessResult request that the Lambda function calls when the action is invoked

        :see: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutJobSuccessResult.html
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "variable", [variable_name]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.LambdaInvokeActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "lambda_": "lambda",
        "inputs": "inputs",
        "outputs": "outputs",
        "user_parameters": "userParameters",
        "user_parameters_string": "userParametersString",
    },
)
class LambdaInvokeActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        lambda_: _IFunction_6adb0ab8,
        inputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        outputs: typing.Optional[typing.Sequence[_Artifact_0cb05964]] = None,
        user_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        user_parameters_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties of the {@link LambdaInvokeAction Lambda invoke CodePipeline Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param lambda_: The lambda function to invoke.
        :param inputs: The optional input Artifacts of the Action. A Lambda Action can have up to 5 inputs. The inputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.inputArtifacts`` path. Default: the Action will not have any inputs
        :param outputs: The optional names of the output Artifacts of the Action. A Lambda Action can have up to 5 outputs. The outputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.outputArtifacts`` path. It is the responsibility of the Lambda to upload ZIP files with the Artifact contents to the provided locations. Default: the Action will not have any outputs
        :param user_parameters: A set of key-value pairs that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with. Only one of ``userParameters`` or ``userParametersString`` can be specified. Default: - no user parameters will be passed
        :param user_parameters_string: The string representation of the user parameters that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with. Only one of ``userParametersString`` or ``userParameters`` can be specified. Default: - no user parameters will be passed

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            # fn is of type Function
            
            source_output = codepipeline.Artifact()
            build_output = codepipeline.Artifact()
            lambda_action = codepipeline_actions.LambdaInvokeAction(
                action_name="Lambda",
                inputs=[source_output, build_output
                ],
                outputs=[
                    codepipeline.Artifact("Out1"),
                    codepipeline.Artifact("Out2")
                ],
                lambda_=fn
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "lambda_": lambda_,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if inputs is not None:
            self._values["inputs"] = inputs
        if outputs is not None:
            self._values["outputs"] = outputs
        if user_parameters is not None:
            self._values["user_parameters"] = user_parameters
        if user_parameters_string is not None:
            self._values["user_parameters_string"] = user_parameters_string

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def lambda_(self) -> _IFunction_6adb0ab8:
        '''The lambda function to invoke.'''
        result = self._values.get("lambda_")
        assert result is not None, "Required property 'lambda_' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def inputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The optional input Artifacts of the Action.

        A Lambda Action can have up to 5 inputs.
        The inputs will appear in the event passed to the Lambda,
        under the ``'CodePipeline.job'.data.inputArtifacts`` path.

        :default: the Action will not have any inputs

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html#actions-invoke-lambda-function-json-event-example
        '''
        result = self._values.get("inputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[_Artifact_0cb05964]]:
        '''The optional names of the output Artifacts of the Action.

        A Lambda Action can have up to 5 outputs.
        The outputs will appear in the event passed to the Lambda,
        under the ``'CodePipeline.job'.data.outputArtifacts`` path.
        It is the responsibility of the Lambda to upload ZIP files with the Artifact contents to the provided locations.

        :default: the Action will not have any outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[_Artifact_0cb05964]], result)

    @builtins.property
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''A set of key-value pairs that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with.

        Only one of ``userParameters`` or ``userParametersString`` can be specified.

        :default: - no user parameters will be passed

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html#actions-invoke-lambda-function-json-event-example
        '''
        result = self._values.get("user_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def user_parameters_string(self) -> typing.Optional[builtins.str]:
        '''The string representation of the user parameters that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with.

        Only one of ``userParametersString`` or ``userParameters`` can be specified.

        :default: - no user parameters will be passed
        '''
        result = self._values.get("user_parameters_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaInvokeActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManualApprovalAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.ManualApprovalAction",
):
    '''Manual approval action.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_sns as sns
        
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        approve_stage = pipeline.add_stage(stage_name="Approve")
        manual_approval_action = codepipeline_actions.ManualApprovalAction(
            action_name="Approve",
            notification_topic=sns.Topic(self, "Topic"),  # optional
            notify_emails=["some_email@example.com"
            ],  # optional
            additional_information="additional info"
        )
        approve_stage.add_action(manual_approval_action)
    '''

    def __init__(
        self,
        *,
        additional_information: typing.Optional[builtins.str] = None,
        external_entity_link: typing.Optional[builtins.str] = None,
        notification_topic: typing.Optional[_ITopic_9eca4852] = None,
        notify_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_information: Any additional information that you want to include in the notification email message.
        :param external_entity_link: URL you want to provide to the reviewer as part of the approval request. Default: - the approval request will not have an external link
        :param notification_topic: Optional SNS topic to send notifications to when an approval is pending.
        :param notify_emails: A list of email addresses to subscribe to notifications when this Action is pending approval. If this has been provided, but not ``notificationTopic``, a new Topic will be created.
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = ManualApprovalActionProps(
            additional_information=additional_information,
            external_entity_link=external_entity_link,
            notification_topic=notification_topic,
            notify_emails=notify_emails,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [scope, stage, options]))

    @jsii.member(jsii_name="grantManualApproval")
    def grant_manual_approval(self, grantable: _IGrantable_71c4f5de) -> None:
        '''grant the provided principal the permissions to approve or reject this manual approval action.

        For more info see:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-iam-permissions.html

        :param grantable: the grantable to attach the permissions to.
        '''
        return typing.cast(None, jsii.invoke(self, "grantManualApproval", [grantable]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationTopic")
    def notification_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        return typing.cast(typing.Optional[_ITopic_9eca4852], jsii.get(self, "notificationTopic"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.ManualApprovalActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "additional_information": "additionalInformation",
        "external_entity_link": "externalEntityLink",
        "notification_topic": "notificationTopic",
        "notify_emails": "notifyEmails",
    },
)
class ManualApprovalActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        additional_information: typing.Optional[builtins.str] = None,
        external_entity_link: typing.Optional[builtins.str] = None,
        notification_topic: typing.Optional[_ITopic_9eca4852] = None,
        notify_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Construction properties of the {@link ManualApprovalAction}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param additional_information: Any additional information that you want to include in the notification email message.
        :param external_entity_link: URL you want to provide to the reviewer as part of the approval request. Default: - the approval request will not have an external link
        :param notification_topic: Optional SNS topic to send notifications to when an approval is pending.
        :param notify_emails: A list of email addresses to subscribe to notifications when this Action is pending approval. If this has been provided, but not ``notificationTopic``, a new Topic will be created.

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            import aws_cdk.aws_sns as sns
            
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            approve_stage = pipeline.add_stage(stage_name="Approve")
            manual_approval_action = codepipeline_actions.ManualApprovalAction(
                action_name="Approve",
                notification_topic=sns.Topic(self, "Topic"),  # optional
                notify_emails=["some_email@example.com"
                ],  # optional
                additional_information="additional info"
            )
            approve_stage.add_action(manual_approval_action)
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if additional_information is not None:
            self._values["additional_information"] = additional_information
        if external_entity_link is not None:
            self._values["external_entity_link"] = external_entity_link
        if notification_topic is not None:
            self._values["notification_topic"] = notification_topic
        if notify_emails is not None:
            self._values["notify_emails"] = notify_emails

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def additional_information(self) -> typing.Optional[builtins.str]:
        '''Any additional information that you want to include in the notification email message.'''
        result = self._values.get("additional_information")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_entity_link(self) -> typing.Optional[builtins.str]:
        '''URL you want to provide to the reviewer as part of the approval request.

        :default: - the approval request will not have an external link
        '''
        result = self._values.get("external_entity_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''Optional SNS topic to send notifications to when an approval is pending.'''
        result = self._values.get("notification_topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    @builtins.property
    def notify_emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of email addresses to subscribe to notifications when this Action is pending approval.

        If this has been provided, but not ``notificationTopic``,
        a new Topic will be created.
        '''
        result = self._values.get("notify_emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManualApprovalActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3DeployAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.S3DeployAction",
):
    '''Deploys the sourceArtifact to Amazon S3.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        source_output = codepipeline.Artifact()
        target_bucket = s3.Bucket(self, "MyBucket")
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        deploy_action = codepipeline_actions.S3DeployAction(
            action_name="S3Deploy",
            bucket=target_bucket,
            input=source_output
        )
        deploy_stage = pipeline.add_stage(
            stage_name="Deploy",
            actions=[deploy_action]
        )
    '''

    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        input: _Artifact_0cb05964,
        access_control: typing.Optional[_BucketAccessControl_466c7e1b] = None,
        cache_control: typing.Optional[typing.Sequence[CacheControl]] = None,
        extract: typing.Optional[builtins.bool] = None,
        object_key: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The Amazon S3 bucket that is the deploy target.
        :param input: The input Artifact to deploy to Amazon S3.
        :param access_control: The specified canned ACL to objects deployed to Amazon S3. This overwrites any existing ACL that was applied to the object. Default: - the original object ACL
        :param cache_control: The caching behavior for requests/responses for objects in the bucket. The final cache control property will be the result of joining all of the provided array elements with a comma (plus a space after the comma). Default: - none, decided by the HTTP client
        :param extract: Should the deploy action extract the artifact before deploying to Amazon S3. Default: true
        :param object_key: The key of the target object. This is required if extract is false.
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = S3DeployActionProps(
            bucket=bucket,
            input=input,
            access_control=access_control,
            cache_control=cache_control,
            extract=extract,
            object_key=object_key,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.S3DeployActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "bucket": "bucket",
        "input": "input",
        "access_control": "accessControl",
        "cache_control": "cacheControl",
        "extract": "extract",
        "object_key": "objectKey",
    },
)
class S3DeployActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        bucket: _IBucket_42e086fd,
        input: _Artifact_0cb05964,
        access_control: typing.Optional[_BucketAccessControl_466c7e1b] = None,
        cache_control: typing.Optional[typing.Sequence[CacheControl]] = None,
        extract: typing.Optional[builtins.bool] = None,
        object_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties of the {@link S3DeployAction S3 deploy Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param bucket: The Amazon S3 bucket that is the deploy target.
        :param input: The input Artifact to deploy to Amazon S3.
        :param access_control: The specified canned ACL to objects deployed to Amazon S3. This overwrites any existing ACL that was applied to the object. Default: - the original object ACL
        :param cache_control: The caching behavior for requests/responses for objects in the bucket. The final cache control property will be the result of joining all of the provided array elements with a comma (plus a space after the comma). Default: - none, decided by the HTTP client
        :param extract: Should the deploy action extract the artifact before deploying to Amazon S3. Default: true
        :param object_key: The key of the target object. This is required if extract is false.

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            source_output = codepipeline.Artifact()
            target_bucket = s3.Bucket(self, "MyBucket")
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            deploy_action = codepipeline_actions.S3DeployAction(
                action_name="S3Deploy",
                bucket=target_bucket,
                input=source_output
            )
            deploy_stage = pipeline.add_stage(
                stage_name="Deploy",
                actions=[deploy_action]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "bucket": bucket,
            "input": input,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if access_control is not None:
            self._values["access_control"] = access_control
        if cache_control is not None:
            self._values["cache_control"] = cache_control
        if extract is not None:
            self._values["extract"] = extract
        if object_key is not None:
            self._values["object_key"] = object_key

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''The Amazon S3 bucket that is the deploy target.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def input(self) -> _Artifact_0cb05964:
        '''The input Artifact to deploy to Amazon S3.'''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def access_control(self) -> typing.Optional[_BucketAccessControl_466c7e1b]:
        '''The specified canned ACL to objects deployed to Amazon S3.

        This overwrites any existing ACL that was applied to the object.

        :default: - the original object ACL
        '''
        result = self._values.get("access_control")
        return typing.cast(typing.Optional[_BucketAccessControl_466c7e1b], result)

    @builtins.property
    def cache_control(self) -> typing.Optional[typing.List[CacheControl]]:
        '''The caching behavior for requests/responses for objects in the bucket.

        The final cache control property will be the result of joining all of the provided array elements with a comma
        (plus a space after the comma).

        :default: - none, decided by the HTTP client
        '''
        result = self._values.get("cache_control")
        return typing.cast(typing.Optional[typing.List[CacheControl]], result)

    @builtins.property
    def extract(self) -> typing.Optional[builtins.bool]:
        '''Should the deploy action extract the artifact before deploying to Amazon S3.

        :default: true
        '''
        result = self._values.get("extract")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def object_key(self) -> typing.Optional[builtins.str]:
        '''The key of the target object.

        This is required if extract is false.
        '''
        result = self._values.get("object_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3DeployActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3SourceAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.S3SourceAction",
):
    '''Source that is provided by a specific Amazon S3 object.

    Will trigger the pipeline as soon as the S3 object changes, but only if there is
    a CloudTrail Trail in the account that captures the S3 event.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_cloudtrail as cloudtrail
        
        # source_bucket is of type Bucket
        
        source_output = codepipeline.Artifact()
        key = "some/key.zip"
        trail = cloudtrail.Trail(self, "CloudTrail")
        trail.add_s3_event_selector([cloudtrail.S3EventSelector(
            bucket=source_bucket,
            object_prefix=key
        )],
            read_write_type=cloudtrail.ReadWriteType.WRITE_ONLY
        )
        source_action = codepipeline_actions.S3SourceAction(
            action_name="S3Source",
            bucket_key=key,
            bucket=source_bucket,
            output=source_output,
            trigger=codepipeline_actions.S3Trigger.EVENTS
        )
    '''

    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        bucket_key: builtins.str,
        output: _Artifact_0cb05964,
        trigger: typing.Optional["S3Trigger"] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The Amazon S3 bucket that stores the source code. If you import an encrypted bucket in your stack, please specify the encryption key at import time by using ``Bucket.fromBucketAttributes()`` method.
        :param bucket_key: The key within the S3 bucket that stores the source code.
        :param output: 
        :param trigger: How should CodePipeline detect source changes for this Action. Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail, as otherwise the CloudWatch Events will not be emitted. Default: S3Trigger.POLL
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = S3SourceActionProps(
            bucket=bucket,
            bucket_key=bucket_key,
            output=output,
            trigger=trigger,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, stage, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variables")
    def variables(self) -> "S3SourceVariables":
        '''The variables emitted by this action.'''
        return typing.cast("S3SourceVariables", jsii.get(self, "variables"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.S3SourceActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "bucket": "bucket",
        "bucket_key": "bucketKey",
        "output": "output",
        "trigger": "trigger",
    },
)
class S3SourceActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        bucket: _IBucket_42e086fd,
        bucket_key: builtins.str,
        output: _Artifact_0cb05964,
        trigger: typing.Optional["S3Trigger"] = None,
    ) -> None:
        '''Construction properties of the {@link S3SourceAction S3 source Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param bucket: The Amazon S3 bucket that stores the source code. If you import an encrypted bucket in your stack, please specify the encryption key at import time by using ``Bucket.fromBucketAttributes()`` method.
        :param bucket_key: The key within the S3 bucket that stores the source code.
        :param output: 
        :param trigger: How should CodePipeline detect source changes for this Action. Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail, as otherwise the CloudWatch Events will not be emitted. Default: S3Trigger.POLL

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            import aws_cdk.aws_cloudtrail as cloudtrail
            
            # source_bucket is of type Bucket
            
            source_output = codepipeline.Artifact()
            key = "some/key.zip"
            trail = cloudtrail.Trail(self, "CloudTrail")
            trail.add_s3_event_selector([cloudtrail.S3EventSelector(
                bucket=source_bucket,
                object_prefix=key
            )],
                read_write_type=cloudtrail.ReadWriteType.WRITE_ONLY
            )
            source_action = codepipeline_actions.S3SourceAction(
                action_name="S3Source",
                bucket_key=key,
                bucket=source_bucket,
                output=source_output,
                trigger=codepipeline_actions.S3Trigger.EVENTS
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "bucket": bucket,
            "bucket_key": bucket_key,
            "output": output,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''The Amazon S3 bucket that stores the source code.

        If you import an encrypted bucket in your stack, please specify
        the encryption key at import time by using ``Bucket.fromBucketAttributes()`` method.
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def bucket_key(self) -> builtins.str:
        '''The key within the S3 bucket that stores the source code.

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            "path/to/file.zip"
        '''
        result = self._values.get("bucket_key")
        assert result is not None, "Required property 'bucket_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output(self) -> _Artifact_0cb05964:
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(_Artifact_0cb05964, result)

    @builtins.property
    def trigger(self) -> typing.Optional["S3Trigger"]:
        '''How should CodePipeline detect source changes for this Action.

        Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail,
        as otherwise the CloudWatch Events will not be emitted.

        :default: S3Trigger.POLL

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/log-s3-data-events.html
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["S3Trigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3SourceActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.S3SourceVariables",
    jsii_struct_bases=[],
    name_mapping={"e_tag": "eTag", "version_id": "versionId"},
)
class S3SourceVariables:
    def __init__(self, *, e_tag: builtins.str, version_id: builtins.str) -> None:
        '''The CodePipeline variables emitted by the S3 source Action.

        :param e_tag: The e-tag of the S3 version of the object that triggered the build.
        :param version_id: The identifier of the S3 version of the object that triggered the build.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            
            s3_source_variables = codepipeline_actions.S3SourceVariables(
                e_tag="eTag",
                version_id="versionId"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "e_tag": e_tag,
            "version_id": version_id,
        }

    @builtins.property
    def e_tag(self) -> builtins.str:
        '''The e-tag of the S3 version of the object that triggered the build.'''
        result = self._values.get("e_tag")
        assert result is not None, "Required property 'e_tag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_id(self) -> builtins.str:
        '''The identifier of the S3 version of the object that triggered the build.'''
        result = self._values.get("version_id")
        assert result is not None, "Required property 'version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3SourceVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codepipeline_actions.S3Trigger")
class S3Trigger(enum.Enum):
    '''How should the S3 Action detect changes.

    This is the type of the {@link S3SourceAction.trigger} property.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_cloudtrail as cloudtrail
        
        # source_bucket is of type Bucket
        
        source_output = codepipeline.Artifact()
        key = "some/key.zip"
        trail = cloudtrail.Trail(self, "CloudTrail")
        trail.add_s3_event_selector([cloudtrail.S3EventSelector(
            bucket=source_bucket,
            object_prefix=key
        )],
            read_write_type=cloudtrail.ReadWriteType.WRITE_ONLY
        )
        source_action = codepipeline_actions.S3SourceAction(
            action_name="S3Source",
            bucket_key=key,
            bucket=source_bucket,
            output=source_output,
            trigger=codepipeline_actions.S3Trigger.EVENTS
        )
    '''

    NONE = "NONE"
    '''The Action will never detect changes - the Pipeline it's part of will only begin a run when explicitly started.'''
    POLL = "POLL"
    '''CodePipeline will poll S3 to detect changes.

    This is the default method of detecting changes.
    '''
    EVENTS = "EVENTS"
    '''CodePipeline will use CloudWatch Events to be notified of changes.

    Note that the Bucket that the Action uses needs to be part of a CloudTrail Trail
    for the events to be delivered.
    '''


class ServiceCatalogDeployActionBeta1(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.ServiceCatalogDeployActionBeta1",
):
    '''CodePipeline action to connect to an existing ServiceCatalog product.

    **Note**: this class is still experimental, and may have breaking changes in the future!

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        cdk_build_output = codepipeline.Artifact()
        service_catalog_deploy_action = codepipeline_actions.ServiceCatalogDeployActionBeta1(
            action_name="ServiceCatalogDeploy",
            template_path=cdk_build_output.at_path("Sample.template.json"),
            product_version_name="Version - " + Date.now.to_string,
            product_version_description="This is a version from the pipeline with a new description.",
            product_id="prod-XXXXXXXX"
        )
    '''

    def __init__(
        self,
        *,
        product_id: builtins.str,
        product_version_name: builtins.str,
        template_path: _ArtifactPath_bf444090,
        product_version_description: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param product_id: The identifier of the product in the Service Catalog. This product must already exist.
        :param product_version_name: The name of the version of the Service Catalog product to be deployed.
        :param template_path: The path to the cloudformation artifact.
        :param product_version_description: The optional description of this version of the Service Catalog product. Default: ''
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = ServiceCatalogDeployActionBeta1Props(
            product_id=product_id,
            product_version_name=product_version_name,
            template_path=template_path,
            product_version_description=product_version_description,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.ServiceCatalogDeployActionBeta1Props",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "product_id": "productId",
        "product_version_name": "productVersionName",
        "template_path": "templatePath",
        "product_version_description": "productVersionDescription",
    },
)
class ServiceCatalogDeployActionBeta1Props(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        product_id: builtins.str,
        product_version_name: builtins.str,
        template_path: _ArtifactPath_bf444090,
        product_version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties of the {@link ServiceCatalogDeployActionBeta1 ServiceCatalog deploy CodePipeline Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param product_id: The identifier of the product in the Service Catalog. This product must already exist.
        :param product_version_name: The name of the version of the Service Catalog product to be deployed.
        :param template_path: The path to the cloudformation artifact.
        :param product_version_description: The optional description of this version of the Service Catalog product. Default: ''

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            cdk_build_output = codepipeline.Artifact()
            service_catalog_deploy_action = codepipeline_actions.ServiceCatalogDeployActionBeta1(
                action_name="ServiceCatalogDeploy",
                template_path=cdk_build_output.at_path("Sample.template.json"),
                product_version_name="Version - " + Date.now.to_string,
                product_version_description="This is a version from the pipeline with a new description.",
                product_id="prod-XXXXXXXX"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "product_id": product_id,
            "product_version_name": product_version_name,
            "template_path": template_path,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if product_version_description is not None:
            self._values["product_version_description"] = product_version_description

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The identifier of the product in the Service Catalog.

        This product must already exist.
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_version_name(self) -> builtins.str:
        '''The name of the version of the Service Catalog product to be deployed.'''
        result = self._values.get("product_version_name")
        assert result is not None, "Required property 'product_version_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_path(self) -> _ArtifactPath_bf444090:
        '''The path to the cloudformation artifact.'''
        result = self._values.get("template_path")
        assert result is not None, "Required property 'template_path' is missing"
        return typing.cast(_ArtifactPath_bf444090, result)

    @builtins.property
    def product_version_description(self) -> typing.Optional[builtins.str]:
        '''The optional description of this version of the Service Catalog product.

        :default: ''
        '''
        result = self._values.get("product_version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceCatalogDeployActionBeta1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StateMachineInput(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.StateMachineInput",
):
    '''Represents the input for the StateMachine.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_stepfunctions as stepfunctions
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        start_state = stepfunctions.Pass(self, "StartState")
        simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
            definition=start_state
        )
        step_function_action = codepipeline_actions.StepFunctionInvokeAction(
            action_name="Invoke",
            state_machine=simple_state_machine,
            state_machine_input=codepipeline_actions.StateMachineInput.literal({"IsHelloWorldExample": True})
        )
        pipeline.add_stage(
            stage_name="StepFunctions",
            actions=[step_function_action]
        )
    '''

    @jsii.member(jsii_name="filePath") # type: ignore[misc]
    @builtins.classmethod
    def file_path(cls, input_file: _ArtifactPath_bf444090) -> "StateMachineInput":
        '''When the input type is FilePath, input artifact and filepath must be specified.

        :param input_file: -
        '''
        return typing.cast("StateMachineInput", jsii.sinvoke(cls, "filePath", [input_file]))

    @jsii.member(jsii_name="literal") # type: ignore[misc]
    @builtins.classmethod
    def literal(
        cls,
        object: typing.Mapping[typing.Any, typing.Any],
    ) -> "StateMachineInput":
        '''When the input type is Literal, input value is passed directly to the state machine input.

        :param object: -
        '''
        return typing.cast("StateMachineInput", jsii.sinvoke(cls, "literal", [object]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="input")
    def input(self) -> typing.Any:
        '''When InputType is set to Literal (default), the Input field is used directly as the input for the state machine execution.

        Otherwise, the state machine is invoked with an empty JSON object {}.

        When InputType is set to FilePath, this field is required.
        An input artifact is also required when InputType is set to FilePath.

        :default: - none
        '''
        return typing.cast(typing.Any, jsii.get(self, "input"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputArtifact")
    def input_artifact(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The optional input Artifact of the Action.

        If InputType is set to FilePath, this artifact is required
        and is used to source the input for the state machine execution.

        :default: - the Action will not have any inputs

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-StepFunctions.html#action-reference-StepFunctions-example
        '''
        return typing.cast(typing.Optional[_Artifact_0cb05964], jsii.get(self, "inputArtifact"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputType")
    def input_type(self) -> typing.Optional[builtins.str]:
        '''Optional StateMachine InputType InputType can be Literal or FilePath.

        :default: - Literal
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputType"))


class StepFunctionInvokeAction(
    Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.StepFunctionInvokeAction",
):
    '''StepFunctionInvokeAction that is provided by an AWS CodePipeline.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_stepfunctions as stepfunctions
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        start_state = stepfunctions.Pass(self, "StartState")
        simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
            definition=start_state
        )
        step_function_action = codepipeline_actions.StepFunctionInvokeAction(
            action_name="Invoke",
            state_machine=simple_state_machine,
            state_machine_input=codepipeline_actions.StateMachineInput.literal({"IsHelloWorldExample": True})
        )
        pipeline.add_stage(
            stage_name="StepFunctions",
            actions=[step_function_action]
        )
    '''

    def __init__(
        self,
        *,
        state_machine: _IStateMachine_73e8d2b0,
        execution_name_prefix: typing.Optional[builtins.str] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        state_machine_input: typing.Optional[StateMachineInput] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param state_machine: The state machine to invoke.
        :param execution_name_prefix: Prefix (optional). By default, the action execution ID is used as the state machine execution name. If a prefix is provided, it is prepended to the action execution ID with a hyphen and together used as the state machine execution name. Default: - action execution ID
        :param output: The optional output Artifact of the Action. Default: the Action will not have any outputs
        :param state_machine_input: Represents the input to the StateMachine. This includes input artifact, input type and the statemachine input. Default: - none
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = StepFunctionsInvokeActionProps(
            state_machine=state_machine,
            execution_name_prefix=execution_name_prefix,
            output=output,
            state_machine_input=state_machine_input,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        _scope: constructs.Construct,
        _stage: _IStage_415fc571,
        *,
        bucket: _IBucket_42e086fd,
        role: _IRole_235f5d8e,
    ) -> _ActionConfig_846fc217:
        '''This is a renamed version of the {@link IAction.bind} method.

        :param _scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        options = _ActionBindOptions_3a612254(bucket=bucket, role=role)

        return typing.cast(_ActionConfig_846fc217, jsii.invoke(self, "bound", [_scope, _stage, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.StepFunctionsInvokeActionProps",
    jsii_struct_bases=[_CommonAwsActionProps_8b809bb6],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "state_machine": "stateMachine",
        "execution_name_prefix": "executionNamePrefix",
        "output": "output",
        "state_machine_input": "stateMachineInput",
    },
)
class StepFunctionsInvokeActionProps(_CommonAwsActionProps_8b809bb6):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        state_machine: _IStateMachine_73e8d2b0,
        execution_name_prefix: typing.Optional[builtins.str] = None,
        output: typing.Optional[_Artifact_0cb05964] = None,
        state_machine_input: typing.Optional[StateMachineInput] = None,
    ) -> None:
        '''Construction properties of the {@link StepFunctionsInvokeAction StepFunction Invoke Action}.

        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your {@link IAction.bind} method in the {@link ActionBindOptions.role} property. Default: a new Role will be generated
        :param state_machine: The state machine to invoke.
        :param execution_name_prefix: Prefix (optional). By default, the action execution ID is used as the state machine execution name. If a prefix is provided, it is prepended to the action execution ID with a hyphen and together used as the state machine execution name. Default: - action execution ID
        :param output: The optional output Artifact of the Action. Default: the Action will not have any outputs
        :param state_machine_input: Represents the input to the StateMachine. This includes input artifact, input type and the statemachine input. Default: - none

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            import aws_cdk.aws_stepfunctions as stepfunctions
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            start_state = stepfunctions.Pass(self, "StartState")
            simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
                definition=start_state
            )
            step_function_action = codepipeline_actions.StepFunctionInvokeAction(
                action_name="Invoke",
                state_machine=simple_state_machine,
                state_machine_input=codepipeline_actions.StateMachineInput.literal({"IsHelloWorldExample": True})
            )
            pipeline.add_stage(
                stage_name="StepFunctions",
                actions=[step_function_action]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_name": action_name,
            "state_machine": state_machine,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if execution_name_prefix is not None:
            self._values["execution_name_prefix"] = execution_name_prefix
        if output is not None:
            self._values["output"] = output
        if state_machine_input is not None:
            self._values["state_machine_input"] = state_machine_input

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your {@link IAction.bind}
        method in the {@link ActionBindOptions.role} property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def state_machine(self) -> _IStateMachine_73e8d2b0:
        '''The state machine to invoke.'''
        result = self._values.get("state_machine")
        assert result is not None, "Required property 'state_machine' is missing"
        return typing.cast(_IStateMachine_73e8d2b0, result)

    @builtins.property
    def execution_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Prefix (optional).

        By default, the action execution ID is used as the state machine execution name.
        If a prefix is provided, it is prepended to the action execution ID with a hyphen and
        together used as the state machine execution name.

        :default: - action execution ID
        '''
        result = self._values.get("execution_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output(self) -> typing.Optional[_Artifact_0cb05964]:
        '''The optional output Artifact of the Action.

        :default: the Action will not have any outputs
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def state_machine_input(self) -> typing.Optional[StateMachineInput]:
        '''Represents the input to the StateMachine.

        This includes input artifact, input type and the statemachine input.

        :default: - none
        '''
        result = self._values.get("state_machine_input")
        return typing.cast(typing.Optional[StateMachineInput], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepFunctionsInvokeActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IJenkinsProvider)
class BaseJenkinsProvider(
    constructs.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.BaseJenkinsProvider",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param version: -
        '''
        jsii.create(self.__class__, self, [scope, id, version])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerName")
    @abc.abstractmethod
    def provider_name(self) -> builtins.str:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverUrl")
    @abc.abstractmethod
    def server_url(self) -> builtins.str:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))


class _BaseJenkinsProviderProxy(BaseJenkinsProvider):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverUrl"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseJenkinsProvider).__jsii_proxy_class__ = lambda : _BaseJenkinsProviderProxy


class JenkinsProvider(
    BaseJenkinsProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codepipeline_actions.JenkinsProvider",
):
    '''A class representing Jenkins providers.

    :see: #import
    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        jenkins_provider = codepipeline_actions.JenkinsProvider(self, "JenkinsProvider",
            provider_name="MyJenkinsProvider",
            server_url="http://my-jenkins.com:8080",
            version="2"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        provider_name: builtins.str,
        server_url: builtins.str,
        for_build: typing.Optional[builtins.bool] = None,
        for_test: typing.Optional[builtins.bool] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param provider_name: The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.
        :param server_url: The base URL of your Jenkins server.
        :param for_build: Whether to immediately register a Jenkins Provider for the build category. The Provider will always be registered if you create a {@link JenkinsAction}. Default: false
        :param for_test: Whether to immediately register a Jenkins Provider for the test category. The Provider will always be registered if you create a {@link JenkinsTestAction}. Default: false
        :param version: The version of your provider. Default: '1'
        '''
        props = JenkinsProviderProps(
            provider_name=provider_name,
            server_url=server_url,
            for_build=for_build,
            for_test=for_test,
            version=version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromJenkinsProviderAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_jenkins_provider_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        provider_name: builtins.str,
        server_url: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> IJenkinsProvider:
        '''Import a Jenkins provider registered either outside the CDK, or in a different CDK Stack.

        :param scope: the parent Construct for the new provider.
        :param id: the identifier of the new provider Construct.
        :param provider_name: The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.
        :param server_url: The base URL of your Jenkins server.
        :param version: The version of your provider. Default: '1'

        :return: a new Construct representing a reference to an existing Jenkins provider
        '''
        attrs = JenkinsProviderAttributes(
            provider_name=provider_name, server_url=server_url, version=version
        )

        return typing.cast(IJenkinsProvider, jsii.sinvoke(cls, "fromJenkinsProviderAttributes", [scope, id, attrs]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverUrl"))


__all__ = [
    "Action",
    "AlexaSkillDeployAction",
    "AlexaSkillDeployActionProps",
    "BaseJenkinsProvider",
    "CacheControl",
    "CloudFormationCreateReplaceChangeSetAction",
    "CloudFormationCreateReplaceChangeSetActionProps",
    "CloudFormationCreateUpdateStackAction",
    "CloudFormationCreateUpdateStackActionProps",
    "CloudFormationDeleteStackAction",
    "CloudFormationDeleteStackActionProps",
    "CloudFormationExecuteChangeSetAction",
    "CloudFormationExecuteChangeSetActionProps",
    "CodeBuildAction",
    "CodeBuildActionProps",
    "CodeBuildActionType",
    "CodeCommitSourceAction",
    "CodeCommitSourceActionProps",
    "CodeCommitSourceVariables",
    "CodeCommitTrigger",
    "CodeDeployEcsContainerImageInput",
    "CodeDeployEcsDeployAction",
    "CodeDeployEcsDeployActionProps",
    "CodeDeployServerDeployAction",
    "CodeDeployServerDeployActionProps",
    "CodeStarConnectionsSourceAction",
    "CodeStarConnectionsSourceActionProps",
    "CodeStarSourceVariables",
    "EcrSourceAction",
    "EcrSourceActionProps",
    "EcrSourceVariables",
    "EcsDeployAction",
    "EcsDeployActionProps",
    "GitHubSourceAction",
    "GitHubSourceActionProps",
    "GitHubSourceVariables",
    "GitHubTrigger",
    "IJenkinsProvider",
    "JenkinsAction",
    "JenkinsActionProps",
    "JenkinsActionType",
    "JenkinsProvider",
    "JenkinsProviderAttributes",
    "JenkinsProviderProps",
    "LambdaInvokeAction",
    "LambdaInvokeActionProps",
    "ManualApprovalAction",
    "ManualApprovalActionProps",
    "S3DeployAction",
    "S3DeployActionProps",
    "S3SourceAction",
    "S3SourceActionProps",
    "S3SourceVariables",
    "S3Trigger",
    "ServiceCatalogDeployActionBeta1",
    "ServiceCatalogDeployActionBeta1Props",
    "StateMachineInput",
    "StepFunctionInvokeAction",
    "StepFunctionsInvokeActionProps",
]

publication.publish()
